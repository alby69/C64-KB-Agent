---
id: src-f1d7-ausgabe-auf-iec-bus
type: source
title: 'Source Summary: Ausgabe auf IEC-Bus'
aliases:
- Ausgabe auf IEC-Bus
- f1d7-ausgabe-auf-iec-bus.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1d7-ausgabe-auf-iec-bus.md
  sha256: 983ed8b64d0740b9bf637a4148c77fa5ddcce07eaa76c553402bd9c7cf7db13a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Ausgabe auf IEC-Bus

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f1d7-ausgabe-auf-iec-bus.md`
**SHA256**: `983ed8b64d0740b9bf637a4148c77fa5ddcce07eaa76c553402bd9c7cf7db13a`

## Summary



# $F1D7 — Ausgabe auf IEC-Bus

## Disassemblatura
```assembly
.F1D7  68       PLA   ; Datenbyte retten
.F1D8  4C DD ED JMP $EDDD   ; ein Byte auf IEC-Bus ausgeben
.F1DB  4A       LSR   ; Bit 0 der Ausgabekanal- Nummer ins Carry
.F1DC  68       PLA   ; Datenbyte wiederholen
.F1DD  85 9E    STA $9E   ; auszugebendes Zeichen merken
.F1DF  8A       TXA   ; X-Register
.F1E0  48       PHA   ; und Y-Register
.F1E1  98       TYA   ; auf Stack
.F1E2  48       PHA   ; retten
.F1E3  90 23    BCC $F208   ...
