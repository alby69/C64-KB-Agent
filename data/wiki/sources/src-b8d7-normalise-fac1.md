---
id: src-b8d7-normalise-fac1
type: source
title: 'Source Summary: normalise FAC1'
aliases:
- normalise FAC1
- b8d7-normalise-fac1.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b8d7-normalise-fac1.md
  sha256: 39978b0dd011362d0faf4bdf676f4943ada5b43f5da892107ee9a0d2a2d4eaed
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: normalise FAC1

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b8d7-normalise-fac1.md`
**SHA256**: `39978b0dd011362d0faf4bdf676f4943ada5b43f5da892107ee9a0d2a2d4eaed`

## Summary



# $B8D7 — normalise FAC1

## Disassemblatura
```assembly
.B8D7  A0 00    LDY #$00   ; clear Y
.B8D9  98       TYA   ; clear A
.B8DA  18       CLC   ; clear carry for add
.B8DB  A6 62    LDX $62   ; get FAC1 mantissa 1
.B8DD  D0 4A    BNE $B929   ; if not zero normalise FAC1
.B8DF  A6 63    LDX $63   ; get FAC1 mantissa 2
.B8E1  86 62    STX $62   ; save FAC1 mantissa 1
.B8E3  A6 64    LDX $64   ; get FAC1 mantissa 3
.B8E5  86 63    STX $63   ; save FAC1 mantissa 2
.B8E7  A6 65    LDX $65   ; g...
