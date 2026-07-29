---
title: perform INT()
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
- bccc-basic-funktion-int
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BCCC
  address_end: $BCE6
  symbol: perform-int
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BCCC**: get FAC1 exponent'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BCCC**: Exponent'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BCCC**: CHECK IF EXPONENT < 32'
---

# $BCCC — perform INT()

## Disassemblatura
```assembly
.BCCC  A5 61    LDA $61   ; get FAC1 exponent
.BCCE  C9 A0    CMP #$A0   ; compare with max int
.BCD0  B0 20    BCS $BCF2   ; exit if >= (already int, too big for fractional part!)
.BCD2  20 9B BC JSR $BC9B   ; convert FAC1 floating to fixed
.BCD5  84 70    STY $70   ; save FAC1 rounding byte
.BCD7  A5 66    LDA $66   ; get FAC1 sign (b7)
.BCD9  84 66    STY $66   ; save FAC1 sign (b7)
.BCDB  49 80    EOR #$80   ; toggle FAC1 sign
.BCDD  2A       ROL   ; shift into carry
.BCDE  A9 A0    LDA #$A0   ; set new exponent
.BCE0  85 61    STA $61   ; save FAC1 exponent
.BCE2  A5 65    LDA $65   ; get FAC1 mantissa 4
.BCE4  85 07    STA $07   ; save FAC1 mantissa 4 for power function
.BCE6  4C D2 B8 JMP $B8D2   ; do ABS and normalise FAC1
```


## Commenti

### Original Disassembly (—)
- **$BCCC**: get FAC1 exponent
- **$BCCE**: compare with max int
- **$BCD0**: exit if >= (already int, too big for fractional part!)
- **$BCD2**: convert FAC1 floating to fixed
- **$BCD5**: save FAC1 rounding byte
- **$BCD7**: get FAC1 sign (b7)
- **$BCD9**: save FAC1 sign (b7)
- **$BCDB**: toggle FAC1 sign
- **$BCDD**: shift into carry
- **$BCDE**: set new exponent
- **$BCE0**: save FAC1 exponent
- **$BCE2**: get FAC1 mantissa 4
- **$BCE4**: save FAC1 mantissa 4 for power function
- **$BCE6**: do ABS and normalise FAC1

### Commodore-64-intern-Buch (Commodore)
- **$BCCC**: Exponent
- **$BCCE**: ganze Zahl ?
- **$BCD0**: ja, dann fertig
- **$BCD2**: FAC nach Integer wandeln
- **$BCD5**: Rundungsstelle löschen
- **$BCD7**: Vorzeichen in Akku
- **$BCD9**: und positiv machen
- **$BCDB**: Bei
- **$BCDD**: negativen Vorzeichen
- **$BCDE**: das
- **$BCE0**: Carry-
- **$BCE2**: flag
- **$BCE4**: löschen
- **$BCE6**: FAC linksbündig machen
- **$BCE9**: Mantisse
- **$BCEB**: mit
- **$BCED**: Nullen
- **$BCEF**: füllen
- **$BCF1**: Y-Reg löschen
- **$BCF2**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BCCC**: CHECK IF EXPONENT < 32
- **$BCCE**: BECAUSE IF > 31 THERE IS NO FRACTION
- **$BCD0**: NO FRACTION, WE ARE FINISHED
- **$BCD2**: USE GENERAL INTEGER CONVERSION
- **$BCD5**: Y=0, CLEAR EXTENSION
- **$BCD7**: GET SIGN OF VALUE
- **$BCD9**: Y=0, CLEAR SIGN
- **$BCDB**: TOGGLE ACTUAL SIGN
- **$BCDD**: AND SAVE IN CARRY
- **$BCDE**: SET EXPONENT TO 32
- **$BCE0**: BECAUSE 4-BYTE INTEGER NOW
- **$BCE2**: SAVE LOW 8-BITS OF INTEGER FORM
- **$BCE4**: FOR EXP AND POWER
- **$BCE6**: NORMALIZE TO FINISH CONVERSION
- **$BCE9**: FAC=0, SO CLEAR ALL 4 BYTES FOR
- **$BCEB**: INTEGER VERSION
- **$BCF1**: Y=0 TOO

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*