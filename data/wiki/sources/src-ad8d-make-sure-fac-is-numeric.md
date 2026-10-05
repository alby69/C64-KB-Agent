---
id: src-ad8d-make-sure-fac-is-numeric
type: source
title: 'Source Summary: MAKE SURE (FAC) IS NUMERIC'
aliases:
- MAKE SURE (FAC) IS NUMERIC
- ad8d-make-sure-fac-is-numeric.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ad8d-make-sure-fac-is-numeric.md
  sha256: 3ecfab3bbff8eaff38cbb86a81743916efaeaaa1a1d6eb9b561372c0272ab4fa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: MAKE SURE (FAC) IS NUMERIC

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ad8d-make-sure-fac-is-numeric.md`
**SHA256**: `3ecfab3bbff8eaff38cbb86a81743916efaeaaa1a1d6eb9b561372c0272ab4fa`

## Summary



# $AD8D — MAKE SURE (FAC) IS NUMERIC

## Disassemblatura
```assembly
.AD8D  18       CLC
.AD8E  24       .BYTE $24   ; DUMMY FOR SKIP
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AD8D**: Flag für Test auf numerisch
- **$AD8E**: BIT-Befehl um folgenden Befehl auszulassen

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AD8E**: DUMMY FOR SKIP

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
