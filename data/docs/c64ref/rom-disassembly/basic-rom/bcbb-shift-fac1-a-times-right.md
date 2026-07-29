---
title: shift FAC1 A times right
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
- bcbb-shift-fac1-a-times-right
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $BCBB
  address_end: $BCCB
  symbol: shift-fac1-a-times-right
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BCBB**: copy shift count'
---

# $BCBB — shift FAC1 A times right

## Disassemblatura
```assembly
.BCBB  A8       TAY   ; copy shift count
.BCBC  A5 66    LDA $66   ; get FAC1 sign (b7)
.BCBE  29 80    AND #$80   ; mask sign bit only (x000 0000)
.BCC0  46 62    LSR $62   ; shift FAC1 mantissa 1
.BCC2  05 62    ORA $62   ; OR sign in b7 FAC1 mantissa 1
.BCC4  85 62    STA $62   ; save FAC1 mantissa 1
.BCC6  20 B0 B9 JSR $B9B0   ; shift FAC1 Y times right
.BCC9  84 68    STY $68   ; clear FAC1 overflow byte
.BCCB  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BCBB**: copy shift count
- **$BCBC**: get FAC1 sign (b7)
- **$BCBE**: mask sign bit only (x000 0000)
- **$BCC0**: shift FAC1 mantissa 1
- **$BCC2**: OR sign in b7 FAC1 mantissa 1
- **$BCC4**: save FAC1 mantissa 1
- **$BCC6**: shift FAC1 Y times right
- **$BCC9**: clear FAC1 overflow byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*