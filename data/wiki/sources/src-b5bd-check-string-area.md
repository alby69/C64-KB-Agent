---
id: src-b5bd-check-string-area
type: source
title: 'Source Summary: check string area'
aliases:
- check string area
- b5bd-check-string-area.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b5bd-check-string-area.md
  sha256: 7671aa96947bc6f2c61c3b17a66b8f29145f49472dc3ee561ef790df35478d59
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check string area

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b5bd-check-string-area.md`
**SHA256**: `7671aa96947bc6f2c61c3b17a66b8f29145f49472dc3ee561ef790df35478d59`

## Summary



# $B5BD — check string area

## Disassemblatura
```assembly
.B5BD  B1 22    LDA ($22),Y
.B5BF  30 35    BMI $B5F6
.B5C1  C8       INY
.B5C2  B1 22    LDA ($22),Y
.B5C4  10 30    BPL $B5F6
.B5C6  C8       INY
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B5BD**: Variablenname erstes Zeichen
- **$B5BF**: Integer o. Funktion ?
- **$B5C1**: Zähler erhöhen
- **$B5C2**: Variablenname zweites Zeichen
- **$B5C4**: wenn Real, dann $B5F6
- **$B5C6**: Zähler erhöhen
- **$B5C7**: holt S...
