---
title: set DSR signal not present
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bit
- ef2e-no-dsr-cts-error
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $EF2E
  address_end: $EF30
  symbol: set-dsr-signal-not-present
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF2E**: set DSR signal not present'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EF2E**: entrypoint for ''NO DSR'''
---

# $EF2E — set DSR signal not present

## Disassemblatura
```assembly
.EF2E  A9 40    LDA #$40   ; set DSR signal not present
.EF30  2C       .BYTE $2C   ; makes next line BIT $10A9
```


## Commenti

### Original Disassembly (—)
- **$EF2E**: set DSR signal not present
- **$EF30**: makes next line BIT $10A9

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EF2E**: entrypoint for 'NO DSR'
- **$EF30**: mask next LDA-command
- **$EF31**: entrypoint for 'NO CTS'
- **$EF33**: RSSTAT, 6551 status register image

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*