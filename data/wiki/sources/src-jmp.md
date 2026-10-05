---
id: src-jmp
type: source
title: 'Source Summary: JMP — Jump'
aliases:
- JMP — Jump
- jmp.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/jmp.md
  sha256: 1bbb43a4d45b502f2df2e0333db3a6d6c2b71bd75239e69330f23a281388d1ac
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: JMP — Jump

**Raw Source File**: `data/docs/c64ref/cpu-instructions/jmp.md`
**SHA256**: `1bbb43a4d45b502f2df2e0333db3a6d6c2b71bd75239e69330f23a281388d1ac`

## Summary



# JMP — JMP — Jump

## Panoramica
L'istruzione `JMP` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `ctrl` |
| Formula | `[PC + 1] → PCL, [PC + 2] → PCH` |
| Flag alterati | `--------` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| Absolute | `$4C` | 3 | 3 | Standard |
| Absolute Indirect | `$6C` | 3 | 5 | Standard |

## Des...
