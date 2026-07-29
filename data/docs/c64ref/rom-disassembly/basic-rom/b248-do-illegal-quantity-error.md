---
title: do illegal quantity error
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
- b248-error-illegal-quantity
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $B248
  address_end: $B24A
  symbol: do-illegal-quantity-error
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B248**: error $0E, illegal quantity error'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B248 — do illegal quantity error

## Disassemblatura
```assembly
.B248  A2 0E    LDX #$0E   ; error $0E, illegal quantity error
.B24A  4C 37 A4 JMP $A437   ; do error #X then warm start
```


## Commenti

### Original Disassembly (—)
- **$B248**: error $0E, illegal quantity error
- **$B24A**: do error #X then warm start

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*