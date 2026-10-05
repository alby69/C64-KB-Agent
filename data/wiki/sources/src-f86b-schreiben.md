---
id: src-f86b-schreiben
type: source
title: 'Source Summary: schreiben'
aliases:
- schreiben
- f86b-schreiben.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f86b-schreiben.md
  sha256: 3c8ad3f32711998e2c4bfa7ee9101930f4315de060ecb47064c75bdf8979c48a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: schreiben

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f86b-schreiben.md`
**SHA256**: `3c8ad3f32711998e2c4bfa7ee9101930f4315de060ecb47064c75bdf8979c48a`

## Summary



# $F86B — schreiben

## Disassemblatura
```assembly
.F86B  20 38 F8 JSR $F838   ; wartet auf Record & Play Taste
.F86E  B0 6C    BCS $F8DC   ; verzweige falls STOP-Taste gedrückt
.F870  78       SEI   ; Interrupt verhindern
.F871  A9 82    LDA #$82   ; Bitwert für IRQ bei Unterlauf von Timer B
.F873  A2 08    LDX #$08   ; Nummer des IRQ-Vektors, $FC6A
.F875  A0 7F    LDY #$7F   ; Bitwert für alle IRQs sperren
.F877  8C 0D DC STY $DC0D   ; Wert schreiben
.F87A  8D 0D DC STA $DC0D   ; und neu se...
