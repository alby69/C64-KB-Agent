---
id: af6e-real-variable-holen
type: entity
title: REAL-Variable holen
aliases:
- REAL-Variable holen
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af6e-real-variable-holen.md
  sha256: 90623c611ad2a2314ac3728850bdaca57c838ea079d5a8bc618fb1e7e37f0879
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-af6e-real-variable-holen
---

# REAL-Variable holen



# $AF6E — REAL-Variable holen

## Disassemblatura
```assembly
.AF6E  20 14 AF JSR $AF14   ; Descriptor im Interpreter?
.AF71  90 2D    BCC $AFA0   ; nein
.AF73  E0 54    CPX #$54   ; 'T'? (von TI)
.AF75  D0 1B    BNE $AF92   ; nein: $AF92
.AF77  C0 49    CPY #$49   ; 'I'? (von TI)
.AF79  D0 25    BNE $AFA0   ; nein: $AFA0
.AF7B  20 84 AF JSR $AF84   ; TIME in FAC holen
.AF7E  98       TYA   ; Akku =0 setzen
.AF7F  A2 A0    LDX #$A0   ; Exponentbyte für FAC
.AF81  4C 4F BC JMP $BC4F   ; FAC linksbündig machen
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AF6E**: Descriptor im Interpreter?
- **$AF71**: nein
- **$AF73**: 'T'? (von TI)
- **$AF75**: nein: $AF92
- **$AF77**: 'I'? (von TI)
- **$AF79**: nein: $AFA0
- **$AF7B**: TIME in FAC holen
- **$AF7E**: Akku =0 setzen
- **$AF7F**: Exponentbyte für FAC
- **$AF81**: FAC linksbündig machen

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-af6e-real-variable-holen]]
