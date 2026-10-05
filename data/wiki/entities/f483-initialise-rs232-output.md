---
id: f483-initialise-rs232-output
type: entity
title: initialise RS232 output
aliases:
- initialise RS232 output
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f483-initialise-rs232-output.md
  sha256: 6e45ef89d339ebb3249a3e15aa3141231dd6a0329eb626c623e443102c04a719
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f483-initialise-rs232-output
---

# initialise RS232 output



# $F483 — initialise RS232 output

## Disassemblatura
```assembly
.F483  A9 7F    LDA #$7F   ; disable all interrupts
.F485  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.F488  A9 06    LDA #$06   ; set RS232 DTR output, RS232 RTS output
.F48A  8D 03 DD STA $DD03   ; save VIA 2 DDRB, RS232 port
.F48D  8D 01 DD STA $DD01   ; save VIA 2 DRB, RS232 port
.F490  A9 04    LDA #$04   ; mask xxxx x1xx, set RS232 Tx DATA high
.F492  0D 00 DD ORA $DD00   ; OR it with VIA 2 DRA, serial port and video address
.F495  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.F498  A0 00    LDY #$00   ; clear Y
.F49A  8C A1 02 STY $02A1   ; clear the RS-232 interrupt enable byte
.F49D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F483**: disable all interrupts
- **$F485**: save VIA 2 ICR
- **$F488**: set RS232 DTR output, RS232 RTS output
- **$F48A**: save VIA 2 DDRB, RS232 port
- **$F48D**: save VIA 2 DRB, RS232 port
- **$F490**: mask xxxx x1xx, set RS232 Tx DATA high
- **$F492**: OR it with VIA 2 DRA, serial port and video address
- **$F495**: save VIA 2 DRA, serial port and video address
- **$F498**: clear Y
- **$F49A**: clear the RS-232 interrupt enable byte

### Commodore-64-intern-Buch (Commodore)
- **$F483**: Bitwert für alle
- **$F485**: NMIs blockieren setzen
- **$F488**: Bit 1 und 2 Ausgang
- **$F48A**: PORT B Richtung
- **$F48D**: PORT A Richtung
- **$F490**: Bit 2 setzen
- **$F492**: Bit 2 = TXD
- **$F495**: Ausgeben
- **$F498**: RS-232
- **$F49A**: NMI-Flag löschen
- **$F49D**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f483-initialise-rs232-output]]
