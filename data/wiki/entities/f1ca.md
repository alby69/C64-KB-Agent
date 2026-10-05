---
id: f1ca
type: entity
title: ;
aliases:
- ;
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1ca.md
  sha256: 2f5fef3487d1640271a343d7e031f10a99920ea118f157a856b4ad3973a370d2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f1ca
---

# ;



# $F1CA — ;

## Disassemblatura
```assembly
.F1CA  48       PHA   ; NBSOUT PHA             ;PRESERVE .A
.F1CB  A5 9A    LDA $9A   ; LDA    DFLTO           ;CHECK DEVICE
.F1CD  C9 03    CMP #$03   ; CMP    #3              ;IS IT THE SCREEN?
.F1CF  D0 04    BNE $F1D5   ; BNE    BO10            ;NO... ; ;PRINT TO CRT ;
.F1D1  68       PLA   ; PLA                    ;RESTORE DATA
.F1D2  4C 16 E7 JMP $E716   ; JMP    PRT             ;PRINT ON CRT ; BO10
.F1D5  90 04    BCC $F1DB   ; BCC    BO20            ;DEVICE 1 OR 2 ; ;PRINT TO SERIAL BUS ;
.F1D7  68       PLA   ; PLA
.F1D8  4C DD ED JMP $EDDD   ; JMP    CIOUT ; ;PRINT TO CASSETTE DEVICES ;
.F1DB  4A       LSR   ; BO20   LSR A           ;RS232?
.F1DC  68       PLA   ; PLA                    ;GET DATA OFF STACK... ;
.F1DD  85 9E    STA $9E   ; CASOUT STA T1          ;PASS DATA IN T1 ; CASOUT MUST BE ENTERED WITH CARRY SET!!! ;PRESERVE REGISTERS ;
.F1DF  8A       TXA   ; TXA
.F1E0  48       PHA   ; PHA
.F1E1  98       TYA   ; TYA
.F1E2  48       PHA   ; PHA
.F1E3  90 23    BCC $F208   ; BCC    BO50            ;C-CLR MEANS DFLTO=2 (RS232) ;
.F1E5  20 0D F8 JSR $F80D   ; JSR    JTP20           ;CHECK BUFFER POINTER
.F1E8  D0 0E    BNE $F1F8   ; BNE    JTP10           ;HAS NOT REACHED END
.F1EA  20 64 F8 JSR $F864   ; JSR    WBLK            ;WRITE FULL BUFFER
.F1ED  B0 0E    BCS $F1FD   ; BCS    RSTOR           ;ABORT ON STOP KEY ; ;PUT BUFFER TYPE BYTE ;
.F1EF  A9 02    LDA #$02   ; LDA    #BDF
.F1F1  A0 00    LDY #$00   ; LDY    #0
.F1F3  91 B2    STA ($B2),Y   ; STA    (TAPE1)Y ; ;RESET BUFFER POINTER ;
.F1F5  C8       INY   ; INY                    ;MAKE .Y=1
.F1F6  84 A6    STY $A6   ; STY    BUFPT           ;BUFPT=1 ;
.F1F8  A5 9E    LDA $9E   ; JTP10  LDA T1
.F1FA  91 B2    STA ($B2),Y   ; STA    (TAPE1)Y        ;DATA TO BUFFER ; ;RESTORE .X AND .Y ;
.F1FC  18       CLC   ; RSTOA  CLC             ;GOOD RETURN
.F1FD  68       PLA   ; RSTOR  PLA
.F1FE  A8       TAY   ; TAY
.F1FF  68       PLA   ; PLA
.F200  AA       TAX   ; TAX
.F201  A5 9E    LDA $9E   ; LDA    T1              ;GET .A FOR RETURN
.F203  90 02    BCC $F207   ; BCC    RSTOR1          ;NO ERROR
.F205  A9 00    LDA #$00   ; LDA    #00             ;STOP ERROR IF C-SET
.F207  60       RTS   ; RSTOR1 RTS ; ;OUTPUT TO RS232 ;
.F208  20 17 F0 JSR $F017   ; BO50   JSR BSO232      ;PASS DATA THROUGH VARIABLE T1
.F20B  4C FC F1 JMP $F1FC   ; JMP    RSTOA           ;GO RESTORE ALL..ALWAYS GOOD .END .LIB   OPENCHANNEL
```


## Commenti

