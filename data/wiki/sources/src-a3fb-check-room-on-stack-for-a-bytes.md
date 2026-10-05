---
id: src-a3fb-check-room-on-stack-for-a-bytes
type: source
title: 'Source Summary: check room on stack for A bytes'
aliases:
- check room on stack for A bytes
- a3fb-check-room-on-stack-for-a-bytes.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a3fb-check-room-on-stack-for-a-bytes.md
  sha256: 60316a28b42bc362775c4d5c0c7778e62817d61e90b780ed556ef11bf90ba858
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check room on stack for A bytes

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a3fb-check-room-on-stack-for-a-bytes.md`
**SHA256**: `60316a28b42bc362775c4d5c0c7778e62817d61e90b780ed556ef11bf90ba858`

## Summary



# $A3FB — check room on stack for A bytes

## Disassemblatura
```assembly
.A3FB  0A       ASL   ; *2
.A3FC  69 3E    ADC #$3E   ; need at least $3E bytes free
.A3FE  B0 35    BCS $A435   ; if overflow go do out of memory error then warm start
.A400  85 22    STA $22   ; save result in temp byte
.A402  BA       TSX   ; copy stack
.A403  E4 22    CPX $22   ; compare new limit with stack
.A405  90 2E    BCC $A435   ; if stack < limit do out of memory error then warm start
.A407  60       RTS
```
...
