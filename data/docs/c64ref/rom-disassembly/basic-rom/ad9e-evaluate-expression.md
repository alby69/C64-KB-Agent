---
title: evaluate expression
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
- ad9e-beliebigen-ausdrucks
- bit
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AD9E
  address_end: $AE1E
  symbol: evaluate-expression
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AD9E**: get BASIC execute pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AD9E**: Programmzeiger (LOW) = 0?'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$ADBC**: code for greater than'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AD9E**: DECREMENT TXTPTR'
---

# $AD9E — evaluate expression

## Disassemblatura
```assembly
.AD9E  A6 7A    LDX $7A   ; get BASIC execute pointer low byte
.ADA0  D0 02    BNE $ADA4   ; skip next if not zero
.ADA2  C6 7B    DEC $7B   ; else decrement BASIC execute pointer high byte
.ADA4  C6 7A    DEC $7A   ; decrement BASIC execute pointer low byte
.ADA6  A2 00    LDX #$00   ; set null precedence, flag done
.ADA8  24       .BYTE $24   ; makes next line BIT $48
.ADA9  48       PHA   ; push compare evaluation byte if branch to here
.ADAA  8A       TXA   ; copy precedence byte
.ADAB  48       PHA   ; push precedence byte
.ADAC  A9 01    LDA #$01   ; 2 bytes
.ADAE  20 FB A3 JSR $A3FB   ; check room on stack for A*2 bytes
.ADB1  20 83 AE JSR $AE83   ; get value from line
.ADB4  A9 00    LDA #$00   ; clear A
.ADB6  85 4D    STA $4D   ; clear comparison evaluation flag
.ADB8  20 79 00 JSR $0079   ; scan memory
.ADBB  38       SEC   ; set carry for subtract
.ADBC  E9 B1    SBC #$B1   ; subtract the token for ">"
.ADBE  90 17    BCC $ADD7   ; branch if < ">"
.ADC0  C9 03    CMP #$03   ; compare with ">" to +3
.ADC2  B0 13    BCS $ADD7   ; branch if >= 3 was token for ">" "=" or "<"
.ADC4  C9 01    CMP #$01   ; compare with token for =
.ADC6  2A       ROL   ; *2, b0 = carry (=1 if token was = or <)
.ADC7  49 01    EOR #$01   ; toggle b0
.ADC9  45 4D    EOR $4D   ; EOR with comparison evaluation flag
.ADCB  C5 4D    CMP $4D   ; compare with comparison evaluation flag
.ADCD  90 61    BCC $AE30   ; if < saved flag do syntax error then warm start
.ADCF  85 4D    STA $4D   ; save new comparison evaluation flag
.ADD1  20 73 00 JSR $0073   ; increment and scan memory
.ADD4  4C BB AD JMP $ADBB   ; go do next character
.ADD7  A6 4D    LDX $4D   ; get comparison evaluation flag
.ADD9  D0 2C    BNE $AE07   ; branch if compare function
.ADDB  B0 7B    BCS $AE58   ; go do functions else was < TK_GT so is operator or lower
.ADDD  69 07    ADC #$07   ; add # of operators (+, -, *, /, ^, AND or OR)
.ADDF  90 77    BCC $AE58   ; branch if < + operator carry was set so token was +, -, *, /, ^, AND or OR
.ADE1  65 0D    ADC $0D   ; add data type flag, $FF = string, $00 = numeric
.ADE3  D0 03    BNE $ADE8   ; branch if not string or not + token will only be $00 if type is string and token was +
.ADE5  4C 3D B6 JMP $B63D   ; add strings, string 1 is in the descriptor, string 2 is in line, and return
.ADE8  69 FF    ADC #$FF   ; -1 (corrects for carry add)
.ADEA  85 22    STA $22   ; save it
.ADEC  0A       ASL   ; *2
.ADED  65 22    ADC $22   ; *3
.ADEF  A8       TAY   ; copy to index
.ADF0  68       PLA   ; pull previous precedence
.ADF1  D9 80 A0 CMP $A080,Y   ; compare with precedence byte
.ADF4  B0 67    BCS $AE5D   ; branch if A >=
.ADF6  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.ADF9  48       PHA   ; save precedence
.ADFA  20 20 AE JSR $AE20   ; get vector, execute function then continue evaluation
.ADFD  68       PLA   ; restore precedence
.ADFE  A4 4B    LDY $4B   ; get precedence stacked flag
.AE00  10 17    BPL $AE19   ; branch if stacked values
.AE02  AA       TAX   ; copy precedence, set flags
.AE03  F0 56    BEQ $AE5B   ; exit if done
.AE05  D0 5F    BNE $AE66   ; else pop FAC2 and return, branch always
.AE07  46 0D    LSR $0D   ; clear data type flag, $FF = string, $00 = numeric
.AE09  8A       TXA   ; copy compare function flag
.AE0A  2A       ROL   ; <<1, shift data type flag into b0, 1 = string, 0 = num
.AE0B  A6 7A    LDX $7A   ; get BASIC execute pointer low byte
.AE0D  D0 02    BNE $AE11   ; branch if no underflow
.AE0F  C6 7B    DEC $7B   ; else decrement BASIC execute pointer high byte
.AE11  C6 7A    DEC $7A   ; decrement BASIC execute pointer low byte
.AE13  A0 1B    LDY #$1B   ; set offset to = operator precedence entry
.AE15  85 4D    STA $4D   ; save new comparison evaluation flag
.AE17  D0 D7    BNE $ADF0   ; branch always
.AE19  D9 80 A0 CMP $A080,Y   ; compare with stacked function precedence
.AE1C  B0 48    BCS $AE66   ; if A >=, pop FAC2 and return
.AE1E  90 D9    BCC $ADF9   ; else go stack this one and continue, branch always
```


