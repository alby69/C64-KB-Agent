---
id: jmp
type: entity
title: JMP — Jump
aliases:
- JMP — Jump
tags:
- opcodes
- addressing-modes
- cpu-instructions
sources:
- path: data/docs/c64ref/cpu-instructions/jmp.md
  sha256: 1bbb43a4d45b502f2df2e0333db3a6d6c2b71bd75239e69330f23a281388d1ac
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-jmp
---

# JMP — Jump



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

## Descrizione
JMP Indirect
     This instruction establishes a new value for the program counter.
     It affects only the program counter in the microprocessor and affects no flags in the status register.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-jmp]]
