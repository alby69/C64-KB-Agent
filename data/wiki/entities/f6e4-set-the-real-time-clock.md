---
id: f6e4-set-the-real-time-clock
type: entity
title: set the real time clock
aliases:
- set the real time clock
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f6e4-set-the-real-time-clock.md
  sha256: 39483f0c93fc7be3fa98b5fb63e2c46c953fa777bd09350d5469d19729ea377e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f6e4-set-the-real-time-clock
---

# set the real time clock



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

## References
- Source: [[src-f6e4-set-the-real-time-clock]]
