---
title: FLOAT UNSIGNED VALUE IN FAC+1,2
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
- 0068-bits
- bc49-float-unsigned-value-in-fac12
- bc5b-fac
- clear
- store
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BC49
  address_end: $BC55
  symbol: float-unsigned-value-in-fac12
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC49**: CLEAR LOWER 16-BITS OF MANTISSA'
---

# $BC49 — FLOAT UNSIGNED VALUE IN FAC+1,2

## Disassemblatura
```assembly
.BC49  A9 00    LDA #$00   ; CLEAR LOWER 16-BITS OF MANTISSA
.BC4B  85 65    STA $65
.BC4D  85 64    STA $64
.BC4F  86 61    STX $61   ; STORE EXPONENT
.BC51  85 70    STA $70   ; CLEAR EXTENSION
.BC53  85 66    STA $66   ; MAKE SIGN POSITIVE
.BC55  4C D2 B8 JMP $B8D2   ; IF C=0, WILL NEGATE FAC
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC49**: CLEAR LOWER 16-BITS OF MANTISSA
- **$BC4F**: STORE EXPONENT
- **$BC51**: CLEAR EXTENSION
- **$BC53**: MAKE SIGN POSITIVE
- **$BC55**: IF C=0, WILL NEGATE FAC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*