---
id: src-fd9b-tape-irq-vectors
type: source
title: 'Source Summary: tape IRQ vectors'
aliases:
- tape IRQ vectors
- fd9b-tape-irq-vectors.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd9b-tape-irq-vectors.md
  sha256: dd69001d1edabe15d9c7008fbd62fff1b5cbb5fd146cdffe02462d12599df012
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: tape IRQ vectors

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fd9b-tape-irq-vectors.md`
**SHA256**: `dd69001d1edabe15d9c7008fbd62fff1b5cbb5fd146cdffe02462d12599df012`

## Summary



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
-...
