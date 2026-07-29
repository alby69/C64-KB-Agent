---
title: Fehler bei READ
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
- 00d7-data
- ab57-fehler-bei-read
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AB57
  address_end: $AB59
  symbol: fehler-bei-read
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AB57**: DATA-Zeilennummer'
---

# $AB57 — Fehler bei READ

## Disassemblatura
```assembly
.AB57  A5 3F    LDA $3F   ; DATA-Zeilennummer
.AB59  A4 40    LDY $40   ; holen (LOW- und HIGH-Byte)
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AB57**: DATA-Zeilennummer
- **$AB59**: holen (LOW- und HIGH-Byte)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*