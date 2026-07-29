---
title: read the real time clock
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
- f6dd-time-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F6DD
  address_end: $F6E2
  symbol: read-the-real-time-clock
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F6DD**: disable the interrupts'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F6DD**: Interrupt verhindern um Uhr anzuhalten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F6DD**: disable interrupt'
---

# $F6DD — read the real time clock

## Disassemblatura
```assembly
.F6DD  78       SEI   ; disable the interrupts
.F6DE  A5 A2    LDA $A2   ; get the jiffy clock low byte
.F6E0  A6 A1    LDX $A1   ; get the jiffy clock mid byte
.F6E2  A4 A0    LDY $A0   ; get the jiffy clock high byte
```


## Commenti

### Original Disassembly (—)
- **$F6DD**: disable the interrupts
- **$F6DE**: get the jiffy clock low byte
- **$F6E0**: get the jiffy clock mid byte
- **$F6E2**: get the jiffy clock high byte

### Commodore-64-intern-Buch (Commodore)
- **$F6DD**: Interrupt verhindern um Uhr anzuhalten
- **$F6DE**: Stunden
- **$F6E0**: Minuten
- **$F6E2**: Sekunden holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F6DD**: disable interrupt
- **$F6DE**: read TIME

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*