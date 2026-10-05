---
id: src-e632-input-from-screen-or-keyboard
type: source
title: 'Source Summary: input from screen or keyboard'
aliases:
- input from screen or keyboard
- e632-input-from-screen-or-keyboard.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e632-input-from-screen-or-keyboard.md
  sha256: c18d07567277ec3891ffe42249ad4f79dfd82e2784a9bdd2254662f063a6d27d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: input from screen or keyboard

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e632-input-from-screen-or-keyboard.md`
**SHA256**: `c18d07567277ec3891ffe42249ad4f79dfd82e2784a9bdd2254662f063a6d27d`

## Summary



# $E632 — input from screen or keyboard

## Disassemblatura
```assembly
.E632  98       TYA   ; copy Y
.E633  48       PHA   ; save Y
.E634  8A       TXA   ; copy X
.E635  48       PHA   ; save X
.E636  A5 D0    LDA $D0   ; input from keyboard or screen, $xx = screen, $00 = keyboard
.E638  F0 93    BEQ $E5CD   ; if keyboard go wait for key
.E63A  A4 D3    LDY $D3   ; get the cursor column
.E63C  B1 D1    LDA ($D1),Y   ; get character from the current screen line
.E63E  85 D7    STA $D7   ; sav...
