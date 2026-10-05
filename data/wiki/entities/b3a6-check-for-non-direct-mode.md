---
id: b3a6-check-for-non-direct-mode
type: entity
title: check for non-direct mode
aliases:
- check for non-direct mode
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b3a6-check-for-non-direct-mode.md
  sha256: 557e9572778ea8f5ef85f9ff5c42c2caaaaaea209a5ae5404a6f7960b2f39a6c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b3a6-check-for-non-direct-mode
---

# check for non-direct mode



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

## References
- Source: [[src-b3a6-check-for-non-direct-mode]]
