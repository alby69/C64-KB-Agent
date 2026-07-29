---
title: I/O Abschluß abwarten
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f8be-io-abschlu-abwarten
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F8BE
  address_end: $F8CD
  symbol: io-abschlu-abwarten
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F8BE**: Band IRQ Vector mit normalem'
---

# $F8BE — I/O Abschluß abwarten

## Disassemblatura
```assembly
.F8BE  AD A0 02 LDA $02A0   ; Band IRQ Vector mit normalem
.F8C1  CD 15 03 CMP $0315   ; IRQ Vector vergleichen
.F8C4  18       CLC   ; Carry =0 (ok Kennzeichen)
.F8C5  F0 15    BEQ $F8DC   ; verzweige falls ja (fertig)
.F8C7  20 D0 F8 JSR $F8D0   ; Testen auf Stop-Taste
.F8CA  20 BC F6 JSR $F6BC   ; bei gedrückter Stop-Taste Flag setzen
.F8CD  4C BE F8 JMP $F8BE   ; weiter warten
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F8BE**: Band IRQ Vector mit normalem
- **$F8C1**: IRQ Vector vergleichen
- **$F8C4**: Carry =0 (ok Kennzeichen)
- **$F8C5**: verzweige falls ja (fertig)
- **$F8C7**: Testen auf Stop-Taste
- **$F8CA**: bei gedrückter Stop-Taste Flag setzen
- **$F8CD**: weiter warten

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*