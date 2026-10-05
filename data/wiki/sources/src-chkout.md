---
id: src-chkout
type: source
title: 'Source Summary: Execution F250/F309-F278/F331'
aliases:
- Execution F250/F309-F278/F331
- chkout.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/chkout.md
  sha256: 3873b18f72284a33b0a4a7d697d6c452cec16c6bf91805045132281f526f799e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Execution F250/F309-F278/F331

**Raw Source File**: `data/docs/c64ref/kernal-api/chkout.md`
**SHA256**: `3873b18f72284a33b0a4a7d697d6c452cec16c6bf91805045132281f526f799e`

## Summary



# CHKOUT — Execution F250/F309-F278/F331 ($F250)

## Panoramica
La routine KERNAL `CHKOUT` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F250`
- **Chiamata**: `JSR CHKOUT` o `SYS 62032`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (0320) from Kernal CHKOUT vector at
FFC9.

 logical file number passed in the accumulator at en-
 not in the logical file table, display the FILE NOT OPEN
m...
