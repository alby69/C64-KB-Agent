---
id: src-a5e5-by-copying-chars-up-to-endchr
type: source
title: 'Source Summary: BY COPYING CHARS UP TO ENDCHR.'
aliases:
- BY COPYING CHARS UP TO ENDCHR.
- a5e5-by-copying-chars-up-to-endchr.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a5e5-by-copying-chars-up-to-endchr.md
  sha256: d69344a56641bdf574e312e71b7a3bc55fb03ad45cd763922f85f34aaa569b12
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BY COPYING CHARS UP TO ENDCHR.

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a5e5-by-copying-chars-up-to-endchr.md`
**SHA256**: `d69344a56641bdf574e312e71b7a3bc55fb03ad45cd763922f85f34aaa569b12`

## Summary



# $A5E5 — BY COPYING CHARS UP TO ENDCHR.

## Disassemblatura
```assembly
.A5E5  BD 00 02 LDA $0200,X
.A5E8  F0 DF    BEQ $A5C9   ; END OF LINE
.A5EA  C5 08    CMP $08
.A5EC  F0 DB    BEQ $A5C9   ; FOUND ENDCHR
.A5EE  C8       INY   ; NEXT OUTPUT CHAR
.A5EF  99 FB 01 STA $01FB,Y
.A5F2  E8       INX   ; NEXT INPUT CHAR
.A5F3  D0 F0    BNE $A5E5   ; ...ALWAYS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A5E8**: END OF LINE
- **$A5EC**: FOUND ENDCHR
- **$A5EE**: NEXT OUTPU...
