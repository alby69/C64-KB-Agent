---
title: user function default vector
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
- fe66-warm-start-basic
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $FE66
  address_end: $FE6F
  symbol: user-function-default-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE66**: restore default I/O vectors'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE66**: KERNAL reset'
---

# $FE66 — user function default vector

## Disassemblatura
```assembly
.FE66  20 15 FD JSR $FD15   ; restore default I/O vectors
.FE69  20 A3 FD JSR $FDA3   ; initialise SID, CIA and IRQ
.FE6C  20 18 E5 JSR $E518   ; initialise the screen and keyboard
.FE6F  6C 02 A0 JMP ($A002)   ; do BASIC break entry
```


## Commenti

### Original Disassembly (—)
- **$FE66**: restore default I/O vectors
- **$FE69**: initialise SID, CIA and IRQ
- **$FE6C**: initialise the screen and keyboard
- **$FE6F**: do BASIC break entry

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE66**: KERNAL reset
- **$FE69**: init I/O
- **$FE6C**: init I/O
- **$FE6F**: jump to Basic warm start vector

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*