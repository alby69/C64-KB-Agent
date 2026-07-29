---
title: read I/O status word
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
- fe07-status-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FE07
  address_end: $FE17
  symbol: read-io-status-word
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE07**: get the device number'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE07**: Gerätenummer holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE07**: read current device number from FA'
---

# $FE07 — read I/O status word

## Disassemblatura
```assembly
.FE07  A5 BA    LDA $BA   ; get the device number
.FE09  C9 02    CMP #$02   ; compare device with RS232 device
.FE0B  D0 0D    BNE $FE1A   ; if not RS232 device go ?? get RS232 device status
.FE0D  AD 97 02 LDA $0297   ; get the RS232 status register
.FE10  48       PHA   ; save the RS232 status value
.FE11  A9 00    LDA #$00   ; clear A
.FE13  8D 97 02 STA $0297   ; clear the RS232 status register
.FE16  68       PLA   ; restore the RS232 status value
.FE17  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE07**: get the device number
- **$FE09**: compare device with RS232 device
- **$FE0B**: if not RS232 device go ?? get RS232 device status
- **$FE0D**: get the RS232 status register
- **$FE10**: save the RS232 status value
- **$FE11**: clear A
- **$FE13**: clear the RS232 status register
- **$FE16**: restore the RS232 status value

### Commodore-64-intern-Buch (Commodore)
- **$FE07**: Gerätenummer holen
- **$FE09**: gleich 2 ? (RS 232)
- **$FE0B**: nein
- **$FE0D**: RS 232-Status holen
- **$FE10**: und auf Stapel retten
- **$FE11**: Status
- **$FE13**: löschen
- **$FE16**: und Statuswert zurückholen
- **$FE17**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE07**: read current device number from FA
- **$FE09**: device = RS232?
- **$FE0B**: nope, read STATUS
- **$FE0D**: RSSTAT
- **$FE10**: temp store
- **$FE13**: clear RSSTAT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*