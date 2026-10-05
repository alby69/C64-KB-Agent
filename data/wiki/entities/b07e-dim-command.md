---
id: b07e-dim-command
type: entity
title: DIM command
aliases:
- DIM command
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b07e-dim-command.md
  sha256: 910c36d90cdde5da12de3e934b8e746791b80db5acb02a0e89ad4c66ff98cc76
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b07e-dim-command
---

# DIM command



# $B07E — DIM command

## Disassemblatura
```assembly
.B07E  20 FD AE JSR $AEFD
.B081  AA       TAX
.B082  20 90 B0 JSR $B090
.B085  20 79 00 JSR $0079
.B088  D0 F4    BNE $B07E
.B08A  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B07E**: SEPARATED BY COMMAS
- **$B081**: NON-ZERO, FLAGS PTRGET DIM CALLED
- **$B082**: ALLOCATE THE ARRAY
- **$B085**: NEXT CHAR
- **$B088**: NOT END OF STATEMENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b07e-dim-command]]
