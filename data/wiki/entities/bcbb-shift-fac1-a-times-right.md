---
id: bcbb-shift-fac1-a-times-right
type: entity
title: shift FAC1 A times right
aliases:
- shift FAC1 A times right
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bcbb-shift-fac1-a-times-right.md
  sha256: dc392e1d13a323949ddcd1657418f5d5ba0e01528a419952aa4b143f37e8eae2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bcbb-shift-fac1-a-times-right
---

# shift FAC1 A times right



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

## References
- Source: [[src-bcbb-shift-fac1-a-times-right]]
