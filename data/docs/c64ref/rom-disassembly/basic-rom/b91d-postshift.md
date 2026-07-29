---
title: postshift
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
  address: $B91D
  address_end: $B946
  symbol: postshift
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B91D**: COUNT BITS SHIFTED'
---

# $B91D — postshift

## Disassemblatura
```assembly
.B91D  69 01    ADC #$01
.B91F  06 70    ASL $70
.B921  26 65    ROL $65
.B923  26 64    ROL $64
.B925  26 63    ROL $63
.B927  26 62    ROL $62
.B929  10 F2    BPL $B91D
.B92B  38       SEC
.B92C  E5 61    SBC $61
.B92E  B0 C7    BCS $B8F7
.B930  49 FF    EOR #$FF
.B932  69 01    ADC #$01
.B934  85 61    STA $61
.B936  90 0E    BCC $B946
.B938  E6 61    INC $61
.B93A  F0 42    BEQ $B97E
.B93C  66 62    ROR $62
.B93E  66 63    ROR $63
.B940  66 64    ROR $64
.B942  66 65    ROR $65
.B944  66 70    ROR $70
.B946  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B91D**: COUNT BITS SHIFTED
- **$B929**: UNTIL TOP BIT = 1
- **$B92C**: ADJUST EXPONENT BY BITS SHIFTED
- **$B92E**: UNDERFLOW, RETURN ZERO
- **$B932**: 2'S COMPLEMENT
- **$B934**: CARRY=0 NOW
- **$B936**: UNLESS MANTISSA CARRIED
- **$B938**: MANTISSA CARRIED, SO SHIFT RIGHT
- **$B93A**: OVERFLOW IF EXPONENT TOO BIG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*