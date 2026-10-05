---
id: src-b77c-perform-len
type: source
title: 'Source Summary: perform LEN()'
aliases:
- perform LEN()
- b77c-perform-len.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b77c-perform-len.md
  sha256: 8b7bffb0eafd85c609951528d1f273508971739af9fc7db17a31d2a81deba800
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform LEN()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b77c-perform-len.md`
**SHA256**: `8b7bffb0eafd85c609951528d1f273508971739af9fc7db17a31d2a81deba800`

## Summary



# $B77C — perform LEN()

## Disassemblatura
```assembly
.B77C  20 82 B7 JSR $B782   ; evaluate string, get length in A (and Y)
.B77F  4C A2 B3 JMP $B3A2   ; convert Y to byte in FAC1 and return
```


## Commenti

### Original Disassembly (—)
- **$B77C**: evaluate string, get length in A (and Y)
- **$B77F**: convert Y to byte in FAC1 and return

### Commodore-64-intern-Buch (Commodore)
- **$B77C**: FRESTR, Stringlänge holen
- **$B77F**: Byte-Wert nach Fließkommaformat wandeln

### Marko Mäkelä ...
