---
title: perform OR
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
- 00a0-time
- afe6-basic-befehl-or
- bit
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AFE6
  address_end: $AFE8
  symbol: perform-or
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AFE6**: set Y for OR'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AFE6**: Flag für OR'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $AFE6 — perform OR

## Disassemblatura
```assembly
.AFE6  A0 FF    LDY #$FF   ; set Y for OR
.AFE8  2C       .BYTE $2C   ; makes next line BIT $00A0
```


## Commenti

### Original Disassembly (—)
- **$AFE6**: set Y for OR
- **$AFE8**: makes next line BIT $00A0

### Commodore-64-intern-Buch (Commodore)
- **$AFE6**: Flag für OR

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*