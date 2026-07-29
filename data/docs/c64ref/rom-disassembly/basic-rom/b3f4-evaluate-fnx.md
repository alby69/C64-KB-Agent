---
title: Evaluate FNx
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
- b3f4-basic-funktion-fn
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B3F4
  address_end: $B446
  symbol: evaluate-fnx
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B3F4**: check FNx syntax'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B3F4**: prüft FN-Syntax'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B3F4**: PARSE "FN", FUNCTION NAME'
---

# $B3F4 — Evaluate FNx

## Disassemblatura
```assembly
.B3F4  20 E1 B3 JSR $B3E1   ; check FNx syntax
.B3F7  A5 4F    LDA $4F   ; get function pointer high byte
.B3F9  48       PHA   ; push it
.B3FA  A5 4E    LDA $4E   ; get function pointer low byte
.B3FC  48       PHA   ; push it
.B3FD  20 F1 AE JSR $AEF1   ; evaluate expression within parentheses
.B400  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.B403  68       PLA   ; pop function pointer low byte
.B404  85 4E    STA $4E   ; restore it
.B406  68       PLA   ; pop function pointer high byte
.B407  85 4F    STA $4F   ; restore it
.B409  A0 02    LDY #$02   ; index to variable pointer high byte
.B40B  B1 4E    LDA ($4E),Y   ; get variable address low byte
.B40D  85 47    STA $47   ; save current variable pointer low byte
.B40F  AA       TAX   ; copy address low byte
.B410  C8       INY   ; index to variable address high byte
.B411  B1 4E    LDA ($4E),Y   ; get variable pointer high byte
.B413  F0 99    BEQ $B3AE   ; branch if high byte zero
.B415  85 48    STA $48   ; save current variable pointer high byte
.B417  C8       INY   ; index to mantissa 3 now stack the function variable value before use
.B418  B1 47    LDA ($47),Y   ; get byte from variable
.B41A  48       PHA   ; stack it
.B41B  88       DEY   ; decrement index
.B41C  10 FA    BPL $B418   ; loop until variable stacked
.B41E  A4 48    LDY $48   ; get current variable pointer high byte
.B420  20 D4 BB JSR $BBD4   ; pack FAC1 into (XY)
.B423  A5 7B    LDA $7B   ; get BASIC execute pointer high byte
.B425  48       PHA   ; push it
.B426  A5 7A    LDA $7A   ; get BASIC execute pointer low byte
.B428  48       PHA   ; push it
.B429  B1 4E    LDA ($4E),Y   ; get function execute pointer low byte
.B42B  85 7A    STA $7A   ; save BASIC execute pointer low byte
.B42D  C8       INY   ; index to high byte
.B42E  B1 4E    LDA ($4E),Y   ; get function execute pointer high byte
.B430  85 7B    STA $7B   ; save BASIC execute pointer high byte
.B432  A5 48    LDA $48   ; get current variable pointer high byte
.B434  48       PHA   ; push it
.B435  A5 47    LDA $47   ; get current variable pointer low byte
.B437  48       PHA   ; push it
.B438  20 8A AD JSR $AD8A   ; evaluate expression and check is numeric, else do type mismatch
.B43B  68       PLA   ; pull variable address low byte
.B43C  85 4E    STA $4E   ; save variable address low byte
.B43E  68       PLA   ; pull variable address high byte
.B43F  85 4F    STA $4F   ; save variable address high byte
.B441  20 79 00 JSR $0079   ; scan memory
.B444  F0 03    BEQ $B449   ; branch if null (should be [EOL] marker)
.B446  4C 08 AF JMP $AF08   ; else syntax error then warm start
```


## Commenti

### Original Disassembly (—)
- **$B3F4**: check FNx syntax
- **$B3F7**: get function pointer high byte
- **$B3F9**: push it
- **$B3FA**: get function pointer low byte
- **$B3FC**: push it
- **$B3FD**: evaluate expression within parentheses
- **$B400**: check if source is numeric, else do type mismatch
- **$B403**: pop function pointer low byte
- **$B404**: restore it
- **$B406**: pop function pointer high byte
- **$B407**: restore it
- **$B409**: index to variable pointer high byte
- **$B40B**: get variable address low byte
- **$B40D**: save current variable pointer low byte
- **$B40F**: copy address low byte
- **$B410**: index to variable address high byte
- **$B411**: get variable pointer high byte
- **$B413**: branch if high byte zero
- **$B415**: save current variable pointer high byte
- **$B417**: index to mantissa 3 now stack the function variable value before use
- **$B418**: get byte from variable
- **$B41A**: stack it
- **$B41B**: decrement index
- **$B41C**: loop until variable stacked
- **$B41E**: get current variable pointer high byte
- **$B420**: pack FAC1 into (XY)
- **$B423**: get BASIC execute pointer high byte
- **$B425**: push it
- **$B426**: get BASIC execute pointer low byte
- **$B428**: push it
- **$B429**: get function execute pointer low byte
- **$B42B**: save BASIC execute pointer low byte
- **$B42D**: index to high byte
- **$B42E**: get function execute pointer high byte
- **$B430**: save BASIC execute pointer high byte
- **$B432**: get current variable pointer high byte
- **$B434**: push it
- **$B435**: get current variable pointer low byte
- **$B437**: push it
- **$B438**: evaluate expression and check is numeric, else do type mismatch
- **$B43B**: pull variable address low byte
- **$B43C**: save variable address low byte
- **$B43E**: pull variable address high byte
- **$B43F**: save variable address high byte
- **$B441**: scan memory
- **$B444**: branch if null (should be [EOL] marker)
- **$B446**: else syntax error then warm start

