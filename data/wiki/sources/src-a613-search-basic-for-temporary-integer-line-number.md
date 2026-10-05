---
id: src-a613-search-basic-for-temporary-integer-line-number
type: source
title: 'Source Summary: search BASIC for temporary integer line number'
aliases:
- search BASIC for temporary integer line number
- a613-search-basic-for-temporary-integer-line-number.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a613-search-basic-for-temporary-integer-line-number.md
  sha256: eeaa82dd5fb429c4fa22306ecc5e74f75999833c7ccb3d30d7b01a461e164d67
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: search BASIC for temporary integer line number

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a613-search-basic-for-temporary-integer-line-number.md`
**SHA256**: `eeaa82dd5fb429c4fa22306ecc5e74f75999833c7ccb3d30d7b01a461e164d67`

## Summary



# $A613 — search BASIC for temporary integer line number

## Disassemblatura
```assembly
.A613  A5 2B    LDA $2B   ; get start of memory low byte
.A615  A6 2C    LDX $2C   ; get start of memory high byte
```


## Commenti

### Original Disassembly (—)
- **$A613**: get start of memory low byte
- **$A615**: get start of memory high byte

### Commodore-64-intern-Buch (Commodore)
- **$A613**: Zeiger auf BASIC-
- **$A615**: Programmstart laden
- **$A617**: Zähler setzen
- **$A619**: BASIC-Programms...
