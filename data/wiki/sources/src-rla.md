---
id: src-rla
type: source
title: 'Source Summary: RLA'
aliases:
- RLA
- rla.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/rla.md
  sha256: 33eeb1780e9c152ab820fdad312d209323acef51db4b84c3a54cf8f7d774c3c1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RLA

**Raw Source File**: `data/docs/c64ref/cpu-instructions/rla.md`
**SHA256**: `33eeb1780e9c152ab820fdad312d209323acef51db4b84c3a54cf8f7d774c3c1`

## Summary



# RLA — RLA

## Panoramica
L'istruzione `RLA` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `C ← /M7...M0/ ← C, A ∧ M → A` |
| Flag alterati | `*-----**` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$23` | 2 | 8 | Non documentata |
| Zero Page | `$27` | 2 | 5 | Non doc...
