---
title: add (AY) to FAC1
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b867-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B867
  address_end: $B867
  symbol: add-ay-to-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B867**: unpack memory (AY) into FAC2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B867**: Konstante (A/Y) nach ARG'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B867 — add (AY) to FAC1

## Disassemblatura
```assembly
.B867  20 8C BA JSR $BA8C   ; unpack memory (AY) into FAC2
```


## Commenti

### Original Disassembly (—)
- **$B867**: unpack memory (AY) into FAC2

### Commodore-64-intern-Buch (Commodore)
- **$B867**: Konstante (A/Y) nach ARG

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*