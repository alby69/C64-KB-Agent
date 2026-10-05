---
id: f6dd-read-the-real-time-clock
type: entity
title: read the real time clock
aliases:
- read the real time clock
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f6dd-read-the-real-time-clock.md
  sha256: 9bdf35d027f8c989645b70cc23312730be701becd420391695ca706bdcd03bc3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f6dd-read-the-real-time-clock
---

# read the real time clock



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

## References
- Source: [[src-f6dd-read-the-real-time-clock]]
