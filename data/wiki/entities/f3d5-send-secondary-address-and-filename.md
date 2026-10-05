---
id: f3d5-send-secondary-address-and-filename
type: entity
title: send secondary address and filename
aliases:
- send secondary address and filename
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f3d5-send-secondary-address-and-filename.md
  sha256: 154fcd4cb0cc9d25de41022ce254df68b5d574510bc7cec2c4972b1a06c22ea6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f3d5-send-secondary-address-and-filename
---

# send secondary address and filename



# $F3D5 — send secondary address and filename

## Disassemblatura
```assembly
.F3D5  A5 B9    LDA $B9   ; get the secondary address
.F3D7  30 FA    BMI $F3D3   ; ok exit if -ve
.F3D9  A4 B7    LDY $B7   ; get file name length
.F3DB  F0 F6    BEQ $F3D3   ; ok exit if null
.F3DD  A9 00    LDA #$00   ; clear A
.F3DF  85 90    STA $90   ; clear the serial status byte
.F3E1  A5 BA    LDA $BA   ; get the device number
.F3E3  20 0C ED JSR $ED0C   ; command devices on the serial bus to LISTEN
.F3E6  A5 B9    LDA $B9   ; get the secondary address
.F3E8  09 F0    ORA #$F0   ; OR with the OPEN command
.F3EA  20 B9 ED JSR $EDB9   ; send secondary address after LISTEN
.F3ED  A5 90    LDA $90   ; get the serial status byte
.F3EF  10 05    BPL $F3F6   ; if device present skip the 'device not present' error
.F3F1  68       PLA   ; else dump calling address low byte
.F3F2  68       PLA   ; dump calling address high byte
.F3F3  4C 07 F7 JMP $F707   ; do 'device not present' error and return
.F3F6  A5 B7    LDA $B7   ; get file name length
.F3F8  F0 0C    BEQ $F406   ; branch if null name
.F3FA  A0 00    LDY #$00   ; clear index
.F3FC  B1 BB    LDA ($BB),Y   ; get file name byte
.F3FE  20 DD ED JSR $EDDD   ; output byte to serial bus
.F401  C8       INY   ; increment index
.F402  C4 B7    CPY $B7   ; compare with file name length
.F404  D0 F6    BNE $F3FC   ; loop if not all done
.F406  4C 54 F6 JMP $F654   ; command serial bus to UNLISTEN and return
```


## Commenti

### Original Disassembly (—)
- **$F3D5**: get the secondary address
- **$F3D7**: ok exit if -ve
- **$F3D9**: get file name length
- **$F3DB**: ok exit if null
- **$F3DD**: clear A
- **$F3DF**: clear the serial status byte
- **$F3E1**: get the device number
- **$F3E3**: command devices on the serial bus to LISTEN
- **$F3E6**: get the secondary address
- **$F3E8**: OR with the OPEN command
- **$F3EA**: send secondary address after LISTEN
- **$F3ED**: get the serial status byte
- **$F3EF**: if device present skip the 'device not present' error
- **$F3F1**: else dump calling address low byte
- **$F3F2**: dump calling address high byte
- **$F3F3**: do 'device not present' error and return
- **$F3F6**: get file name length
- **$F3F8**: branch if null name
- **$F3FA**: clear index
- **$F3FC**: get file name byte
- **$F3FE**: output byte to serial bus
- **$F401**: increment index
- **$F402**: compare with file name length
- **$F404**: loop if not all done
- **$F406**: command serial bus to UNLISTEN and return

### Commodore-64-intern-Buch (Commodore)
- **$F3D5**: Sekundäradresse laden
- **$F3D7**: Rücksprung wenn größer, gleich 128
- **$F3D9**: Länge des Filenamens laden
- **$F3DB**: gleich Null, dann fertig
- **$F3DD**: Status
- **$F3DF**: löschen
- **$F3E1**: Geräteadressse laden
- **$F3E3**: LISTEN
- **$F3E6**: Sekundäradresse laden
- **$F3E8**: Bits 4 bis 7 setzen (Open Kennzeichnung)
- **$F3EA**: Sekundäradresse senden
- **$F3ED**: Status testen
- **$F3EF**: verzweige wenn ok
- **$F3F1**: Stack
- **$F3F2**: rücksetzen
- **$F3F3**: 'device not present'
- **$F3F6**: Länge des Filenamens
- **$F3F8**: kein Filename, dann fertig
- **$F3FA**: Zeiger auf Null setzen
- **$F3FC**: Filenamen holen
- **$F3FE**: auf IEC-Bus ausgeben
- **$F401**: Zeiger erhöhen
- **$F402**: mit Länge des Filenamens vergleichen
- **$F404**: verzweige wenn noch nicht alle Zeichen
- **$F406**: UNLISTEN, return

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F3D5**: SA, current secondary address
- **$F3D7**: exit
- **$F3D9**: FNLEN, length of filename
- **$F3DB**: exit
- **$F3DF**: clear STATUS, I/O status word
- **$F3E1**: FA, current device number
- **$F3E3**: send LISTEN to serial bus
- **$F3E6**: SA
- **$F3EA**: send LISTEN SA
- **$F3ED**: STATUS
- **$F3EF**: ok
- **$F3F1**: remove two stack entries for RTS command
- **$F3F3**: I/O error #5, device not present
- **$F3F6**: FNLEN
- **$F3F8**: unlisten and exit
- **$F3FA**: clear offset
- **$F3FC**: FNADR, pointer to filename
- **$F3FE**: send byte on serial bus
- **$F401**: next character
- **$F402**: until entire filename is sent
- **$F404**: again
- **$F406**: unlisten and exit

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f3d5-send-secondary-address-and-filename]]
