---
id: src-asr
type: source
title: 'Source Summary: ASR'
aliases:
- ASR
- asr.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/asr.md
  sha256: f6be1562308cbdb6c7f8e479f7f332c5ca29df7daa1a6d18a3bb9fcd9cb42164
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ASR

**Raw Source File**: `data/docs/c64ref/cpu-instructions/asr.md`
**SHA256**: `f6be1562308cbdb6c7f8e479f7f332c5ca29df7daa1a6d18a3bb9fcd9cb42164`

## Summary



# ASR — ASR

## Panoramica
L'istruzione `ASR` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `(A ∧ M) / 2 → A            ## Ormston, groepaz: ALR` |
| Flag alterati | `0-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Immediate | `$4B` | 2 | 2 | Non documentata |

## Descrizione
"AND" then Logica...
