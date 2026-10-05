---
id: src-f84a-programm-vom-band-laden
type: source
title: 'Source Summary: Programm vom Band laden'
aliases:
- Programm vom Band laden
- f84a-programm-vom-band-laden.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f84a-programm-vom-band-laden.md
  sha256: 265372d6f2d8ed9dbd7f5ff3aa538409a114cfdc69b1e5cbbf91c4e227e3ec5e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Programm vom Band laden

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f84a-programm-vom-band-laden.md`
**SHA256**: `265372d6f2d8ed9dbd7f5ff3aa538409a114cfdc69b1e5cbbf91c4e227e3ec5e`

## Summary



# $F84A — Programm vom Band laden

## Disassemblatura
```assembly
.F84A  20 17 F8 JSR $F817   ; wartet auf Play-Taste
.F84D  B0 1F    BCS $F86E   ; STOP-Taste gedrückt ?
.F84F  78       SEI   ; Interrupt verhindern
.F850  A9 00    LDA #$00   ; Arbeitsspeicher für IRQ- Routine löschen
.F852  85 AA    STA $AA   ; Eingabebytespeicher (read)
.F854  85 B4    STA $B4   ; Band Hilfszeiger
.F856  85 B0    STA $B0   ; Kassetten Zeitkonstante
.F858  85 9E    STA $9E   ; Korrekturzähler Pass 1
.F85A  85 ...
