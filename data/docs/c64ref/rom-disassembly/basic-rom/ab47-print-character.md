---
title: print character
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
- ab47-print-character
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $AB47
  address_end: $AB4C
  symbol: print-character
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AB47**: output character to channel with error check'
---

# $AB47 — print character

## Disassemblatura
```assembly
.AB47  20 0C E1 JSR $E10C   ; output character to channel with error check
.AB4A  29 FF    AND #$FF   ; set the flags on A
.AB4C  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$AB47**: output character to channel with error check
- **$AB4A**: set the flags on A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*