---
id: src-lkupla
type: source
title: 'Source Summary: LKUPLA'
aliases:
- LKUPLA
- lkupla.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/lkupla.md
  sha256: ca7d54a845131b5f32704cd052531406cb84cf573474d48302c17865863be585
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LKUPLA

**Raw Source File**: `data/docs/c64ref/kernal-api/lkupla.md`
**SHA256**: `ca7d54a845131b5f32704cd052531406cb84cf573474d48302c17865863be585`

## Summary




# LKUPLA —  ($FF59)

## Panoramica
La routine KERNAL `LKUPLA` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF59`
- **Chiamata**: `JSR LKUPLA` o `SYS 65369`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine checks whether a specified logical file number is
tly used. Call the routine with the accumulator holding
gical-file-number value in question. If that file number is
ble, the carry bit will be set upon ...
