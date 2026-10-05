---
id: src-chkin
type: source
title: 'Source Summary: Execution F20E/F2C7-F236/F2EF'
aliases:
- Execution F20E/F2C7-F236/F2EF
- chkin.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/chkin.md
  sha256: e9d2e1efb0fb573458b9bc153f3ffa6782174e4f2a33fc347e01d570a553204f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Execution F20E/F2C7-F236/F2EF

**Raw Source File**: `data/docs/c64ref/kernal-api/chkin.md`
**SHA256**: `e9d2e1efb0fb573458b9bc153f3ffa6782174e4f2a33fc347e01d570a553204f`

## Summary



# CHKIN — Execution F20E/F2C7-F236/F2EF ($F20E)

## Panoramica
La routine KERNAL `CHKIN` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F20E`
- **Chiamata**: `JSR CHKIN` o `SYS 61966`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**:
ct JMP through (031E) from Kernal CHKIN vector at FFC6.

 current logical file passed in the X register is in the
l file number table, obtain its corresponding device num-
d second...
