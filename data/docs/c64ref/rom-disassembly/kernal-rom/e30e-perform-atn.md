---
title: perform ATN()
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e30e-basic-funktion-atn
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  - marko_mäkelä.txt
  - bob_sander-cederlof.txt
  - magnus_nyman.txt
  address: $E30E
  address_end: $E33D
  symbol: perform-atn
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E30E**: get FAC1 sign (b7)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E30E**: Vorzeichen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E31D**: low  B9BC'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E30E**: FOLD THE ARGUMENT RANGE FIRST'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: Nessun commento disponibile.
---

# $E30E — perform ATN()

## Disassemblatura
```assembly
.E30E  A5 66    LDA $66   ; get FAC1 sign (b7)
.E310  48       PHA   ; save sign
.E311  10 03    BPL $E316   ; branch if +ve
.E313  20 B4 BF JSR $BFB4   ; else do - FAC1
.E316  A5 61    LDA $61   ; get FAC1 exponent
.E318  48       PHA   ; push exponent
.E319  C9 81    CMP #$81   ; compare with 1
.E31B  90 07    BCC $E324   ; branch if FAC1 < 1
.E31D  A9 BC    LDA #$BC   ; pointer to 1 low byte
.E31F  A0 B9    LDY #$B9   ; pointer to 1 high byte
.E321  20 0F BB JSR $BB0F   ; convert AY and do (AY)/FAC1
.E324  A9 3E    LDA #$3E   ; pointer to series low byte
.E326  A0 E3    LDY #$E3   ; pointer to series high byte
.E328  20 43 E0 JSR $E043   ; ^2 then series evaluation
.E32B  68       PLA   ; restore old FAC1 exponent
.E32C  C9 81    CMP #$81   ; compare with 1
.E32E  90 07    BCC $E337   ; branch if FAC1 < 1
.E330  A9 E0    LDA #$E0   ; pointer to (pi/2) low byte
.E332  A0 E2    LDY #$E2   ; pointer to (pi/2) low byte
.E334  20 50 B8 JSR $B850   ; perform subtraction, FAC1 from (AY)
.E337  68       PLA   ; restore FAC1 sign
.E338  10 03    BPL $E33D   ; exit if was +ve
.E33A  4C B4 BF JMP $BFB4   ; else do - FAC1 and return
.E33D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E30E**: get FAC1 sign (b7)
- **$E310**: save sign
- **$E311**: branch if +ve
- **$E313**: else do - FAC1
- **$E316**: get FAC1 exponent
- **$E318**: push exponent
- **$E319**: compare with 1
- **$E31B**: branch if FAC1 < 1
- **$E31D**: pointer to 1 low byte
- **$E31F**: pointer to 1 high byte
- **$E321**: convert AY and do (AY)/FAC1
- **$E324**: pointer to series low byte
- **$E326**: pointer to series high byte
- **$E328**: ^2 then series evaluation
- **$E32B**: restore old FAC1 exponent
- **$E32C**: compare with 1
- **$E32E**: branch if FAC1 < 1
- **$E330**: pointer to (pi/2) low byte
- **$E332**: pointer to (pi/2) low byte
- **$E334**: perform subtraction, FAC1 from (AY)
- **$E337**: restore FAC1 sign
- **$E338**: exit if was +ve
- **$E33A**: else do - FAC1 and return

### Commodore-64-intern-Buch (Commodore)
- **$E30E**: Vorzeichen
- **$E310**: retten
- **$E311**: positiv ?
- **$E313**: Vorzeichen vertauschen
- **$E316**: Exponent
- **$E318**: retten
- **$E319**: Zahl mit 1 vergleichen
- **$E31B**: kleiner ?
- **$E31D**: Zeiger auf
- **$E31F**: Konstante 1
- **$E321**: 1 durch FAC dividieren (Kehrwert)
- **$E324**: Zeiger auf
- **$E326**: Polynomkoeffizienten
- **$E328**: Polynom berechnen
- **$E32B**: Exponent zurückholen
- **$E32C**: war Zahl
- **$E32E**: kleiner 1, dann zu $E337
- **$E330**: Zeiger auf
- **$E332**: Konstante Pi/2
- **$E334**: Pi/2 minus FAC
- **$E337**: Vorzeichen holen
- **$E338**: positiv ?
- **$E33A**: Vorzeichen wechseln
- **$E33D**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E31D**: low  B9BC
- **$E31F**: high B9BC
- **$E324**: low  E33E
- **$E326**: high E33E
- **$E330**: low  E2E0
- **$E332**: high E2E0

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E30E**: FOLD THE ARGUMENT RANGE FIRST
- **$E310**: SAVE SIGN FOR LATER UNFOLDING
- **$E311**: .GE. 0
- **$E313**: .LT. 0, SO COMPLEMENT
- **$E316**: IF .GE. 1, FORM RECIPROCAL
- **$E318**: SAVE FOR LATER UNFOLDING
- **$E319**: (EXPONENT FOR .GE. 1
- **$E31B**: X < 1
- **$E31D**: FORM 1/X
- **$E321**: 0 <= X <= 1 0 <= ATN(X) <= PI/8
- **$E324**: COMPUTE POLYNOMIAL APPROXIMATION
- **$E32B**: START TO UNFOLD
- **$E32C**: WAS IT .GE. 1?
- **$E32E**: NO
- **$E330**: YES, SUBTRACT FROM PI/2
- **$E337**: WAS IT NEGATIVE?
- **$E338**: NO
- **$E33A**: YES, COMPLEMENT
- **$E33E**: POWER OF POLYNOMIAL

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*