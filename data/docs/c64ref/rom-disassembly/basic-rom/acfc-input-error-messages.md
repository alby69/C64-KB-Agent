---
title: input error messages
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- acfc-messages-used-during-read
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $ACFC
  address_end: $AD1C
  symbol: input-error-messages
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ACFC**: ''?extra ignored'''
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$ACFC**: ?EXTRA IGNORED'
---

# $ACFC — input error messages

## Disassemblatura
```assembly
.ACFC  3F 45 58 54 52 41 20 49   ; '?extra ignored'
.AD04  47 4E 4F 52 45 44 0D 00
.AD0C  3F 52 45 44 4F 20 46 52   ; '?redo from start'
.AD14  4F 4D 20 53 54 41 52 54
.AD1C  0D 00
```


## Commenti

### Original Disassembly (—)
- **$ACFC**: '?extra ignored'
- **$AD0C**: '?redo from start'

### Marko Mäkelä (Marko Mäkelä)
- **$ACFC**: ?EXTRA IGNORED
- **$AD0C**: ?REDO FROM START

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*