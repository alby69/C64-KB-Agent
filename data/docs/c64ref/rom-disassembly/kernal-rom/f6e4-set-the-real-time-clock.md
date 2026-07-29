---
title: set the real time clock
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
- f6e4-time-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F6E4
  address_end: $F6EC
  symbol: set-the-real-time-clock
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F6E4**: disable the interrupts'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F6E4**: Interrupt verhindern um Uhr anzuhalten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F6E4**: disable interrupt'
---

# $F6E4 — set the real time clock

## Disassemblatura
```assembly
.F6E4  78       SEI   ; disable the interrupts
.F6E5  85 A2    STA $A2   ; save the jiffy clock low byte
.F6E7  86 A1    STX $A1   ; save the jiffy clock mid byte
.F6E9  84 A0    STY $A0   ; save the jiffy clock high byte
.F6EB  58       CLI   ; enable the interrupts
.F6EC  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F6E4**: disable the interrupts
- **$F6E5**: save the jiffy clock low byte
- **$F6E7**: save the jiffy clock mid byte
- **$F6E9**: save the jiffy clock high byte
- **$F6EB**: enable the interrupts

### Commodore-64-intern-Buch (Commodore)
- **$F6E4**: Interrupt verhindern um Uhr anzuhalten
- **$F6E5**: Stunden
- **$F6E7**: Minuten
- **$F6E9**: Sekunden schreiben
- **$F6EB**: Interrupt wieder ermöglichen
- **$F6EC**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F6E4**: disable interrupt
- **$F6E5**: write TIME
- **$F6EB**: enable interrupts

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*