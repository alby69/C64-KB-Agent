---
title: continue of get value of variable
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
- af92-continue-of-get-value-of-variable
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $AF92
  address_end: $AFA4
  symbol: continue-of-get-value-of-variable
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AF92**: S'
---

# $AF92 — continue of get value of variable

## Disassemblatura
```assembly
.AF92  E0 53    CPX #$53   ; S
.AF94  D0 0A    BNE $AFA0
.AF96  C0 54    CPY #$54   ; T
.AF98  D0 06    BNE $AFA0
.AF9A  20 B7 FF JSR $FFB7
.AF9D  4C 3C BC JMP $BC3C
.AFA0  A5 64    LDA $64
.AFA2  A4 65    LDY $65
.AFA4  4C A2 BB JMP $BBA2
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$AF92**: S
- **$AF96**: T

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*