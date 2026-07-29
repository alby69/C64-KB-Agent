---
title: print file name
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
- f5c1-print-filename
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $F5C1
  address_end: $F5D1
  symbol: print-file-name
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F5C1**: get file name length'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F5C1**: FNLEN, length of current filename'
---

# $F5C1 — print file name

## Disassemblatura
```assembly
.F5C1  A4 B7    LDY $B7   ; get file name length
.F5C3  F0 0C    BEQ $F5D1   ; exit if null file name
.F5C5  A0 00    LDY #$00   ; clear index
.F5C7  B1 BB    LDA ($BB),Y   ; get file name byte
.F5C9  20 D2 FF JSR $FFD2   ; output character to channel
.F5CC  C8       INY   ; increment index
.F5CD  C4 B7    CPY $B7   ; compare with file name length
.F5CF  D0 F6    BNE $F5C7   ; loop if more to do
.F5D1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F5C1**: get file name length
- **$F5C3**: exit if null file name
- **$F5C5**: clear index
- **$F5C7**: get file name byte
- **$F5C9**: output character to channel
- **$F5CC**: increment index
- **$F5CD**: compare with file name length
- **$F5CF**: loop if more to do

### Magnus Nyman (Magnus Nyman)
- **$F5C1**: FNLEN, length of current filename
- **$F5C3**: exit
- **$F5C7**: get character in filename
- **$F5C9**: output
- **$F5CC**: next character
- **$F5CD**: ready?
- **$F5D1**: back

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*