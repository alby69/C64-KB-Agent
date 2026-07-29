---
title: perform PRINT
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
- aaa0-basic-befehl-print
- ab45-print
- cursor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AAA0
  address_end: $AAC8
  symbol: perform-print
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AAA0**: if nothing following just print CR/LF'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AAA0**: Trennzeichen: $AAD7'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AAA4**: TAB( code'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AAA0**: NO MORE LIST, PRINT <RETURN>'
---

# $AAA0 — perform PRINT

## Disassemblatura
```assembly
.AAA0  F0 35    BEQ $AAD7   ; if nothing following just print CR/LF
.AAA2  F0 43    BEQ $AAE7   ; exit if nothing following, end of PRINT branch
.AAA4  C9 A3    CMP #$A3   ; compare with token for TAB(
.AAA6  F0 50    BEQ $AAF8   ; if TAB( go handle it
.AAA8  C9 A6    CMP #$A6   ; compare with token for SPC(
.AAAA  18       CLC   ; flag SPC(
.AAAB  F0 4B    BEQ $AAF8   ; if SPC( go handle it
.AAAD  C9 2C    CMP #$2C   ; compare with ","
.AAAF  F0 37    BEQ $AAE8   ; if "," go skip to the next TAB position
.AAB1  C9 3B    CMP #$3B   ; compare with ";"
.AAB3  F0 5E    BEQ $AB13   ; if ";" go continue the print loop
.AAB5  20 9E AD JSR $AD9E   ; evaluate expression
.AAB8  24 0D    BIT $0D   ; test data type flag, $FF = string, $00 = numeric
.AABA  30 DE    BMI $AA9A   ; if string go print string, scan memory and continue PRINT
.AABC  20 DD BD JSR $BDDD   ; convert FAC1 to ASCII string result in (AY)
.AABF  20 87 B4 JSR $B487   ; print " terminated string to utility pointer
.AAC2  20 21 AB JSR $AB21   ; print string from utility pointer
.AAC5  20 3B AB JSR $AB3B   ; print [SPACE] or [CURSOR RIGHT]
.AAC8  D0 D3    BNE $AA9D   ; go scan memory and continue PRINT, branch always
```


## Commenti

### Original Disassembly (—)
- **$AAA0**: if nothing following just print CR/LF
- **$AAA2**: exit if nothing following, end of PRINT branch
- **$AAA4**: compare with token for TAB(
- **$AAA6**: if TAB( go handle it
- **$AAA8**: compare with token for SPC(
- **$AAAA**: flag SPC(
- **$AAAB**: if SPC( go handle it
- **$AAAD**: compare with ","
- **$AAAF**: if "," go skip to the next TAB position
- **$AAB1**: compare with ";"
- **$AAB3**: if ";" go continue the print loop
- **$AAB5**: evaluate expression
- **$AAB8**: test data type flag, $FF = string, $00 = numeric
- **$AABA**: if string go print string, scan memory and continue PRINT
- **$AABC**: convert FAC1 to ASCII string result in (AY)
- **$AABF**: print " terminated string to utility pointer
- **$AAC2**: print string from utility pointer
- **$AAC5**: print [SPACE] or [CURSOR RIGHT]
- **$AAC8**: go scan memory and continue PRINT, branch always

### Commodore-64-intern-Buch (Commodore)
- **$AAA0**: Trennzeichen: $AAD7
- **$AAA2**: Trennz. (TAB, SPC): RTS
- **$AAA4**: 'TAB('-Code?
- **$AAA6**: ja: $AAF8
- **$AAA8**: 'SPC('-Code?
- **$AAAA**: Flag für SPC setzen
- **$AAAB**: SPC-Code: $AAF8
- **$AAAD**: ','-Code? (Komma)
- **$AAAF**: ja: $AAE8
- **$AAB1**: ';'-Code? (Semikolon)
- **$AAB3**: ja: nächstes Zeichen, weiter
- **$AAB5**: FRMEVL: Term holen
- **$AAB8**: Typflag
- **$AABA**: String?
- **$AABC**: FAC in ASCII-String wandeln
- **$AABF**: Stringparameter holen
- **$AAC2**: String drucken
- **$AAC5**: Cursor right bzw. Leerzeichen
- **$AAC8**: weiter machen
- **$AACA**: Eingabepuffer
- **$AACC**: mit $0 abschließen
- **$AACF**: Zeiger auf
- **$AAD1**: Eingabepuffer ab $0200 setzen
- **$AAD3**: Nummer des Ausgabegeräts
- **$AAD5**: Tastatur? nein: RTS
- **$AAD7**: 'CR' carriage return
- **$AAD9**: ausgeben
- **$AADC**: logische Filenummer
- **$AADE**: kleiner 128?
- **$AAE0**: 'LF' line feed
- **$AAE2**: ausgeben
- **$AAE5**: NOT
- **$AAE7**: Rücksprung
- **$AAE8**: Zehner-Tabulator mit Komma
- **$AAE9**: Cursorposition holen
- **$AAEC**: Spalte ins Y-Reg.
- **$AAED**: Carry setzen (Subtr.)
- **$AAEE**: 10 abziehen
- **$AAF0**: nicht negativ?
- **$AAF2**: invertieren
- **$AAF4**: +1 (Zweierkomplement)
- **$AAF6**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
- **$AAA4**: TAB( code
- **$AAA8**: SPC( code
- **$AAAD**: comma
- **$AAB1**: semi-colon

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AAA0**: NO MORE LIST, PRINT <RETURN>
- **$AAA2**: NO MORE LIST, DON'T PRINT <RETURN>
- **$AAA6**: C=1 FOR TAB(
- **$AAAB**: C=0 FOR SPC(
- **$AAB5**: EVALUATE EXPRESSION
- **$AAB8**: STRING OR FP VALUE?
- **$AABA**: STRING
- **$AABC**: FP: CONVERT INTO BUFFER
- **$AABF**: MAKE BUFFER INTO STRING
- **$AAC8**: PRINT THE STRING
- **$AAD7**: PRINT <RETURN>
- **$AAE5**: <<< WHY??? >>>
- **$AAF8**: C=0 FOR SPC(, C=1 FOR TAB(
- **$AAFF**: GET VALUE
- **$AB02**: TRAILING PARENTHESIS
- **$AB04**: NO, SYNTAX ERROR
- **$AB06**: TAB( OR SPC(
- **$AB07**: SPC(
- **$AB09**: CALCULATE SPACES NEEDED FOR TAB(
- **$AB0C**: ALREADY PAST THAT COLUMN
- **$AB0E**: NOW DO A SPC( TO THE SPECIFIED COLUMN
- **$AB11**: MORE SPACES TO PRINT
- **$AB16**: CONTINUE PARSING PRINT LIST
- **$AB1C**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*