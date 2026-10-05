---
id: src-cbm64mctime
type: source
title: 'Source Summary: Commodore 64 machine instruction execution times'
aliases:
- Commodore 64 machine instruction execution times
- cbm64mctime.md
tags:
- assembly
sources:
- path: data/docs/sta_c64_org/cbm64mctime.md
  sha256: 7d14bd09d493ae855f1b04c29e1c9687da1e2d18a594fccdbe118e6c39d5f6f2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 machine instruction execution times

**Raw Source File**: `data/docs/sta_c64_org/cbm64mctime.md`
**SHA256**: `7d14bd09d493ae855f1b04c29e1c9687da1e2d18a594fccdbe118e6c39d5f6f2`

## Summary



# Commodore 64 machine instruction execution times

| Instruction | - | # | ZP | ZP,X | ZP,Y | (ZP,X) | (ZP),Y | ABS | ABS,X | ABS,Y | (ABS) | REL | A | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ADC |  | 2 | 3 | 4 |  | 6 | 5+ | 4 | 4+ | 4+ |  |  |  | 
| AND |  | 2 | 3 | 4 |  | 6 | 5+ | 4 | 4+ | 4+ |  |  |  | 
| ASL |  |  | 5 | 6 |  |  |  | 6 | 7 |  |  |  | 2 | 
| BCC |  |  |  |  |  |  |  |  |  |  |  | 2+* |  | 
| BCS |  |  |  |  |  |  |  |  |  |  |  | 2+* |  | 
| BEQ |  |  |...
