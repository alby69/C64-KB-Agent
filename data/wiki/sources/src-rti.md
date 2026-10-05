---
id: src-rti
type: source
title: 'Source Summary: RTI — Return from Interrupt'
aliases:
- RTI — Return from Interrupt
- rti.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/rti.md
  sha256: 333609a19bcb99c6a35bc1e225e365236eaf9f820817aaf9dd82d62997605ca8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RTI — Return from Interrupt

**Raw Source File**: `data/docs/c64ref/cpu-instructions/rti.md`
**SHA256**: `333609a19bcb99c6a35bc1e225e365236eaf9f820817aaf9dd82d62997605ca8`

## Summary



# RTI — RTI — Return from Interrupt

## Panoramica
L'istruzione `RTI` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `P↑ PC↑` |
| Flag alterati | `NV--DIZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Implied | `$40` | 1 | 6 | Standard |

## Descrizione
Return From Interrupt
     This instruction tran...
