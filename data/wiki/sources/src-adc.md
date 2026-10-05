---
id: src-adc
type: source
title: 'Source Summary: ADC — Add with Carry'
aliases:
- ADC — Add with Carry
- adc.md
tags:
- cpu-instructions
- opcodes
- addressing-modes
sources:
- path: data/docs/c64ref/cpu-instructions/adc.md
  sha256: 19f5d2454399b924a6ba593b02ae0bf8ad0d6ca734f9a0e93ad4191e93aa86a2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ADC — Add with Carry

**Raw Source File**: `data/docs/c64ref/cpu-instructions/adc.md`
**SHA256**: `19f5d2454399b924a6ba593b02ae0bf8ad0d6ca734f9a0e93ad4191e93aa86a2`

## Summary



# ADC — ADC — Add with Carry

## Panoramica
L'istruzione `ADC` viene descritta di seguito con dettagli operativi e tecnici.

## Dettagli Tecnici
| Attributo | Valore |
|-----------|--------|
| Categoria | `arith` |
| Formula | `A + M + C → A, C` |
| Flag alterati | `NV----ZC` |


## Modalità di Indirizzamento
| Modalità | Opcode | Byte | Cicli | Note |
|----------|--------|------|-------|------|
| X-Indexed Zero Page Indirect | `$61` | 2 | 6 | Standard |
| Zero Page | `$65` | 2 | 3 | Standard ...
