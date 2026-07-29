---
title: divisors for decimal conversion
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
  - commodore-64-intern-buch.txt
  address: $BF16
  address_end: $BF36
  symbol: divisors-for-decimal-conversion
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BF16**: -100 000 000'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BF16**: -100000000'
---

# $BF16 — divisors for decimal conversion

## Disassemblatura
```assembly
.BF16  FA 0A 1F 00
.BF1A  00 98 96 80
.BF1E  FF F0 BD C0
.BF22  00 01 86 A0
.BF26  FF FF D8 F0
.BF2A  00 00 03 E8
.BF2E  FF FF FF 9C
.BF32  00 00 00 0A
.BF36  FF FF FF FF
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$BF16**: -100 000 000
- **$BF1A**: 10 000 000
- **$BF1E**: -1 000 000
- **$BF22**: 100 000
- **$BF26**: -10 000
- **$BF2A**: 1 000
- **$BF2E**: - 100
- **$BF32**: 10
- **$BF36**: -1

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BF16**: -100000000
- **$BF1A**: 10000000
- **$BF1E**: -1000000
- **$BF22**: 100000
- **$BF26**: -10000
- **$BF2A**: 1000
- **$BF2E**: -100
- **$BF32**: 10
- **$BF36**: -1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*