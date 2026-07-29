---
title: get byte from RS232 buffer
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
- f086-get-von-rs-232
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F086
  address_end: $F0A3
  symbol: get-byte-from-rs232-buffer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F086**: get the RS232 status register'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F086**: RS-232 Status holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F086 — get byte from RS232 buffer

## Disassemblatura
```assembly
.F086  AD 97 02 LDA $0297   ; get the RS232 status register
.F089  AC 9C 02 LDY $029C   ; get index to Rx buffer start
.F08C  CC 9B 02 CPY $029B   ; compare with index to Rx buffer end
.F08F  F0 0B    BEQ $F09C   ; return null if buffer empty
.F091  29 F7    AND #$F7   ; clear the Rx buffer empty bit
.F093  8D 97 02 STA $0297   ; save the RS232 status register
.F096  B1 F7    LDA ($F7),Y   ; get byte from Rx buffer
.F098  EE 9C 02 INC $029C   ; increment index to Rx buffer start
.F09B  60       RTS
.F09C  09 08    ORA #$08   ; set the Rx buffer empty bit
.F09E  8D 97 02 STA $0297   ; save the RS232 status register
.F0A1  A9 00    LDA #$00   ; return null
.F0A3  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F086**: get the RS232 status register
- **$F089**: get index to Rx buffer start
- **$F08C**: compare with index to Rx buffer end
- **$F08F**: return null if buffer empty
- **$F091**: clear the Rx buffer empty bit
- **$F093**: save the RS232 status register
- **$F096**: get byte from Rx buffer
- **$F098**: increment index to Rx buffer start
- **$F09C**: set the Rx buffer empty bit
- **$F09E**: save the RS232 status register
- **$F0A1**: return null

### Commodore-64-intern-Buch (Commodore)
- **$F086**: RS-232 Status holen
- **$F089**: Zeiger auf Ende des Eingabepuffers
- **$F08C**: mit Zeiger auf Anfang vergleichen
- **$F08F**: verzweige wenn gleich (Puffer leer)
- **$F091**: Bit 3 (Puffer leer)
- **$F093**: im Status löschen (Zeichen im Puffer)
- **$F096**: Byte aus Puffer holen
- **$F098**: Pufferzeiger erhöhen
- **$F09B**: Rücksprung
- **$F09C**: Bitwert für Puffer leer
- **$F09E**: Status setzen
- **$F0A1**: Null übergeben
- **$F0A3**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*