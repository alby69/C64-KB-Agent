---
title: SAVE TO SERIAL BUS
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
- 00ac-sal
- 00b7-fnlen
- f5ed-save
- f642-file-auf-iec-bus-schlieen
- listen
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F5FA
  address_end: $F68E
  symbol: save-to-serial-bus
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F5FA**: Sekundäradresse 1'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F5FC**: set SA, secondary address, to #1'
---

# $F5FA — SAVE TO SERIAL BUS

## Disassemblatura
```assembly
.F5FA  A9 61    LDA #$61
.F5FC  85 B9    STA $B9   ; set SA, secondary address, to #1
.F5FE  A4 B7    LDY $B7   ; FNLEN, length of current filename
.F600  D0 03    BNE $F605   ; ok
.F602  4C 10 F7 JMP $F710   ; I/O error #8, missing filename
.F605  20 D5 F3 JSR $F3D5   ; send SA & filename
.F608  20 8F F6 JSR $F68F   ; print 'SAVING' and filename
.F60B  A5 BA    LDA $BA   ; FA, current device number
.F60D  20 0C ED JSR $ED0C   ; send LISTEN
.F610  A5 B9    LDA $B9   ; SA
.F612  20 B9 ED JSR $EDB9   ; send LISTEN SA
.F615  A0 00    LDY #$00
.F617  20 8E FB JSR $FB8E   ; reset pointer
.F61A  A5 AC    LDA $AC   ; SAL, holds start address
.F61C  20 DD ED JSR $EDDD   ; send low byte of start address
.F61F  A5 AD    LDA $AD
.F621  20 DD ED JSR $EDDD   ; send high byte of start address
.F624  20 D1 FC JSR $FCD1   ; check read/write pointer
.F627  B0 16    BCS $F63F
.F629  B1 AC    LDA ($AC),Y   ; get character from memory
.F62B  20 DD ED JSR $EDDD   ; send byte to serial device
.F62E  20 E1 FF JSR $FFE1   ; test <STOP> key
.F631  D0 07    BNE $F63A   ; not pressed
.F633  20 42 F6 JSR $F642   ; exit and unlisten
.F636  A9 00    LDA #$00   ; flag break
.F638  38       SEC
.F639  60       RTS
.F63A  20 DB FC JSR $FCDB   ; bump r/w pointer
.F63D  D0 E5    BNE $F624   ; save next byte
.F63F  20 FE ED JSR $EDFE   ; send UNLISTEN
.F642  24 B9    BIT $B9   ; SA
.F644  30 11    BMI $F657
.F646  A5 BA    LDA $BA   ; FA
.F648  20 0C ED JSR $ED0C   ; send LISTEN
.F64B  A5 B9    LDA $B9
.F64D  29 EF    AND #$EF
.F64F  09 E0    ORA #$E0
.F651  20 B9 ED JSR $EDB9   ; send UNLISTEN SA
.F654  20 FE ED JSR $EDFE   ; send UNLISTEN
.F657  18       CLC
.F658  60       RTS
.F659  4A       LSR
.F65A  B0 03    BCS $F65F
.F65C  4C 13 F7 JMP $F713
.F65F  20 D0 F7 JSR $F7D0
.F662  90 8D    BCC $F5F1
.F664  20 38 F8 JSR $F838
.F667  B0 25    BCS $F68E
.F669  20 8F F6 JSR $F68F
.F66C  A2 03    LDX #$03
.F66E  A5 B9    LDA $B9
.F670  29 01    AND #$01
.F672  D0 02    BNE $F676
.F674  A2 01    LDX #$01
.F676  8A       TXA
.F677  20 6A F7 JSR $F76A
.F67A  B0 12    BCS $F68E
.F67C  20 67 F8 JSR $F867
.F67F  B0 0D    BCS $F68E
.F681  A5 B9    LDA $B9
.F683  29 02    AND #$02
.F685  F0 06    BEQ $F68D
.F687  A9 05    LDA #$05
.F689  20 6A F7 JSR $F76A
.F68C  24       .BYTE $24
.F68D  18       CLC
.F68E  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F5FA**: Sekundäradresse 1
- **$F5FC**: setzen
- **$F5FE**: Länge des Filenamens laden
- **$F600**: ungleich Null, dann ok
- **$F602**: sonst 'MISSING FILENAME'
- **$F605**: Filenamen auf IEC-Bus
- **$F608**: 'SAVING' ausgeben
- **$F60B**: Geräteadresse laden
- **$F60D**: und LISTEN senden
- **$F610**: Sekundäradresse laden
- **$F612**: und für LISTEN senden
- **$F615**: Zähler auf Null setzen
- **$F617**: Startadresse nach $AC/$AD
- **$F61A**: Startadresse LOW-
- **$F61C**: Byte senden
- **$F61F**: und HIGH-
- **$F621**: senden
- **$F624**: Endadresse schon erreicht ?
- **$F627**: ja, dann fertig
- **$F629**: Programmbyte laden
- **$F62B**: auf IEC-Bus ausgeben
- **$F62E**: STOP-Taste abfragen
- **$F631**: nicht gedrückt, dann weitermachen
- **$F633**: IEC-Bus Kanal schließen
- **$F636**: Kennzeichnung für 'BREAK'
- **$F638**: Carry =1 (Fehlerkennzeichen)
- **$F639**: Rücksprung
- **$F63A**: laufende Adresse erhöhen
- **$F63D**: unbedingter Sprung
- **$F63F**: UNLISTEN senden

### Magnus Nyman (Magnus Nyman)
- **$F5FC**: set SA, secondary address, to #1
- **$F5FE**: FNLEN, length of current filename
- **$F600**: ok
- **$F602**: I/O error #8, missing filename
- **$F605**: send SA & filename
- **$F608**: print 'SAVING' and filename
- **$F60B**: FA, current device number
- **$F60D**: send LISTEN
- **$F610**: SA
- **$F612**: send LISTEN SA
- **$F617**: reset pointer
- **$F61A**: SAL, holds start address
- **$F61C**: send low byte of start address
- **$F621**: send high byte of start address
- **$F624**: check read/write pointer
- **$F629**: get character from memory
- **$F62B**: send byte to serial device
- **$F62E**: test <STOP> key
- **$F631**: not pressed
- **$F633**: exit and unlisten
- **$F636**: flag break
- **$F63A**: bump r/w pointer
- **$F63D**: save next byte
- **$F63F**: send UNLISTEN
- **$F642**: SA
- **$F646**: FA
- **$F648**: send LISTEN
- **$F651**: send UNLISTEN SA
- **$F654**: send UNLISTEN

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*