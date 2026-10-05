---
id: src-membot
type: source
title: 'Source Summary: Execution FE34/FE82-FE42/FE90'
aliases:
- Execution FE34/FE82-FE42/FE90
- membot.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/membot.md
  sha256: f51821898b722e1ad4ab122d40e652fa9e0047e5302ad3d68232d5634930251d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Execution FE34/FE82-FE42/FE90

**Raw Source File**: `data/docs/c64ref/kernal-api/membot.md`
**SHA256**: `f51821898b722e1ad4ab122d40e652fa9e0047e5302ad3d68232d5634930251d`

## Summary



# MEMBOT — Execution FE34/FE82-FE42/FE90 ($FE34)

## Panoramica
La routine KERNAL `MEMBOT` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FE34`
- **Chiamata**: `JSR MEMBOT` o `SYS 65076`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal MEMBOT vector at FF9C.

 carry is clear at entry, set (0281), the pointer to the
 of memory, from the X and Y registers. If carry is set at
 load X and Y registe...
