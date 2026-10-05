---
id: src-b248-do-illegal-quantity-error
type: source
title: 'Source Summary: do illegal quantity error'
aliases:
- do illegal quantity error
- b248-do-illegal-quantity-error.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b248-do-illegal-quantity-error.md
  sha256: c8de763238dbb702fc02e146a74c7de3543191936dd1848beff4fda060437524
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do illegal quantity error

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b248-do-illegal-quantity-error.md`
**SHA256**: `c8de763238dbb702fc02e146a74c7de3543191936dd1848beff4fda060437524`

## Summary



# $B248 — do illegal quantity error

## Disassemblatura
```assembly
.B248  A2 0E    LDX #$0E   ; error $0E, illegal quantity error
.B24A  4C 37 A4 JMP $A437   ; do error #X then warm start
```


## Commenti

### Original Disassembly (—)
- **$B248**: error $0E, illegal quantity error
- **$B24A**: do error #X then warm start

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
