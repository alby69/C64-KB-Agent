---
id: src-lkupsa
type: source
title: 'Source Summary: LKUPSA'
aliases:
- LKUPSA
- lkupsa.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/lkupsa.md
  sha256: 66de5370d267f67e3351f5dec485f80e996d8b8937c487c452f6c18f594daa33
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: LKUPSA

**Raw Source File**: `data/docs/c64ref/kernal-api/lkupsa.md`
**SHA256**: `66de5370d267f67e3351f5dec485f80e996d8b8937c487c452f6c18f594daa33`

## Summary




# LKUPSA —  ($FF5C)

## Panoramica
La routine KERNAL `LKUPSA` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF5C`
- **Chiamata**: `JSR LKUPSA` o `SYS 65372`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine checks whether a specified secondary address is
tly in use. Call the routine with .Y holding the secondary-
s value in question. If that secondary address is not
tly used, the status-register carry bit ...
