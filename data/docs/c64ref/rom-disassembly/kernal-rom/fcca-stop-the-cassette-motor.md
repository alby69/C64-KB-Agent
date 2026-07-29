---
title: stop the cassette motor
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
- fcca-stop-cassette-motor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $FCCA
  address_end: $FCD0
  symbol: stop-the-cassette-motor
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FCCA**: read the 6510 I/O port'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FCCA — stop the cassette motor

## Disassemblatura
```assembly
.FCCA  A5 01    LDA $01   ; read the 6510 I/O port
.FCCC  09 20    ORA #$20   ; mask xxxx xx1x, turn the cassette motor off
.FCCE  85 01    STA $01   ; save the 6510 I/O port
.FCD0  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FCCA**: read the 6510 I/O port
- **$FCCC**: mask xxxx xx1x, turn the cassette motor off
- **$FCCE**: save the 6510 I/O port

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*