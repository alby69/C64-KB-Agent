---
id: fd9b-tape-irq-vectors
type: entity
title: tape IRQ vectors
aliases:
- tape IRQ vectors
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd9b-tape-irq-vectors.md
  sha256: dd69001d1edabe15d9c7008fbd62fff1b5cbb5fd146cdffe02462d12599df012
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fd9b-tape-irq-vectors
---

# tape IRQ vectors



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

## References
- Source: [[src-fd9b-tape-irq-vectors]]
