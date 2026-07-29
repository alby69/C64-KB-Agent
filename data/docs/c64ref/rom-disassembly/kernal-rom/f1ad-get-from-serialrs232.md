---
title: GET FROM SERIAL/RS232
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/magnus_nyman.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0090-status
- 0297-rsstat
- acptr
- f1ad-eingabe-vom-iec-bus
- f1b5-read-a-byte-from-serial-bus
- f1b8-rs-232-eingabe
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F1AD
  address_end: $F1C8
  symbol: get-from-serialrs232
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F1AD**: Status testen'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F1AD**: STATUS, I/O status word'
---

# $F1AD — GET FROM SERIAL/RS232

## Disassemblatura
```assembly
.F1AD  A5 90    LDA $90   ; STATUS, I/O status word
.F1AF  F0 04    BEQ $F1B5   ; status OK
.F1B1  A9 0D    LDA #$0D   ; else return <CR> and exit
.F1B3  18       CLC
.F1B4  60       RTS
.F1B5  4C 13 EE JMP $EE13   ; ACPTR, get byte from serial bus
.F1B8  20 4E F1 JSR $F14E   ; receive from RS232
.F1BB  B0 F7    BCS $F1B4   ; end with carry set
.F1BD  C9 00    CMP #$00
.F1BF  D0 F2    BNE $F1B3   ; end with  carry clear
.F1C1  AD 97 02 LDA $0297   ; RSSTAT, 6551 status register
.F1C4  29 60    AND #$60   ; mask
.F1C6  D0 E9    BNE $F1B1   ; return with <CR>
.F1C8  F0 EE    BEQ $F1B8   ; get from RS232
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F1AD**: Status testen
- **$F1AF**: verzweige wenn ok
- **$F1B1**: 'CR' Kode ausgeben
- **$F1B3**: Carry =0 (ok Kennzeichen)
- **$F1B4**: Rücksprung
- **$F1B5**: ein Byte vom IEC-Bus holen

### Magnus Nyman (Magnus Nyman)
- **$F1AD**: STATUS, I/O status word
- **$F1AF**: status OK
- **$F1B1**: else return <CR> and exit
- **$F1B5**: ACPTR, get byte from serial bus
- **$F1B8**: receive from RS232
- **$F1BB**: end with carry set
- **$F1BF**: end with  carry clear
- **$F1C1**: RSSTAT, 6551 status register
- **$F1C4**: mask
- **$F1C6**: return with <CR>
- **$F1C8**: get from RS232

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*