---
id: src-f199-get-byte-from-tape
type: source
title: 'Source Summary: get byte from tape'
aliases:
- get byte from tape
- f199-get-byte-from-tape.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f199-get-byte-from-tape.md
  sha256: ac672980fc6c1a7a6d6dc3f02e954b544faade180ee65643953e928dce710864
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get byte from tape

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f199-get-byte-from-tape.md`
**SHA256**: `ac672980fc6c1a7a6d6dc3f02e954b544faade180ee65643953e928dce710864`

## Summary



# $F199 — get byte from tape

## Disassemblatura
```assembly
.F199  20 0D F8 JSR $F80D   ; bump tape pointer
.F19C  D0 0B    BNE $F1A9   ; if not end get next byte and exit
.F19E  20 41 F8 JSR $F841   ; initiate tape read
.F1A1  B0 11    BCS $F1B4   ; exit if error flagged
.F1A3  A9 00    LDA #$00   ; clear A
.F1A5  85 A6    STA $A6   ; clear tape buffer index
.F1A7  F0 F0    BEQ $F199   ; loop, branch always
.F1A9  B1 B2    LDA ($B2),Y   ; get next byte from buffer
.F1AB  18       CLC   ; fla...
