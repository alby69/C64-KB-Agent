---
title: RS-232 Ausgabe
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
- chrout
- f208-rs-232-ausgabe
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F208
  address_end: $F20B
  symbol: rs-232-ausgabe
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F208**: ein Zeichen in RS-232 Puffer schreiben'
---

# $F208 — RS-232 Ausgabe

## Disassemblatura
```assembly
.F208  20 17 F0 JSR $F017   ; ein Zeichen in RS-232 Puffer schreiben
.F20B  4C FC F1 JMP $F1FC   ; CHROUT
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F208**: ein Zeichen in RS-232 Puffer schreiben
- **$F20B**: CHROUT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*