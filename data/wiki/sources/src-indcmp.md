---
id: src-indcmp
type: source
title: 'Source Summary: INDCMP'
aliases:
- INDCMP
- indcmp.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/indcmp.md
  sha256: e107f2e2943d60379223c1b34ab137e5c31759829296f47a686f2c0c090968e6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: INDCMP

**Raw Source File**: `data/docs/c64ref/kernal-api/indcmp.md`
**SHA256**: `e107f2e2943d60379223c1b34ab137e5c31759829296f47a686f2c0c090968e6`

## Summary




# INDCMP —  ($FF7A)

## Panoramica
La routine KERNAL `INDCMP` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF7A`
- **Chiamata**: `JSR INDCMP` o `SYS 65402`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine compares .A to the number held in a memory
on in a specified bank. In preparing to call EMDCMP,
 two-byte zero-page pointer with the address of the
on with which the accumulator is to be compared (or
he...
