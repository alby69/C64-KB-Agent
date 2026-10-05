---
id: src-a38a-search-the-stack-for-for-or-gosub-activity
type: source
title: 'Source Summary: search the stack for FOR or GOSUB activity'
aliases:
- search the stack for FOR or GOSUB activity
- a38a-search-the-stack-for-for-or-gosub-activity.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a38a-search-the-stack-for-for-or-gosub-activity.md
  sha256: 5b82e4db48fcdd7df3196a9e5cc180f7b4523e9656ec158274d658470b95cdea
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: search the stack for FOR or GOSUB activity

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a38a-search-the-stack-for-for-or-gosub-activity.md`
**SHA256**: `5b82e4db48fcdd7df3196a9e5cc180f7b4523e9656ec158274d658470b95cdea`

## Summary



# $A38A — search the stack for FOR or GOSUB activity

## Disassemblatura
```assembly
.A38A  BA       TSX   ; copy stack pointer
.A38B  E8       INX   ; +1 pass return address
.A38C  E8       INX   ; +2 pass return address
.A38D  E8       INX   ; +3 pass calling routine return address
.A38E  E8       INX   ; +4 pass calling routine return address
.A38F  BD 01 01 LDA $0101,X   ; get the token byte from the stack
.A392  C9 81    CMP #$81   ; is it the FOR token
.A394  D0 21    BNE $A3B7   ; if no...
