---
title: display control I/O message if in direct mode
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
- f12b-systemmeldungen-ausgeben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F12B
  address_end: $F13D
  symbol: display-control-io-message-if-in-direct-mode
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F12B**: test message mode flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F12B**: Direkt-Modus Flag'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F12B**: MSGFLG, test if direct or program mode'
---

# $F12B — display control I/O message if in direct mode

## Disassemblatura
```assembly
.F12B  24 9D    BIT $9D   ; test message mode flag
.F12D  10 0D    BPL $F13C   ; exit if control messages off display kernel I/O message
.F12F  B9 BD F0 LDA $F0BD,Y   ; get byte from message table
.F132  08       PHP   ; save status
.F133  29 7F    AND #$7F   ; clear b7
.F135  20 D2 FF JSR $FFD2   ; output character to channel
.F138  C8       INY   ; increment index
.F139  28       PLP   ; restore status
.F13A  10 F3    BPL $F12F   ; loop if not end of message
.F13C  18       CLC
.F13D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F12B**: test message mode flag
- **$F12D**: exit if control messages off display kernel I/O message
- **$F12F**: get byte from message table
- **$F132**: save status
- **$F133**: clear b7
- **$F135**: output character to channel
- **$F138**: increment index
- **$F139**: restore status
- **$F13A**: loop if not end of message

### Commodore-64-intern-Buch (Commodore)
- **$F12B**: Direkt-Modus Flag
- **$F12D**: Programm, dann überspringen
- **$F12F**: Zeichen holen mit Offset der Meldung in Y-Register
- **$F132**: Status-Register retten
- **$F133**: Bit 7 löschen
- **$F135**: und Zeichen ausgeben
- **$F138**: Zeiger erhöhen
- **$F139**: Status wiederholen
- **$F13A**: verzweige wenn noch weitere Buchstaben
- **$F13C**: Carry löschen, ok
- **$F13D**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F12B**: MSGFLG, test if direct or program mode
- **$F12D**: program mode, don't print message
- **$F12F**: get output character from table
- **$F132**: store processor registers
- **$F133**: clear bit7
- **$F135**: output character using CHROUT
- **$F138**: increment pointer to next character
- **$F139**: retrieve message
- **$F13A**: until bit7 was set
- **$F13C**: clear carry to indicate no error

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*