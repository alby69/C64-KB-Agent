---
id: src-ecb9-vic-ii-chip-initialisation-values
type: source
title: 'Source Summary: vic ii chip initialisation values'
aliases:
- vic ii chip initialisation values
- ecb9-vic-ii-chip-initialisation-values.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ecb9-vic-ii-chip-initialisation-values.md
  sha256: 61acb8e36bf4d14d289e4d7e97e0f8545dff8401ee0b91e107b9d121caa605e7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: vic ii chip initialisation values

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ecb9-vic-ii-chip-initialisation-values.md`
**SHA256**: `61acb8e36bf4d14d289e4d7e97e0f8545dff8401ee0b91e107b9d121caa605e7`

## Summary



# $ECB9 — vic ii chip initialisation values

## Disassemblatura
```assembly
.ECB9  00 00   ; sprite 0 x,y
.ECBB  00 00   ; sprite 1 x,y
.ECBD  00 00   ; sprite 2 x,y
.ECBF  00 00   ; sprite 3 x,y
.ECC1  00 00   ; sprite 4 x,y
.ECC3  00 00   ; sprite 5 x,y
.ECC5  00 00   ; sprite 6 x,y
.ECC7  00 00   ; sprite 7 x,y
.ECC9  00   ; sprites 0 to 7 x bit 8
.ECCA  9B   ; enable screen, enable 25 rows vertical fine scroll and control bit function --- ------- 7  raster compare bit 8 6  1 = enable exten...
