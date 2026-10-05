---
id: src-e5b4-input-from-the-keyboard-buffer
type: source
title: 'Source Summary: input from the keyboard buffer'
aliases:
- input from the keyboard buffer
- e5b4-input-from-the-keyboard-buffer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e5b4-input-from-the-keyboard-buffer.md
  sha256: 52a6420baae7d3f8b24943cd1f092609600672e246a59d193f000f41d27a1354
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: input from the keyboard buffer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e5b4-input-from-the-keyboard-buffer.md`
**SHA256**: `52a6420baae7d3f8b24943cd1f092609600672e246a59d193f000f41d27a1354`

## Summary



# $E5B4 — input from the keyboard buffer

## Disassemblatura
```assembly
.E5B4  AC 77 02 LDY $0277   ; get the current character from the buffer
.E5B7  A2 00    LDX #$00   ; clear the index
.E5B9  BD 78 02 LDA $0278,X   ; get the next character,X from the buffer
.E5BC  9D 77 02 STA $0277,X   ; save it as the current character,X in the buffer
.E5BF  E8       INX   ; increment the index
.E5C0  E4 C6    CPX $C6   ; compare it with the keyboard buffer index
.E5C2  D0 F5    BNE $E5B9   ; loop if mo...
