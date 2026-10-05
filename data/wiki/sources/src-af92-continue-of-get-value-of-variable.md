---
id: src-af92-continue-of-get-value-of-variable
type: source
title: 'Source Summary: continue of get value of variable'
aliases:
- continue of get value of variable
- af92-continue-of-get-value-of-variable.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af92-continue-of-get-value-of-variable.md
  sha256: 8e23b9332afc989ed7d6045bf16e361f81300fe5fdb5767d8e864ee2395484a7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: continue of get value of variable

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/af92-continue-of-get-value-of-variable.md`
**SHA256**: `8e23b9332afc989ed7d6045bf16e361f81300fe5fdb5767d8e864ee2395484a7`

## Summary



# $AF92 — continue of get value of variable

## Disassemblatura
```assembly
.AF92  E0 53    CPX #$53   ; S
.AF94  D0 0A    BNE $AFA0
.AF96  C0 54    CPY #$54   ; T
.AF98  D0 06    BNE $AFA0
.AF9A  20 B7 FF JSR $FFB7
.AF9D  4C 3C BC JMP $BC3C
.AFA0  A5 64    LDA $64
.AFA2  A4 65    LDY $65
.AFA4  4C A2 BB JMP $BBA2
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$AF92**: S
- **$AF96**: T

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
