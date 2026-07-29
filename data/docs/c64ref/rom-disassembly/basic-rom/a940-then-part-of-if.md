---
title: THEN part of IF
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $A940
  address_end: $A948
  symbol: then-part-of-if
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A945**: do GOTO'
---

# $A940 — THEN part of IF

## Disassemblatura
```assembly
.A940  20 79 00 JSR $0079
.A943  B0 03    BCS $A948
.A945  4C A0 A8 JMP $A8A0   ; do GOTO
.A948  4C ED A7 JMP $A7ED
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$A945**: do GOTO

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*