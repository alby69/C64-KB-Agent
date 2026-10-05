---
id: src-b737-perform-mid
type: source
title: 'Source Summary: perform MID$()'
aliases:
- perform MID$()
- b737-perform-mid.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b737-perform-mid.md
  sha256: ff4f16377bfcd7f4d939b7ed00fd386e5efe82db935c33fe5a100e29f4cc80b4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform MID$()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b737-perform-mid.md`
**SHA256**: `ff4f16377bfcd7f4d939b7ed00fd386e5efe82db935c33fe5a100e29f4cc80b4`

## Summary



# $B737 — perform MID$()

## Disassemblatura
```assembly
.B737  A9 FF    LDA #$FF   ; set default length = 255
.B739  85 65    STA $65   ; save default length
.B73B  20 79 00 JSR $0079   ; scan memory
.B73E  C9 29    CMP #$29   ; compare with ")"
.B740  F0 06    BEQ $B748   ; branch if = ")" (skip second byte get)
.B742  20 FD AE JSR $AEFD   ; scan for ",", else do syntax error then warm start
.B745  20 9E B7 JSR $B79E   ; get byte parameter
.B748  20 61 B7 JSR $B761   ; pull string data and b...
