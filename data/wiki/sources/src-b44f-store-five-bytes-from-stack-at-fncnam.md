---
id: src-b44f-store-five-bytes-from-stack-at-fncnam
type: source
title: 'Source Summary: STORE FIVE BYTES FROM STACK AT (FNCNAM)'
aliases:
- STORE FIVE BYTES FROM STACK AT (FNCNAM)
- b44f-store-five-bytes-from-stack-at-fncnam.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b44f-store-five-bytes-from-stack-at-fncnam.md
  sha256: c3744ee777f4942b6df366501a8ab6cbcd8373a5abdedce347b9ddfe83cc2ef1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: STORE FIVE BYTES FROM STACK AT (FNCNAM)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b44f-store-five-bytes-from-stack-at-fncnam.md`
**SHA256**: `c3744ee777f4942b6df366501a8ab6cbcd8373a5abdedce347b9ddfe83cc2ef1`

## Summary



# $B44F — STORE FIVE BYTES FROM STACK AT (FNCNAM)

## Disassemblatura
```assembly
.B44F  A0 00    LDY #$00
.B451  68       PLA
.B452  91 4E    STA ($4E),Y
.B454  68       PLA
.B455  C8       INY
.B456  91 4E    STA ($4E),Y
.B458  68       PLA
.B459  C8       INY
.B45A  91 4E    STA ($4E),Y
.B45C  68       PLA
.B45D  C8       INY
.B45E  91 4E    STA ($4E),Y
.B460  68       PLA
.B461  C8       INY
.B462  91 4E    STA ($4E),Y
.B464  60       RTS
```


## Commenti

### Bob Sander-Cederlof (Bob San...
