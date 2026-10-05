---
id: src-a94b-perform-on
type: source
title: 'Source Summary: perform ON'
aliases:
- perform ON
- a94b-perform-on.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a94b-perform-on.md
  sha256: 95e08cb9ffbbea4604f2b0dde726460774f44c17fbe2d5573c0f55e7a5254a34
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform ON

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a94b-perform-on.md`
**SHA256**: `95e08cb9ffbbea4604f2b0dde726460774f44c17fbe2d5573c0f55e7a5254a34`

## Summary



# $A94B — perform ON

## Disassemblatura
```assembly
.A94B  20 9E B7 JSR $B79E   ; get byte parameter
.A94E  48       PHA   ; push next character
.A94F  C9 8D    CMP #$8D   ; compare with GOSUB token
.A951  F0 04    BEQ $A957   ; if GOSUB go see if it should be executed
.A953  C9 89    CMP #$89   ; compare with GOTO token
.A955  D0 91    BNE $A8E8   ; if not GOTO do syntax error then warm start next character was GOTO or GOSUB, see if it should be executed
.A957  C6 65    DEC $65   ; decrement...
