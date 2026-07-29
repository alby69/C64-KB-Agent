---
title: convert FAC1 floating to fixed
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
- bc9b-integer
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BC9B
  address_end: $BCBA
  symbol: convert-fac1-floating-to-fixed
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC9B**: get FAC1 exponent'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BC9B**: Exponent'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC9B**: LOOK AT FAC EXPONENT'
---

# $BC9B — convert FAC1 floating to fixed

## Disassemblatura
```assembly
.BC9B  A5 61    LDA $61   ; get FAC1 exponent
.BC9D  F0 4A    BEQ $BCE9   ; if zero go clear FAC1 and return
.BC9F  38       SEC   ; set carry for subtract
.BCA0  E9 A0    SBC #$A0   ; subtract maximum integer range exponent
.BCA2  24 66    BIT $66   ; test FAC1 sign (b7)
.BCA4  10 09    BPL $BCAF   ; branch if FAC1 +ve FAC1 was -ve
.BCA6  AA       TAX   ; copy subtracted exponent
.BCA7  A9 FF    LDA #$FF   ; overflow for -ve number
.BCA9  85 68    STA $68   ; set FAC1 overflow byte
.BCAB  20 4D B9 JSR $B94D   ; twos complement FAC1 mantissa
.BCAE  8A       TXA   ; restore subtracted exponent
.BCAF  A2 61    LDX #$61   ; set index to FAC1
.BCB1  C9 F9    CMP #$F9   ; compare exponent result
.BCB3  10 06    BPL $BCBB   ; if < 8 shifts shift FAC1 A times right and return
.BCB5  20 99 B9 JSR $B999   ; shift FAC1 A times right (> 8 shifts)
.BCB8  84 68    STY $68   ; clear FAC1 overflow byte
.BCBA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BC9B**: get FAC1 exponent
- **$BC9D**: if zero go clear FAC1 and return
- **$BC9F**: set carry for subtract
- **$BCA0**: subtract maximum integer range exponent
- **$BCA2**: test FAC1 sign (b7)
- **$BCA4**: branch if FAC1 +ve FAC1 was -ve
- **$BCA6**: copy subtracted exponent
- **$BCA7**: overflow for -ve number
- **$BCA9**: set FAC1 overflow byte
- **$BCAB**: twos complement FAC1 mantissa
- **$BCAE**: restore subtracted exponent
- **$BCAF**: set index to FAC1
- **$BCB1**: compare exponent result
- **$BCB3**: if < 8 shifts shift FAC1 A times right and return
- **$BCB5**: shift FAC1 A times right (> 8 shifts)
- **$BCB8**: clear FAC1 overflow byte

### Commodore-64-intern-Buch (Commodore)
- **$BC9B**: Exponent
- **$BC9D**: null ?
- **$BC9F**: Integer-
- **$BCA0**: Exponent
- **$BCA2**: wenn FAC positiv,
- **$BCA4**: dann zu $BCAF
- **$BCA6**: FAC
- **$BCA7**: Rundungsbyte
- **$BCA9**: setzen
- **$BCAB**: Mantisse von FAC invertieren
- **$BCAE**: Exponent in Akku
- **$BCAF**: FAC-Offset-Zeiger
- **$BCB1**: wenn Exponent größer als
- **$BCB3**: -8, dann zu BCBB
- **$BCB5**: FAC rechtsverschieben
- **$BCB8**: FAC-Rundungsbyte löschen
- **$BCBA**: Rücksprung
- **$BCBB**: Akku löschen
- **$BCBC**: FAC-Vorzeichen laden
- **$BCBE**: das
- **$BCC0**: FAC-
- **$BCC2**: Vorzeichen
- **$BCC4**: isolieren
- **$BCC6**: FAC bitweise nach rechts verschieben
- **$BCC9**: FAC-Rundungsbyte löschen
- **$BCCB**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC9B**: LOOK AT FAC EXPONENT
- **$BC9D**: FAC=0, SO FINISHED
- **$BC9F**: GET -(NUMBER OF FRACTIONAL BITS)
- **$BCA0**: IN A-REG FOR SHIFT COUNT
- **$BCA2**: CHECK SIGN OF FAC
- **$BCA4**: POSITIVE, CONTINUE
- **$BCA6**: NEGATIVE, SO COMPLEMENT MANTISSA
- **$BCA7**: AND SET SIGN EXTENSION FOR SHIFT
- **$BCAE**: RESTORE BIT COUNT TO A-REG
- **$BCAF**: POINT SHIFT SUBROUTINE AT FAC
- **$BCB1**: MORE THAN 7 BITS TO SHIFT?
- **$BCB3**: NO, SHORT SHIFT
- **$BCB5**: YES, USE GENERAL ROUTINE
- **$BCB8**: Y=0, CLEAR SIGN EXTENSION
- **$BCBB**: SAVE SHIFT COUNT
- **$BCBC**: GET SIGN BIT
- **$BCC0**: START RIGHT SHIFT
- **$BCC2**: AND MERGE WITH SIGN
- **$BCC6**: JUMP INTO MIDDLE OF SHIFTER
- **$BCC9**: Y=0, CLEAR SIGN EXTENSION

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*