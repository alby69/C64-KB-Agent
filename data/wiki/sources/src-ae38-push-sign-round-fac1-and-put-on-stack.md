---
id: src-ae38-push-sign-round-fac1-and-put-on-stack
type: source
title: 'Source Summary: push sign, round FAC1 and put on stack'
aliases:
- push sign, round FAC1 and put on stack
- ae38-push-sign-round-fac1-and-put-on-stack.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae38-push-sign-round-fac1-and-put-on-stack.md
  sha256: 30a66d778e571f61655de75d279c6f3eeb8dc67c602796c2117ddc215ed8b6c6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: push sign, round FAC1 and put on stack

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ae38-push-sign-round-fac1-and-put-on-stack.md`
**SHA256**: `30a66d778e571f61655de75d279c6f3eeb8dc67c602796c2117ddc215ed8b6c6`

## Summary



# $AE38 — push sign, round FAC1 and put on stack

## Disassemblatura
```assembly
.AE38  A8       TAY   ; copy sign
.AE39  68       PLA   ; get return address low byte
.AE3A  85 22    STA $22   ; save it
.AE3C  E6 22    INC $22   ; increment it as return-1 is pushed note, no check is made on the high byte so if the calling routine ever assembles to a page edge then this all goes horribly wrong!
.AE3E  68       PLA   ; get return address high byte
.AE3F  85 23    STA $23   ; save it
.AE41  98   ...
