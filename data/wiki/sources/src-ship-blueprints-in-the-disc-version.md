---
id: src-ship-blueprints-in-the-disc-version
type: source
title: 'Source Summary: Ship blueprints in the BBC Micro disc version'
aliases:
- Ship blueprints in the BBC Micro disc version
- ship_blueprints_in_the_disc_version.md
tags:
- basic
- assembly
- graphics
sources:
- path: data/docs/elite_bbcelite_com/deep_dives/ship_blueprints_in_the_disc_version.md
  sha256: 95c63a694c345d439cb5275999e902ca524e8ec350deb4d188cbe42721ce495f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Ship blueprints in the BBC Micro disc version

**Raw Source File**: `data/docs/elite_bbcelite_com/deep_dives/ship_blueprints_in_the_disc_version.md`
**SHA256**: `95c63a694c345d439cb5275999e902ca524e8ec350deb4d188cbe42721ce495f`

## Summary



# Ship blueprints in the BBC Micro disc version

## How the BBC Micro disc version loads its ship blueprints into memory

When you launch from the space station in the disc version of BBC Micro Elite, there's an awful lot of disc activity - noticeably more than when you dock. This is because the flight code, once loaded, initiates a second load of the ship blueprints.

Unlike the 6502 Second Processor version, there is only room for around 12-13 ship blueprints at any one time, and because the...
