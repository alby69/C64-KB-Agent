---
id: src-f333
type: source
title: 'Source Summary: ;**'
aliases:
- ;**
- f333.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f333.md
  sha256: 13f8287832c8dcaa120ab14af44d576ee8a6e70e8ad11537b000dffced7b2b9d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;**

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f333.md`
**SHA256**: `13f8287832c8dcaa120ab14af44d576ee8a6e70e8ad11537b000dffced7b2b9d`

## Summary



# $F333 — ;**

## Disassemblatura
```assembly
.F333  A2 03    LDX #$03   ; NCLRCH LDX #3
.F335  E4 9A    CPX $9A   ; CPX    DFLTO           ;IS OUTPUT CHANNEL IEEE?
.F337  B0 03    BCS $F33C   ; BCS    JX750           ;NO... ;
.F339  20 FE ED JSR $EDFE   ; JSR    UNLSN           ;YES...UNLISTEN IT ;
.F33C  E4 99    CPX $99   ; JX750  CPX DFLTN       ;IS INPUT CHANNEL IEEE?
.F33E  B0 03    BCS $F343   ; BCS    CLALL2          ;NO... ;
.F340  20 EF ED JSR $EDEF   ; JSR    UNTLK           ;YES......
