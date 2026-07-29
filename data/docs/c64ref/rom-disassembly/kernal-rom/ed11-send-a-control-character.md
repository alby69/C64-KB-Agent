---
title: send a control character
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
- ed11-send-a-control-character
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $ED11
  address_end: $ED20
  symbol: send-a-control-character
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ED11**: save device address'
---

# $ED11 — send a control character

## Disassemblatura
```assembly
.ED11  48       PHA   ; save device address
.ED12  24 94    BIT $94   ; test deferred character flag
.ED14  10 0A    BPL $ED20   ; if no deferred character continue
.ED16  38       SEC   ; else flag EOI
.ED17  66 A3    ROR $A3   ; rotate into EOI flag byte
.ED19  20 40 ED JSR $ED40   ; Tx byte on serial bus
.ED1C  46 94    LSR $94   ; clear deferred character flag
.ED1E  46 A3    LSR $A3   ; clear EOI flag
.ED20  68       PLA   ; restore the device address
```


## Commenti

### Original Disassembly (—)
- **$ED11**: save device address
- **$ED12**: test deferred character flag
- **$ED14**: if no deferred character continue
- **$ED16**: else flag EOI
- **$ED17**: rotate into EOI flag byte
- **$ED19**: Tx byte on serial bus
- **$ED1C**: clear deferred character flag
- **$ED1E**: clear EOI flag
- **$ED20**: restore the device address

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*