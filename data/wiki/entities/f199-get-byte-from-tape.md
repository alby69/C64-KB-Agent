---
id: f199-get-byte-from-tape
type: entity
title: get byte from tape
aliases:
- get byte from tape
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f199-get-byte-from-tape.md
  sha256: ac672980fc6c1a7a6d6dc3f02e954b544faade180ee65643953e928dce710864
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f199-get-byte-from-tape
---

# get byte from tape



# $F199 — get byte from tape

## Disassemblatura
```assembly
.F199  20 0D F8 JSR $F80D   ; bump tape pointer
.F19C  D0 0B    BNE $F1A9   ; if not end get next byte and exit
.F19E  20 41 F8 JSR $F841   ; initiate tape read
.F1A1  B0 11    BCS $F1B4   ; exit if error flagged
.F1A3  A9 00    LDA #$00   ; clear A
.F1A5  85 A6    STA $A6   ; clear tape buffer index
.F1A7  F0 F0    BEQ $F199   ; loop, branch always
.F1A9  B1 B2    LDA ($B2),Y   ; get next byte from buffer
.F1AB  18       CLC   ; flag no error
.F1AC  60       RTS   ; input device was serial bus
.F1AD  A5 90    LDA $90   ; get the serial status byte
.F1AF  F0 04    BEQ $F1B5   ; if no errors flagged go input byte and return
.F1B1  A9 0D    LDA #$0D   ; else return [EOL]
.F1B3  18       CLC   ; flag no error
.F1B4  60       RTS
.F1B5  4C 13 EE JMP $EE13   ; input byte from serial bus and return input device was RS232 device
.F1B8  20 4E F1 JSR $F14E   ; get byte from RS232 device
.F1BB  B0 F7    BCS $F1B4   ; branch if error, this doesn't get taken as the last instruction in the get byte from RS232 device routine is CLC ??
.F1BD  C9 00    CMP #$00   ; compare with null
.F1BF  D0 F2    BNE $F1B3   ; exit if not null
.F1C1  AD 97 02 LDA $0297   ; get the RS232 status register
.F1C4  29 60    AND #$60   ; mask 0xx0 0000, DSR detected and ??
.F1C6  D0 E9    BNE $F1B1   ; if ?? return null
.F1C8  F0 EE    BEQ $F1B8   ; else loop, branch always
```


## Commenti

### Original Disassembly (—)
- **$F199**: bump tape pointer
- **$F19C**: if not end get next byte and exit
- **$F19E**: initiate tape read
- **$F1A1**: exit if error flagged
- **$F1A3**: clear A
- **$F1A5**: clear tape buffer index
- **$F1A7**: loop, branch always
- **$F1A9**: get next byte from buffer
- **$F1AB**: flag no error
- **$F1AC**: input device was serial bus
- **$F1AD**: get the serial status byte
- **$F1AF**: if no errors flagged go input byte and return
- **$F1B1**: else return [EOL]
- **$F1B3**: flag no error
- **$F1B5**: input byte from serial bus and return input device was RS232 device
- **$F1B8**: get byte from RS232 device
- **$F1BB**: branch if error, this doesn't get taken as the last instruction in the get byte from RS232 device routine is CLC ??
- **$F1BD**: compare with null
- **$F1BF**: exit if not null
- **$F1C1**: get the RS232 status register
- **$F1C4**: mask 0xx0 0000, DSR detected and ??
- **$F1C6**: if ?? return null
- **$F1C8**: else loop, branch always

### Commodore-64-intern-Buch (Commodore)
- **$F199**: Bandpuffer Zeiger erhöhen
- **$F19C**: verzweige wenn noch Zeichen im Puffer
- **$F19E**: sonst nächsten Block vom Band holen
- **$F1A1**: STOP-Taste, dann Abbruch
- **$F1A3**: Pufferzeiger
- **$F1A5**: auf Null
- **$F1A7**: unbedingter Sprung
- **$F1A9**: Zeichen aus Puffer lesen
- **$F1AB**: Carry =0 (ok Kennzeichen)
- **$F1AC**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f199-get-byte-from-tape]]
