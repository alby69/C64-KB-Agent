---
id: src-cbm1541mem
type: source
title: 'Source Summary: Commodore 1541 drive memory map'
aliases:
- Commodore 1541 drive memory map
- cbm1541mem.md
tags:
- basic
- memory management
- sprite programming
- assembly
sources:
- path: data/docs/sta_c64_org/cbm1541mem.md
  sha256: aa3f85a44ec28fad11fda2de3787dcadcb4f4b3bfd75b7c0cd3d7dc7de8106ff
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 1541 drive memory map

**Raw Source File**: `data/docs/sta_c64_org/cbm1541mem.md`
**SHA256**: `aa3f85a44ec28fad11fda2de3787dcadcb4f4b3bfd75b7c0cd3d7dc7de8106ff`

## Summary



# Commodore 1541 drive memory map

| **Address** | Description   | 
|---|---|
| **$0000-$00FF Zero page** |  | 
| $0000 | Buffer #0 command and status registers. Bits: Bits #0-#6: Status or command code. Bit #7: 0 = Job finished, register contains status code; 1 = Job to be executed, register contains command code. Values: $00: "24,READ ERROR" (only during disk format). $01: "00,OK" (no error). $02: "20,READ ERROR". $03: "21,READ ERROR". $04: "22,READ ERROR". $05: "23,READ ERROR". $06: "24,REA...
