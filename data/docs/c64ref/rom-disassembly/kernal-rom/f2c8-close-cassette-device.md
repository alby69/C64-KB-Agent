---
title: close cassette device
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $F2C8
  address_end: $F2EB
  symbol: close-cassette-device
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F2C8**: Sekundäradresse laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F2C8 — close cassette device

## Disassemblatura
```assembly
.F2C8  A5 B9    LDA $B9
.F2CA  29 0F    AND #$0F
.F2CC  F0 23    BEQ $F2F1
.F2CE  20 D0 F7 JSR $F7D0
.F2D1  A9 00    LDA #$00
.F2D3  38       SEC
.F2D4  20 DD F1 JSR $F1DD
.F2D7  20 64 F8 JSR $F864
.F2DA  90 04    BCC $F2E0
.F2DC  68       PLA
.F2DD  A9 00    LDA #$00
.F2DF  60       RTS
.F2E0  A5 B9    LDA $B9
.F2E2  C9 62    CMP #$62
.F2E4  D0 0B    BNE $F2F1
.F2E6  A9 05    LDA #$05
.F2E8  20 6A F7 JSR $F76A
.F2EB  4C F1 F2 JMP $F2F1
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F2C8**: Sekundäradresse laden
- **$F2CA**: Bits 0 bis 3 isolieren
- **$F2CC**: verzweige wenn File zum Lesen
- **$F2CE**: Band-Puffer Startadresse holen
- **$F2D1**: Markierung für letztes Zeichen im Datenpuffer
- **$F2D3**: Flag für Ausgabe auf Recorder
- **$F2D4**: Zeichen in Kassettenpuffer
- **$F2D7**: Puffer auf Band schreiben
- **$F2DA**: verzweige wenn alles ok
- **$F2DC**: Zeiger auf Fileeintrag holen
- **$F2DD**: 0 für Break
- **$F2DF**: Rücksprung
- **$F2E0**: Sekundäradresse laden
- **$F2E2**: vergleiche auf Open mit EOT
- **$F2E4**: verzweige wenn kein EOT
- **$F2E6**: Kontrollbyte für EOT-Header
- **$F2E8**: Block auf Band schreiben
- **$F2EB**: Überspringe nächsten Befehl
- **$F2EE**: IEC-File schließen
- **$F2F1**: Zeiger auf Fileeintrag holen
- **$F2F2**: ins X-Register schieben
- **$F2F3**: Anzahl der offenen Files erniedrigen
- **$F2F5**: und mit Zeiger auf Fileeintrag vergleichen
- **$F2F7**: gleich, dann fertig
- **$F2F9**: Anzahl der offenen Files
- **$F2FB**: Letzten Fileeintrag
- **$F2FE**: an die
- **$F301**: freigewordene
- **$F304**: Stelle in der
- **$F307**: Filetabelle
- **$F30A**: schreiben
- **$F30D**: Carry =0 (ok Kennzeichnung)
- **$F30E**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*