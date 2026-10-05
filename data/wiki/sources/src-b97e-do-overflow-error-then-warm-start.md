---
id: src-b97e-do-overflow-error-then-warm-start
type: source
title: 'Source Summary: do overflow error then warm start'
aliases:
- do overflow error then warm start
- b97e-do-overflow-error-then-warm-start.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b97e-do-overflow-error-then-warm-start.md
  sha256: 28114cd6f7556ddf760ef99158d63ca2483943ea27d3926f8a64aeffc0382ee0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do overflow error then warm start

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b97e-do-overflow-error-then-warm-start.md`
**SHA256**: `28114cd6f7556ddf760ef99158d63ca2483943ea27d3926f8a64aeffc0382ee0`

## Summary



# $B97E — do overflow error then warm start

## Disassemblatura
```assembly
.B97E  A2 0F    LDX #$0F   ; error $0F, overflow error
.B980  4C 37 A4 JMP $A437   ; do error #X then warm start
```


## Commenti

### Original Disassembly (—)
- **$B97E**: error $0F, overflow error
- **$B980**: do error #X then warm start

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
