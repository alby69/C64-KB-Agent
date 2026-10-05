---
id: bdcd-print-xa-as-unsigned-integer
type: entity
title: print XA as unsigned integer
aliases:
- print XA as unsigned integer
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bdcd-print-xa-as-unsigned-integer.md
  sha256: d246bd0bf212a9fb4a547d1360cb6614ebd893c1ff71c07c5e2b4f5c94566930
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bdcd-print-xa-as-unsigned-integer
---

# print XA as unsigned integer



# $BDCD — print XA as unsigned integer

## Disassemblatura
```assembly
.BDCD  85 62    STA $62   ; save high byte as FAC1 mantissa1
.BDCF  86 63    STX $63   ; save low byte as FAC1 mantissa2
.BDD1  A2 90    LDX #$90   ; set exponent to 16d bits
.BDD3  38       SEC   ; set integer is +ve flag
.BDD4  20 49 BC JSR $BC49   ; set exponent = X, clear mantissa 4 and 3 and normalise FAC1
.BDD7  20 DF BD JSR $BDDF   ; convert FAC1 to string
.BDDA  4C 1E AB JMP $AB1E   ; print null terminated string
```


## Commenti

### Original Disassembly (—)
- **$BDCD**: save high byte as FAC1 mantissa1
- **$BDCF**: save low byte as FAC1 mantissa2
- **$BDD1**: set exponent to 16d bits
- **$BDD3**: set integer is +ve flag
- **$BDD4**: set exponent = X, clear mantissa 4 and 3 and normalise FAC1
- **$BDD7**: convert FAC1 to string
- **$BDDA**: print null terminated string

### Commodore-64-intern-Buch (Commodore)
- **$BDCD**: für Umwandlung
- **$BDCF**: in FAC schreiben
- **$BDD1**: Exponent
- **$BDD3**: = 16
- **$BDD4**: Integer nach Fließkomma wandeln
- **$BDD7**: FAC nach ASCII wandeln
- **$BDDA**: String ausgeben

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BDCD**: PRINT A,X IN DECIMAL
- **$BDD1**: EXPONENT = 2^16
- **$BDD3**: CONVERT UNSIGNED
- **$BDD4**: CONVERT LINE # TO FP

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bdcd-print-xa-as-unsigned-integer]]
