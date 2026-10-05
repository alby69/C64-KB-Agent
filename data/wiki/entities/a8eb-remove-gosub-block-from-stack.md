---
id: a8eb-remove-gosub-block-from-stack
type: entity
title: remove GOSUB block from stack
aliases:
- remove GOSUB block from stack
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a8eb-remove-gosub-block-from-stack.md
  sha256: be42a6f627613a5201a9e63d5a8f5bf63e50930da882f74a09162a80aff04bed
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a8eb-remove-gosub-block-from-stack
---

# remove GOSUB block from stack



# $A8EB — remove GOSUB block from stack

## Disassemblatura
```assembly
.A8EB  68       PLA
.A8EC  68       PLA
.A8ED  85 39    STA $39
.A8EF  68       PLA
.A8F0  85 3A    STA $3A
.A8F2  68       PLA
.A8F3  85 7A    STA $7A
.A8F5  68       PLA
.A8F6  85 7B    STA $7B
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a8eb-remove-gosub-block-from-stack]]
