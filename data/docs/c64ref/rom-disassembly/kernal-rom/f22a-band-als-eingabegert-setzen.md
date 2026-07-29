---
title: Band als Eingabegerät setzen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f22a-band-als-eingabegert-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F22A
  address_end: $F236
  symbol: band-als-eingabegert-setzen
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F22A**: Sekundäradresse laden'
---

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