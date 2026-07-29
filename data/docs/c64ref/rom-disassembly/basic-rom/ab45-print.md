---
title: print "?"
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
- ab45-print
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $AB45
  address_end: $AB45
  symbol: print
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AB45**: set "?"'
---

# $AB45 — print "?"

## Disassemblatura
```assembly
.AB45  A9 3F    LDA #$3F   ; set "?"
```


## Commenti

### Original Disassembly (—)
- **$AB45**: set "?"

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*