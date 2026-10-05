---
id: src-f279-set-serial-bus-output-device
type: source
title: 'Source Summary: set serial bus output device'
aliases:
- set serial bus output device
- f279-set-serial-bus-output-device.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f279-set-serial-bus-output-device.md
  sha256: 6b6e5a207110f629f7eccac810a5e9f5e1badbb620849ebd7131e0510128dbad
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set serial bus output device

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f279-set-serial-bus-output-device.md`
**SHA256**: `6b6e5a207110f629f7eccac810a5e9f5e1badbb620849ebd7131e0510128dbad`

## Summary



# $F279 — set serial bus output device

## Disassemblatura
```assembly
.F279  AA       TAX
.F27A  20 0C ED JSR $ED0C
.F27D  A5 B9    LDA $B9
.F27F  10 05    BPL $F286
.F281  20 BE ED JSR $EDBE
.F284  D0 03    BNE $F289
.F286  20 B9 ED JSR $EDB9
.F289  8A       TXA
.F28A  24 90    BIT $90
.F28C  10 E7    BPL $F275
.F28E  4C 07 F7 JMP $F707
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F279**: Geräteadresse retten
- **$F27A**: LISTEN senden
- **$F27D**: Sekundäradresse laden
-...
