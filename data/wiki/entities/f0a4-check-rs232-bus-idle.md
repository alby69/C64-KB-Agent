---
id: f0a4-check-rs232-bus-idle
type: entity
title: check RS232 bus idle
aliases:
- check RS232 bus idle
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f0a4-check-rs232-bus-idle.md
  sha256: ec7b244c0e1a45fd900e7d5b8321f4a7a6f43a97c076ad1607f835c2c02cc8f3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f0a4-check-rs232-bus-idle
---

# check RS232 bus idle



# $F0A4 — check RS232 bus idle

## Disassemblatura
```assembly
.F0A4  48       PHA   ; save A
.F0A5  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.F0A8  F0 11    BEQ $F0BB   ; if no interrupts enabled just exit
.F0AA  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.F0AD  29 03    AND #$03   ; mask 0000 00xx, the error bits
.F0AF  D0 F9    BNE $F0AA   ; if there are errors loop
.F0B1  A9 10    LDA #$10   ; disable FLAG interrupt
.F0B3  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.F0B6  A9 00    LDA #$00   ; clear A
.F0B8  8D A1 02 STA $02A1   ; clear the RS-232 interrupt enable byte
.F0BB  68       PLA   ; restore A
.F0BC  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F0A4**: save A
- **$F0A5**: get the RS-232 interrupt enable byte
- **$F0A8**: if no interrupts enabled just exit
- **$F0AA**: get the RS-232 interrupt enable byte
- **$F0AD**: mask 0000 00xx, the error bits
- **$F0AF**: if there are errors loop
- **$F0B1**: disable FLAG interrupt
- **$F0B3**: save VIA 2 ICR
- **$F0B6**: clear A
- **$F0B8**: clear the RS-232 interrupt enable byte
- **$F0BB**: restore A

### Commodore-64-intern-Buch (Commodore)
- **$F0A4**: Akku auf Stack retten
- **$F0A5**: RS-232 NMI Status laden
- **$F0A8**: nicht gesetzt, dann ok
- **$F0AA**: RS-232 NMI Status laden
- **$F0AD**: Bit 0 = senden und Bit 1 = empfangen
- **$F0AF**: warten bis beide Bits gelöscht
- **$F0B1**: Bitwert für Interrupt durch
- **$F0B3**: 'Flag'-Leitung setzen
- **$F0B6**: RS-232 NMI Status
- **$F0B8**: zurücksetzen
- **$F0BB**: Akku wieder holen
- **$F0BC**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F0A4**: store (A)
- **$F0A5**: ENABL, RS232 enables
- **$F0A8**: bus not in use
- **$F0AA**: ENABL
- **$F0AD**: test RS232
- **$F0AF**: yes, wait for port to clear
- **$F0B3**: set up CIA#2 I.C.R
- **$F0B6**: clear
- **$F0B8**: ENABL
- **$F0BB**: retrieve (A)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f0a4-check-rs232-bus-idle]]
