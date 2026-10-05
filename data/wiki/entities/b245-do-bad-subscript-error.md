---
id: b245-do-bad-subscript-error
type: entity
title: do bad subscript error
aliases:
- do bad subscript error
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b245-do-bad-subscript-error.md
  sha256: 385438572ef3414f7f093bc453b7e1684fb2d6f9d694eb67beed82aeec7095ee
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b245-do-bad-subscript-error
---

# do bad subscript error



# $B245 — do bad subscript error

## Disassemblatura
```assembly
.B245  A2 12    LDX #$12   ; error $12, bad subscript error
.B247  2C       .BYTE $2C   ; makes next line BIT $0EA2
```


## Commenti

### Original Disassembly (—)
- **$B245**: error $12, bad subscript error
- **$B247**: makes next line BIT $0EA2

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B247**: TRICK TO SKIP NEXT LINE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b245-do-bad-subscript-error]]
