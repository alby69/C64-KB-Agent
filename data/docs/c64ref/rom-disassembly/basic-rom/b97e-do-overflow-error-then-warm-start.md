---
title: do overflow error then warm start
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b97e-do-overflow-error-then-warm-start
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $B97E
  address_end: $B980
  symbol: do-overflow-error-then-warm-start
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B97E**: error $0F, overflow error'
---

# $B97E — do overflow error then warm start

## Disassemblatura
```assembly
.B97E  A2 0F    LDX #$0F   ; error $0F, overflow error
.B980  4C 37 A4 JMP $A437   ; do error #X then warm start
```


## Commenti

### Original Disassembly (—)
- **$B97E**: error $0F, overflow error
- **$B980**: do error #X then warm start

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*