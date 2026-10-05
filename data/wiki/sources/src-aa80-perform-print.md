---
id: src-aa80-perform-print
type: source
title: 'Source Summary: perform PRINT#'
aliases:
- perform PRINT#
- aa80-perform-print.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aa80-perform-print.md
  sha256: 6bee5ea68a789d918a20982d910e7c87ecd816850458951b6e271fb323dfbf4e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform PRINT#

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aa80-perform-print.md`
**SHA256**: `6bee5ea68a789d918a20982d910e7c87ecd816850458951b6e271fb323dfbf4e`

## Summary



# $AA80 — perform PRINT#

## Disassemblatura
```assembly
.AA80  20 86 AA JSR $AA86   ; perform CMD
.AA83  4C B5 AB JMP $ABB5   ; close input and output channels and return
```


## Commenti

### Original Disassembly (—)
- **$AA80**: perform CMD
- **$AA83**: close input and output channels and return

### Commodore-64-intern-Buch (Commodore)
- **$AA80**: CMD-Befehl
- **$AA83**: und CLRCH

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist6...
