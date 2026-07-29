---
title: set filename
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
- e257-set-filename
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $E257
  address_end: $E261
  symbol: set-filename
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E257**: evaluate expression'
---

# $E257 — set filename

## Disassemblatura
```assembly
.E257  20 9E AD JSR $AD9E   ; evaluate expression
.E25A  20 A3 B6 JSR $B6A3   ; evaluate string
.E25D  A6 22    LDX $22   ; get string pointer low byte
.E25F  A4 23    LDY $23   ; get string pointer high byte
.E261  4C BD FF JMP $FFBD   ; set the filename and return
```


## Commenti

### Original Disassembly (—)
- **$E257**: evaluate expression
- **$E25A**: evaluate string
- **$E25D**: get string pointer low byte
- **$E25F**: get string pointer high byte
- **$E261**: set the filename and return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*