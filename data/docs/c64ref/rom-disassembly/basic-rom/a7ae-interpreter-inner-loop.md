---
title: interpreter inner loop
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
- a7ae-interpreterschleife
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A7AE
  address_end: $A7E1
  symbol: interpreter-inner-loop
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A7AE**: do CRTL-C check vector'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A7AE**: prüft auf Stop-Taste'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A7E1**: normally A7E4'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A7AE**: SEE IF CONTROL-C HAS BEEN TYPED'
---

# $A7AE — interpreter inner loop

## Disassemblatura
```assembly
.A7AE  20 2C A8 JSR $A82C   ; do CRTL-C check vector
.A7B1  A5 7A    LDA $7A   ; get the BASIC execute pointer low byte
.A7B3  A4 7B    LDY $7B   ; get the BASIC execute pointer high byte
.A7B5  C0 02    CPY #$02   ; compare the high byte with $02xx
.A7B7  EA       NOP   ; unused byte
.A7B8  F0 04    BEQ $A7BE   ; if immediate mode skip the continue pointer save
.A7BA  85 3D    STA $3D   ; save the continue pointer low byte
.A7BC  84 3E    STY $3E   ; save the continue pointer high byte
.A7BE  A0 00    LDY #$00   ; clear the index
.A7C0  B1 7A    LDA ($7A),Y   ; get a BASIC byte
.A7C2  D0 43    BNE $A807   ; if not [EOL] go test for ":"
.A7C4  A0 02    LDY #$02   ; else set the index
.A7C6  B1 7A    LDA ($7A),Y   ; get next line pointer high byte
.A7C8  18       CLC   ; clear carry for no "BREAK" message
.A7C9  D0 03    BNE $A7CE   ; branch if not end of program
.A7CB  4C 4B A8 JMP $A84B   ; else go to immediate mode,was immediate or [EOT] marker
.A7CE  C8       INY   ; increment index
.A7CF  B1 7A    LDA ($7A),Y   ; get line number low byte
.A7D1  85 39    STA $39   ; save current line number low byte
.A7D3  C8       INY   ; increment index
.A7D4  B1 7A    LDA ($7A),Y   ; get line # high byte
.A7D6  85 3A    STA $3A   ; save current line number high byte
.A7D8  98       TYA   ; A now = 4
.A7D9  65 7A    ADC $7A   ; add BASIC execute pointer low byte, now points to code
.A7DB  85 7A    STA $7A   ; save BASIC execute pointer low byte
.A7DD  90 02    BCC $A7E1   ; branch if no overflow
.A7DF  E6 7B    INC $7B   ; else increment BASIC execute pointer high byte
.A7E1  6C 08 03 JMP ($0308)   ; do start new BASIC code
```


## Commenti

### Original Disassembly (—)
- **$A7AE**: do CRTL-C check vector
- **$A7B1**: get the BASIC execute pointer low byte
- **$A7B3**: get the BASIC execute pointer high byte
- **$A7B5**: compare the high byte with $02xx
- **$A7B7**: unused byte
- **$A7B8**: if immediate mode skip the continue pointer save
- **$A7BA**: save the continue pointer low byte
- **$A7BC**: save the continue pointer high byte
- **$A7BE**: clear the index
- **$A7C0**: get a BASIC byte
- **$A7C2**: if not [EOL] go test for ":"
- **$A7C4**: else set the index
- **$A7C6**: get next line pointer high byte
- **$A7C8**: clear carry for no "BREAK" message
- **$A7C9**: branch if not end of program
- **$A7CB**: else go to immediate mode,was immediate or [EOT] marker
- **$A7CE**: increment index
- **$A7CF**: get line number low byte
- **$A7D1**: save current line number low byte
- **$A7D3**: increment index
- **$A7D4**: get line # high byte
- **$A7D6**: save current line number high byte
- **$A7D8**: A now = 4
- **$A7D9**: add BASIC execute pointer low byte, now points to code
- **$A7DB**: save BASIC execute pointer low byte
- **$A7DD**: branch if no overflow
- **$A7DF**: else increment BASIC execute pointer high byte
- **$A7E1**: do start new BASIC code

### Commodore-64-intern-Buch (Commodore)
- **$A7AE**: prüft auf Stop-Taste
- **$A7B1**: CHRGET Zeiger (LOW und HIGH)
- **$A7B3**: laden
- **$A7B5**: Direkt-Modus?
- **$A7B7**: No OPeration
- **$A7B8**: ja: $A7BE
- **$A7BA**: als Zeiger für CONT
- **$A7BC**: merken
- **$A7BE**: Zeiger setzen
- **$A7C0**: laufendes Zeichen holen
- **$A7C2**: nicht Zeilenende?
- **$A7C4**: Zeiger neu setzen
- **$A7C6**: Programmende?
- **$A7C8**: Flag für END setzen
- **$A7C9**: Kein Programmende: $A7CE
- **$A7CB**: ja: dann END ausführen
- **$A7CE**: Zeiger erhöhen
- **$A7CF**: laufende Zeilennummer
- **$A7D1**: (LOW) nach $39
- **$A7D3**: Zeiger auf nächstes Byte
- **$A7D4**: laufende Zeilennummer
- **$A7D6**: (HIGH) nach $3A
- **$A7D8**: Zeiger nach Akku
- **$A7D9**: Programmzeiger auf
- **$A7DB**: Programmzeile setzen
- **$A7DD**: C=0: Erhöhung umgehen
- **$A7DF**: Programmzeiger (HIGH) erhöhen
- **$A7E1**: Statement ausführen
- **$A7E4**: CHRGET nächstes Zeichen holen
- **$A7E7**: Statement ausführen
- **$A7EA**: zurück zur Interpreterschlei.

### Marko Mäkelä (Marko Mäkelä)
- **$A7E1**: normally A7E4

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A7AE**: SEE IF CONTROL-C HAS BEEN TYPED
- **$A7B1**: NO, KEEP EXECUTING
- **$A7B8**: IN DIRECT MODE
- **$A7BA**: IN RUNNING MODE
- **$A7C0**: END OF LINE YET?
- **$A7C2**: NO
- **$A7C4**: YES, SEE IF END OF PROGRAM
- **$A7CB**: YES, END OF PROGRAM
- **$A7CF**: GET LINE # OF NEXT LINE
- **$A7D8**: ADJUST TXTPTR TO START
- **$A7D9**: OF NEW LINE
- **$A7E4**: GET FIRST CHR OF STATEMENT
- **$A7E7**: AND START PROCESSING
- **$A7EA**: BACK FOR MORE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*