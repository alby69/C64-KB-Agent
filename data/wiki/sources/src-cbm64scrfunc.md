---
id: src-cbm64scrfunc
type: source
title: 'Source Summary: Commodore 64 screen functions'
aliases:
- Commodore 64 screen functions
- cbm64scrfunc.md
tags:
- graphics
- sprite programming
- assembly
sources:
- path: data/docs/sta_c64_org/cbm64scrfunc.md
  sha256: ae2f9c72e7743a2c4d3f26eae893f271ed31d79d0b931120b24e199c45c7e104
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 screen functions

**Raw Source File**: `data/docs/sta_c64_org/cbm64scrfunc.md`
**SHA256**: `ae2f9c72e7743a2c4d3f26eae893f271ed31d79d0b931120b24e199c45c7e104`

## Summary



# Commodore 64 screen functions

| **Address** | Function | 
|---|---|
| $E4DA | Put current color,   at memory address $0286, into color RAM, pointed at by memory addresses   $00F3-$00F4. Input: Y = Column number. Output: – Used registers: A. | 
| $E505 | Fetch number of screen rows and   columns. Input: – Output: X = Number of columns (40); Y = Number of rows (25). Used registers: X, Y. | 
| $E50A | Save or restore cursor position. Input: Carry: 0 = Restore from input, 1 = Save to output; X ...
