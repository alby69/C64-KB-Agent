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
- afa0-real-variable-holen
- bc5b-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AFA0
  address_end: $AFA4
  symbol: real-variable-holen
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AFA0**: LOW- und HIGH-Byte der'
---

# $AFA0 — REAL-Variable holen

## Disassemblatura
```assembly
.AFA0  A5 64    LDA $64   ; LOW- und HIGH-Byte der
.AFA2  A4 65    LDY $65   ; Variablenadresse
.AFA4  4C A2 BB JMP $BBA2   ; Variable in FAC holen
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AFA0**: LOW- und HIGH-Byte der
- **$AFA2**: Variablenadresse
- **$AFA4**: Variable in FAC holen

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*