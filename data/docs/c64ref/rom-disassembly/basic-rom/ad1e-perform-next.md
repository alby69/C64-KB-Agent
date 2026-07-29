---
title: perform NEXT
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ad1e-basic-befehl-next
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AD1E
  address_end: $AD87
  symbol: perform-next
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AD1E**: branch if NEXT variable'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AD1E**: folgt Variablenname? ja:$AD24'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AD30**: error number'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AD1E**: VARIABLE AFTER "NEXT"'
---

# $AD1E — perform NEXT

## Disassemblatura
```assembly
.AD1E  D0 04    BNE $AD24   ; branch if NEXT variable
.AD20  A0 00    LDY #$00   ; else clear Y
.AD22  F0 03    BEQ $AD27   ; branch always NEXT variable
.AD24  20 8B B0 JSR $B08B   ; get variable address
.AD27  85 49    STA $49   ; save FOR/NEXT variable pointer low byte
.AD29  84 4A    STY $4A   ; save FOR/NEXT variable pointer high byte (high byte cleared if no variable defined)
.AD2B  20 8A A3 JSR $A38A   ; search the stack for FOR or GOSUB activity
.AD2E  F0 05    BEQ $AD35   ; branch if FOR, this variable, found
.AD30  A2 0A    LDX #$0A   ; else set error $0A, next without for error
.AD32  4C 37 A4 JMP $A437   ; do error #X then warm start found this FOR variable
.AD35  9A       TXS   ; update stack pointer
.AD36  8A       TXA   ; copy stack pointer
.AD37  18       CLC   ; clear carry for add
.AD38  69 04    ADC #$04   ; point to STEP value
.AD3A  48       PHA   ; save it
.AD3B  69 06    ADC #$06   ; point to TO value
.AD3D  85 24    STA $24   ; save pointer to TO variable for compare
.AD3F  68       PLA   ; restore pointer to STEP value
.AD40  A0 01    LDY #$01   ; point to stack page
.AD42  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
.AD45  BA       TSX   ; get stack pointer back
.AD46  BD 09 01 LDA $0109,X   ; get step sign
.AD49  85 66    STA $66   ; save FAC1 sign (b7)
.AD4B  A5 49    LDA $49   ; get FOR/NEXT variable pointer low byte
.AD4D  A4 4A    LDY $4A   ; get FOR/NEXT variable pointer high byte
.AD4F  20 67 B8 JSR $B867   ; add FOR variable to FAC1
.AD52  20 D0 BB JSR $BBD0   ; pack FAC1 into FOR variable
.AD55  A0 01    LDY #$01   ; point to stack page
.AD57  20 5D BC JSR $BC5D   ; compare FAC1 with TO value
.AD5A  BA       TSX   ; get stack pointer back
.AD5B  38       SEC   ; set carry for subtract
.AD5C  FD 09 01 SBC $0109,X   ; subtract step sign
.AD5F  F0 17    BEQ $AD78   ; branch if =, loop complete loop back and do it all again
.AD61  BD 0F 01 LDA $010F,X   ; get FOR line low byte
.AD64  85 39    STA $39   ; save current line number low byte
.AD66  BD 10 01 LDA $0110,X   ; get FOR line high byte
.AD69  85 3A    STA $3A   ; save current line number high byte
.AD6B  BD 12 01 LDA $0112,X   ; get BASIC execute pointer low byte
.AD6E  85 7A    STA $7A   ; save BASIC execute pointer low byte
.AD70  BD 11 01 LDA $0111,X   ; get BASIC execute pointer high byte
.AD73  85 7B    STA $7B   ; save BASIC execute pointer high byte
.AD75  4C AE A7 JMP $A7AE   ; go do interpreter inner loop NEXT loop complete
.AD78  8A       TXA   ; stack copy to A
.AD79  69 11    ADC #$11   ; add $12, $11 + carry, to dump FOR structure
.AD7B  AA       TAX   ; copy back to index
.AD7C  9A       TXS   ; copy to stack pointer
.AD7D  20 79 00 JSR $0079   ; scan memory
.AD80  C9 2C    CMP #$2C   ; compare with ","
.AD82  D0 F1    BNE $AD75   ; if not "," go do interpreter inner loop was "," so another NEXT variable to do
.AD84  20 73 00 JSR $0073   ; increment and scan memory
.AD87  20 24 AD JSR $AD24   ; do NEXT variable
```


## Commenti

### Original Disassembly (—)
- **$AD1E**: branch if NEXT variable
- **$AD20**: else clear Y
- **$AD22**: branch always NEXT variable
- **$AD24**: get variable address
- **$AD27**: save FOR/NEXT variable pointer low byte
- **$AD29**: save FOR/NEXT variable pointer high byte (high byte cleared if no variable defined)
- **$AD2B**: search the stack for FOR or GOSUB activity
- **$AD2E**: branch if FOR, this variable, found
- **$AD30**: else set error $0A, next without for error
- **$AD32**: do error #X then warm start found this FOR variable
- **$AD35**: update stack pointer
- **$AD36**: copy stack pointer
- **$AD37**: clear carry for add
- **$AD38**: point to STEP value
- **$AD3A**: save it
- **$AD3B**: point to TO value
- **$AD3D**: save pointer to TO variable for compare
- **$AD3F**: restore pointer to STEP value
- **$AD40**: point to stack page
- **$AD42**: unpack memory (AY) into FAC1
- **$AD45**: get stack pointer back
- **$AD46**: get step sign
- **$AD49**: save FAC1 sign (b7)
- **$AD4B**: get FOR/NEXT variable pointer low byte
- **$AD4D**: get FOR/NEXT variable pointer high byte
- **$AD4F**: add FOR variable to FAC1
- **$AD52**: pack FAC1 into FOR variable
- **$AD55**: point to stack page
- **$AD57**: compare FAC1 with TO value
- **$AD5A**: get stack pointer back
- **$AD5B**: set carry for subtract
- **$AD5C**: subtract step sign
- **$AD5F**: branch if =, loop complete loop back and do it all again
- **$AD61**: get FOR line low byte
- **$AD64**: save current line number low byte
- **$AD66**: get FOR line high byte
- **$AD69**: save current line number high byte
- **$AD6B**: get BASIC execute pointer low byte
- **$AD6E**: save BASIC execute pointer low byte
- **$AD70**: get BASIC execute pointer high byte
- **$AD73**: save BASIC execute pointer high byte
- **$AD75**: go do interpreter inner loop NEXT loop complete
- **$AD78**: stack copy to A
- **$AD79**: add $12, $11 + carry, to dump FOR structure
- **$AD7B**: copy back to index
- **$AD7C**: copy to stack pointer
- **$AD7D**: scan memory
- **$AD80**: compare with ","
- **$AD82**: if not "," go do interpreter inner loop was "," so another NEXT variable to do
- **$AD84**: increment and scan memory
- **$AD87**: do NEXT variable

