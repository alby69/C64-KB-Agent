---
title: find specific tape header
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f7ea-bandheader-nach-namen-suchen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F7EA
  address_end: $F80C
  symbol: find-specific-tape-header
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F7EA**: find tape header, exit with header in buffer'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F7EA**: nächsten Bandheader suchen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F7EA — find specific tape header

## Disassemblatura
```assembly
.F7EA  20 2C F7 JSR $F72C   ; find tape header, exit with header in buffer
.F7ED  B0 1D    BCS $F80C   ; just exit if error
.F7EF  A0 05    LDY #$05   ; index to name
.F7F1  84 9F    STY $9F   ; save as tape buffer index
.F7F3  A0 00    LDY #$00   ; clear Y
.F7F5  84 9E    STY $9E   ; save as name buffer index
.F7F7  C4 B7    CPY $B7   ; compare with file name length
.F7F9  F0 10    BEQ $F80B   ; ok exit if match
.F7FB  B1 BB    LDA ($BB),Y   ; get file name byte
.F7FD  A4 9F    LDY $9F   ; get index to tape buffer
.F7FF  D1 B2    CMP ($B2),Y   ; compare with tape header name byte
.F801  D0 E7    BNE $F7EA   ; if no match go get next header
.F803  E6 9E    INC $9E   ; else increment name buffer index
.F805  E6 9F    INC $9F   ; increment tape buffer index
.F807  A4 9E    LDY $9E   ; get name buffer index
.F809  D0 EC    BNE $F7F7   ; loop, branch always
.F80B  18       CLC   ; flag ok
.F80C  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F7EA**: find tape header, exit with header in buffer
- **$F7ED**: just exit if error
- **$F7EF**: index to name
- **$F7F1**: save as tape buffer index
- **$F7F3**: clear Y
- **$F7F5**: save as name buffer index
- **$F7F7**: compare with file name length
- **$F7F9**: ok exit if match
- **$F7FB**: get file name byte
- **$F7FD**: get index to tape buffer
- **$F7FF**: compare with tape header name byte
- **$F801**: if no match go get next header
- **$F803**: else increment name buffer index
- **$F805**: increment tape buffer index
- **$F807**: get name buffer index
- **$F809**: loop, branch always
- **$F80B**: flag ok

### Commodore-64-intern-Buch (Commodore)
- **$F7EA**: nächsten Bandheader suchen
- **$F7ED**: verzweige falls EOT (fertig)
- **$F7EF**: Offset für Filenamen im Header
- **$F7F1**: und speichern
- **$F7F3**: Zähler für Länge des Filena- mens auf Null setzen
- **$F7F5**: und Zähler speichern
- **$F7F7**: mit Länge des gesuchten Namens vergleichen
- **$F7F9**: gleich, dann gefunden
- **$F7FB**: Buchstaben des Filenamens
- **$F7FD**: Position im Header laden
- **$F7FF**: mit Filenamen im Header vergleichen
- **$F801**: verzweige falls ungleich, dann nächsten Header testen
- **$F803**: Zähler für Filenamen erhöhen
- **$F805**: Zeiger auf Position im Header erhöhen
- **$F807**: Zähler für Filenamen laden
- **$F809**: unbedingter Sprung
- **$F80B**: Carry =0 (ok Kennzeichen)
- **$F80C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*