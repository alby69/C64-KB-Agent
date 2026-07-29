---
title: scan and get byte, else do syntax error then warm start
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
- e200-combyt-get-next-one-byte-parameter
- e206-prft-auf-weitere-zeichen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $E200
  address_end: $E20D
  symbol: scan-and-get-byte-else-do-syntax-error-then-warm-start
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E200**: scan for ",byte", else do syntax error then warm start'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E200**: check for comma'
---

# $E200 — scan and get byte, else do syntax error then warm start

## Disassemblatura
```assembly
.E200  20 0E E2 JSR $E20E   ; scan for ",byte", else do syntax error then warm start
.E203  4C 9E B7 JMP $B79E   ; get byte parameter and return exit function if [EOT] or ":"
.E206  20 79 00 JSR $0079   ; scan memory
.E209  D0 02    BNE $E20D   ; branch if not [EOL] or ":"
.E20B  68       PLA   ; dump return address low byte
.E20C  68       PLA   ; dump return address high byte
.E20D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E200**: scan for ",byte", else do syntax error then warm start
- **$E203**: get byte parameter and return exit function if [EOT] or ":"
- **$E206**: scan memory
- **$E209**: branch if not [EOL] or ":"
- **$E20B**: dump return address low byte
- **$E20C**: dump return address high byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E200**: check for comma
- **$E203**: input one byte parameter to (X)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*