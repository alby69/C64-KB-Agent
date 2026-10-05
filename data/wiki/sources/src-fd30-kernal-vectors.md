---
id: src-fd30-kernal-vectors
type: source
title: 'Source Summary: kernal vectors'
aliases:
- kernal vectors
- fd30-kernal-vectors.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd30-kernal-vectors.md
  sha256: 20e9e3585f51957897ae5855d55e967473d7ecfeac3775a56120c1a68a544d44
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: kernal vectors

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fd30-kernal-vectors.md`
**SHA256**: `20e9e3585f51957897ae5855d55e967473d7ecfeac3775a56120c1a68a544d44`

## Summary



# $FD30 — kernal vectors

## Disassemblatura
```assembly
.FD30  31 EA   ; $0314 IRQ vector
.FD32  66 FE   ; $0316 BRK vector
.FD34  47 FE   ; $0318 NMI vector
.FD36  4A F3   ; $031A open a logical file
.FD38  91 F2   ; $031C close a specified logical file
.FD3A  0E F2   ; $031E open channel for input
.FD3C  50 F2   ; $0320 open channel for output
.FD3E  33 F3   ; $0322 close input and output channels
.FD40  57 F1   ; $0324 input character from channel
.FD42  CA F1   ; $0326 output character to...
