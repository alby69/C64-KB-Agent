---
title: push sign, round FAC1 and put on stack
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
- ae38-push-sign-round-fac1-and-put-on-stack
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $AE38
  address_end: $AE42
  symbol: push-sign-round-fac1-and-put-on-stack
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AE38**: copy sign'
---

# $AE38 — push sign, round FAC1 and put on stack

## Disassemblatura
```assembly
.AE38  A8       TAY   ; copy sign
.AE39  68       PLA   ; get return address low byte
.AE3A  85 22    STA $22   ; save it
.AE3C  E6 22    INC $22   ; increment it as return-1 is pushed note, no check is made on the high byte so if the calling routine ever assembles to a page edge then this all goes horribly wrong!
.AE3E  68       PLA   ; get return address high byte
.AE3F  85 23    STA $23   ; save it
.AE41  98       TYA   ; restore sign
.AE42  48       PHA   ; push sign
```


## Commenti

### Original Disassembly (—)
- **$AE38**: copy sign
- **$AE39**: get return address low byte
- **$AE3A**: save it
- **$AE3C**: increment it as return-1 is pushed note, no check is made on the high byte so if the calling routine ever assembles to a page edge then this all goes horribly wrong!
- **$AE3E**: get return address high byte
- **$AE3F**: save it
- **$AE41**: restore sign
- **$AE42**: push sign

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*