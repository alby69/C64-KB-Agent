---
title: round FAC1 and put on stack
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
- ae43-round-fac1-and-put-on-stack
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $AE43
  address_end: $AE55
  symbol: round-fac1-and-put-on-stack
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AE43**: round FAC1'
---

# $AE43 — round FAC1 and put on stack

## Disassemblatura
```assembly
.AE43  20 1B BC JSR $BC1B   ; round FAC1
.AE46  A5 65    LDA $65   ; get FAC1 mantissa 4
.AE48  48       PHA   ; save it
.AE49  A5 64    LDA $64   ; get FAC1 mantissa 3
.AE4B  48       PHA   ; save it
.AE4C  A5 63    LDA $63   ; get FAC1 mantissa 2
.AE4E  48       PHA   ; save it
.AE4F  A5 62    LDA $62   ; get FAC1 mantissa 1
.AE51  48       PHA   ; save it
.AE52  A5 61    LDA $61   ; get FAC1 exponent
.AE54  48       PHA   ; save it
.AE55  6C 22 00 JMP ($0022)   ; return, sort of
```


## Commenti

### Original Disassembly (—)
- **$AE43**: round FAC1
- **$AE46**: get FAC1 mantissa 4
- **$AE48**: save it
- **$AE49**: get FAC1 mantissa 3
- **$AE4B**: save it
- **$AE4C**: get FAC1 mantissa 2
- **$AE4E**: save it
- **$AE4F**: get FAC1 mantissa 1
- **$AE51**: save it
- **$AE52**: get FAC1 exponent
- **$AE54**: save it
- **$AE55**: return, sort of

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*