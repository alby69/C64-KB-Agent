---
title: print XA as unsigned integer
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
- bdcd-in-ax-ausgeben
- bdd7-convert-fac-to-string-and-print-it
- bdda-print-string-starting-at-ya
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BDCD
  address_end: $BDDA
  symbol: print-xa-as-unsigned-integer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BDCD**: save high byte as FAC1 mantissa1'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BDCD**: für Umwandlung'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BDCD**: PRINT A,X IN DECIMAL'
---

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