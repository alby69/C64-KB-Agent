---
id: f1ad-get-from-serialrs232
type: entity
title: GET FROM SERIAL/RS232
aliases:
- GET FROM SERIAL/RS232
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1ad-get-from-serialrs232.md
  sha256: 6df3b8feaad83be40f45525867b84d6dab594b1594242439c7655b80fe9bcdcc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f1ad-get-from-serialrs232
---

# GET FROM SERIAL/RS232



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

## References
- Source: [[src-f1ad-get-from-serialrs232]]
