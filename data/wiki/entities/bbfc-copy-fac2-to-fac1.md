---
id: bbfc-copy-fac2-to-fac1
type: entity
title: copy FAC2 to FAC1
aliases:
- copy FAC2 to FAC1
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bbfc-copy-fac2-to-fac1.md
  sha256: b092c40aa1f8cc1fbc692db5f77a367a9514e74f87e828da4af50a2be3fb3966
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bbfc-copy-fac2-to-fac1
---

# copy FAC2 to FAC1



# $BBFC — copy FAC2 to FAC1

## Disassemblatura
```assembly
.BBFC  A5 6E    LDA $6E   ; get FAC2 sign (b7) save FAC1 sign and copy ABS(FAC2) to FAC1
.BBFE  85 66    STA $66   ; save FAC1 sign (b7)
.BC00  A2 05    LDX #$05   ; 5 bytes to copy
.BC02  B5 68    LDA $68,X   ; get byte from FAC2,X
.BC04  95 60    STA $60,X   ; save byte at FAC1,X
.BC06  CA       DEX   ; decrement count
.BC07  D0 F9    BNE $BC02   ; loop if not all done
.BC09  86 70    STX $70   ; clear FAC1 rounding byte
.BC0B  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BBFC**: get FAC2 sign (b7) save FAC1 sign and copy ABS(FAC2) to FAC1
- **$BBFE**: save FAC1 sign (b7)
- **$BC00**: 5 bytes to copy
- **$BC02**: get byte from FAC2,X
- **$BC04**: save byte at FAC1,X
- **$BC06**: decrement count
- **$BC07**: loop if not all done
- **$BC09**: clear FAC1 rounding byte

### Commodore-64-intern-Buch (Commodore)
- **$BBFC**: ARG-Vorzeichen
- **$BBFE**: in FAC-Reg übertragen
- **$BC00**: 5 Bytes
- **$BC02**: ARG in
- **$BC04**: FAC
- **$BC06**: übertragen
- **$BC07**: schon alle Zeichen ?
- **$BC09**: FAC-Rundungsstelle löschen
- **$BC0B**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BBFC**: COPY SIGN
- **$BC00**: MOVE 5 BYTES
- **$BC09**: ZERO EXTENSION

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bbfc-copy-fac2-to-fac1]]
