---
id: b8d7-normalise-fac1
type: entity
title: normalise FAC1
aliases:
- normalise FAC1
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b8d7-normalise-fac1.md
  sha256: 39978b0dd011362d0faf4bdf676f4943ada5b43f5da892107ee9a0d2a2d4eaed
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b8d7-normalise-fac1
---

# normalise FAC1



# $B8D7 — normalise FAC1

## Disassemblatura
```assembly
.B8D7  A0 00    LDY #$00   ; clear Y
.B8D9  98       TYA   ; clear A
.B8DA  18       CLC   ; clear carry for add
.B8DB  A6 62    LDX $62   ; get FAC1 mantissa 1
.B8DD  D0 4A    BNE $B929   ; if not zero normalise FAC1
.B8DF  A6 63    LDX $63   ; get FAC1 mantissa 2
.B8E1  86 62    STX $62   ; save FAC1 mantissa 1
.B8E3  A6 64    LDX $64   ; get FAC1 mantissa 3
.B8E5  86 63    STX $63   ; save FAC1 mantissa 2
.B8E7  A6 65    LDX $65   ; get FAC1 mantissa 4
.B8E9  86 64    STX $64   ; save FAC1 mantissa 3
.B8EB  A6 70    LDX $70   ; get FAC1 rounding byte
.B8ED  86 65    STX $65   ; save FAC1 mantissa 4
.B8EF  84 70    STY $70   ; clear FAC1 rounding byte
.B8F1  69 08    ADC #$08   ; add x to exponent offset
.B8F3  C9 20    CMP #$20   ; compare with $20, max offset, all bits would be = 0
.B8F5  D0 E4    BNE $B8DB   ; loop if not max
```


## Commenti

### Original Disassembly (—)
- **$B8D7**: clear Y
- **$B8D9**: clear A
- **$B8DA**: clear carry for add
- **$B8DB**: get FAC1 mantissa 1
- **$B8DD**: if not zero normalise FAC1
- **$B8DF**: get FAC1 mantissa 2
- **$B8E1**: save FAC1 mantissa 1
- **$B8E3**: get FAC1 mantissa 3
- **$B8E5**: save FAC1 mantissa 2
- **$B8E7**: get FAC1 mantissa 4
- **$B8E9**: save FAC1 mantissa 3
- **$B8EB**: get FAC1 rounding byte
- **$B8ED**: save FAC1 mantissa 4
- **$B8EF**: clear FAC1 rounding byte
- **$B8F1**: add x to exponent offset
- **$B8F3**: compare with $20, max offset, all bits would be = 0
- **$B8F5**: loop if not max

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b8d7-normalise-fac1]]
