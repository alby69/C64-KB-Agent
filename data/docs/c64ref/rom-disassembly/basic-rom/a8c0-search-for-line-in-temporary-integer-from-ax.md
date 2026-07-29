---
title: 'search for line # in temporary integer from (AX)'
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
- a8c0-search-for-line-in-temporary-integer-from-ax
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $A8C0
  address_end: $A8D1
  symbol: search-for-line-in-temporary-integer-from-ax
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A8C0**: search Basic for temp integer line number from AX'
---

# $A8C0 — search for line # in temporary integer from (AX)

## Disassemblatura
```assembly
.A8C0  20 17 A6 JSR $A617   ; search Basic for temp integer line number from AX
.A8C3  90 1E    BCC $A8E3   ; if carry clear go do unsdefined statement error carry all ready set for subtract
.A8C5  A5 5F    LDA $5F   ; get pointer low byte
.A8C7  E9 01    SBC #$01   ; -1
.A8C9  85 7A    STA $7A   ; save BASIC execute pointer low byte
.A8CB  A5 60    LDA $60   ; get pointer high byte
.A8CD  E9 00    SBC #$00   ; subtract carry
.A8CF  85 7B    STA $7B   ; save BASIC execute pointer high byte
.A8D1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A8C0**: search Basic for temp integer line number from AX
- **$A8C3**: if carry clear go do unsdefined statement error carry all ready set for subtract
- **$A8C5**: get pointer low byte
- **$A8C7**: -1
- **$A8C9**: save BASIC execute pointer low byte
- **$A8CB**: get pointer high byte
- **$A8CD**: subtract carry
- **$A8CF**: save BASIC execute pointer high byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*