## Commenti

### Original Disassembly (—)
- **$AD9E**: get BASIC execute pointer low byte
- **$ADA0**: skip next if not zero
- **$ADA2**: else decrement BASIC execute pointer high byte
- **$ADA4**: decrement BASIC execute pointer low byte
- **$ADA6**: set null precedence, flag done
- **$ADA8**: makes next line BIT $48
- **$ADA9**: push compare evaluation byte if branch to here
- **$ADAA**: copy precedence byte
- **$ADAB**: push precedence byte
- **$ADAC**: 2 bytes
- **$ADAE**: check room on stack for A*2 bytes
- **$ADB1**: get value from line
- **$ADB4**: clear A
- **$ADB6**: clear comparison evaluation flag
- **$ADB8**: scan memory
- **$ADBB**: set carry for subtract
- **$ADBC**: subtract the token for ">"
- **$ADBE**: branch if < ">"
- **$ADC0**: compare with ">" to +3
- **$ADC2**: branch if >= 3 was token for ">" "=" or "<"
- **$ADC4**: compare with token for =
- **$ADC6**: *2, b0 = carry (=1 if token was = or <)
- **$ADC7**: toggle b0
- **$ADC9**: EOR with comparison evaluation flag
- **$ADCB**: compare with comparison evaluation flag
- **$ADCD**: if < saved flag do syntax error then warm start
- **$ADCF**: save new comparison evaluation flag
- **$ADD1**: increment and scan memory
- **$ADD4**: go do next character
- **$ADD7**: get comparison evaluation flag
- **$ADD9**: branch if compare function
- **$ADDB**: go do functions else was < TK_GT so is operator or lower
- **$ADDD**: add # of operators (+, -, *, /, ^, AND or OR)
- **$ADDF**: branch if < + operator carry was set so token was +, -, *, /, ^, AND or OR
- **$ADE1**: add data type flag, $FF = string, $00 = numeric
- **$ADE3**: branch if not string or not + token will only be $00 if type is string and token was +
- **$ADE5**: add strings, string 1 is in the descriptor, string 2 is in line, and return
- **$ADE8**: -1 (corrects for carry add)
- **$ADEA**: save it
- **$ADEC**: *2
- **$ADED**: *3
- **$ADEF**: copy to index
- **$ADF0**: pull previous precedence
- **$ADF1**: compare with precedence byte
- **$ADF4**: branch if A >=
- **$ADF6**: check if source is numeric, else do type mismatch
- **$ADF9**: save precedence
- **$ADFA**: get vector, execute function then continue evaluation
- **$ADFD**: restore precedence
- **$ADFE**: get precedence stacked flag
- **$AE00**: branch if stacked values
- **$AE02**: copy precedence, set flags
- **$AE03**: exit if done
- **$AE05**: else pop FAC2 and return, branch always
- **$AE07**: clear data type flag, $FF = string, $00 = numeric
- **$AE09**: copy compare function flag
- **$AE0A**: <<1, shift data type flag into b0, 1 = string, 0 = num
- **$AE0B**: get BASIC execute pointer low byte
- **$AE0D**: branch if no underflow
- **$AE0F**: else decrement BASIC execute pointer high byte
- **$AE11**: decrement BASIC execute pointer low byte
- **$AE13**: set offset to = operator precedence entry
- **$AE15**: save new comparison evaluation flag
- **$AE17**: branch always
- **$AE19**: compare with stacked function precedence
- **$AE1C**: if A >=, pop FAC2 and return
- **$AE1E**: else go stack this one and continue, branch always

