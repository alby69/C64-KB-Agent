---
id: src-rr-flashing
type: source
title: 'Source Summary: base:rr_flashing [Codebase64 wiki]'
aliases:
- base:rr_flashing [Codebase64 wiki]
- rr_flashing.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/rr_flashing.md
  sha256: 3c1f7a62eb663ea94f1b4e5ade5d6c504d4b287139e8792ec32fb0715ac43b73
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:rr_flashing [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/rr_flashing.md`
**SHA256**: `3c1f7a62eb663ea94f1b4e5ade5d6c504d4b287139e8792ec32fb0715ac43b73`

## Summary




# base:rr_flashing [Codebase64 wiki]

This article deals with a very sophisticated issue: programming the FlashROM. You will need thorough understanding of how the chip works. All of the code provided is commented well, but you still have to know what you are doing. You won't physically destroy your ROM chip or the cart, though.

The code originates from my FMEEPROMPP utility. The ordinal numbers and byte codes refer to the FlashROM command sequence steps. PA and PD stand for the address and ...
