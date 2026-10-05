---
id: src-rts
type: source
title: 'Source Summary: RTS — Return from Subroutine'
aliases:
- RTS — Return from Subroutine
- rts.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/rts.md
  sha256: ba1435af35a83eaa1c0882c5c84d490854e9678eff4e21ea16224623526e76bc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RTS — Return from Subroutine

**Raw Source File**: `data/docs/c64ref/cpu-instructions/rts.md`
**SHA256**: `ba1435af35a83eaa1c0882c5c84d490854e9678eff4e21ea16224623526e76bc`

## Summary



# RTS — RTS — Return from Subroutine

## Panoramica
L'istruzione `RTS` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `PC↑, PC + 1 → PC` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$60` | 1 | 6 | Standard |

## Descrizione
Return From Subroutine
      This ins...
