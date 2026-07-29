---
title: check string area
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  address: $B5C7
  address_end: $B605
  symbol: check-string-area
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B5C7 — check string area

## Disassemblatura
```assembly
.B5C7  B1 22    LDA ($22),Y
.B5C9  F0 2B    BEQ $B5F6
.B5CB  C8       INY
.B5CC  B1 22    LDA ($22),Y
.B5CE  AA       TAX
.B5CF  C8       INY
.B5D0  B1 22    LDA ($22),Y
.B5D2  C5 34    CMP $34
.B5D4  90 06    BCC $B5DC
.B5D6  D0 1E    BNE $B5F6
.B5D8  E4 33    CPX $33
.B5DA  B0 1A    BCS $B5F6
.B5DC  C5 60    CMP $60
.B5DE  90 16    BCC $B5F6
.B5E0  D0 04    BNE $B5E6
.B5E2  E4 5F    CPX $5F
.B5E4  90 10    BCC $B5F6
.B5E6  86 5F    STX $5F
.B5E8  85 60    STA $60
.B5EA  A5 22    LDA $22
.B5EC  A6 23    LDX $23
.B5EE  85 4E    STA $4E
.B5F0  86 4F    STX $4F
.B5F2  A5 53    LDA $53
.B5F4  85 55    STA $55
.B5F6  A5 53    LDA $53
.B5F8  18       CLC
.B5F9  65 22    ADC $22
.B5FB  85 22    STA $22
.B5FD  90 02    BCC $B601
.B5FF  E6 23    INC $23
.B601  A6 23    LDX $23
.B603  A0 00    LDY #$00
.B605  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*