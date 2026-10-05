---
id: src-memtop
type: source
title: 'Source Summary: Execution FE25/FE73-FE33/FE81'
aliases:
- Execution FE25/FE73-FE33/FE81
- memtop.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/memtop.md
  sha256: 602c45fca40d3d5c1f277c8d870d803fe2f26dacca45182020c5b9e68c3a184a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Execution FE25/FE73-FE33/FE81

**Raw Source File**: `data/docs/c64ref/kernal-api/memtop.md`
**SHA256**: `602c45fca40d3d5c1f277c8d870d803fe2f26dacca45182020c5b9e68c3a184a`

## Summary



# MEMTOP — Execution FE25/FE73-FE33/FE81 ($FE25)

## Panoramica
La routine KERNAL `MEMTOP` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FE25`
- **Chiamata**: `JSR MEMTOP` o `SYS 65061`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal MEMTOP vector at FF99; alternate entry at
E75 by JSR at F2B2/F377 in Close Logical File for RS-
SR at F468/F527 in Open RS-232 Device; alternate entry
D/FE7B by ...
