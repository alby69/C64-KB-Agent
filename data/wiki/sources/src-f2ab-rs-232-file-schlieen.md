---
id: src-f2ab-rs-232-file-schlieen
type: source
title: 'Source Summary: RS-232 File schließen'
aliases:
- RS-232 File schließen
- f2ab-rs-232-file-schlieen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f2ab-rs-232-file-schlieen.md
  sha256: c64db8e2b40e027e5d59a806fc5d94ec008689575603d48865ceb199436fab87
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: RS-232 File schließen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f2ab-rs-232-file-schlieen.md`
**SHA256**: `c64db8e2b40e027e5d59a806fc5d94ec008689575603d48865ceb199436fab87`

## Summary



# $F2AB — RS-232 File schließen

## Disassemblatura
```assembly
.F2AB  68       PLA   ; Zeiger auf Parametereintrag
.F2AC  20 F2 F2 JSR $F2F2   ; Fileeintrag in Tabelle löschen
.F2AF  20 83 F4 JSR $F483   ; CIAs für I/O rücksetzen
.F2B2  20 27 FE JSR $FE27   ; Memory-Top holen
.F2B5  A5 F8    LDA $F8   ; RS-232 Eingabepuffer HIGH-Byte laden
.F2B7  F0 01    BEQ $F2BA   ; verzweige wenn 0
.F2B9  C8       INY   ; HIGH-Byte von Memory-Top erhöhen
.F2BA  A5 FA    LDA $FA   ; RS-232 Ausgabepuffer HI...
