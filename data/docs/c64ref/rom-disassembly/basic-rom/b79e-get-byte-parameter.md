---
title: get byte parameter
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
- b79e-convert-it-to-single-byte-in-x-reg
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $B79E
  address_end: $B79E
  symbol: get-byte-parameter
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B79E**: evaluate expression and check is numeric, else do type
      mismatch'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B79E — get byte parameter

## Disassemblatura
```assembly
.B79E  20 8A AD JSR $AD8A   ; evaluate expression and check is numeric, else do type mismatch
```


## Commenti

### Original Disassembly (—)
- **$B79E**: evaluate expression and check is numeric, else do type mismatch

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*