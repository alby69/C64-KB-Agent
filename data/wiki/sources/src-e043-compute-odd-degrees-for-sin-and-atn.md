---
id: src-e043-compute-odd-degrees-for-sin-and-atn
type: source
title: 'Source Summary: compute odd degrees for SIN and ATN'
aliases:
- compute odd degrees for SIN and ATN
- e043-compute-odd-degrees-for-sin-and-atn.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e043-compute-odd-degrees-for-sin-and-atn.md
  sha256: ecd499d22f6ead937b447c6f02d2377dbd1e539536935dff0d7761ada796a2a2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: compute odd degrees for SIN and ATN

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e043-compute-odd-degrees-for-sin-and-atn.md`
**SHA256**: `ecd499d22f6ead937b447c6f02d2377dbd1e539536935dff0d7761ada796a2a2`

## Summary



# $E043 — compute odd degrees for SIN and ATN

## Disassemblatura
```assembly
.E043  85 71    STA $71
.E045  84 72    STY $72
.E047  20 CA BB JSR $BBCA
.E04A  A9 57    LDA #$57
.E04C  20 28 BA JSR $BA28
.E04F  20 5D E0 JSR $E05D
.E052  A9 57    LDA #$57
.E054  A0 00    LDY #$00
.E056  4C 28 BA JMP $BA28
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$E043**: Zeiger auf
- **$E045**: Polynomkoeffizienten
- **$E047**: FAC nach Akku #3 bringen
- **$E04A**: Zeiger auf Akku #3
- **$...
