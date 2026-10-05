---
id: src-b849-add-05-to-fac1-round-fac1
type: source
title: 'Source Summary: add 0.5 to FAC1 (round FAC1)'
aliases:
- add 0.5 to FAC1 (round FAC1)
- b849-add-05-to-fac1-round-fac1.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b849-add-05-to-fac1-round-fac1.md
  sha256: e0ef17903fb3ea784cc93ec64fe430aff27d0249a07621dd102c27ad329af743
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: add 0.5 to FAC1 (round FAC1)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b849-add-05-to-fac1-round-fac1.md`
**SHA256**: `e0ef17903fb3ea784cc93ec64fe430aff27d0249a07621dd102c27ad329af743`

## Summary



# $B849 — add 0.5 to FAC1 (round FAC1)

## Disassemblatura
```assembly
.B849  A9 11    LDA #$11   ; set 0.5 pointer low byte
.B84B  A0 BF    LDY #$BF   ; set 0.5 pointer high byte
.B84D  4C 67 B8 JMP $B867   ; add (AY) to FAC1
```


## Commenti

### Original Disassembly (—)
- **$B849**: set 0.5 pointer low byte
- **$B84B**: set 0.5 pointer high byte
- **$B84D**: add (AY) to FAC1

### Commodore-64-intern-Buch (Commodore)
- **$B849**: Zeiger auf
- **$B84B**: Konstante 0.5
- **$B84D**: FAC = FAC ...
