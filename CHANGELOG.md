## v0.1.2 (2026-08-02)

### Feat

- add Makefile targets for test, precommit, and release
- add commitizen for conventional commits

### Fix

- remove bleak deps from manifest.json requirements

## v0.1.1 (2026-07-26)

### Fix

- align with Android SDK protocol

### Refactor

- modernlize code way

## v0.1.0 (2026-07-15)

### Added

- initial integration using Home Assistant Bluetooth wrappers
- QR code pairing to extract public and secret keys
- BLE communication with Sesame smart locks
- DataUpdateCoordinator + CoordinatorEntity pattern
- lock binary sensor with correct state mapping
- session staleness detection and reconnection logic
- command queuing and chunked BLE transmission
- RSSI-based device sorting
- GitHub issue templates, CONTRIBUTING, LICENSE
- HACS configuration and brand images
- pre-commit hooks for ruff linting and formatting
- Makefile with install/lint/format/typecheck/fix/clean targets
- CI workflows for GitHub Actions

### Fix

- InvalidTag exception handling during BLE notifications
- session staleness when decrypt fails with InvalidTag
- wrong lock binary sensor state
- config flow translation
- BleTransmitter.getChunk() bug when fragments > 0
- rssi not coming from device

### Changed

- migrated from persistent connection to on-demand connect pattern
- refactored entities to use DataUpdateCoordinator + CoordinatorEntity
- improved status parsing and logging
- timed connection timeout values
- renamed integration to "Sesame BLE"
- sorted manifest keys
- modernlized code patterns
- aligned protocol with Android SDK reference