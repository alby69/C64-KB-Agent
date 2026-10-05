---
id: src-af61-integervariable-holen
type: source
title: 'Source Summary: Integervariable holen'
aliases:
- Integervariable holen
- af61-integervariable-holen.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af61-integervariable-holen.md
  sha256: 4033ad9ef310d0cdf905b5a570176e77454cf93b89aa4a6ec008b414a8dc9991
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Integervariable holen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/af61-integervariable-holen.md`
**SHA256**: `4033ad9ef310d0cdf905b5a570176e77454cf93b89aa4a6ec008b414a8dc9991`

## Summary



# $AF61 — Integervariable holen

## Disassemblatura
```assembly
.AF61  A0 00    LDY #$00   ; Zeiger setzen
.AF63  B1 64    LDA ($64),Y   ; Intgerzahl holen (1. Byte)
.AF65  AA       TAX   ; ins X-Reg.
.AF66  C8       INY   ; Zeiger erhöhen
.AF67  B1 64    LDA ($64),Y   ; 2. Byte holen
.AF69  A8       TAY   ; ins Y-Register
.AF6A  8A       TXA   ; 1. Byte in Akku holen
.AF6B  4C 91 B3 JMP $B391   ; und nach Fließkomma wandeln
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AF61...
