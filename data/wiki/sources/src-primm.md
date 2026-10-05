---
id: src-primm
type: source
title: 'Source Summary: PRIMM'
aliases:
- PRIMM
- primm.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/primm.md
  sha256: 723ebceb4cc0dbe165be83af281db2528b880fb53ef29156a916cda6e0911a4c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PRIMM

**Raw Source File**: `data/docs/c64ref/kernal-api/primm.md`
**SHA256**: `723ebceb4cc0dbe165be83af281db2528b880fb53ef29156a916cda6e0911a4c`

## Summary




# PRIMM —  ($FF7D)

## Panoramica
La routine KERNAL `PRIMM` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF7D`
- **Chiamata**: `JSR PRIMM` o `SYS 65405`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine prints the string of character codes which im-
ely follows the JSR to this routine. (You must always
his routine with JSR, never with JMP. Only JSR places the
ed address information on the stack.) The rout...
