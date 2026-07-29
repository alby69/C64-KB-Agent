---
title: scan for valid byte, not [EOL] or ":", else do syntax error then warm start
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
- e211-scan-for-valid-byte-not-eol-or-else-do-syntax-error-then-warm-start
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $E211
  address_end: $E216
  symbol: scan-for-valid-byte-not-eol-or-else-do-syntax-error-then-warm-start
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E211**: scan memory'
---

# $E211 — scan for valid byte, not [EOL] or ":", else do syntax error then warm start

## Disassemblatura
```assembly
.E211  20 79 00 JSR $0079   ; scan memory
.E214  D0 F7    BNE $E20D   ; exit if following byte
.E216  4C 08 AF JMP $AF08   ; else do syntax error then warm start
```


## Commenti

### Original Disassembly (—)
- **$E211**: scan memory
- **$E214**: exit if following byte
- **$E216**: else do syntax error then warm start

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*