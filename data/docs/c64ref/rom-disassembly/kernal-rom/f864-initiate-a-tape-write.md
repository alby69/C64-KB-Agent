---
title: initiate a tape write
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
- f864-bandpuffer-auf-band-schreiben
- f86b-schreiben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F864
  address_end: $F873
  symbol: initiate-a-tape-write
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F864**: set tape buffer start and end pointers do tape write,
      20 cycle c...'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F864**: Bandpufferadresse holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F864 — initiate a tape write

## Disassemblatura
```assembly
.F864  20 D7 F7 JSR $F7D7   ; set tape buffer start and end pointers do tape write, 20 cycle count
.F867  A9 14    LDA #$14   ; set write lead cycle count
.F869  85 AB    STA $AB   ; save write lead cycle count do tape write, no cycle count set
.F86B  20 38 F8 JSR $F838   ; wait for PLAY/RECORD
.F86E  B0 6C    BCS $F8DC   ; if STOPped clear save IRQ address and exit
.F870  78       SEI   ; disable interrupts
.F871  A9 82    LDA #$82   ; enable ?? interrupt
.F873  A2 08    LDX #$08   ; set index for tape write tape leader vector
```


## Commenti

### Original Disassembly (—)
- **$F864**: set tape buffer start and end pointers do tape write, 20 cycle count
- **$F867**: set write lead cycle count
- **$F869**: save write lead cycle count do tape write, no cycle count set
- **$F86B**: wait for PLAY/RECORD
- **$F86E**: if STOPped clear save IRQ address and exit
- **$F870**: disable interrupts
- **$F871**: enable ?? interrupt
- **$F873**: set index for tape write tape leader vector

### Commodore-64-intern-Buch (Commodore)
- **$F864**: Bandpufferadresse holen
- **$F867**: Länge des Vorspanns vor WRITE
- **$F869**: speichern

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*