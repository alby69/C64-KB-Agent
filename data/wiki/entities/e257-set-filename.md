---
id: e257-set-filename
type: entity
title: set filename
aliases:
- set filename
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e257-set-filename.md
  sha256: eb8760a879bc0188a0d96139514d5e91c45ba86d369993196ae8372a6f22e14c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e257-set-filename
---

# set filename



# $E257 — set filename

## Disassemblatura
```assembly
.E257  20 9E AD JSR $AD9E   ; evaluate expression
.E25A  20 A3 B6 JSR $B6A3   ; evaluate string
.E25D  A6 22    LDX $22   ; get string pointer low byte
.E25F  A4 23    LDY $23   ; get string pointer high byte
.E261  4C BD FF JMP $FFBD   ; set the filename and return
```


## Commenti

### Original Disassembly (—)
- **$E257**: evaluate expression
- **$E25A**: evaluate string
- **$E25D**: get string pointer low byte
- **$E25F**: get string pointer high byte
- **$E261**: set the filename and return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e257-set-filename]]
