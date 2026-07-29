---
title: return the base address of the I/O devices
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
- fff3-return-the-base-address-of-the-io-devices
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $FFF3
  address_end: $FFF3
  symbol: return-the-base-address-of-the-io-devices
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FFF3**: return the base address of the I/O devices'
---

# $FFF3 — return the base address of the I/O devices

## Disassemblatura
```assembly
.FFF3  4C 00 E5 JMP $E500   ; return the base address of the I/O devices
```


## Commenti

### Original Disassembly (—)
- **$FFF3**: return the base address of the I/O devices

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*