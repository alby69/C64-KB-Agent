---
id: src-fa60-store-character
type: source
title: 'Source Summary: # store character'
aliases:
- '# store character'
- fa60-store-character.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fa60-store-character.md
  sha256: d8db6bc704d51a9f301211acc179bced1cdcdc585a33540c08c644bee8455d91
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: # store character

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fa60-store-character.md`
**SHA256**: `d8db6bc704d51a9f301211acc179bced1cdcdc585a33540c08c644bee8455d91`

## Summary



# $FA60 — # store character

## Disassemblatura
```assembly
.FA60  20 97 FB JSR $FB97   ; new tape byte setup
.FA63  85 9C    STA $9C   ; clear byte received flag
.FA65  A2 DA    LDX #$DA   ; set timing max byte
.FA67  20 E2 F8 JSR $F8E2   ; set timing
.FA6A  A5 BE    LDA $BE   ; get copies count
.FA6C  F0 02    BEQ $FA70
.FA6E  85 A7    STA $A7   ; save receiver input bit temporary storage
.FA70  A9 0F    LDA #$0F
.FA72  24 AA    BIT $AA
.FA74  10 17    BPL $FA8D
.FA76  A5 B5    LDA $B5
.FA78...
