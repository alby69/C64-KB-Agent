---
id: src-f314-find-file-a
type: source
title: 'Source Summary: find file A'
aliases:
- find file A
- f314-find-file-a.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f314-find-file-a.md
  sha256: 88b453dcca6c5fb9733ad2c496aaca35590a7f345faaa9ef140a2585c37f2e4b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: find file A

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f314-find-file-a.md`
**SHA256**: `88b453dcca6c5fb9733ad2c496aaca35590a7f345faaa9ef140a2585c37f2e4b`

## Summary



# $F314 — find file A

## Disassemblatura
```assembly
.F314  A6 98    LDX $98   ; get the open file count
.F316  CA       DEX   ; decrement the count to give the index
.F317  30 15    BMI $F32E   ; if no files just exit
.F319  DD 59 02 CMP $0259,X   ; compare the logical file number with the table logical file number
.F31C  D0 F8    BNE $F316   ; if no match go try again
.F31E  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F314**: get the open file count
- **$F316**: decrem...
