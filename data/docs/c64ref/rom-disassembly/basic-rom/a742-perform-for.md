---
title: perform FOR
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
- a742-basic-befehl-for
- a78b-step-phrase-of-for-statement
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A742
  address_end: $A7AD
  symbol: perform-for
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A742**: set FNX'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A742**: Wert laden und'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A780**: low  A78B'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A744**: SUBSCRIPTS NOT ALLOWED'
---

# $A742 — perform FOR

## Disassemblatura
```assembly
.A742  A9 80    LDA #$80   ; set FNX
.A744  85 10    STA $10   ; set subscript/FNX flag
.A746  20 A5 A9 JSR $A9A5   ; perform LET
.A749  20 8A A3 JSR $A38A   ; search the stack for FOR or GOSUB activity
.A74C  D0 05    BNE $A753   ; branch if FOR, this variable, not found FOR, this variable, was found so first we dump the old one
.A74E  8A       TXA   ; copy index
.A74F  69 0F    ADC #$0F   ; add FOR structure size-2
.A751  AA       TAX   ; copy to index
.A752  9A       TXS   ; set stack (dump FOR structure (-2 bytes))
.A753  68       PLA   ; pull return address
.A754  68       PLA   ; pull return address
.A755  A9 09    LDA #$09   ; we need 18d bytes !
.A757  20 FB A3 JSR $A3FB   ; check room on stack for 2*A bytes
.A75A  20 06 A9 JSR $A906   ; scan for next BASIC statement ([:] or [EOL])
.A75D  18       CLC   ; clear carry for add
.A75E  98       TYA   ; copy index to A
.A75F  65 7A    ADC $7A   ; add BASIC execute pointer low byte
.A761  48       PHA   ; push onto stack
.A762  A5 7B    LDA $7B   ; get BASIC execute pointer high byte
.A764  69 00    ADC #$00   ; add carry
.A766  48       PHA   ; push onto stack
.A767  A5 3A    LDA $3A   ; get current line number high byte
.A769  48       PHA   ; push onto stack
.A76A  A5 39    LDA $39   ; get current line number low byte
.A76C  48       PHA   ; push onto stack
.A76D  A9 A4    LDA #$A4   ; set "TO" token
.A76F  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.A772  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.A775  20 8A AD JSR $AD8A   ; evaluate expression and check is numeric, else do type mismatch
.A778  A5 66    LDA $66   ; get FAC1 sign (b7)
.A77A  09 7F    ORA #$7F   ; set all non sign bits
.A77C  25 62    AND $62   ; and FAC1 mantissa 1
.A77E  85 62    STA $62   ; save FAC1 mantissa 1
.A780  A9 8B    LDA #$8B   ; set return address low byte
.A782  A0 A7    LDY #$A7   ; set return address high byte
.A784  85 22    STA $22   ; save return address low byte
.A786  84 23    STY $23   ; save return address high byte
.A788  4C 43 AE JMP $AE43   ; round FAC1 and put on stack, returns to next instruction
.A78B  A9 BC    LDA #$BC   ; set 1 pointer low address, default step size
.A78D  A0 B9    LDY #$B9   ; set 1 pointer high address
.A78F  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
.A792  20 79 00 JSR $0079   ; scan memory
.A795  C9 A9    CMP #$A9   ; compare with STEP token
.A797  D0 06    BNE $A79F   ; if not "STEP" continue was step so ....
.A799  20 73 00 JSR $0073   ; increment and scan memory
.A79C  20 8A AD JSR $AD8A   ; evaluate expression and check is numeric, else do type mismatch
.A79F  20 2B BC JSR $BC2B   ; get FAC1 sign, return A = $FF -ve, A = $01 +ve
.A7A2  20 38 AE JSR $AE38   ; push sign, round FAC1 and put on stack
.A7A5  A5 4A    LDA $4A   ; get FOR/NEXT variable pointer high byte
.A7A7  48       PHA   ; push on stack
.A7A8  A5 49    LDA $49   ; get FOR/NEXT variable pointer low byte
.A7AA  48       PHA   ; push on stack
.A7AB  A9 81    LDA #$81   ; get FOR token
.A7AD  48       PHA   ; push on stack
```


## Commenti

### Original Disassembly (—)
- **$A742**: set FNX
- **$A744**: set subscript/FNX flag
- **$A746**: perform LET
- **$A749**: search the stack for FOR or GOSUB activity
- **$A74C**: branch if FOR, this variable, not found FOR, this variable, was found so first we dump the old one
- **$A74E**: copy index
- **$A74F**: add FOR structure size-2
- **$A751**: copy to index
- **$A752**: set stack (dump FOR structure (-2 bytes))
- **$A753**: pull return address
- **$A754**: pull return address
- **$A755**: we need 18d bytes !
- **$A757**: check room on stack for 2*A bytes
- **$A75A**: scan for next BASIC statement ([:] or [EOL])
- **$A75D**: clear carry for add
- **$A75E**: copy index to A
- **$A75F**: add BASIC execute pointer low byte
- **$A761**: push onto stack
- **$A762**: get BASIC execute pointer high byte
- **$A764**: add carry
- **$A766**: push onto stack
- **$A767**: get current line number high byte
- **$A769**: push onto stack
- **$A76A**: get current line number low byte
- **$A76C**: push onto stack
- **$A76D**: set "TO" token
- **$A76F**: scan for CHR$(A), else do syntax error then warm start
- **$A772**: check if source is numeric, else do type mismatch
- **$A775**: evaluate expression and check is numeric, else do type mismatch
- **$A778**: get FAC1 sign (b7)
- **$A77A**: set all non sign bits
- **$A77C**: and FAC1 mantissa 1
- **$A77E**: save FAC1 mantissa 1
- **$A780**: set return address low byte
- **$A782**: set return address high byte
- **$A784**: save return address low byte
- **$A786**: save return address high byte
- **$A788**: round FAC1 and put on stack, returns to next instruction
- **$A78B**: set 1 pointer low address, default step size
- **$A78D**: set 1 pointer high address
- **$A78F**: unpack memory (AY) into FAC1
- **$A792**: scan memory
- **$A795**: compare with STEP token
- **$A797**: if not "STEP" continue was step so ....
- **$A799**: increment and scan memory
- **$A79C**: evaluate expression and check is numeric, else do type mismatch
- **$A79F**: get FAC1 sign, return A = $FF -ve, A = $01 +ve
- **$A7A2**: push sign, round FAC1 and put on stack
- **$A7A5**: get FOR/NEXT variable pointer high byte
- **$A7A7**: push on stack
- **$A7A8**: get FOR/NEXT variable pointer low byte
- **$A7AA**: push on stack
- **$A7AB**: get FOR token
- **$A7AD**: push on stack

