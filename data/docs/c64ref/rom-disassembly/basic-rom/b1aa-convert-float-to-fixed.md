---
title: convert float to fixed
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
- b1aa-umwandlung-fac-nach-integer
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B1AA
  address_end: $B1B1
  symbol: convert-float-to-fixed
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B1AA**: evaluate integer expression, no sign check'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B1AA**: FAC nach Integer wandeln'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B1AA — convert float to fixed

## Disassemblatura
```assembly
.B1AA  20 BF B1 JSR $B1BF   ; evaluate integer expression, no sign check
.B1AD  A5 64    LDA $64   ; get result low byte
.B1AF  A4 65    LDY $65   ; get result high byte
.B1B1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B1AA**: evaluate integer expression, no sign check
- **$B1AD**: get result low byte
- **$B1AF**: get result high byte

### Commodore-64-intern-Buch (Commodore)
- **$B1AA**: FAC nach Integer wandeln
- **$B1AD**: LOW-Byte
- **$B1AF**: HIGH-Byte
- **$B1B1**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*