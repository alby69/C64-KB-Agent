---
id: src-cbm64kbdfunc
type: source
title: 'Source Summary: Commodore 64 keyboard functions'
aliases:
- Commodore 64 keyboard functions
- cbm64kbdfunc.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/sta_c64_org/cbm64kbdfunc.md
  sha256: 39b9cab652c7c642f77f6c012d022a5b5cdfceaba16c9689ff31da02cfd9b3cc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 keyboard functions

**Raw Source File**: `data/docs/sta_c64_org/cbm64kbdfunc.md`
**SHA256**: `39b9cab652c7c642f77f6c012d022a5b5cdfceaba16c9689ff31da02cfd9b3cc`

## Summary



# Commodore 64 keyboard functions

| **Address** | Function | 
|---|---|
| $E5B4 | Read byte from   keyboard buffer; shift keyboard buffer; decrease buffer pointer. Input: – Output: A = Byte read. Used registers: A, X, Y. | 
| $EA87 | Query keyboard; put current matrix code   into memory address $00CB, current status of shift keys into memory address   $028D and PETSCII code into keyboard buffer; handle Commodore-Shift; repeat   keys. Input: – Output: – Used registers: A, X, Y. | 
| $F142 | Re...
