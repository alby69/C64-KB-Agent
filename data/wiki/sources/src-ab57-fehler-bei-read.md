---
id: src-ab57-fehler-bei-read
type: source
title: 'Source Summary: Fehler bei READ'
aliases:
- Fehler bei READ
- ab57-fehler-bei-read.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab57-fehler-bei-read.md
  sha256: b00334612a241d6c80eeb006eab65604a234538ca73413304874f416137cbaa4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Fehler bei READ

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ab57-fehler-bei-read.md`
**SHA256**: `b00334612a241d6c80eeb006eab65604a234538ca73413304874f416137cbaa4`

## Summary



# $AB57 — Fehler bei READ

## Disassemblatura
```assembly
.AB57  A5 3F    LDA $3F   ; DATA-Zeilennummer
.AB59  A4 40    LDY $40   ; holen (LOW- und HIGH-Byte)
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AB57**: DATA-Zeilennummer
- **$AB59**: holen (LOW- und HIGH-Byte)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
