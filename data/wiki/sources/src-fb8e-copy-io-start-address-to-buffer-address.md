---
id: src-fb8e-copy-io-start-address-to-buffer-address
type: source
title: 'Source Summary: copy I/O start address to buffer address'
aliases:
- copy I/O start address to buffer address
- fb8e-copy-io-start-address-to-buffer-address.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fb8e-copy-io-start-address-to-buffer-address.md
  sha256: e5cf2dca0d530d17ffc302bf1165088725d322ee6cb58cc4ceb054a0fc815c55
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: copy I/O start address to buffer address

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fb8e-copy-io-start-address-to-buffer-address.md`
**SHA256**: `e5cf2dca0d530d17ffc302bf1165088725d322ee6cb58cc4ceb054a0fc815c55`

## Summary



# $FB8E — copy I/O start address to buffer address

## Disassemblatura
```assembly
.FB8E  A5 C2    LDA $C2   ; get I/O start address high byte
.FB90  85 AD    STA $AD   ; set buffer address high byte
.FB92  A5 C1    LDA $C1   ; get I/O start address low byte
.FB94  85 AC    STA $AC   ; set buffer address low byte
.FB96  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FB8E**: get I/O start address high byte
- **$FB90**: set buffer address high byte
- **$FB92**: get I/O start a...
