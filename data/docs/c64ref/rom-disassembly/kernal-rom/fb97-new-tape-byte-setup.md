---
title: new tape byte setup
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
- fb97-ausgabe-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FB97
  address_end: $FBA5
  symbol: new-tape-byte-setup
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FB97**: eight bits to do'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FB97**: Zähler für 8 Bits'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FB97 — new tape byte setup

## Disassemblatura
```assembly
.FB97  A9 08    LDA #$08   ; eight bits to do
.FB99  85 A3    STA $A3   ; set bit count
.FB9B  A9 00    LDA #$00   ; clear A
.FB9D  85 A4    STA $A4   ; clear tape bit cycle phase
.FB9F  85 A8    STA $A8   ; clear start bit first cycle done flag
.FBA1  85 9B    STA $9B   ; clear byte parity
.FBA3  85 A9    STA $A9   ; clear start bit check flag, set no start bit yet
.FBA5  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FB97**: eight bits to do
- **$FB99**: set bit count
- **$FB9B**: clear A
- **$FB9D**: clear tape bit cycle phase
- **$FB9F**: clear start bit first cycle done flag
- **$FBA1**: clear byte parity
- **$FBA3**: clear start bit check flag, set no start bit yet

### Commodore-64-intern-Buch (Commodore)
- **$FB97**: Zähler für 8 Bits
- **$FB99**: Nach $A3
- **$FB9B**: Akku mit $00 laden
- **$FB9D**: Bit-Impuls-Flag löschen
- **$FB9F**: Lesefehler Byte löschen
- **$FBA1**: Parity-Bit löschen
- **$FBA3**: Impulswechsel-Flag löschen
- **$FBA5**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*