### Commodore-64-intern-Buch (Commodore)
- **$B3F4**: prüft FN-Syntax
- **$B3F7**: LOW- und HiGH-Byte des
- **$B3F9**: FN-Variablenzeigers
- **$B3FA**: auf den Stapel
- **$B3FC**: legen
- **$B3FD**: holt Term in Klammern
- **$B400**: prüft auf numerisch
- **$B403**: LOW- und HIGH-Byte
- **$B404**: des
- **$B406**: FN-Variablenzeigers wieder-
- **$B407**: holen und speichern
- **$B409**: Zeiger setzen
- **$B40B**: Zeiger (LOW) auf FN-Variable
- **$B40D**: in Variablenadresszeiger
- **$B40F**: und ins X-Reg.
- **$B410**: Zeiger erhöhen
- **$B411**: Zeiger (HIGH) laden
- **$B413**: gibt 'undef'd function'
- **$B415**: in Variablenadresse
- **$B417**: Zeiger erhöhen
- **$B418**: FN-Variablenwert holen
- **$B41A**: und auf Stapel retten
- **$B41B**: Zeiger vermindern
- **$B41C**: fertig? nein: nächster Wert
- **$B420**: FAC in FN-Variable übertragen
- **$B423**: Programmzeiger (LOW)
- **$B425**: auf Stapel
- **$B426**: Programmzeiger (HIGH)
- **$B428**: auf Stapel
- **$B429**: LOW und HIGH-Byte
- **$B42B**: des
- **$B42D**: Programmzeigers auf
- **$B42E**: FN-Ausdruck
- **$B430**: speichern
- **$B432**: Zeiger auf FN-Variable
- **$B434**: holen und
- **$B435**: auf den Stapel
- **$B437**: retten
- **$B438**: numerischen Ausdruck holen
- **$B43B**: LOW- und HIGH-Byte
- **$B43C**: des Zeigers auf FN-
- **$B43E**: Variable vom Stapel holen
- **$B43F**: und in FN-Zeiger speichern
- **$B441**: CHRGOT letztes Zeichen holen
- **$B444**: keine weiteren Zeichen?
- **$B446**: gibt 'SYNTAX ERROR'
- **$B449**: LOW- und HIGH-Byte
- **$B44A**: des
- **$B44C**: Programmzeigers
- **$B44D**: zurückholen
- **$B44F**: Zeiger setzen
- **$B451**: FN-Variable vom Stapel
- **$B452**: zurückholen
- **$B454**: und abspeichern
- **$B455**: Zeiger erhöhen
- **$B456**: 2. Wert abspeichern
- **$B458**: 3. Wert vom Stapel holen
- **$B459**: Zeiger erhöhen
- **$B45A**: und abspeichern
- **$B45C**: 4. Wert vom Stapel holen
- **$B45D**: Zeiger erhöhen
- **$B45E**: und abspeichern
- **$B460**: 5. Wert vom Stapel holen
- **$B461**: Zeiger erhöhen
- **$B462**: und abspeichern
- **$B464**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B3F4**: PARSE "FN", FUNCTION NAME
- **$B3F7**: STACK FUNCTION ADDRESS
- **$B3F9**: IN CASE OF A NESTED FN CALL
- **$B3FD**: MUST NOW HAVE "(EXPRESSION)"
- **$B400**: MUST BE NUMERIC EXPRESSION
- **$B403**: GET FUNCTION ADDRESS BACK
- **$B409**: POINT AT ADD OF ARGUMENT VARIABLE
- **$B413**: UNDEFINED FUNCTION
- **$B417**: Y=4 NOW
- **$B418**: SAVE OLD VALUE OF ARGUMENT VARIABLE
- **$B41A**: ON STACK, IN CASE ALSO USED AS
- **$B41B**: A NORMAL VARIABLE!
- **$B41E**: (Y,X)= ADDRESS, STORE FAC IN VARIABLE
- **$B423**: REMEMBER TXTPTR AFTER FN CALL
- **$B429**: Y=0 FROM MOVMF
- **$B42B**: POINT TO FUNCTION DEF'N
- **$B432**: SAVE ADDRESS OF ARGUMENT VARIABLE
- **$B438**: EVALUATE THE FUNCTION EXPRESSION
- **$B43B**: GET ADDRESS OF ARGUMENT VARIABLE
- **$B43C**: AND SAVE IT
- **$B441**: MUST BE AT ":" OR EOL
- **$B444**: WE ARE
- **$B446**: WE ARE NOT, SLYNTAX ERROR
- **$B449**: RETRIEVE TXTPTR AFTER "FN" CALL
- **$B44D**: STACK NOW HAS 5-BYTE VALUE OF THE ARGUMENT VARIABLE, AND FNCNAM POINTS AT THE VARIABLE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*