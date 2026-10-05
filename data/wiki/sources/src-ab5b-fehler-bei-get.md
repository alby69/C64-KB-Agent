---
id: src-ab5b-fehler-bei-get
type: source
title: 'Source Summary: Fehler bei GET'
aliases:
- Fehler bei GET
- ab5b-fehler-bei-get.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab5b-fehler-bei-get.md
  sha256: 690f51ec8a7ecdbcd21ea17e284370a2bf725752ca04ef329aba569788b7978e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Fehler bei GET

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ab5b-fehler-bei-get.md`
**SHA256**: `690f51ec8a7ecdbcd21ea17e284370a2bf725752ca04ef329aba569788b7978e`

## Summary



# $AB5B — Fehler bei GET

## Disassemblatura
```assembly
.AB5B  85 39    STA $39   ; gleiche Zeilennummer
.AB5D  84 3A    STY $3A   ; des Fehlers
.AB5F  4C 08 AF JMP $AF08   ; 'SYNTAX ERROR'
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AB5B**: gleiche Zeilennummer
- **$AB5D**: des Fehlers
- **$AB5F**: 'SYNTAX ERROR'

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
