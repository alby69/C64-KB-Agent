---
title: Fehler bei GET
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
- ab5b-fehler-bei-get
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AB5B
  address_end: $AB5F
  symbol: fehler-bei-get
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AB5B**: gleiche Zeilennummer'
---

# $AB5B — Fehler bei GET

## Disassemblatura
```assembly
.AB5B  85 39    STA $39   ; gleiche Zeilennummer
.AB5D  84 3A    STY $3A   ; des Fehlers
.AB5F  4C 08 AF JMP $AF08   ; 'SYNTAX ERROR'
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AB5B**: gleiche Zeilennummer
- **$AB5D**: des Fehlers
- **$AB5F**: 'SYNTAX ERROR'

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*