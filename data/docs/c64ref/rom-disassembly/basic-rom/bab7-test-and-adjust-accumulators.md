---
title: test and adjust accumulators
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
- 0100-bad
- bab7-add-exponents-of-arg-and-fac
- bada-pop-return-address-and-set-fac0
- bit
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $BAB7
  address_end: $BADF
  symbol: test-and-adjust-accumulators
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BAB7**: get FAC2 exponent'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BAB9**: IF ARG=0, RESULT IS ZERO'
---

# $BAB7 — test and adjust accumulators

## Disassemblatura
```assembly
.BAB7  A5 69    LDA $69   ; get FAC2 exponent
.BAB9  F0 1F    BEQ $BADA   ; branch if FAC2 = $00 (handle underflow)
.BABB  18       CLC   ; clear carry for add
.BABC  65 61    ADC $61   ; add FAC1 exponent
.BABE  90 04    BCC $BAC4   ; branch if sum of exponents < $0100
.BAC0  30 1D    BMI $BADF   ; do overflow error
.BAC2  18       CLC   ; clear carry for the add
.BAC3  2C       .BYTE $2C   ; makes next line BIT $1410
.BAC4  10 14    BPL $BADA   ; if +ve go handle underflow
.BAC6  69 80    ADC #$80   ; adjust exponent
.BAC8  85 61    STA $61   ; save FAC1 exponent
.BACA  D0 03    BNE $BACF   ; branch if not zero
.BACC  4C FB B8 JMP $B8FB   ; save FAC1 sign and return
.BACF  A5 6F    LDA $6F   ; get sign compare (FAC1 EOR FAC2)
.BAD1  85 66    STA $66   ; save FAC1 sign (b7)
.BAD3  60       RTS   ; handle overflow and underflow
.BAD4  A5 66    LDA $66   ; get FAC1 sign (b7)
.BAD6  49 FF    EOR #$FF   ; complement it
.BAD8  30 05    BMI $BADF   ; do overflow error handle underflow
.BADA  68       PLA   ; pop return address low byte
.BADB  68       PLA   ; pop return address high byte
.BADC  4C F7 B8 JMP $B8F7   ; clear FAC1 exponent and sign and return
.BADF  4C 7E B9 JMP $B97E   ; do overflow error then warm start
```


## Commenti

### Original Disassembly (—)
- **$BAB7**: get FAC2 exponent
- **$BAB9**: branch if FAC2 = $00 (handle underflow)
- **$BABB**: clear carry for add
- **$BABC**: add FAC1 exponent
- **$BABE**: branch if sum of exponents < $0100
- **$BAC0**: do overflow error
- **$BAC2**: clear carry for the add
- **$BAC3**: makes next line BIT $1410
- **$BAC4**: if +ve go handle underflow
- **$BAC6**: adjust exponent
- **$BAC8**: save FAC1 exponent
- **$BACA**: branch if not zero
- **$BACC**: save FAC1 sign and return
- **$BACF**: get sign compare (FAC1 EOR FAC2)
- **$BAD1**: save FAC1 sign (b7)
- **$BAD3**: handle overflow and underflow
- **$BAD4**: get FAC1 sign (b7)
- **$BAD6**: complement it
- **$BAD8**: do overflow error handle underflow
- **$BADA**: pop return address low byte
- **$BADB**: pop return address high byte
- **$BADC**: clear FAC1 exponent and sign and return
- **$BADF**: do overflow error then warm start

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BAB9**: IF ARG=0, RESULT IS ZERO
- **$BABE**: IN RANGE
- **$BAC0**: OVERFLOW
- **$BAC3**: TRICK TO SKIP
- **$BAC4**: OVERFLOW
- **$BAC6**: RE-BIAS
- **$BAC8**: RESULT
- **$BACC**: RESULT IS ZERO <<< CRAZY TO JUMP WAY BACK THERE! >>> <<< SAME IDENTICAL CODE IS BELOW! >>> <<< INSTEAD OF BNE .2, JMP STA.IN.FAC.SIGN   >>> <<< ONLY NEEDED BEQ .3            >>>
- **$BACF**: SET SIGN OF RESULT
- **$BAD3**: IF (FAC) IS POSITIVE, GIVE "OVERFLOW" ERROR IF (FAC) IS NEGATIVE, SET FAC=0, POP ONE RETURN, AND RTS CALLED FROM "EXP" FUNCTION
- **$BAD8**: ERROR IF POSITIVE #

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*