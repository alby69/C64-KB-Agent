---
title: orphan bytes ??
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
- e599-orphan-bytes
- e59a-set-io-defaults
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $E599
  address_end: $E59D
  symbol: orphan-bytes
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E599**: huh'
---

# $E599 — orphan bytes ??

## Disassemblatura
```assembly
.E599  EA       NOP   ; huh
.E59A  20 A0 E5 JSR $E5A0   ; initialise the vic chip
.E59D  4C 66 E5 JMP $E566   ; home the cursor and return
```


## Commenti

### Original Disassembly (—)
- **$E599**: huh
- **$E59A**: initialise the vic chip
- **$E59D**: home the cursor and return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*