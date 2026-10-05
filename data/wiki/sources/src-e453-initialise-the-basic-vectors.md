---
id: src-e453-initialise-the-basic-vectors
type: source
title: 'Source Summary: initialise the BASIC vectors'
aliases:
- initialise the BASIC vectors
- e453-initialise-the-basic-vectors.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e453-initialise-the-basic-vectors.md
  sha256: db50776f77144a1f42ef123adac03a570000c391eaed543f44405fe96fae5191
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initialise the BASIC vectors

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e453-initialise-the-basic-vectors.md`
**SHA256**: `db50776f77144a1f42ef123adac03a570000c391eaed543f44405fe96fae5191`

## Summary



# $E453 — initialise the BASIC vectors

## Disassemblatura
```assembly
.E453  A2 0B    LDX #$0B   ; set byte count
.E455  BD 47 E4 LDA $E447,X   ; get byte from table
.E458  9D 00 03 STA $0300,X   ; save byte to RAM
.E45B  CA       DEX   ; decrement index
.E45C  10 F7    BPL $E455   ; loop if more to do
.E45E  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E453**: set byte count
- **$E455**: get byte from table
- **$E458**: save byte to RAM
- **$E45B**: decrement index
- **$...
