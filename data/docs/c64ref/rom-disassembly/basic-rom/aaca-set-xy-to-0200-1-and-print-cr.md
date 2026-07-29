---
title: set XY to $0200 - 1 and print [CR]
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
- 0200-buf
- aaca-end-statement-in-buffer-and-screen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $AACA
  address_end: $AAD5
  symbol: set-xy-to-0200-1-and-print-cr
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AACA**: clear A'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $AACA — set XY to $0200 - 1 and print [CR]

## Disassemblatura
```assembly
.AACA  A9 00    LDA #$00   ; clear A
.AACC  9D 00 02 STA $0200,X   ; clear first byte of input buffer
.AACF  A2 FF    LDX #$FF   ; $0200 - 1 low byte
.AAD1  A0 01    LDY #$01   ; $0200 - 1 high byte
.AAD3  A5 13    LDA $13   ; get current I/O channel
.AAD5  D0 10    BNE $AAE7   ; exit if not default channel
```


## Commenti

### Original Disassembly (—)
- **$AACA**: clear A
- **$AACC**: clear first byte of input buffer
- **$AACF**: $0200 - 1 low byte
- **$AAD1**: $0200 - 1 high byte
- **$AAD3**: get current I/O channel
- **$AAD5**: exit if not default channel

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*