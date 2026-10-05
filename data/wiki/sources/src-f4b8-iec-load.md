---
id: src-f4b8-iec-load
type: source
title: 'Source Summary: IEC-Load'
aliases:
- IEC-Load
- f4b8-iec-load.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f4b8-iec-load.md
  sha256: 2dc63cf4cb9f1301f991520a1a4fa16d163ddad4de8d33852f70cc28668e22f9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: IEC-Load

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f4b8-iec-load.md`
**SHA256**: `2dc63cf4cb9f1301f991520a1a4fa16d163ddad4de8d33852f70cc28668e22f9`

## Summary



# $F4B8 — IEC-Load

## Disassemblatura
```assembly
.F4B8  A4 B7    LDY $B7   ; Länge des Filenamens laden
.F4BA  D0 03    BNE $F4BF   ; ungleich Null, dann ok
.F4BC  4C 10 F7 JMP $F710   ; 'MISSING FILENAME'
.F4BF  A6 B9    LDX $B9   ; Sekundäradresse laden
.F4C1  20 AF F5 JSR $F5AF   ; 'SEARCHING FOR' (filename)
.F4C4  A9 60    LDA #$60   ; Sekundäradresse Null laden (für OPEN)
.F4C6  85 B9    STA $B9   ; und speichern
.F4C8  20 D5 F3 JSR $F3D5   ; File auf IEC-Bus eröffnen
.F4CB  A5 BA    LD...
