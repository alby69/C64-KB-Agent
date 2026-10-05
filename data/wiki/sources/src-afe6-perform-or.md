---
id: src-afe6-perform-or
type: source
title: 'Source Summary: perform OR'
aliases:
- perform OR
- afe6-perform-or.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/afe6-perform-or.md
  sha256: 7e642ce7edebd1dccbc2a9c1a9e050d7f4a2eeef9e9f9f64ccf1cf2ddb888607
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform OR

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/afe6-perform-or.md`
**SHA256**: `7e642ce7edebd1dccbc2a9c1a9e050d7f4a2eeef9e9f9f64ccf1cf2ddb888607`

## Summary



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
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
