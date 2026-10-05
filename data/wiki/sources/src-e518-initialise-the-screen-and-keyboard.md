---
id: src-e518-initialise-the-screen-and-keyboard
type: source
title: 'Source Summary: initialise the screen and keyboard'
aliases:
- initialise the screen and keyboard
- e518-initialise-the-screen-and-keyboard.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e518-initialise-the-screen-and-keyboard.md
  sha256: 63e7a5e71d3d381ce2eee84026f1521b00884660c34da2d7b6048a64851f47ce
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initialise the screen and keyboard

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e518-initialise-the-screen-and-keyboard.md`
**SHA256**: `63e7a5e71d3d381ce2eee84026f1521b00884660c34da2d7b6048a64851f47ce`

## Summary



# $E518 — initialise the screen and keyboard

## Disassemblatura
```assembly
.E518  20 A0 E5 JSR $E5A0   ; initialise the vic chip
.E51B  A9 00    LDA #$00   ; clear A
.E51D  8D 91 02 STA $0291   ; clear the shift mode switch
.E520  85 CF    STA $CF   ; clear the cursor blink phase
.E522  A9 48    LDA #$48   ; get the keyboard decode logic pointer low byte
.E524  8D 8F 02 STA $028F   ; save the keyboard decode logic pointer low byte
.E527  A9 EB    LDA #$EB   ; get the keyboard decode logic po...
