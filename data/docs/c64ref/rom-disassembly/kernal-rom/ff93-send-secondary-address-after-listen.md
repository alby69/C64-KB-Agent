---
title: send secondary address after LISTEN
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
- ff93-send-secondary-address-after-listen
- listen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF93
  address_end: $FF93
  symbol: send-secondary-address-after-listen
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF93**: send secondary address after LISTEN'
---

# $FF93 — send secondary address after LISTEN

## Disassemblatura
```assembly
.FF93  4C B9 ED JMP $EDB9   ; send secondary address after LISTEN
```


## Commenti

### Original Disassembly (—)
- **$FF93**: send secondary address after LISTEN

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*