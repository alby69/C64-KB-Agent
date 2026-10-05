---
id: src-ae86-get-arithmetic-element-the-get-arithmetic-element-vector-is-initialised-to-point-here
type: source
title: 'Source Summary: get arithmetic element, the get arithmetic element vector
  is initialised to point here'
aliases:
- get arithmetic element, the get arithmetic element vector is initialised to point
  here
- ae86-get-arithmetic-element-the-get-arithmetic-element-vector-is-initialised-to-point-here.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae86-get-arithmetic-element-the-get-arithmetic-element-vector-is-initialised-to-point-here.md
  sha256: f13548e8e770d237c79aac17d7c98ca7a4fa7c01231582385a91be2e17b834fb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get arithmetic element, the get arithmetic element vector is initialised to point here

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ae86-get-arithmetic-element-the-get-arithmetic-element-vector-is-initialised-to-point-here.md`
**SHA256**: `f13548e8e770d237c79aac17d7c98ca7a4fa7c01231582385a91be2e17b834fb`

## Summary



# $AE86 — get arithmetic element, the get arithmetic element vector is initialised to point here

## Disassemblatura
```assembly
.AE86  A9 00    LDA #$00   ; clear byte
.AE88  85 0D    STA $0D   ; clear data type flag, $FF = string, $00 = numeric
.AE8A  20 73 00 JSR $0073   ; increment and scan memory
.AE8D  B0 03    BCS $AE92   ; branch if not numeric character else numeric string found (e.g. 123)
.AE8F  4C F3 BC JMP $BCF3   ; get FAC1 from string and return get value from line .. continued w...
