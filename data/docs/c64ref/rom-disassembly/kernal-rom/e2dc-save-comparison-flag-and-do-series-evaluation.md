---
title: save comparison flag and do series evaluation
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
- e2dc-save-comparison-flag-and-do-series-evaluation
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $E2DC
  address_end: $E2DD
  symbol: save-comparison-flag-and-do-series-evaluation
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E2DC**: save comparison flag'
---

# $E2DC — save comparison flag and do series evaluation

## Disassemblatura
```assembly
.E2DC  48       PHA   ; save comparison flag
.E2DD  4C 9D E2 JMP $E29D   ; add 0.25, ^2 then series evaluation
```


## Commenti

### Original Disassembly (—)
- **$E2DC**: save comparison flag
- **$E2DD**: add 0.25, ^2 then series evaluation

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*