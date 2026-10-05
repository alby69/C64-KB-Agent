---
id: fc93-restore-everything-for-stop
type: entity
title: restore everything for STOP
aliases:
- restore everything for STOP
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fc93-restore-everything-for-stop.md
  sha256: 68c00e90f0685bfe13b30414e5111edc1154ce101f8e8a892cf7e6f8df036ac6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fc93-restore-everything-for-stop
---

# restore everything for STOP



# $FC93 — restore everything for STOP

## Disassemblatura
```assembly
.FC93  08       PHP   ; save status
.FC94  78       SEI   ; disable the interrupts
.FC95  AD 11 D0 LDA $D011   ; read the vertical fine scroll and control register
.FC98  09 10    ORA #$10   ; mask xxx1 xxxx, unblank the screen
.FC9A  8D 11 D0 STA $D011   ; save the vertical fine scroll and control register
.FC9D  20 CA FC JSR $FCCA   ; stop the cassette motor
.FCA0  A9 7F    LDA #$7F   ; disable all interrupts
.FCA2  8D 0D DC STA $DC0D   ; save VIA 1 ICR
.FCA5  20 DD FD JSR $FDDD
.FCA8  AD A0 02 LDA $02A0   ; get saved IRQ vector high byte
.FCAB  F0 09    BEQ $FCB6   ; branch if null
.FCAD  8D 15 03 STA $0315   ; restore IRQ vector high byte
.FCB0  AD 9F 02 LDA $029F   ; get saved IRQ vector low byte
.FCB3  8D 14 03 STA $0314   ; restore IRQ vector low byte
.FCB6  28       PLP   ; restore status
.FCB7  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FC93**: save status
- **$FC94**: disable the interrupts
- **$FC95**: read the vertical fine scroll and control register
- **$FC98**: mask xxx1 xxxx, unblank the screen
- **$FC9A**: save the vertical fine scroll and control register
- **$FC9D**: stop the cassette motor
- **$FCA0**: disable all interrupts
- **$FCA2**: save VIA 1 ICR
- **$FCA8**: get saved IRQ vector high byte
- **$FCAB**: branch if null
- **$FCAD**: restore IRQ vector high byte
- **$FCB0**: get saved IRQ vector low byte
- **$FCB3**: restore IRQ vector low byte
- **$FCB6**: restore status

### Commodore-64-intern-Buch (Commodore)
- **$FC93**: Status merken
- **$FC94**: Interrupt verhindern
- **$FC95**: Bildschirm
- **$FC98**: wieder
- **$FC9A**: einschalten
- **$FC9D**: Rekordermotor ausschalten
- **$FCA0**: Interruptmöglichkeiten
- **$FCA2**: löschen
- **$FCA5**: CIA wieder auf Standardwerte, 1/60 s Timing
- **$FCA8**: Interruptvektor schon auf Standardwert ?
- **$FCAB**: falls ja, dann fertig
- **$FCAD**: ansonsten zurücksetzen
- **$FCB0**: geretteten lRQ zurückholen
- **$FCB3**: und speichern
- **$FCB6**: Status zurückholen
- **$FCB7**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fc93-restore-everything-for-stop]]
