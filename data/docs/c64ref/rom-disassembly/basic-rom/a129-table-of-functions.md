---
title: table of functions
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a129-table-of-functions
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $A129
  address_end: $A197
  symbol: table-of-functions
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A129**: tab('
---

# $A129 — table of functions

## Disassemblatura
```assembly
.A129  54 41 42 A8   ; tab(
.A12D  54 CF   ; to
.A12F  46 CE   ; fn
.A131  53 50 43 A8   ; spc(
.A135  54 48 45 CE   ; then
.A139  4E 4F D4   ; not
.A13C  53 54 45 D0   ; step
.A140  AB   ; plus
.A141  AD   ; minus
.A142  AA   ; multiply
.A143  AF   ; divide
.A144  DE   ; power
.A145  41 4E C4   ; and
.A148  4F D2   ; on
.A14A  BE   ; greater
.A14B  BD   ; equal
.A14C  BC   ; less
.A14D  53 47 CE   ; sgn
.A150  49 4E D4   ; int
.A153  41 42 D3   ; abs
.A156  55 53 D2   ; usr
.A159  46 52 C5   ; fre
.A15C  50 4F D3   ; pos
.A15F  53 51 D2   ; sqr
.A162  52 4E C4   ; rnd
.A165  4C 4F C7   ; log
.A168  45 58 D0   ; exp
.A16B  43 4F D3   ; cos
.A16E  53 49 CE   ; sin
.A171  54 41 CE   ; tan
.A174  41 54 CE   ; atn
.A177  50 45 45 CB   ; peek
.A17B  4C 45 CE   ; len
.A17E  53 54 52 A4   ; str$
.A182  56 41 CC   ; val
.A185  41 53 C3   ; asc
.A188  43 48 52 A4   ; chr$
.A18C  4C 45 46 54 A4   ; left$
.A191  52 49 47 48 54 A4   ; right$
.A197  4D 49 44 A4   ; mid$
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$A129**: tab(
- **$A12D**: to
- **$A12F**: fn
- **$A131**: spc(
- **$A135**: then
- **$A139**: not
- **$A13C**: step
- **$A140**: plus
- **$A141**: minus
- **$A142**: multiply
- **$A143**: divide
- **$A144**: power
- **$A145**: and
- **$A148**: on
- **$A14A**: greater
- **$A14B**: equal
- **$A14C**: less
- **$A14D**: sgn
- **$A150**: int
- **$A153**: abs
- **$A156**: usr
- **$A159**: fre
- **$A15C**: pos
- **$A15F**: sqr
- **$A162**: rnd
- **$A165**: log
- **$A168**: exp
- **$A16B**: cos
- **$A16E**: sin
- **$A171**: tan
- **$A174**: atn
- **$A177**: peek
- **$A17B**: len
- **$A17E**: str$
- **$A182**: val
- **$A185**: asc
- **$A188**: chr$
- **$A18C**: left$
- **$A191**: right$
- **$A197**: mid$

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*