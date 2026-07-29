---
title: TAB( (C=1) und SPC( (C=0)
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- aaf8-tab-c1-und-spc-c0
- rts
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AAF8
  address_end: $AB1C
  symbol: tab-c1-und-spc-c0
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AAF8**: Flags merken'
---

# $AAF8 — TAB( (C=1) und SPC( (C=0)

## Disassemblatura
```assembly
.AAF8  08       PHP   ; Flags merken
.AAF9  38       SEC   ; Carry setzen
.AAFA  20 F0 FF JSR $FFF0   ; Cursorposition holen
.AAFD  84 09    STY $09   ; und Spalte merken
.AAFF  20 9B B7 JSR $B79B   ; Byte-Wert holen
.AB02  C9 29    CMP #$29   ; ')' Klammer zu?
.AB04  D0 59    BNE $AB5F   ; nein: 'SYNTAX ERROR'
.AB06  28       PLP   ; Flags wiederherstellen
.AB07  90 06    BCC $AB0F   ; zu SPC(
.AB09  8A       TXA   ; TAB-Wert in Akku
.AB0A  E5 09    SBC $09   ; mit Cursorspalte vergleichen
.AB0C  90 05    BCC $AB13   ; kleiner Cursor-Position: RTS
.AB0E  AA       TAX   ; Schritte bis zum Tabulator
.AB0F  E8       INX   ; aus Zähler initialisieren
.AB10  CA       DEX   ; um 1 vermindern
.AB11  D0 06    BNE $AB19   ; =0? nein: Cursor right
.AB13  20 73 00 JSR $0073   ; nächstes Zeichen holen
.AB16  4C A2 AA JMP $AAA2   ; und weitermachen
.AB19  20 3B AB JSR $AB3B   ; Cursor right bzw. Leerzeichen
.AB1C  D0 F2    BNE $AB10   ; zum Schleifenanfang
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AAF8**: Flags merken
- **$AAF9**: Carry setzen
- **$AAFA**: Cursorposition holen
- **$AAFD**: und Spalte merken
- **$AAFF**: Byte-Wert holen
- **$AB02**: ')' Klammer zu?
- **$AB04**: nein: 'SYNTAX ERROR'
- **$AB06**: Flags wiederherstellen
- **$AB07**: zu SPC(
- **$AB09**: TAB-Wert in Akku
- **$AB0A**: mit Cursorspalte vergleichen
- **$AB0C**: kleiner Cursor-Position: RTS
- **$AB0E**: Schritte bis zum Tabulator
- **$AB0F**: aus Zähler initialisieren
- **$AB10**: um 1 vermindern
- **$AB11**: =0? nein: Cursor right
- **$AB13**: nächstes Zeichen holen
- **$AB16**: und weitermachen
- **$AB19**: Cursor right bzw. Leerzeichen
- **$AB1C**: zum Schleifenanfang

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*