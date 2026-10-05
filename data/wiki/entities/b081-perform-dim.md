---
id: b081-perform-dim
type: entity
title: perform DIM
aliases:
- perform DIM
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b081-perform-dim.md
  sha256: 8389c7432ea5f9b108a64ae6c071e37f428d7ae3220125b29208124d651294f0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b081-perform-dim
---

# perform DIM



# $B081 — perform DIM

## Disassemblatura
```assembly
.B081  AA       TAX   ; copy "DIM" flag to X
.B082  20 90 B0 JSR $B090   ; search for variable
.B085  20 79 00 JSR $0079   ; scan memory
.B088  D0 F4    BNE $B07E   ; scan for "," and loop if not null
.B08A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B081**: copy "DIM" flag to X
- **$B082**: search for variable
- **$B085**: scan memory
- **$B088**: scan for "," and loop if not null

### Commodore-64-intern-Buch (Commodore)
- **$B081**: nächstes Zeichen
- **$B082**: Variable dimensionieren
- **$B085**: CHRGOT letztes Zeichen holen
- **$B088**: nicht Ende: zur nächsten Var.
- **$B08A**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b081-perform-dim]]
