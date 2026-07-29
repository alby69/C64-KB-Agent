---
title: check for non-direct mode
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $B3A6
  address_end: $B3B0
  symbol: check-for-non-direct-mode
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B3A6**: Flag laden (Direktm. = $FF)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B3AB**: error number'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B3A6**: =$FF IF DIRECT MODE'
---

# $B3A6 — check for non-direct mode

## Disassemblatura
```assembly
.B3A6  A6 3A    LDX $3A
.B3A8  E8       INX
.B3A9  D0 A0    BNE $B34B
.B3AB  A2 15    LDX #$15   ; error number
.B3AD  2C       .BYTE $2C
.B3AE  A2 1B    LDX #$1B   ; error number
.B3B0  4C 37 A4 JMP $A437
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B3A6**: Flag laden (Direktm. = $FF)
- **$B3A8**: testen
- **$B3A9**: nein: dann RTS
- **$B3AB**: Nummer für 'illegal direct'
- **$B3AE**: Nummer für 'undef'd function'
- **$B3B0**: Fehlermeldung ausgeben

### Marko Mäkelä (Marko Mäkelä)
- **$B3AB**: error number
- **$B3AE**: error number

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B3A6**: =$FF IF DIRECT MODE
- **$B3A8**: MAKES $FF INTO ZERO
- **$B3A9**: RETURN IF RUNNING MODE
- **$B3AB**: DIRECT MODE, GIVE ERROR
- **$B3AD**: TRICK TO SKIP NEXT 2 BYTES
- **$B3AE**: UNDEFINDED FUNCTION ERROR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*