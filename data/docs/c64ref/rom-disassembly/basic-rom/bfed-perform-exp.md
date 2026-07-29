---
title: perform EXP()
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
- bfed-basic-funktion-exp
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BFED
  address_end: $BFFD
  symbol: perform-exp
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BFED**: set 1.443 pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BFED**: Zeiger auf'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BFED**: CONVERT TO POWER OF TWO PROBLEM'
---

# $BFED — perform EXP()

## Disassemblatura
```assembly
.BFED  A9 BF    LDA #$BF   ; set 1.443 pointer low byte
.BFEF  A0 BF    LDY #$BF   ; set 1.443 pointer high byte
.BFF1  20 28 BA JSR $BA28   ; do convert AY, FCA1*(AY)
.BFF4  A5 70    LDA $70   ; get FAC1 rounding byte
.BFF6  69 50    ADC #$50   ; +$50/$100
.BFF8  90 03    BCC $BFFD   ; skip rounding if no carry
.BFFA  20 23 BC JSR $BC23   ; round FAC1 (no check)
.BFFD  4C 00 E0 JMP $E000   ; continue EXP()
```


## Commenti

### Original Disassembly (—)
- **$BFED**: set 1.443 pointer low byte
- **$BFEF**: set 1.443 pointer high byte
- **$BFF1**: do convert AY, FCA1*(AY)
- **$BFF4**: get FAC1 rounding byte
- **$BFF6**: +$50/$100
- **$BFF8**: skip rounding if no carry
- **$BFFA**: round FAC1 (no check)
- **$BFFD**: continue EXP()

### Commodore-64-intern-Buch (Commodore)
- **$BFED**: Zeiger auf
- **$BFEF**: Konstante 1/LOG(2)
- **$BFF1**: mit FAC multiplizieren
- **$BFF4**: 80 zu Rundungsstelle
- **$BFF6**: addieren
- **$BFF8**: wenn kleiner als $FF, dann zu $BFFD
- **$BFFA**: Mantisse von FAC um eins erhöhen
- **$BFFD**: weiter bei $E000
- **$E000**: Rundungsstelle
- **$E002**: FAC nach ARG bringen
- **$E005**: Exponent
- **$E007**: Zahl größer 128 ?,
- **$E009**: dann zu $E00E
- **$E00B**: falls positiv 'OVERFLOW'
- **$E00E**: INTEGER-Funktion
- **$E011**: ganze Zahl
- **$E013**: Zahl
- **$E014**: gleich
- **$E016**: 127 ?, dann zu $E00B
- **$E018**: ansonsten
- **$E019**: subtrahieren
- **$E01B**: und in Stack
- **$E01C**: FAC
- **$E01E**: und
- **$E020**: ARG
- **$E022**: ver-
- **$E024**: tauschen
- **$E026**: Zähler erniedrigen
- **$E027**: schon alle Zeichen?
- **$E029**: Rundungs-
- **$E02B**: stelle
- **$E02D**: ARG - FAC
- **$E030**: Vorzeichenwechsel
- **$E033**: Zeiger auf
- **$E035**: Polynomkoeffizienten
- **$E037**: Polynom berechnen
- **$E03A**: Vergleichsbyte
- **$E03C**: löschen
- **$E03E**: Zahl aus Stack
- **$E03F**: Exponenten von FAC und ARG addieren
- **$E042**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BFED**: CONVERT TO POWER OF TWO PROBLEM
- **$BFEF**: E^X = 2^(LOG2(E)*X)
- **$BFF4**: NON-STANDARD ROUNDING HERE
- **$BFF6**: ROUND UP IF EXTENSION > $AF
- **$BFF8**: NO, DON'T ROUND UP
- **$E000**: STRANGE VALUE
- **$E002**: COPY FAC INTO ARG
- **$E005**: MAXIMUM EXPONENT IS < 128
- **$E007**: WITHIN RANGE?
- **$E009**: YES
- **$E00B**: OVERFLOW IF +, RETURN 0.0 IF -
- **$E00E**: GET INT(FAC)
- **$E011**: THIS IS THE INETGRAL PART OF THE POWER
- **$E013**: ADD TO EXPONENT BIAS + 1
- **$E016**: OVERFLOW
- **$E018**: BACK OFF TO NORMAL BIAS
- **$E01B**: SAVE EXPONENT
- **$E01C**: SWAP ARG AND FAC
- **$E01E**: <<< WHY SWAP? IT IS DOING      >>>
- **$E020**: <<< -(A-B) WHEN (B-A) IS THE   >>>
- **$E022**: <<< SAME THING!                >>>
- **$E02D**: POWER-INT(POWER) --> FRACTIONAL PART
- **$E037**: COMPUTE F(X) ON FRACTIONAL PART
- **$E03E**: GET EXPONENT
- **$E042**: <<< WASTED BYTE HERE, COULD HAVE >>> <<< JUST USED "JMP ADD.EXPO..."  >>>

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*