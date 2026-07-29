---
title: flag block done and exit interrupt
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- fbc8-irq-routine-for-cassette-write-b
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $FBC8
  address_end: $FBCB
  symbol: flag-block-done-and-exit-interrupt
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FBC8**: set carry flag'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FBC8 — flag block done and exit interrupt

## Disassemblatura
```assembly
.FBC8  38       SEC   ; set carry flag
.FBC9  66 B6    ROR $B6   ; set buffer address high byte negative, flag all sync, data and checksum bytes written
.FBCB  30 3C    BMI $FC09   ; restore registers and exit interrupt, branch always
```


## Commenti

### Original Disassembly (—)
- **$FBC8**: set carry flag
- **$FBC9**: set buffer address high byte negative, flag all sync, data and checksum bytes written
- **$FBCB**: restore registers and exit interrupt, branch always

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*