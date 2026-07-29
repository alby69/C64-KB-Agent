---
title: command serial bus to UNTALK
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
- bit
- edef-untalk-senden
- untalk
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EDEF
  address_end: $EDFD
  symbol: command-serial-bus-to-untalk
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EDEF**: disable the interrupts'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EDEF**: Interruptflag setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EDEF**: disable interrupts'
---

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