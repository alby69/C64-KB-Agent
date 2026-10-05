---
id: a435-do-out-of-memory-error-then-warm-start
type: entity
title: do out of memory error then warm start
aliases:
- do out of memory error then warm start
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a435-do-out-of-memory-error-then-warm-start.md
  sha256: 76d8fd949f84474218853f95984e8ab226376d083f8d0ad6ede6ccc02f85f716
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a435-do-out-of-memory-error-then-warm-start
---

# do out of memory error then warm start



# $A435 — do out of memory error then warm start

## Disassemblatura
```assembly
.A435  A2 10    LDX #$10   ; error code $10, out of memory error do error #X then warm start
.A437  6C 00 03 JMP ($0300)   ; do error message
```


## Commenti

### Original Disassembly (—)
- **$A435**: error code $10, out of memory error do error #X then warm start
- **$A437**: do error message

### Marko Mäkelä (Marko Mäkelä)
- **$A435**: error number

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a435-do-out-of-memory-error-then-warm-start]]
