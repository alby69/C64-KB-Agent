---
title: divide operator
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $BB12
  address_end: $BBC6
  symbol: divide-operator
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BB12**: FAC gleich null, ''DIVISION BY ZERO'''
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BB8A**: error number'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BB12**: FAC = 0, DIVIDE BY ZERO ERROR'
---

# $BB12 — divide operator

## Disassemblatura
```assembly
.BB12  F0 76    BEQ $BB8A
.BB14  20 1B BC JSR $BC1B
.BB17  A9 00    LDA #$00
.BB19  38       SEC
.BB1A  E5 61    SBC $61
.BB1C  85 61    STA $61
.BB1E  20 B7 BA JSR $BAB7
.BB21  E6 61    INC $61
.BB23  F0 BA    BEQ $BADF
.BB25  A2 FC    LDX #$FC
.BB27  A9 01    LDA #$01
.BB29  A4 6A    LDY $6A
.BB2B  C4 62    CPY $62
.BB2D  D0 10    BNE $BB3F
.BB2F  A4 6B    LDY $6B
.BB31  C4 63    CPY $63
.BB33  D0 0A    BNE $BB3F
.BB35  A4 6C    LDY $6C
.BB37  C4 64    CPY $64
.BB39  D0 04    BNE $BB3F
.BB3B  A4 6D    LDY $6D
.BB3D  C4 65    CPY $65
.BB3F  08       PHP
.BB40  2A       ROL
.BB41  90 09    BCC $BB4C
.BB43  E8       INX
.BB44  95 29    STA $29,X
.BB46  F0 32    BEQ $BB7A
.BB48  10 34    BPL $BB7E
.BB4A  A9 01    LDA #$01
.BB4C  28       PLP
.BB4D  B0 0E    BCS $BB5D
.BB4F  06 6D    ASL $6D
.BB51  26 6C    ROL $6C
.BB53  26 6B    ROL $6B
.BB55  26 6A    ROL $6A
.BB57  B0 E6    BCS $BB3F
.BB59  30 CE    BMI $BB29
.BB5B  10 E2    BPL $BB3F
.BB5D  A8       TAY
.BB5E  A5 6D    LDA $6D
.BB60  E5 65    SBC $65
.BB62  85 6D    STA $6D
.BB64  A5 6C    LDA $6C
.BB66  E5 64    SBC $64
.BB68  85 6C    STA $6C
.BB6A  A5 6B    LDA $6B
.BB6C  E5 63    SBC $63
.BB6E  85 6B    STA $6B
.BB70  A5 6A    LDA $6A
.BB72  E5 62    SBC $62
.BB74  85 6A    STA $6A
.BB76  98       TYA
.BB77  4C 4F BB JMP $BB4F
.BB7A  A9 40    LDA #$40
.BB7C  D0 CE    BNE $BB4C
.BB7E  0A       ASL
.BB7F  0A       ASL
.BB80  0A       ASL
.BB81  0A       ASL
.BB82  0A       ASL
.BB83  0A       ASL
.BB84  85 70    STA $70
.BB86  28       PLP
.BB87  4C 8F BB JMP $BB8F
.BB8A  A2 14    LDX #$14   ; error number
.BB8C  4C 37 A4 JMP $A437
.BB8F  A5 26    LDA $26
.BB91  85 62    STA $62
.BB93  A5 27    LDA $27
.BB95  85 63    STA $63
.BB97  A5 28    LDA $28
.BB99  85 64    STA $64
.BB9B  A5 29    LDA $29
.BB9D  85 65    STA $65
.BB9F  4C D7 B8 JMP $B8D7
.BBA2  85 22    STA $22
.BBA4  84 23    STY $23
.BBA6  A0 04    LDY #$04
.BBA8  B1 22    LDA ($22),Y
.BBAA  85 65    STA $65
.BBAC  88       DEY
.BBAD  B1 22    LDA ($22),Y
.BBAF  85 64    STA $64
.BBB1  88       DEY
.BBB2  B1 22    LDA ($22),Y
.BBB4  85 63    STA $63
.BBB6  88       DEY
.BBB7  B1 22    LDA ($22),Y
.BBB9  85 66    STA $66
.BBBB  09 80    ORA #$80
.BBBD  85 62    STA $62
.BBBF  88       DEY
.BBC0  B1 22    LDA ($22),Y
.BBC2  85 61    STA $61
.BBC4  84 70    STY $70
.BBC6  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$BB12**: FAC gleich null, 'DIVISION BY ZERO'
- **$BB14**: FAC runden
- **$BB17**: Vorzeichen
- **$BB19**: von FAC-
- **$BB1A**: Exponent
- **$BB1C**: wechseln
- **$BB1E**: Exponent des Ergebnisses bestimmen
- **$BB21**: wenn Exponentenüberlauf,
- **$BB23**: dann ’OVERFLOW ERROR’
- **$BB25**: Zeiger
- **$BB27**: auf
- **$BB29**: Funktionsregister
- **$BB2B**: diese
- **$BB2D**: Routine
- **$BB2F**: vergleicht
- **$BB31**: das
- **$BB33**: FAC
- **$BB35**: und
- **$BB37**: das
- **$BB39**: ARG
- **$BB3B**: byte-
- **$BB3D**: weise
- **$BB3F**: Statusregister retten
- **$BB40**: Carry gelöscht,
- **$BB41**: dann zu $BB4C
- **$BB43**: Ergebnis
- **$BB44**: aufbauen
- **$BB46**: wenn X-Reg =0, dann zu $BB7A
- **$BB48**: wenn X-Reg =1, dann zu $BB7E
- **$BB4A**: wenn
- **$BB4C**: FAC kleiner oder gleich
- **$BB4D**: ARG, dann zu $BB5D
- **$BB4F**: Das
- **$BB51**: ARG
- **$BB53**: ver-
- **$BB55**: doppeln
- **$BB57**: wenn Überlauf, dann zu $BB3F
- **$BB59**: wenn Bit 7 gesetzt, dann zu $BB29
- **$BB5B**: ansonsten zu $BB3F
- **$BB5D**: Die
- **$BB5E**: Mantisse
- **$BB60**: von
- **$BB62**: ARG
- **$BB64**: minus
- **$BB66**: der
- **$BB68**: Mantisse
- **$BB6A**: von
- **$BB6C**: FAC
- **$BB6E**: sub-
- **$BB70**: tra-
- **$BB72**: hie-
- **$BB74**: ren
- **$BB76**: und wieder
- **$BB77**: zu $BB4C
- **$BB7A**: unbedingter
- **$BB7C**: Sprung
- **$BB7E**: den
- **$BB7F**: Akku
- **$BB80**: mit
- **$BB81**: 64
- **$BB82**: multi -
- **$BB83**: plizieren
- **$BB84**: Ergeben = RundungssteLle
- **$BB86**: Statusregister aus Stack
- **$BB87**: Hilfsregister nach FAC
- **$BB8A**: Nummer für 'DIVISION BY ZERO'
- **$BB8C**: Fehlermeldung ausgeben
- **$BB8F**: Hilfs-
- **$BB91**: register
- **$BB93**: ($26 - $29)
- **$BB95**: nach
- **$BB97**: FAC
- **$BB99**: über-
- **$BB9B**: tra-
- **$BB9D**: gen
- **$BB9F**: FAC linksbündig machen

### Marko Mäkelä (Marko Mäkelä)
- **$BB8A**: error number

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BB12**: FAC = 0, DIVIDE BY ZERO ERROR
- **$BB17**: NEGATE FAC EXPONENT, SO
- **$BB19**: ADD.EXPONENTS FORMS DIFFERENCE
- **$BB23**: OVERFLOW
- **$BB25**: INDEX FOR RESULT
- **$BB27**: SENTINEL
- **$BB29**: SEE IF FAC CAN BE SUBTRACTED
- **$BB3F**: SAVE THE ANSWER, AND ALSO ROLL THE
- **$BB40**: BIT INTO THE QUOTIENT, SENTINEL OUT
- **$BB41**: NO SENTINEL, STILL NOT 8 TRIPS
- **$BB43**: 8 TRIPS, STORE BYTE OF QUOTIENT
- **$BB46**: 32-BITS COMPLETED
- **$BB48**: FINAL EXIT WHEN X=1
- **$BB4A**: RE-START SENTINEL
- **$BB4C**: GET ANSWER, CAN FAC BE SUBTRACTED?
- **$BB4D**: YES, DO IT
- **$BB4F**: NO, SHIFT ARG LEFT
- **$BB57**: ANOTHER TRIP
- **$BB59**: HAVE TO COMPARE FIRST
- **$BB5B**: ...ALWAYS
- **$BB5D**: SAVE QUOTIENT/SENTINEL BYTE
- **$BB5E**: SUBTRACT FAC FROM ARG ONCE
- **$BB76**: RESTORE QUOTIENT/SENTINEL BYTE
- **$BB77**: GO TO SHIFT ARG AND CONTINUE
- **$BB7A**: DO A FEW EXTENSION BITS
- **$BB7C**: ...ALWAYS
- **$BB7E**: LEFT JUSTIFY THE EXTENSION BITS WE DID

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*