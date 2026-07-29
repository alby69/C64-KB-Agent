---
title: tape IRQ vectors
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
- fd9b-irq-vektoren
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FD9B
  address_end: $FDA1
  symbol: tape-irq-vectors
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FD9B**: $08 write tape leader IRQ routine'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FD9B**: $FC6A, $FBCD, $EA31, $F92C'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FD9B**: cassette write A'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FD9B**: $fc6a - tape write'
---

# $FD9B — tape IRQ vectors

## Disassemblatura
```assembly
.FD9B  6A FC   ; $08 write tape leader IRQ routine
.FD9D  CD FB   ; $0A tape write IRQ routine
.FD9F  31 EA   ; $0C normal IRQ vector
.FDA1  2C F9   ; $0E read tape bits IRQ routine
```


## Commenti

### Original Disassembly (—)
- **$FD9B**: $08 write tape leader IRQ routine
- **$FD9D**: $0A tape write IRQ routine
- **$FD9F**: $0C normal IRQ vector
- **$FDA1**: $0E read tape bits IRQ routine

### Commodore-64-intern-Buch (Commodore)
- **$FD9B**: $FC6A, $FBCD, $EA31, $F92C

### Marko Mäkelä (Marko Mäkelä)
- **$FD9B**: cassette write A
- **$FD9D**: cassette write B
- **$FD9F**: standard IRQ
- **$FDA1**: cassette read

### Magnus Nyman (Magnus Nyman)
- **$FD9B**: $fc6a - tape write
- **$FD9D**: $fbcd - tape write II
- **$FD9F**: $ea31 - normal IRQ
- **$FDA1**: $f92c - tape read

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*