---
id: src-pfkey
type: source
title: 'Source Summary: PFKEY'
aliases:
- PFKEY
- pfkey.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/pfkey.md
  sha256: 66aedd22a3764d01cbb1bea21522ee655a6635c11631a75ba1a6890df98d4f7d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PFKEY

**Raw Source File**: `data/docs/c64ref/kernal-api/pfkey.md`
**SHA256**: `66aedd22a3764d01cbb1bea21522ee655a6635c11631a75ba1a6890df98d4f7d`

## Summary




# PFKEY —  ($FF65)

## Panoramica
La routine KERNAL `PFKEY` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF65`
- **Chiamata**: `JSR PFKEY` o `SYS 65381`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
ou turn on the 128, its function keys are predefined.
ng F3 prints DIRECTORY, F7 holds the LIST command,
 on. The PFKEY Kernal routine assigns a new definition
 of the 10 programmable function keys (F1-F8, SHIFT-...
