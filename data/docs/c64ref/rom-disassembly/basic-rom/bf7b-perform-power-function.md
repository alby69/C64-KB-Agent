---
title: perform power function
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
- bf7b-hoch-fac
- bfb4-vorzeichenwechsel
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BF7B
  address_end: $BFBE
  symbol: perform-power-function
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BF7B**: perform EXP()'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BF7B**: wenn FAC=0, dann zu $BFED'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BF84**: low  004E'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BF7B**: IF FAC=0, ARG^FAC=EXP(0)'
---

# $BF7B — perform power function

## Disassemblatura
```assembly
.BF7B  F0 70    BEQ $BFED   ; perform EXP()
.BF7D  A5 69    LDA $69   ; get FAC2 exponent
.BF7F  D0 03    BNE $BF84   ; branch if FAC2<>0
.BF81  4C F9 B8 JMP $B8F9   ; clear FAC1 exponent and sign and return
.BF84  A2 4E    LDX #$4E   ; set destination pointer low byte
.BF86  A0 00    LDY #$00   ; set destination pointer high byte
.BF88  20 D4 BB JSR $BBD4   ; pack FAC1 into (XY)
.BF8B  A5 6E    LDA $6E   ; get FAC2 sign (b7)
.BF8D  10 0F    BPL $BF9E   ; branch if FAC2>0 else FAC2 is -ve and can only be raised to an integer power which gives an x + j0 result
.BF8F  20 CC BC JSR $BCCC   ; perform INT()
.BF92  A9 4E    LDA #$4E   ; set source pointer low byte
.BF94  A0 00    LDY #$00   ; set source pointer high byte
.BF96  20 5B BC JSR $BC5B   ; compare FAC1 with (AY)
.BF99  D0 03    BNE $BF9E   ; branch if FAC1 <> (AY) to allow Function Call error this will leave FAC1 -ve and cause a Function Call error when LOG() is called
.BF9B  98       TYA   ; clear sign b7
.BF9C  A4 07    LDY $07   ; get FAC1 mantissa 4 from INT() function as sign in Y for possible later negation, b0 only needed
.BF9E  20 FE BB JSR $BBFE   ; save FAC1 sign and copy ABS(FAC2) to FAC1
.BFA1  98       TYA   ; copy sign back ..
.BFA2  48       PHA   ; .. and save it
.BFA3  20 EA B9 JSR $B9EA   ; perform LOG()
.BFA6  A9 4E    LDA #$4E   ; set pointer low byte
.BFA8  A0 00    LDY #$00   ; set pointer high byte
.BFAA  20 28 BA JSR $BA28   ; do convert AY, FCA1*(AY)
.BFAD  20 ED BF JSR $BFED   ; perform EXP()
.BFB0  68       PLA   ; pull sign from stack
.BFB1  4A       LSR   ; b0 is to be tested
.BFB2  90 0A    BCC $BFBE   ; if no bit then exit do - FAC1
.BFB4  A5 61    LDA $61   ; get FAC1 exponent
.BFB6  F0 06    BEQ $BFBE   ; exit if FAC1_e = $00
.BFB8  A5 66    LDA $66   ; get FAC1 sign (b7)
.BFBA  49 FF    EOR #$FF   ; complement it
.BFBC  85 66    STA $66   ; save FAC1 sign (b7)
.BFBE  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BF7B**: perform EXP()
- **$BF7D**: get FAC2 exponent
- **$BF7F**: branch if FAC2<>0
- **$BF81**: clear FAC1 exponent and sign and return
- **$BF84**: set destination pointer low byte
- **$BF86**: set destination pointer high byte
- **$BF88**: pack FAC1 into (XY)
- **$BF8B**: get FAC2 sign (b7)
- **$BF8D**: branch if FAC2>0 else FAC2 is -ve and can only be raised to an integer power which gives an x + j0 result
- **$BF8F**: perform INT()
- **$BF92**: set source pointer low byte
- **$BF94**: set source pointer high byte
- **$BF96**: compare FAC1 with (AY)
- **$BF99**: branch if FAC1 <> (AY) to allow Function Call error this will leave FAC1 -ve and cause a Function Call error when LOG() is called
- **$BF9B**: clear sign b7
- **$BF9C**: get FAC1 mantissa 4 from INT() function as sign in Y for possible later negation, b0 only needed
- **$BF9E**: save FAC1 sign and copy ABS(FAC2) to FAC1
- **$BFA1**: copy sign back ..
- **$BFA2**: .. and save it
- **$BFA3**: perform LOG()
- **$BFA6**: set pointer low byte
- **$BFA8**: set pointer high byte
- **$BFAA**: do convert AY, FCA1*(AY)
- **$BFAD**: perform EXP()
- **$BFB0**: pull sign from stack
- **$BFB1**: b0 is to be tested
- **$BFB2**: if no bit then exit do - FAC1
- **$BFB4**: get FAC1 exponent
- **$BFB6**: exit if FAC1_e = $00
- **$BFB8**: get FAC1 sign (b7)
- **$BFBA**: complement it
- **$BFBC**: save FAC1 sign (b7)

### Commodore-64-intern-Buch (Commodore)
- **$BF7B**: wenn FAC=0, dann zu $BFED
- **$BF7D**: Exponent ARG = Basis
- **$BF7F**: nicht null ?,
- **$BF81**: dann fertig
- **$BF84**: Zeiger auf
- **$BF86**: Hilfsakku
- **$BF88**: FAC nach Hilfsakku
- **$BF8B**: Exponent FAC = Potenzexponent
- **$BF8D**: kleiner eins ?,
- **$BF8F**: dann INT-Funktion
- **$BF92**: Zeiger auf
- **$BF94**: Hilfsakku
- **$BF96**: mit FAC vergleichen
- **$BF99**: Exponent nicht ganzzahlig, dann zu $BF9E
- **$BF9B**: Akku= 4
- **$BF9C**: Exponentenstelle
- **$BF9E**: ARG nach FAC
- **$BFA1**: Exponentenstelle
- **$BFA2**: in Stack
- **$BFA3**: LOG-Funktion
- **$BFA6**: Zeiger auf
- **$BFA8**: Hilfsakku
- **$BFAA**: mit FAC multiplizieren
- **$BFAD**: EXP-Funktion
- **$BFB0**: Exponent aus Stack
- **$BFB1**: wenn Exponent gradzahlig,
- **$BFB2**: dann fertig

### Marko Mäkelä (Marko Mäkelä)
- **$BF84**: low  004E
- **$BF86**: high 004E
- **$BF92**: low  004E
- **$BF94**: high 004E
- **$BFA6**: low  004E
- **$BFA8**: high 004E

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BF7B**: IF FAC=0, ARG^FAC=EXP(0)
- **$BF7D**: IF ARG=0, ARG^FAC=0
- **$BF7F**: NEITHER IS ZERO
- **$BF81**: SET FAC = 0
- **$BF84**: SAVE FAC IN TEMP3
- **$BF8B**: NORMALLY, ARG MUST BE POSITIVE
- **$BF8D**: IT IS POSITIVE, SO ALL IS WELL
- **$BF8F**: NEGATIVE, BUT OK IF INTEGRAL POWER
- **$BF92**: SEE IF INT(FAC)=FAC
- **$BF96**: IS IT AN INTEGER POWER?
- **$BF99**: NOT INTEGRAL,  WILL CAUSE ERROR LATER
- **$BF9B**: MAKE ARG SIGN + AS IT IS MOVED TO FAC
- **$BF9C**: INTEGRAL, SO ALLOW NEGATIVE ARG
- **$BF9E**: MOVE ARGUMENT TO FAC
- **$BFA1**: SAVE FLAG FOR NEGATIVE ARG (0=+)
- **$BFA3**: GET LOG(ARG)
- **$BFA6**: MULTIPLY BY POWER
- **$BFAD**: E ^ LOG(FAC)
- **$BFB0**: GET FLAG FOR NEGATIVE ARG
- **$BFB1**: <<<LSR,BCC COULD BE MERELY BPL>>>
- **$BFB2**: NOT NEGATIVE, FINISHED NEGATIVE ARG, SO NEGATE RESULT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*