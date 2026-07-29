---
title: REAL-Variable holen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 00a0-time
- af6e-real-variable-holen
- af92-continue-of-get-value-of-variable
- afa0-real-variable-holen
- bc5b-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AF6E
  address_end: $AF81
  symbol: real-variable-holen
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AF6E**: Descriptor im Interpreter?'
---

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