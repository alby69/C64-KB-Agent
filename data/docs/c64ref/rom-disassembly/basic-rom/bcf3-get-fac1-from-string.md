---
title: get FAC1 from string
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
- bcf3-fliekommaformat
- bd41-found-a-decimal-point
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BCF3
  address_end: $BD66
  symbol: get-fac1-from-string
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BCF3**: clear Y'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BCF3**: Wert festlegen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BCFE**: minus'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BCF3**: CLEAR WORKING AREA ($99...$A3)'
---

# $BCF3 — get FAC1 from string

## Disassemblatura
```assembly
.BCF3  A0 00    LDY #$00   ; clear Y
.BCF5  A2 0A    LDX #$0A   ; set index
.BCF7  94 5D    STY $5D,X   ; clear byte
.BCF9  CA       DEX   ; decrement index
.BCFA  10 FB    BPL $BCF7   ; loop until numexp to negnum (and FAC1) = $00
.BCFC  90 0F    BCC $BD0D   ; branch if first character is numeric
.BCFE  C9 2D    CMP #$2D   ; else compare with "-"
.BD00  D0 04    BNE $BD06   ; branch if not "-"
.BD02  86 67    STX $67   ; set flag for -ve n (negnum = $FF)
.BD04  F0 04    BEQ $BD0A   ; branch always
.BD06  C9 2B    CMP #$2B   ; else compare with "+"
.BD08  D0 05    BNE $BD0F   ; branch if not "+"
.BD0A  20 73 00 JSR $0073   ; increment and scan memory
.BD0D  90 5B    BCC $BD6A   ; branch if numeric character
.BD0F  C9 2E    CMP #$2E   ; else compare with "."
.BD11  F0 2E    BEQ $BD41   ; branch if "."
.BD13  C9 45    CMP #$45   ; else compare with "E"
.BD15  D0 30    BNE $BD47   ; branch if not "E" was "E" so evaluate exponential part
.BD17  20 73 00 JSR $0073   ; increment and scan memory
.BD1A  90 17    BCC $BD33   ; branch if numeric character
.BD1C  C9 AB    CMP #$AB   ; else compare with token for -
.BD1E  F0 0E    BEQ $BD2E   ; branch if token for -
.BD20  C9 2D    CMP #$2D   ; else compare with "-"
.BD22  F0 0A    BEQ $BD2E   ; branch if "-"
.BD24  C9 AA    CMP #$AA   ; else compare with token for +
.BD26  F0 08    BEQ $BD30   ; branch if token for +
.BD28  C9 2B    CMP #$2B   ; else compare with "+"
.BD2A  F0 04    BEQ $BD30   ; branch if "+"
.BD2C  D0 07    BNE $BD35   ; branch always
.BD2E  66 60    ROR $60   ; set exponent -ve flag (C, which=1, into b7)
.BD30  20 73 00 JSR $0073   ; increment and scan memory
.BD33  90 5C    BCC $BD91   ; branch if numeric character
.BD35  24 60    BIT $60   ; test exponent -ve flag
.BD37  10 0E    BPL $BD47   ; if +ve go evaluate exponent else do exponent = -exponent
.BD39  A9 00    LDA #$00   ; clear result
.BD3B  38       SEC   ; set carry for subtract
.BD3C  E5 5E    SBC $5E   ; subtract exponent byte
.BD3E  4C 49 BD JMP $BD49   ; go evaluate exponent
.BD41  66 5F    ROR $5F   ; set decimal point flag
.BD43  24 5F    BIT $5F   ; test decimal point flag
.BD45  50 C3    BVC $BD0A   ; branch if only one decimal point so far evaluate exponent
.BD47  A5 5E    LDA $5E   ; get exponent count byte
.BD49  38       SEC   ; set carry for subtract
.BD4A  E5 5D    SBC $5D   ; subtract numerator exponent
.BD4C  85 5E    STA $5E   ; save exponent count byte
.BD4E  F0 12    BEQ $BD62   ; branch if no adjustment
.BD50  10 09    BPL $BD5B   ; else if +ve go do FAC1*10^expcnt else go do FAC1/10^(0-expcnt)
.BD52  20 FE BA JSR $BAFE   ; divide FAC1 by 10
.BD55  E6 5E    INC $5E   ; increment exponent count byte
.BD57  D0 F9    BNE $BD52   ; loop until all done
.BD59  F0 07    BEQ $BD62   ; branch always
.BD5B  20 E2 BA JSR $BAE2   ; multiply FAC1 by 10
.BD5E  C6 5E    DEC $5E   ; decrement exponent count byte
.BD60  D0 F9    BNE $BD5B   ; loop until all done
.BD62  A5 67    LDA $67   ; get -ve flag
.BD64  30 01    BMI $BD67   ; if -ve do - FAC1 and return
.BD66  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BCF3**: clear Y
- **$BCF5**: set index
- **$BCF7**: clear byte
- **$BCF9**: decrement index
- **$BCFA**: loop until numexp to negnum (and FAC1) = $00
- **$BCFC**: branch if first character is numeric
- **$BCFE**: else compare with "-"
- **$BD00**: branch if not "-"
- **$BD02**: set flag for -ve n (negnum = $FF)
- **$BD04**: branch always
- **$BD06**: else compare with "+"
- **$BD08**: branch if not "+"
- **$BD0A**: increment and scan memory
- **$BD0D**: branch if numeric character
- **$BD0F**: else compare with "."
- **$BD11**: branch if "."
- **$BD13**: else compare with "E"
- **$BD15**: branch if not "E" was "E" so evaluate exponential part
- **$BD17**: increment and scan memory
- **$BD1A**: branch if numeric character
- **$BD1C**: else compare with token for -
- **$BD1E**: branch if token for -
- **$BD20**: else compare with "-"
- **$BD22**: branch if "-"
- **$BD24**: else compare with token for +
- **$BD26**: branch if token for +
- **$BD28**: else compare with "+"
- **$BD2A**: branch if "+"
- **$BD2C**: branch always
- **$BD2E**: set exponent -ve flag (C, which=1, into b7)
- **$BD30**: increment and scan memory
- **$BD33**: branch if numeric character
- **$BD35**: test exponent -ve flag
- **$BD37**: if +ve go evaluate exponent else do exponent = -exponent
- **$BD39**: clear result
- **$BD3B**: set carry for subtract
- **$BD3C**: subtract exponent byte
- **$BD3E**: go evaluate exponent
- **$BD41**: set decimal point flag
- **$BD43**: test decimal point flag
- **$BD45**: branch if only one decimal point so far evaluate exponent
- **$BD47**: get exponent count byte
- **$BD49**: set carry for subtract
- **$BD4A**: subtract numerator exponent
- **$BD4C**: save exponent count byte
- **$BD4E**: branch if no adjustment
- **$BD50**: else if +ve go do FAC1*10^expcnt else go do FAC1/10^(0-expcnt)
- **$BD52**: divide FAC1 by 10
- **$BD55**: increment exponent count byte
- **$BD57**: loop until all done
- **$BD59**: branch always
- **$BD5B**: multiply FAC1 by 10
- **$BD5E**: decrement exponent count byte
- **$BD60**: loop until all done
- **$BD62**: get -ve flag
- **$BD64**: if -ve do - FAC1 and return

### Commodore-64-intern-Buch (Commodore)
- **$BCF3**: Wert festlegen
- **$BCF5**: Zähler stellen
- **$BCF7**: den Bereich
- **$BCF9**: von $5D bis $66 mit
- **$BCFA**: Nullen füllen
- **$BCFC**: wenn erstes Zeichen eine Ziffer, dann zu $BD0D
- **$BCFE**: Nummer für '-'?
- **$BD00**: wenn nicht, dann zu $BD06
- **$BD02**: Flag für negativ
- **$BD04**: unbedingter Sprung
- **$BD06**: Nummer für ' + '
- **$BD08**: wenn nicht, dann zu $BD0F
- **$BD0A**: CHRGET nächstes Zeichen holen
- **$BD0D**: wenn Ziffer, dann zu $BD6A
- **$BD0F**: Nummer für '.'
- **$BD11**: wenn ja, dann zu $BD41
- **$BD13**: Nummer für 'E'
- **$BD15**: wenn nicht, dann zu $BD47
- **$BD17**: CHRGET nächstes Zeichen holen
- **$BD1A**: wenn Ziffer, dann zu $BD33
- **$BD1C**: '-' BASIC-Kode
- **$BD1E**: wenn ja, dann zu $BD2E
- **$BD20**: Nummer für '-'
- **$BD22**: wenn ja, dann zu $BD2E
- **$BD24**: '+' BASIC-Kode
- **$BD26**: wenn ja, dann zu $BD30
- **$BD28**: Nummer für '+'
- **$BD2A**: wenn ja, dann zu $BD30
- **$BD2C**: unbedingter Sprung
- **$BD2E**: Bit 7 setzen
- **$BD30**: CHRGET nächstes Zeichen holen
- **$BD33**: wenn Ziffer, dann zu $BD91
- **$BD35**: Bit 7 gesetzt ?
- **$BD37**: wenn nicht, dann zu $BD47
- **$BD39**: Vorzeichen des
- **$BD3B**: Exponenten
- **$BD3C**: wechseln
- **$BD3E**: weiter bei $BD49
- **$BD41**: Aufruf durch Dezimalpunkt
- **$BD43**: schon zweiter Dezimalpunkt
- **$BD45**: wenn nicht, dann weiter
- **$BD47**: Zahl gemäß
- **$BD49**: Position
- **$BD4A**: des Dezimalpunkts
- **$BD4C**: und Exponenten anpassen
- **$BD4E**: Zahl= Null, dann zu $BD62
- **$BD50**: Zahl kleiner als $7F
- **$BD52**: FAC = FAC / 10
- **$BD55**: Zahl erhöhen
- **$BD57**: unbedingter
- **$BD59**: Sprung
- **$BD5B**: FAC = FAC * 10
- **$BD5E**: Zahl gemäß
- **$BD60**: Exponenten anpassen
- **$BD62**: wenn negativ,
- **$BD64**: dann Vorzeichen invertieren
- **$BD66**: Rücksprung
- **$BD67**: Vorzeichenwechsel FAC = -FAC
- **$BD6A**: Aufruf durch Mantisse
- **$BD6B**: wenn Vorkommastelle,
- **$BD6D**: dann zu $BD71
- **$BD6F**: Zähler erhöhen
- **$BD71**: FAC = FAC * 10
- **$BD74**: ASCII in
- **$BD75**: Ziffer umwandeln
- **$BD76**: '0' abziehen gibt hex
- **$BD78**: addiert nächste Stelle zu FAC
- **$BD7B**: nächstes Zeichen
- **$BD7E**: Wert aus Stack
- **$BD7F**: FAC nach ARG
- **$BD82**: Wert in Stack
- **$BD83**: Accu in höchste Stelle von FAC
- **$BD86**: FAC-Vorzeichen und
- **$BD88**: ARG-Vorzeichen
- **$BD8A**: verknüpfen
- **$BD8C**: erste Stelle von FAC holen
- **$BD8E**: FAC = FAC + ARG
- **$BD91**: Aufruf durch 'E'
- **$BD93**: wenn dritte Exponentenziffer,
- **$BD95**: dann zu $BDA0
- **$BD97**: wenn Vorzeichen
- **$BD99**: negativ,
- **$BD9B**: dann Unterlauf
- **$BD9D**: zu 'OVERFLOW ERROR'
- **$BDA0**: Den
- **$BDA1**: Exponenten
- **$BDA2**: mit
- **$BDA3**: 10
- **$BDA5**: multi-
- **$BDA6**: plizieren
- **$BDA7**: Zähler setzen
- **$BDA9**: Exponenten-
- **$BDAB**: ziffer
- **$BDAC**: addie-
- **$BDAE**: ren
- **$BDB0**: nächstes Zeichen holen

### Marko Mäkelä (Marko Mäkelä)
- **$BCFE**: minus
- **$BD06**: plus
- **$BD0F**: decimal point
- **$BD13**: E
- **$BD1C**: minus code
- **$BD20**: minus
- **$BD24**: plus code
- **$BD28**: plus
- **$BD76**: 0

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BCF3**: CLEAR WORKING AREA ($99...$A3)
- **$BCF5**: TMPEXP, EXPON, DPFLG, EXPSGN, FAC, SERLEN
- **$BCFC**: FIRST CHAR IS A DIGIT
- **$BCFE**: CHECK FOR LEADING SIGN
- **$BD00**: NOT MINUS
- **$BD02**: MINUS, SET SERLEN = $FF FOR FLAG
- **$BD04**: ...ALWAYS
- **$BD06**: MIGHT BE PLUS
- **$BD08**: NOT PLUS EITHER, CHECK DECIMAL POINT
- **$BD0A**: GET NEXT CHAR OF STRING
- **$BD0D**: INSERT THIS DIGIT
- **$BD0F**: CHECK FOR DECIMAL POINT
- **$BD11**: YES
- **$BD13**: CHECK FOR EXPONENT PART
- **$BD15**: NO, END OF NUMBER
- **$BD17**: YES, START CONVERTING EXPONENT
- **$BD1A**: EXPONENT DIGIT
- **$BD1C**: NEGATIVE EXPONENT?
- **$BD1E**: YES
- **$BD20**: MIGHT NOT BE TOKENIZED YET
- **$BD22**: YES, IT IS NEGATIVE
- **$BD24**: OPTIONAL "+"
- **$BD26**: YES
- **$BD28**: MIGHT NOT BE TOKENIZED YET
- **$BD2A**: YES, FOUND "+"
- **$BD2C**: ...ALWAYS, NUMBER COMPLETED
- **$BD2E**: C=1, SET FLAG NEGATIVE
- **$BD30**: GET NEXT DIGIT OF EXPONENT
- **$BD33**: CHAR IS A DIGIT OF EXPONENT
- **$BD35**: END OF NUMBER, CHECK EXP SIGN
- **$BD37**: POSITIVE EXPONENT
- **$BD39**: NEGATIVE EXPONENT
- **$BD3B**: MAKE 2'S COMPLEMENT OF EXPONENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*