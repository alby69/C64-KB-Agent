---
id: src-f22a-band-als-eingabegert-setzen
type: source
title: 'Source Summary: Band als Eingabegerät setzen'
aliases:
- Band als Eingabegerät setzen
- f22a-band-als-eingabegert-setzen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f22a-band-als-eingabegert-setzen.md
  sha256: 8582eaea762311885512157bbdf56e71e0a8a024176fec4312ed01955c2ef880
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Band als Eingabegerät setzen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f22a-band-als-eingabegert-setzen.md`
**SHA256**: `8582eaea762311885512157bbdf56e71e0a8a024176fec4312ed01955c2ef880`

## Summary



# $F22A — Band als Eingabegerät setzen

## Disassemblatura
```assembly
.F22A  A6 B9    LDX $B9   ; Sekundäradresse laden
.F22C  E0 60    CPX #$60   ; vergleichemit 'Null'
.F22E  F0 03    BEQ $F233   ; verzweige wenn 'Null'
.F230  4C 0A F7 JMP $F70A   ; sonst 'not input file'
.F233  85 99    STA $99   ; Gerätenummer für Ausgabe speichern
.F235  18       CLC   ; Carry =0 (ok Kennzeichen)
.F236  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F22A**: S...
