---
title: send secondary address after TALK
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
- ff96-send-secondary-address-after-talk
- talk
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FF96
  address_end: $FF96
  symbol: send-secondary-address-after-talk
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF96**: send secondary address after TALK'
---

# $FF96 — send secondary address after TALK

## Disassemblatura
```assembly
.FF96  4C C7 ED JMP $EDC7   ; send secondary address after TALK
```


## Commenti

### Original Disassembly (—)
- **$FF96**: send secondary address after TALK

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*