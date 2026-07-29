---
title: return cassette sense in Zb
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
- f82e-gedrckt
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F82E
  address_end: $F837
  symbol: return-cassette-sense-in-zb
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F82E**: set the mask for the cassette switch'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F82E**: Bit 4 testen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F82E — return cassette sense in Zb

## Disassemblatura
```assembly
.F82E  A9 10    LDA #$10   ; set the mask for the cassette switch
.F830  24 01    BIT $01   ; test the 6510 I/O port
.F832  D0 02    BNE $F836   ; branch if cassette sense high
.F834  24 01    BIT $01   ; test the 6510 I/O port
.F836  18       CLC
.F837  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F82E**: set the mask for the cassette switch
- **$F830**: test the 6510 I/O port
- **$F832**: branch if cassette sense high
- **$F834**: test the 6510 I/O port

### Commodore-64-intern-Buch (Commodore)
- **$F82E**: Bit 4 testen
- **$F830**: mit Port vergleichen
- **$F832**: verzweige wenn Bandtaste nicht gedrückt
- **$F834**: nochmal abfragen (Entprellen)
- **$F836**: Carry =0 (ok Kennzeichen)
- **$F837**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*