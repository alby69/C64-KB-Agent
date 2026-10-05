---
id: src-f2f2-close-file-index-x
type: source
title: 'Source Summary: close file index X'
aliases:
- close file index X
- f2f2-close-file-index-x.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f2f2-close-file-index-x.md
  sha256: d8290fd4e21f6ac9138bae82dcdf4d7a58b7bb6e2603cfb08315ca26d532f268
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: close file index X

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f2f2-close-file-index-x.md`
**SHA256**: `d8290fd4e21f6ac9138bae82dcdf4d7a58b7bb6e2603cfb08315ca26d532f268`

## Summary



# $F2F2 — close file index X

## Disassemblatura
```assembly
.F2F2  AA       TAX   ; copy index to file to close
.F2F3  C6 98    DEC $98   ; decrement the open file count
.F2F5  E4 98    CPX $98   ; compare the index with the open file count
.F2F7  F0 14    BEQ $F30D   ; exit if equal, last entry was closing file else entry was not last in list so copy last table entry file details over the details of the closing one
.F2F9  A4 98    LDY $98   ; get the open file count as index
.F2FB  B9 59 02 ...
