---
id: f22a-band-als-eingabegert-setzen
type: entity
title: Band als Eingabegerät setzen
aliases:
- Band als Eingabegerät setzen
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f22a-band-als-eingabegert-setzen.md
  sha256: 8582eaea762311885512157bbdf56e71e0a8a024176fec4312ed01955c2ef880
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f22a-band-als-eingabegert-setzen
---

# Band als Eingabegerät setzen



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
- **$F22A**: Sekundäradresse laden
- **$F22C**: vergleichemit 'Null'
- **$F22E**: verzweige wenn 'Null'
- **$F230**: sonst 'not input file'
- **$F233**: Gerätenummer für Ausgabe speichern
- **$F235**: Carry =0 (ok Kennzeichen)
- **$F236**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f22a-band-als-eingabegert-setzen]]
