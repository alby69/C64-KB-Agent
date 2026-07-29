---
title: make string space A bytes long
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
- b47d-allocate-area-according-to-a
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $B47D
  address_end: $B486
  symbol: make-string-space-a-bytes-long
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B47D**: make space in string memory for string A long'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B47D — make string space A bytes long

## Disassemblatura
```assembly
.B47D  20 F4 B4 JSR $B4F4   ; make space in string memory for string A long
.B480  86 62    STX $62   ; save string pointer low byte
.B482  84 63    STY $63   ; save string pointer high byte
.B484  85 61    STA $61   ; save length
.B486  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B47D**: make space in string memory for string A long
- **$B480**: save string pointer low byte
- **$B482**: save string pointer high byte
- **$B484**: save length

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*