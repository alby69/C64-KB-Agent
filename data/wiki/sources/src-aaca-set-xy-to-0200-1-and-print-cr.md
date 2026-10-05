---
id: src-aaca-set-xy-to-0200-1-and-print-cr
type: source
title: 'Source Summary: set XY to $0200 - 1 and print [CR]'
aliases:
- set XY to $0200 - 1 and print [CR]
- aaca-set-xy-to-0200-1-and-print-cr.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aaca-set-xy-to-0200-1-and-print-cr.md
  sha256: 0192fb5fe4d554bb1dea744070c33a2230aaa2d28812bb28fa3bb08a20e91d45
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set XY to $0200 - 1 and print [CR]

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aaca-set-xy-to-0200-1-and-print-cr.md`
**SHA256**: `0192fb5fe4d554bb1dea744070c33a2230aaa2d28812bb28fa3bb08a20e91d45`

## Summary



# $AACA — set XY to $0200 - 1 and print [CR]

## Disassemblatura
```assembly
.AACA  A9 00    LDA #$00   ; clear A
.AACC  9D 00 02 STA $0200,X   ; clear first byte of input buffer
.AACF  A2 FF    LDX #$FF   ; $0200 - 1 low byte
.AAD1  A0 01    LDY #$01   ; $0200 - 1 high byte
.AAD3  A5 13    LDA $13   ; get current I/O channel
.AAD5  D0 10    BNE $AAE7   ; exit if not default channel
```


## Commenti

### Original Disassembly (—)
- **$AACA**: clear A
- **$AACC**: clear first byte of input buff...
