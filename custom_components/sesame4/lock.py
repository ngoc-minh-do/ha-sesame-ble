"""Lock entity for Sesame 4 BLE integration."""

from __future__ import annotations

from typing import Any

from homeassistant.components.lock import LockEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .device import Sesame4Device


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    device: Sesame4Device = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([Sesame4Lock(device, entry)])


class Sesame4Lock(LockEntity):
    _attr_has_entity_name = True

    def __init__(self, device: Sesame4Device, entry: ConfigEntry) -> None:
        self._device = device
        self._entry = entry
        self._attr_unique_id = f"{device.address}_lock"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, device.address)},
            "name": "Sesame 4 Lock",
            "manufacturer": "CANDY HOUSE",
            "model": entry.data.get("model", "Sesame 4"),
        }
        self._attr_name = "Lock"

    @property
    def available(self) -> bool:
        return self._device.is_connected

    @property
    def is_locked(self) -> bool | None:
        status = self._device.mech_status
        if status is None:
            return None
        return status.isLocked()

    @property
    def is_locking(self) -> bool:
        status = self._device.mech_status
        if status is None:
            return False
        target = status.getTarget()
        settings = self._device.mech_settings
        if settings is None:
            return False
        return target == settings.getLockPosition() and not status.isInLockRange()

    @property
    def is_unlocking(self) -> bool:
        status = self._device.mech_status
        if status is None:
            return False
        target = status.getTarget()
        settings = self._device.mech_settings
        if settings is None:
            return False
        return target == settings.getUnlockPosition() and not status.isInUnlockRange()

    async def async_lock(self, **kwargs: Any) -> None:
        await self._device.lock()

    async def async_unlock(self, **kwargs: Any) -> None:
        await self._device.unlock()

    @callback
    def _on_device_update(self) -> None:
        self.async_schedule_update_ha_state()

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self._device.add_update_callback(self._on_device_update)

    async def async_will_remove_from_hass(self) -> None:
        self._device.remove_update_callback(self._on_device_update)
        await super().async_will_remove_from_hass()
