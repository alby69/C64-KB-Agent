---
id: src-ba59-multiply-arg-by-a-into-result
type: source
title: 'Source Summary: MULTIPLY ARG BY (A) INTO RESULT'
aliases:
- MULTIPLY ARG BY (A) INTO RESULT
- ba59-multiply-arg-by-a-into-result.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ba59-multiply-arg-by-a-into-result.md
  sha256: 027cb83ce4df36329ebfea2aa24c7d14c7cb8357ca8b443669059ace1652cee8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: MULTIPLY ARG BY (A) INTO RESULT

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ba59-multiply-arg-by-a-into-result.md`
**SHA256**: `027cb83ce4df36329ebfea2aa24c7d14c7cb8357ca8b443669059ace1652cee8`

## Summary



# $BA59 — MULTIPLY ARG BY (A) INTO RESULT

## Disassemblatura
```assembly
.BA59  D0 03    BNE $BA5E   ; THIS BYTE NON-ZERO
.BA5B  4C 83 B9 JMP $B983   ; (A)=0, JUST SHIFT ARG RIGHT 8
.BA5E  4A       LSR   ; SHIFT BIT INTO CARRY
.BA5F  09 80    ORA #$80   ; SUPPLY SENTINEL BIT
.BA61  A8       TAY   ; REMAINING MULTIPLIER TO Y
.BA62  90 19    BCC $BA7D   ; THIS MULTIPLIER BIT = 0
.BA64  18       CLC   ; = 1, SO ADD ARG TO RESULT
.BA65  A5 29    LDA $29
.BA67  65 6D    ADC $6D
.BA69  85 29    STA...
