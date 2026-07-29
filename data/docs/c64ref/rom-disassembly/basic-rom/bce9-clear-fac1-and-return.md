---
title: clear FAC1 and return
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
- bce9-clear-float-accu
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $BCE9
  address_end: $BCF2
  symbol: clear-fac1-and-return
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BCE9**: clear FAC1 mantissa 1'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $BCE9 — clear FAC1 and return

## Disassemblatura
```assembly
.BCE9  85 62    STA $62   ; clear FAC1 mantissa 1
.BCEB  85 63    STA $63   ; clear FAC1 mantissa 2
.BCED  85 64    STA $64   ; clear FAC1 mantissa 3
.BCEF  85 65    STA $65   ; clear FAC1 mantissa 4
.BCF1  A8       TAY   ; clear Y
.BCF2  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BCE9**: clear FAC1 mantissa 1
- **$BCEB**: clear FAC1 mantissa 2
- **$BCED**: clear FAC1 mantissa 3
- **$BCEF**: clear FAC1 mantissa 4
- **$BCF1**: clear Y

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*