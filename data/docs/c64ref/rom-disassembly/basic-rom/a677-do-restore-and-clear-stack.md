---
title: do RESTORE and clear stack
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
- a677-do-restore-and-clear-stack
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $A677
  address_end: $A677
  symbol: do-restore-and-clear-stack
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A677**: perform RESTORE'
---

# $A677 — do RESTORE and clear stack

## Disassemblatura
```assembly
.A677  20 1D A8 JSR $A81D   ; perform RESTORE
```


## Commenti

### Original Disassembly (—)
- **$A677**: perform RESTORE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*