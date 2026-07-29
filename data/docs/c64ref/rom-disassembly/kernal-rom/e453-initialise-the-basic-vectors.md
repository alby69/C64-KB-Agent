---
title: initialise the BASIC vectors
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
- e453-init-vectors
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $E453
  address_end: $E45E
  symbol: initialise-the-basic-vectors
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E453**: set byte count'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E453**: 6 vectors to be copied'
---

# $E453 — initialise the BASIC vectors

## Disassemblatura
```assembly
.E453  A2 0B    LDX #$0B   ; set byte count
.E455  BD 47 E4 LDA $E447,X   ; get byte from table
.E458  9D 00 03 STA $0300,X   ; save byte to RAM
.E45B  CA       DEX   ; decrement index
.E45C  10 F7    BPL $E455   ; loop if more to do
.E45E  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E453**: set byte count
- **$E455**: get byte from table
- **$E458**: save byte to RAM
- **$E45B**: decrement index
- **$E45C**: loop if more to do

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E453**: 6 vectors to be copied
- **$E45B**: next byte
- **$E45C**: ready
- **$E45E**: return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*