---
id: src-b194-compute-pointer-to-array-body
type: source
title: 'Source Summary: compute pointer to array body'
aliases:
- compute pointer to array body
- b194-compute-pointer-to-array-body.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b194-compute-pointer-to-array-body.md
  sha256: f253b57a57c3cc708c5e6f688f367ef563c418d86e3a6e3599960f94b297475b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: compute pointer to array body

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b194-compute-pointer-to-array-body.md`
**SHA256**: `f253b57a57c3cc708c5e6f688f367ef563c418d86e3a6e3599960f94b297475b`

## Summary



# $B194 — compute pointer to array body

## Disassemblatura
```assembly
.B194  A5 0B    LDA $0B
.B196  0A       ASL
.B197  69 05    ADC #$05
.B199  65 5F    ADC $5F
.B19B  A4 60    LDY $60
.B19D  90 01    BCC $B1A0
.B19F  C8       INY
.B1A0  85 58    STA $58
.B1A2  84 59    STY $59
.B1A4  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B194**: Anzahl der Dimensionen
- **$B196**: mal 2
- **$B197**: plus 5
- **$B199**: zu $5F und
- **$B19B**: $60 addieren
- **$B19D*...
