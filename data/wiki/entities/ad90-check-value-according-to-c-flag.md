---
id: ad90-check-value-according-to-c-flag
type: entity
title: check value according to C flag
aliases:
- check value according to C flag
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ad90-check-value-according-to-c-flag.md
  sha256: 74ec4f4052eea7203355e1e5438908f906c2a3488a27d64b52bb28b8ccb3d431
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ad90-check-value-according-to-c-flag
---

# check value according to C flag



# $AD90 — check value according to C flag

## Disassemblatura
```assembly
.AD90  24 0D    BIT $0D
.AD92  30 03    BMI $AD97
.AD94  B0 03    BCS $AD99
.AD96  60       RTS
.AD97  B0 FD    BCS $AD96
.AD99  A2 16    LDX #$16
.AD9B  4C 37 A4 JMP $A437
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AD90**: $00 IF NUMERIC, $FF IF STRING
- **$AD92**: TYPE IS STRING
- **$AD94**: NOT STRING, BUT WE NEED STRING
- **$AD96**: TYPE IS CORRECT
- **$AD97**: IS STRING AND WE WANTED STRING
- **$AD99**: TYPE MISMATCH

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ad90-check-value-according-to-c-flag]]
