---
title: scan for ",valid byte", else do syntax error then warm start
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
- e20e-cmmerr-check-for-comma
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $E20E
  address_end: $E20E
  symbol: scan-for-valid-byte-else-do-syntax-error-then-warm-start
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E20E**: scan for ",", else do syntax error then warm start'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E20E**: confirm comma'
---

# $E20E — scan for ",valid byte", else do syntax error then warm start

## Disassemblatura
```assembly
.E20E  20 FD AE JSR $AEFD   ; scan for ",", else do syntax error then warm start
```


## Commenti

### Original Disassembly (—)
- **$E20E**: scan for ",", else do syntax error then warm start

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E20E**: confirm comma
- **$E211**: get CHRGOT
- **$E214**: else than null
- **$E216**: execute SYNTAX error

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*