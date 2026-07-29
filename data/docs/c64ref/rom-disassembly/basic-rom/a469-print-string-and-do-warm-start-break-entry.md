---
title: print string and do warm start, break entry
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
- a469-print-string-and-do-warm-start-break-entry
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $A469
  address_end: $A471
  symbol: print-string-and-do-warm-start-break-entry
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A469**: print null terminated string'
---

# $A469 — print string and do warm start, break entry

## Disassemblatura
```assembly
.A469  20 1E AB JSR $AB1E   ; print null terminated string
.A46C  A4 3A    LDY $3A   ; get current line number high byte
.A46E  C8       INY   ; increment it
.A46F  F0 03    BEQ $A474   ; branch if was in immediate mode
.A471  20 C2 BD JSR $BDC2   ; do " IN " line number message
```


## Commenti

### Original Disassembly (—)
- **$A469**: print null terminated string
- **$A46C**: get current line number high byte
- **$A46E**: increment it
- **$A46F**: branch if was in immediate mode
- **$A471**: do " IN " line number message

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*