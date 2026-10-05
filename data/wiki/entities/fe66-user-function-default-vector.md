---
id: fe66-user-function-default-vector
type: entity
title: user function default vector
aliases:
- user function default vector
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe66-user-function-default-vector.md
  sha256: 7e55025a74c6ee426bb84bdbc7b8bee6c444a0914cafa128853084a69c9612f6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe66-user-function-default-vector
---

# user function default vector



# $FE66 — user function default vector

## Disassemblatura
```assembly
.FE66  20 15 FD JSR $FD15   ; restore default I/O vectors
.FE69  20 A3 FD JSR $FDA3   ; initialise SID, CIA and IRQ
.FE6C  20 18 E5 JSR $E518   ; initialise the screen and keyboard
.FE6F  6C 02 A0 JMP ($A002)   ; do BASIC break entry
```


## Commenti

### Original Disassembly (—)
- **$FE66**: restore default I/O vectors
- **$FE69**: initialise SID, CIA and IRQ
- **$FE6C**: initialise the screen and keyboard
- **$FE6F**: do BASIC break entry

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE66**: KERNAL reset
- **$FE69**: init I/O
- **$FE6C**: init I/O
- **$FE6F**: jump to Basic warm start vector

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fe66-user-function-default-vector]]
