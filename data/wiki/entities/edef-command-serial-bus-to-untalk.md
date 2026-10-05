---
id: edef-command-serial-bus-to-untalk
type: entity
title: command serial bus to UNTALK
aliases:
- command serial bus to UNTALK
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edef-command-serial-bus-to-untalk.md
  sha256: 9750c18ca232e2307117e1ba2db438d64653b7f7c691a01e2be50039c6bdf74e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-edef-command-serial-bus-to-untalk
---

# command serial bus to UNTALK



# $EDEF — command serial bus to UNTALK

## Disassemblatura
```assembly
.EDEF  78       SEI   ; disable the interrupts
.EDF0  20 8E EE JSR $EE8E   ; set the serial clock out low
.EDF3  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EDF6  09 08    ORA #$08   ; mask xxxx 1xxx, set the serial ATN low
.EDF8  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EDFB  A9 5F    LDA #$5F   ; set the UNTALK command
.EDFD  2C       .BYTE $2C   ; makes next line BIT $3FA9
```


## Commenti

### Original Disassembly (—)
- **$EDEF**: disable the interrupts
- **$EDF0**: set the serial clock out low
- **$EDF3**: read VIA 2 DRA, serial port and video address
- **$EDF6**: mask xxxx 1xxx, set the serial ATN low
- **$EDF8**: save VIA 2 DRA, serial port and video address
- **$EDFB**: set the UNTALK command
- **$EDFD**: makes next line BIT $3FA9

### Commodore-64-intern-Buch (Commodore)
- **$EDEF**: Interruptflag setzen
- **$EDF0**: CLOCK auf HIGH setzen
- **$EDF3**: Poar A laden
- **$EDF6**: ATN HIGH setzen und
- **$EDF8**: ausgeben
- **$EDFB**: Kennzeichnung für UNTALK
- **$EDFD**: Skip nach $EE00

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EDEF**: disable interrupts
- **$EDF0**: serial bus I/O
- **$EDF3**: set bit4
- **$EDF6**: and store, set ATN 0
- **$EDF8**: set CLK 0
- **$EDFB**: flag UNTALK
- **$EDFD**: mask LDA #$3f with BIT $3fa9
- **$EDFE**: flag UNLISTEN
- **$EE00**: send command to serial bus
- **$EE03**: clear ATN
- **$EE07**: init delay
- **$EE09**: decrement counter
- **$EE0A**: till ready
- **$EE0D**: set CLK 1
- **$EE10**: set data 1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-edef-command-serial-bus-to-untalk]]
