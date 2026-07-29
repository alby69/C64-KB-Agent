---
title: close input and output channels
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
- abb5-close-input-and-output-channels
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $ABB5
  address_end: $ABBE
  symbol: close-input-and-output-channels
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ABB5**: get current I/O channel'
---

# $ABB5 — close input and output channels

## Disassemblatura
```assembly
.ABB5  A5 13    LDA $13   ; get current I/O channel
.ABB7  20 CC FF JSR $FFCC   ; close input and output channels
.ABBA  A2 00    LDX #$00   ; clear X
.ABBC  86 13    STX $13   ; clear current I/O channel, flag default
.ABBE  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$ABB5**: get current I/O channel
- **$ABB7**: close input and output channels
- **$ABBA**: clear X
- **$ABBC**: clear current I/O channel, flag default

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*