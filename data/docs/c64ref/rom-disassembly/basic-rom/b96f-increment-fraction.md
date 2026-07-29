---
title: increment fraction
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
- b97e-do-overflow-error-then-warm-start
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  address: $B96F
  address_end: $B980
  symbol: increment-fraction
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B97E**: error number'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B96F**: ADD CARRY FROM EXTRA'
---

# $B96F — increment fraction

## Disassemblatura
```assembly
.B96F  E6 65    INC $65
.B971  D0 0A    BNE $B97D
.B973  E6 64    INC $64
.B975  D0 06    BNE $B97D
.B977  E6 63    INC $63
.B979  D0 02    BNE $B97D
.B97B  E6 62    INC $62
.B97D  60       RTS
.B97E  A2 0F    LDX #$0F   ; error number
.B980  4C 37 A4 JMP $A437
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$B97E**: error number

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B96F**: ADD CARRY FROM EXTRA

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*