### Commodore-64-intern-Buch (Commodore)
- **$AD1E**: folgt Variablenname? ja:$AD24
- **$AD20**: Variablenzeiger = 0
- **$AD22**: unbedingter Sprung
- **$AD24**: sucht Variable
- **$AD27**: Adresse der
- **$AD29**: Variablen speichern
- **$AD2B**: sucht FOR-NEXT-Schleife
- **$AD2E**: gefunden: $AD35
- **$AD30**: Nummer für 'next without for'
- **$AD32**: Fehlermeldung ausgeben
- **$AD35**: X-Reg. retten
- **$AD36**: X-Register nach Akku
- **$AD37**: Carry löschen (Addition)
- **$AD38**: Zeiger auf Exponenten des
- **$AD3A**: STEP-Wert + 4 und retten
- **$AD3B**: Zeiger auf Exponent des TO-
- **$AD3D**: Wert und retten
- **$AD3F**: Akku wieder vom Stapel holen
- **$AD40**: Zeiger für Konstante setzen
- **$AD42**: Variable vom Stapel nach FAC
- **$AD45**: Stapelzeiger als Zeiger h.
- **$AD46**: Vorzeichenbyte holen und
- **$AD49**: für FAC speichern
- **$AD4B**: Variablenadresse für
- **$AD4D**: FOR-NEXT holen
- **$AD4F**: addiert STEP-Wert zu FAC
- **$AD52**: FAC nach Variable bringen
- **$AD55**: Zeiger auf Konstante setzen
- **$AD57**: FAC mit Schleifenendwert vergleichen
- **$AD5A**: Stapelzeiger als Zeiger h.
- **$AD5B**: Carry setzen (Subtraktion)
- **$AD5C**: Stapelwert größer?
- **$AD5F**: ja: Schleife verlassen
- **$AD61**: Zeilennummer des Schleifen-
- **$AD64**: anfangs holen (LOW- und
- **$AD66**: HIGH-Byte) und als aktuelle
- **$AD69**: BASIC-Zeilennummer speichern
- **$AD6B**: Schleifenanfang holen (LOW-
- **$AD6E**: und HIGH-Byte) und
- **$AD70**: als neuen Programmzeiger
- **$AD73**: abspeichern
- **$AD75**: zur Interpreterschleife
- **$AD78**: Zeiger in Akku holen
- **$AD79**: (Werte der Schleife aus
- **$AD7B**: Stapel entfernen)
- **$AD7C**: neuen Stapelzeiger setzen
- **$AD7D**: CHRGOT letztes Zeichen holen
- **$AD80**: ',' Komma?
- **$AD82**: nein: dann fertig
- **$AD84**: CHRGET nächstes Zeichen holen
- **$AD87**: nächste NEXT-Variable

### Marko Mäkelä (Marko Mäkelä)
- **$AD30**: error number
- **$AD80**: comma

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AD1E**: VARIABLE AFTER "NEXT"
- **$AD20**: FLAG BY SETTING FORPNT+1 = 0
- **$AD22**: ...ALWAYS
- **$AD24**: GET PNTR TO VARIABLE IN (Y,A)
- **$AD2B**: FIND FOR-FRAME FOR THIS VARIABLE
- **$AD2E**: FOUND IT
- **$AD30**: NOT THERE, ABORT
- **$AD32**: ...ALWAYS
- **$AD35**: SET STACK PTR TO POINT TO THIS FRAME,
- **$AD40**: (Y,A) IS ADDRESS OF STEP VALUE
- **$AD42**: STEP TO FAC
- **$AD4F**: ADD TO FOR VALUE
- **$AD52**: PUT NEW VALUE BACK
- **$AD55**: (Y,A) IS ADDRESS OF END VALUE
- **$AD57**: COMPARE TO END VALUE
- **$AD5C**: SIGN OF STEP
- **$AD5F**: BRANCH IF FOR COMPLETE
- **$AD61**: OTHERWISE SET UP
- **$AD64**: FOR LINE #
- **$AD6B**: AND SET TXTPTR TO JUST
- **$AD6E**: AFTER FOR STATEMENT
- **$AD78**: POP OFF FOR-FRAME, LOOP IS DONE
- **$AD79**: CARRY IS SET, SO ADDS 18
- **$AD7D**: CHAR AFTER VARIABLE
- **$AD80**: ANOTHER VARIABLE IN NEXT?
- **$AD82**: NO, GO TO NEXT STATEMENT
- **$AD84**: YES, PRIME FOR NEXT VARIABLE
- **$AD87**: (DOES NOT RETURN)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*