### Commodore-64-intern-Buch (Commodore)
- **$AD9E**: Programmzeiger (LOW) = 0?
- **$ADA0**: ja: HIGH-B. nicht vermindern
- **$ADA2**: HIGH-Byte vermindern
- **$ADA4**: LOW-Byte vermindern
- **$ADA6**: Prioritätswert laden
- **$ADA9**: Operatormaske retten
- **$ADAA**: Prioritätswert in Akku
- **$ADAB**: schieben und retten
- **$ADAC**: 2 Bytes
- **$ADAE**: prüft auf Platz im Stapel
- **$ADB1**: Nächstes Element holen
- **$ADB4**: Wert laden und
- **$ADB6**: Maske für Vergleichsoperator
- **$ADB8**: CHRGOT letztes Zeichen holen
- **$ADBB**: Carry setzen (Subtraktion)
- **$ADBC**: $B1 von Operatorcode subtr.
- **$ADBE**: C=0: $ADD7
- **$ADC0**: mit $3 vergleichen
- **$ADC2**: =3: $ADD7
- **$ADC6**: Maske für kleiner
- **$ADC7**: gleich und größer
- **$ADC9**: für Bits 0,1 und 2
- **$ADCB**: in $40 erstellen
- **$ADCD**: (Wenn Codes von 177
- **$ADCF**: bis 179 folgen)
- **$ADD1**: CHRGET nächstes Zeichen holen
- **$ADD4**: nächstes Zeichen auswerten
- **$ADD7**: Operatormaske holen
- **$ADD9**: gleich 0? nein: $AE07
- **$ADDB**: Code größer oder gleich 180?
- **$ADDD**: Code kleiner 170?
- **$ADDF**: ja: $AE58
- **$ADE1**: Stringaddition?
- **$ADE3**: nein: Verkettung umgehen
- **$ADE5**: Stringverkettung
- **$ADE8**: Code-$AA (wiederherstellen)
- **$ADEA**: und speichern
- **$ADEC**: verdoppeln
- **$ADED**: + Wert (also mal 3)
- **$ADEF**: als Zeiger ins Y-Register
- **$ADF0**: bisheriger Prioritätswert
- **$ADF1**: mit Prioritätsw. vergleichen
- **$ADF4**: größer: $AE5D
- **$ADF6**: prüft auf numerisch
- **$ADF9**: Prioritätswert retten
- **$ADFA**: Operatoradr. und Operanden r.
- **$ADFE**: Operator?
- **$AE00**: ja: $AE19
- **$AE02**: weitere Operation?
- **$AE03**: nein: RTS
- **$AE05**: ARG vom Stapel holen
- **$AE07**: Stringflag löschen
- **$AE09**: Operatormaske nach
- **$AE0A**: links schieben
- **$AE0B**: Programmzeiger holen (LOW)
- **$AE0D**: =0: HIGH-Byte vermindern
- **$AE0F**: HIGH-Byte vermindern
- **$AE11**: LOW-Byte vermindern
- **$AE13**: Offset des Hierarchieflags
- **$AE15**: Flag setzen
- **$AE17**: unbedingter Sprung
- **$AE19**: mit Hierarchieflag vergl.
- **$AE1C**: größer: $AE66
- **$AE1E**: sonst weiter
- **$AE20**: Operationsadresse (HIGH)
- **$AE23**: auf Stapel retten
- **$AE24**: Operationsadresse (LOW)
- **$AE27**: auf Stapel retten
- **$AE28**: Operanden auf Stapel retten
- **$AE2B**: Operatormaske laden
- **$AE2D**: zum Schleifenanfang
- **$AE30**: gibt 'SYNTAX ERROR'
- **$AE33**: Vorzeichen von FAC
- **$AE35**: Hierarchieflag
- **$AE38**: Vorzeichen ins Y-Reg.
- **$AE39**: Rücksprungadresse holen
- **$AE3A**: und merken
- **$AE3C**: Rücksprungadresse erhöhen
- **$AE3E**: nächstes Adressbyte holen
- **$AE3F**: und speichern
- **$AE41**: Vorzeichen wieder in Akku
- **$AE42**: und auf Stapel legen
- **$AE43**: FAC runden
- **$AE46**: FAC auf Stapel legen
- **$AE48**: 1. Byte retten
- **$AE49**: 2. Byte holen
- **$AE4B**: und retten
- **$AE4C**: 3. Byte holen
- **$AE4E**: und retten
- **$AE4F**: 4. Byte holen
- **$AE51**: und retten
- **$AE52**: 5. Byte holen
- **$AE54**: und retten
- **$AE55**: Sprung auf Operation
- **$AE58**: Flagwert für Operator
- **$AE5A**: Prioritätsflag retten
- **$AE5B**: =0? ja: $AE80
- **$AE5D**: =$64?
- **$AE5F**: ja: $AE64
- **$AE61**: prüft auf numerisch
- **$AE64**: flag fur Operator
- **$AE66**: Akku vom Stapel holen
- **$AE67**: halbieren
- **$AE68**: und abspeichern
- **$AE6A**: ARG von Stapel holen
- **$AE6B**: 1. Byte speichern
- **$AE6D**: 2. Byte holen
- **$AE6E**: und speichern
- **$AE70**: 3. Byte holen
- **$AE71**: und speichern
- **$AE73**: 4. Byte holen
- **$AE74**: und speichern
- **$AE76**: 5. Byte holen
- **$AE77**: und speichern
- **$AE79**: 6. Byte (Vorzeichen holen
- **$AE7A**: und speichern
- **$AE7C**: Vorzeichen von ARG und FAC
- **$AE7E**: verknüpfen und speichern
- **$AE80**: Exponentbyte von FAC laden
- **$AE82**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$ADBC**: code for greater than

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AD9E**: DECREMENT TXTPTR
- **$ADA6**: START WITH PRECEDENCE = 0
- **$ADA8**: TRICK TO SKIP FOLLOWING "PHA"
- **$ADA9**: PUSH RELOPS FLAGS
- **$ADAB**: SAVE LAST PRECEDENCE
- **$ADAE**: CHECK IF ENOUGH ROOM ON STACK
- **$ADB1**: GET AN ELEMENT
- **$ADB6**: CLEAR COMPARISON OPERATOR FLAGS
- **$ADB8**: CHECK FOR RELATIONAL OPERATORS
- **$ADBB**: > IS $CF, = IS $D0, < IS $D1
- **$ADBC**: > IS 0, = IS 1, < IS 2
- **$ADBE**: NOT RELATIONAL OPERATOR
- **$ADC2**: NOT RELATIONAL OPERATOR
- **$ADC4**: SET CARRY IF "=" OR "<"
- **$ADC6**: NOW > IS 0, = IS 3, < IS 5
- **$ADC7**: NOW > IS 1, = IS 2, < IS 4
- **$ADC9**: SET BITS OF CPRTYP:  00000<=>
- **$ADCB**: CHECK FOR ILLEGAL COMBINATIONS
- **$ADCD**: IF LESS THAN, A RELOP WAS REPEATED
- **$ADD1**: ANOTHER OPERATOR?
- **$ADD4**: CHECK FOR <,=,> AGAIN
- **$ADD7**: DID WE FIND A RELATIONAL OPERATOR?
- **$ADD9**: YES
- **$ADDB**: NO, AND NEXT TOKEN IS > $D1
- **$ADDD**: NO, AND NEXT TOKEN < $CF
- **$ADDF**: IF NEXT TOKEN < "+"
- **$ADE1**: + AND LAST RESULT A STRING?
- **$ADE3**: BRANCH IF NOT
- **$ADE5**: CONCATENATE IF SO.
- **$ADE8**: +-*/ IS 0123
- **$ADEC**: MULTIPLY BY 3
- **$ADED**: +-*/ IS 0,3,6,9
- **$ADF0**: GET LAST PRECEDENCE
- **$ADF4**: DO NOW IF HIGHER PRECEDENCE
- **$ADF6**: WAS LAST RESULT A #?
- **$ADF9**: YES, SAVE PRECEDENCE ON STACK
- **$ADFA**: SAVE REST, CALL FRMEVL RECURSIVELY
- **$AE03**: EXIT IF NO MATH IN EXPRESSION
- **$AE05**: ...ALWAYS FOUND ONE OR MORE RELATIONAL OPERATORS <,=,>
- **$AE07**: (VALTYP) = 0 (NUMERIC), = $FF (STRING)
- **$AE09**: SET CPRTYP TO 0000<=>C
- **$AE0A**: WHERE C=0 IF #, C=1 IF STRING
- **$AE0B**: BACK UP TXTPTR
- **$AE13**: POINT AT RELOPS ENTRY
- **$AE17**: ...ALWAYS
- **$AE1C**: DO NOW IF HIGHER PRECEDENCE
- **$AE1E**: ...ALWAYS STACK THIS OPERATION AND CALL FRMEVL FOR ANOTHER ONE
- **$AE23**: PUSH ADDRESS OF OPERATION PERFORMER
- **$AE28**: STACK FAC.SIGN AND FAC
- **$AE2B**: A=RELOP FLAGS, X=PRECEDENCE BYTE
- **$AE2D**: RECURSIVELY CALL FRMEVL

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*