### Original Disassembly (Commodore)
- **$F1CA**: NBSOUT PHA             ;PRESERVE .A
- **$F1CB**: LDA    DFLTO           ;CHECK DEVICE
- **$F1CD**: CMP    #3              ;IS IT THE SCREEN?
- **$F1CF**: BNE    BO10            ;NO... ; ;PRINT TO CRT ;
- **$F1D1**: PLA                    ;RESTORE DATA
- **$F1D2**: JMP    PRT             ;PRINT ON CRT ; BO10
- **$F1D5**: BCC    BO20            ;DEVICE 1 OR 2 ; ;PRINT TO SERIAL BUS ;
- **$F1D7**: PLA
- **$F1D8**: JMP    CIOUT ; ;PRINT TO CASSETTE DEVICES ;
- **$F1DB**: BO20   LSR A           ;RS232?
- **$F1DC**: PLA                    ;GET DATA OFF STACK... ;
- **$F1DD**: CASOUT STA T1          ;PASS DATA IN T1 ; CASOUT MUST BE ENTERED WITH CARRY SET!!! ;PRESERVE REGISTERS ;
- **$F1DF**: TXA
- **$F1E0**: PHA
- **$F1E1**: TYA
- **$F1E2**: PHA
- **$F1E3**: BCC    BO50            ;C-CLR MEANS DFLTO=2 (RS232) ;
- **$F1E5**: JSR    JTP20           ;CHECK BUFFER POINTER
- **$F1E8**: BNE    JTP10           ;HAS NOT REACHED END
- **$F1EA**: JSR    WBLK            ;WRITE FULL BUFFER
- **$F1ED**: BCS    RSTOR           ;ABORT ON STOP KEY ; ;PUT BUFFER TYPE BYTE ;
- **$F1EF**: LDA    #BDF
- **$F1F1**: LDY    #0
- **$F1F3**: STA    (TAPE1)Y ; ;RESET BUFFER POINTER ;
- **$F1F5**: INY                    ;MAKE .Y=1
- **$F1F6**: STY    BUFPT           ;BUFPT=1 ;
- **$F1F8**: JTP10  LDA T1
- **$F1FA**: STA    (TAPE1)Y        ;DATA TO BUFFER ; ;RESTORE .X AND .Y ;
- **$F1FC**: RSTOA  CLC             ;GOOD RETURN
- **$F1FD**: RSTOR  PLA
- **$F1FE**: TAY
- **$F1FF**: PLA
- **$F200**: TAX
- **$F201**: LDA    T1              ;GET .A FOR RETURN
- **$F203**: BCC    RSTOR1          ;NO ERROR
- **$F205**: LDA    #00             ;STOP ERROR IF C-SET
- **$F207**: RSTOR1 RTS ; ;OUTPUT TO RS232 ;
- **$F208**: BO50   JSR BSO232      ;PASS DATA THROUGH VARIABLE T1
- **$F20B**: JMP    RSTOA           ;GO RESTORE ALL..ALWAYS GOOD .END .LIB   OPENCHANNEL

### Original Disassembly (—)
- **$F1CA**: save the character to output
- **$F1CB**: get the output device number
- **$F1CD**: compare the output device with the screen
- **$F1CF**: if not the screen go ??
- **$F1D1**: else restore the output character
- **$F1D2**: go output the character to the screen
- **$F1D5**: if < screen go ??
- **$F1D7**: else restore the output character
- **$F1D8**: go output the character to the serial bus
- **$F1DB**: shift b0 of the device into Cb
- **$F1DC**: restore the output character

### Commodore-64-intern-Buch (Commodore)
- **$F1CA**: Datenbyte retten
- **$F1CB**: Gerätenummer für Ausgabe
- **$F1CD**: vergleiche mit Bildschirm
- **$F1CF**: verzweige wenn nein
- **$F1D1**: Datenbyte wiederholen
- **$F1D2**: ein Zeichen auf Bildschirm ausgeben
- **$F1D5**: verzweige wenn keine Ausgabe IEC-Bus

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F1CA**: temp store on stack
- **$F1CB**: DFLTO, default output device
- **$F1CD**: screen?
- **$F1CF**: nope, test next device
- **$F1D1**: retrieve (A)
- **$F1D2**: output to screen
- **$F1D5**: device <3
- **$F1D7**: retrieve (A)
- **$F1D8**: send serial deferred
- **$F1DD**: PTR1
- **$F1E3**: RS232
- **$F208**: send to RS232
- **$F20B**: end output

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f1ca]]
