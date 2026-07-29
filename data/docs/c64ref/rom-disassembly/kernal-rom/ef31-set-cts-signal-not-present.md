---
title: set CTS signal not present
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
- ef31-set-cts-signal-not-present
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $EF31
  address_end: $EF36
  symbol: set-cts-signal-not-present
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF31**: set CTS signal not present'
---

# $EF31 — set CTS signal not present

## Disassemblatura
```assembly
.EF31  A9 10    LDA #$10   ; set CTS signal not present
.EF33  0D 97 02 ORA $0297   ; OR it with the RS232 status register
.EF36  8D 97 02 STA $0297   ; save the RS232 status register
```


## Commenti

### Original Disassembly (—)
- **$EF31**: set CTS signal not present
- **$EF33**: OR it with the RS232 status register
- **$EF36**: save the RS232 status register

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*