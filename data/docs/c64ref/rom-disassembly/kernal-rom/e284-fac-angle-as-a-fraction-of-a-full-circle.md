---
title: (FAC) = ANGLE AS A FRACTION OF A FULL CIRCLE
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 00f3-user
- bc5b-fac
- e284-fac-angle-as-a-fraction-of-a-full-circle
- f5ed-save
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $E284
  address_end: $E2B1
  symbol: fac-angle-as-a-fraction-of-a-full-circle
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E284**: 1/4 - FRACTION MAKES'
---

# $E284 — (FAC) = ANGLE AS A FRACTION OF A FULL CIRCLE

## Disassemblatura
```assembly
.E284  A9 EA    LDA #$EA   ; 1/4 - FRACTION MAKES
.E286  A0 E2    LDY #$E2   ; -3/4 <= FRACTION < 1/4
.E288  20 50 B8 JSR $B850
.E28B  A5 66    LDA $66   ; TEST SIGN OF RESULT
.E28D  48       PHA   ; SAVE SIGN FOR LATER UNFOLDING
.E28E  10 0D    BPL $E29D   ; ALREADY 0...1/4
.E290  20 49 B8 JSR $B849   ; ADD 1/2 TO SHIFT TO -1/4...1/2
.E293  A5 66    LDA $66   ; TEST SIGN
.E295  30 09    BMI $E2A0   ; -1/4...0 0...1/2
.E297  A5 12    LDA $12   ; SIGNFLG INITIALIZED = 0 IN "TAN"
.E299  49 FF    EOR #$FF   ; FUNCTION
.E29B  85 12    STA $12   ; "TAN" IS ONLY USER OF SIGNFLG TOO IF FALL THRU, RANGE IS 0...1/2 IF BRANCH HERE, RANGE IS 0...1/4
.E29D  20 B4 BF JSR $BFB4   ; IF FALL THRU, RANGE IS -1/2...0 IF BRANCH HERE, RANGE IS -1/4...0
.E2A0  A9 EA    LDA #$EA   ; ADD 1/4 TO SHIFT RANGE
.E2A2  A0 E2    LDY #$E2   ; TO -1/4...1/4
.E2A4  20 67 B8 JSR $B867
.E2A7  68       PLA   ; GET SAVED SIGN FROM ABOVE
.E2A8  10 03    BPL $E2AD
.E2AA  20 B4 BF JSR $BFB4   ; MAKE RANGE 0...1/4
.E2AD  A9 EF    LDA #$EF   ; DO STANDARD SIN SERIES
.E2AF  A0 E2    LDY #$E2
.E2B1  4C 43 E0 JMP $E043
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E284**: 1/4 - FRACTION MAKES
- **$E286**: -3/4 <= FRACTION < 1/4
- **$E28B**: TEST SIGN OF RESULT
- **$E28D**: SAVE SIGN FOR LATER UNFOLDING
- **$E28E**: ALREADY 0...1/4
- **$E290**: ADD 1/2 TO SHIFT TO -1/4...1/2
- **$E293**: TEST SIGN
- **$E295**: -1/4...0 0...1/2
- **$E297**: SIGNFLG INITIALIZED = 0 IN "TAN"
- **$E299**: FUNCTION
- **$E29B**: "TAN" IS ONLY USER OF SIGNFLG TOO IF FALL THRU, RANGE IS 0...1/2 IF BRANCH HERE, RANGE IS 0...1/4
- **$E29D**: IF FALL THRU, RANGE IS -1/2...0 IF BRANCH HERE, RANGE IS -1/4...0
- **$E2A0**: ADD 1/4 TO SHIFT RANGE
- **$E2A2**: TO -1/4...1/4
- **$E2A7**: GET SAVED SIGN FROM ABOVE
- **$E2AA**: MAKE RANGE 0...1/4
- **$E2AD**: DO STANDARD SIN SERIES

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*