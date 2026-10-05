---
id: src-rr-chip-data
type: source
title: 'Source Summary: base:rr_chip_data [Codebase64 wiki]'
aliases:
- base:rr_chip_data [Codebase64 wiki]
- rr_chip_data.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/rr_chip_data.md
  sha256: 62486ed869001f4a517af7b4b0ff6fd438710b9b2c23a5b88bc13acc11e23154
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:rr_chip_data [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/rr_chip_data.md`
**SHA256**: `62486ed869001f4a517af7b4b0ff6fd438710b9b2c23a5b88bc13acc11e23154`

## Summary



# base:rr_chip_data [Codebase64 wiki]

base:rr_chip_data

                This routine accesses the FlashROM chip of Retro Replay in a special way, to find out the chip type and manufacturer. The chip used by the RR reports these using a specific command via its programming interface. Included are useful subroutines to deal with the chip on low level.

See the data sheets to learn how to interpret the information retrieved by this code. Manufacturer: ST = 1, AMD = 20 (decimal). These routines ...
