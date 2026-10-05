---
id: src-setbnk
type: source
title: 'Source Summary: SETBNK'
aliases:
- SETBNK
- setbnk.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/setbnk.md
  sha256: ee6c5b98055df0f29f624b5edea3ec37837c6f5bc7445bd56d68fe1668ff2ea6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SETBNK

**Raw Source File**: `data/docs/c64ref/kernal-api/setbnk.md`
**SHA256**: `ee6c5b98055df0f29f624b5edea3ec37837c6f5bc7445bd56d68fe1668ff2ea6`

## Summary




# SETBNK —  ($FF68)

## Panoramica
La routine KERNAL `SETBNK` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF68`
- **Chiamata**: `JSR SETBNK` o `SYS 65384`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
ernal routine establishes the current memory bank from
data will be read or to which data will be written dur-
ad/save operations, as well as the bank where the file-
or the I/O operations can be found. Call t...
