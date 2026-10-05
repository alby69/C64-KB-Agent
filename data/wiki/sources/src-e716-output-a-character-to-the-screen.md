---
id: src-e716-output-a-character-to-the-screen
type: source
title: 'Source Summary: output a character to the screen'
aliases:
- output a character to the screen
- e716-output-a-character-to-the-screen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e716-output-a-character-to-the-screen.md
  sha256: fab6a50655d600767dab56fdfe8a3f9fbd8b09b3bf578259a3f081856b82e2a9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: output a character to the screen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e716-output-a-character-to-the-screen.md`
**SHA256**: `fab6a50655d600767dab56fdfe8a3f9fbd8b09b3bf578259a3f081856b82e2a9`

## Summary



# $E716 — output a character to the screen

## Disassemblatura
```assembly
.E716  48       PHA   ; save character
.E717  85 D7    STA $D7   ; save temporary last character
.E719  8A       TXA   ; copy X
.E71A  48       PHA   ; save X
.E71B  98       TYA   ; copy Y
.E71C  48       PHA   ; save Y
.E71D  A9 00    LDA #$00   ; clear A
.E71F  85 D0    STA $D0   ; clear input from keyboard or screen, $xx = screen, $00 = keyboard
.E721  A4 D3    LDY $D3   ; get cursor column
.E723  A5 D7    LDA $D7  ...
