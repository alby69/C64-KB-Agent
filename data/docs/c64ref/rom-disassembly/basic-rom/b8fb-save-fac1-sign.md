---
title: save FAC1 sign
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
- b8fb-save-fac1-sign
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $B8FB
  address_end: $B8FD
  symbol: save-fac1-sign
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B8FB**: save FAC1 sign (b7)'
---

# $B8FB — save FAC1 sign

## Disassemblatura
```assembly
.B8FB  85 66    STA $66   ; save FAC1 sign (b7)
.B8FD  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B8FB**: save FAC1 sign (b7)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*