### Commodore-64-intern-Buch (Commodore)
- **$A742**: Wert laden und
- **$A744**: Integer sperren
- **$A746**: LET, setzt FOR-Variable
- **$A749**: sucht offene FOR-NEXT-Schlei.
- **$A74C**: nicht gefunden: $A753
- **$A74E**: X-Reg. nach Akku
- **$A74F**: Stapelzejger erhöhen
- **$A751**: Akku zurück nach X-Reg. und
- **$A752**: in den Stapelzeiger
- **$A753**: Rücksprungadresse vom Stapel
- **$A754**: holen (LOW und HIGH)
- **$A755**: Wert für Prüfung laden
- **$A757**: prüft auf Platz im Stapel
- **$A75A**: sucht nächstes BAS.-Statement
- **$A75D**: Carry löschen (Addition)
- **$A75E**: CHRGET-Zeiger und Offset
- **$A75F**: = Startadresse der Schleife
- **$A761**: auf Stapel speichern
- **$A762**: HIGH-Byte holen und
- **$A764**: Übertrag addieren und
- **$A766**: auf den Stapel legen
- **$A767**: Aktuelle
- **$A769**: Zeilennummer laden und auf
- **$A76A**: den Stapel schieben
- **$A76C**: (LOW und HIGH-Byte)
- **$A76D**: 'TO' - Code
- **$A76F**: prüft auf Code
- **$A772**: prüft ob numerische Variable
- **$A775**: numerischer Ausdruck nach FAC
- **$A778**: Vorzeichenbyte von FAC holen
- **$A77A**: Bit 0 bis 6 setzen
- **$A77C**: mit $62 angleichen
- **$A77E**: und abspeichern
- **$A780**: Rücksprungadresse laden
- **$A782**: (LOW und HIGH)
- **$A784**: und Zwischenspeichern
- **$A786**: (LOW und HIGH)
- **$A788**: Schleifenendwert auf Stapel
- **$A78B**: Zeiger auf Konstante 1 setzen
- **$A78D**: (Ersatzwert für STEP)
- **$A78F**: als Default-STEP-Wert in FAC
- **$A792**: CHRGOT: letztes Zeichen holen
- **$A795**: 'STEP' - Code?
- **$A797**: kein STEP-Wert: $A79F
- **$A799**: CHRGET nächstes Zeichen holen
- **$A79C**: numerischer Ausdruck nach FAC
- **$A79F**: holt Vorzeichenbyte
- **$A7A2**: Vorz. und STEP-Wert auf Stack
- **$A7A5**: Zeiger auf Variablenwert
- **$A7A7**: (LOW) auf den Stapel
- **$A7A8**: Zeiger (HIGH)
- **$A7AA**: auf den Stapel
- **$A7AB**: und FOR-Code
- **$A7AD**: auf den Stapel legen

### Marko Mäkelä (Marko Mäkelä)
- **$A780**: low  A78B
- **$A782**: high A78B
- **$A78B**: low  B9BC
- **$A78D**: high B9BC
- **$A7AB**: FOR block code

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A744**: SUBSCRIPTS NOT ALLOWED
- **$A746**: DO <VAR> = <EXP>, STORE ADDR IN FORPNT
- **$A749**: IS THIS FOR VARIABLE ACTIVE?
- **$A74C**: NO
- **$A74E**: YES, CANCEL IT AND ENCLOSED LOOPS
- **$A74F**: CARRY=1, THIS ADDS 16
- **$A751**: X WAS ALREADY S+2
- **$A753**: POP RETURN ADDRESS TOO
- **$A755**: BE CERTAIN ENOUGH ROOM IN STACK
- **$A75A**: SCAN AHEAD TO NEXT STATEMENT
- **$A75D**: PUSH STATEMENT ADDRESS ON STACK
- **$A767**: PUSH LINE NUMBER ON STACK
- **$A76F**: REQUIRE "TO"
- **$A772**: <VAR> = <EXP> MUST BE NUMERIC
- **$A775**: GET FINAL VALUE, MUST BE NUMERIC
- **$A778**: PUT SIGN INTO VALUE IN FAC
- **$A780**: SET UP FOR RETURN
- **$A782**: TO STEP
- **$A788**: RETURNS BY "JMP (INDEX)"

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*