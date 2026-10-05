---
id: src-b218-search-array-table-for-this-array-name
type: source
title: 'Source Summary: SEARCH ARRAY TABLE FOR THIS ARRAY NAME'
aliases:
- SEARCH ARRAY TABLE FOR THIS ARRAY NAME
- b218-search-array-table-for-this-array-name.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b218-search-array-table-for-this-array-name.md
  sha256: f3cc775bd96ca3d4f1bd56153f4eb100d8321050ebf32dd7491d7658ae954b10
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SEARCH ARRAY TABLE FOR THIS ARRAY NAME

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b218-search-array-table-for-this-array-name.md`
**SHA256**: `f3cc775bd96ca3d4f1bd56153f4eb100d8321050ebf32dd7491d7658ae954b10`

## Summary



# $B218 — SEARCH ARRAY TABLE FOR THIS ARRAY NAME

## Disassemblatura
```assembly
.B218  A6 2F    LDX $2F   ; (A,X) = START OF ARRAY TABLE
.B21A  A5 30    LDA $30
.B21C  86 5F    STX $5F   ; USE LOWTR FOR RUNNING POINTER
.B21E  85 60    STA $60
.B220  C5 32    CMP $32   ; DID WE REACH THE END OF ARRAYS YET?
.B222  D0 04    BNE $B228   ; NO, KEEP SEARCHING
.B224  E4 31    CPX $31
.B226  F0 39    BEQ $B261   ; YES, THIS IS A NEW ARRAY NAME
.B228  A0 00    LDY #$00   ; POINT AT 1ST CHAR OF ARRAY N...
