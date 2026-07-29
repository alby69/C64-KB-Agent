---
title: return X,Y organization of screen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ffed-return-xy-organization-of-screen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFED
  address_end: $FFED
  symbol: return-xy-organization-of-screen
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFED**: return X,Y organization of screen'
---

# $FFED — return X,Y organization of screen

## Disassemblatura
```assembly
.FFED  4C 05 E5 JMP $E505   ; return X,Y organization of screen
```


## Commenti

### Original Disassembly (—)
- **$FFED**: return X,Y organization of screen

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*