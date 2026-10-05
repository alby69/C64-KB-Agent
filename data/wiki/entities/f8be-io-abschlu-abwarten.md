---
id: f8be-io-abschlu-abwarten
type: entity
title: I/O Abschluß abwarten
aliases:
- I/O Abschluß abwarten
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f8be-io-abschlu-abwarten.md
  sha256: d9b6f636892d56722ba48989eb51425d50379d2ea2dbbaddb691497abc738037
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f8be-io-abschlu-abwarten
---

# I/O Abschluß abwarten



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

## References
- Source: [[src-f8be-io-abschlu-abwarten]]
