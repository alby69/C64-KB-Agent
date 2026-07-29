---
title: variable found
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
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
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  address: $B185
  address_end: $B193
  symbol: variable-found
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B185**: LOWTR POINTS AT NAME OF VARIABLE,'
---

# $B185 — variable found

## Disassemblatura
```assembly
.B185  A5 5F    LDA $5F
.B187  18       CLC
.B188  69 02    ADC #$02
.B18A  A4 60    LDY $60
.B18C  90 01    BCC $B18F
.B18E  C8       INY
.B18F  85 47    STA $47
.B191  84 48    STY $48
.B193  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B185**: LOWTR POINTS AT NAME OF VARIABLE,
- **$B187**: SO ADD 2 TO GET TO VALUE
- **$B18F**: ADDRESS IN VARPNT AND Y,A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*