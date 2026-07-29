---
title: constants
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bf11-05
- bf16-nach-ascii
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $BF11
  address_end: $BF36
  symbol: constants
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BF11**: 0.5, first two bytes'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $BF11 — constants

## Disassemblatura
```assembly
.BF11  80 00   ; 0.5, first two bytes
.BF13  00 00 00   ; null return for undefined variables
.BF16  FA 0A 1F 00   ; -100 000 000
.BF1A  00 98 96 80   ; +10 000 000
.BF1E  FF F0 BD C0   ; -1 000 000
.BF22  00 01 86 A0   ; +100 000
.BF26  FF FF D8 F0   ; -10 000
.BF2A  00 00 03 E8   ; +1 000
.BF2E  FF FF FF 9C   ; - 100
.BF32  00 00 00 0A   ; +10
.BF36  FF FF FF FF   ; -1
```


## Commenti

### Original Disassembly (—)
- **$BF11**: 0.5, first two bytes
- **$BF13**: null return for undefined variables
- **$BF16**: -100 000 000
- **$BF1A**: +10 000 000
- **$BF1E**: -1 000 000
- **$BF22**: +100 000
- **$BF26**: -10 000
- **$BF2A**: +1 000
- **$BF2E**: - 100
- **$BF32**: +10
- **$BF36**: -1

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*