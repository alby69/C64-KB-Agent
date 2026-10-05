---
id: src-af0d-recursive-get-value
type: source
title: 'Source Summary: recursive get value'
aliases:
- recursive get value
- af0d-recursive-get-value.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af0d-recursive-get-value.md
  sha256: 8a559f86b15a572806d95a2ecca5148da3f9ee527d1fbc2a99acae795798adf0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: recursive get value

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/af0d-recursive-get-value.md`
**SHA256**: `8a559f86b15a572806d95a2ecca5148da3f9ee527d1fbc2a99acae795798adf0`

## Summary



# $AF0D — recursive get value

## Disassemblatura
```assembly
.AF0D  A0 15    LDY #$15
.AF0F  68       PLA
.AF10  68       PLA
.AF11  4C FA AD JMP $ADFA
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
