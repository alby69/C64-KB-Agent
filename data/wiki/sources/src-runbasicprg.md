---
id: src-runbasicprg
type: source
title: 'Source Summary: Running a Basic program from Assembler'
aliases:
- Running a Basic program from Assembler
- runbasicprg.md
tags:
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/runbasicprg.md
  sha256: 748e4406f285acde835d2549c7a1c137caa94816c34f3a428f20167d1f402dbc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Running a Basic program from Assembler

**Raw Source File**: `data/docs/codebase_c64_org/base/runbasicprg.md`
**SHA256**: `748e4406f285acde835d2549c7a1c137caa94816c34f3a428f20167d1f402dbc`

## Summary



# Running a Basic program from Assembler

base:runbasicprg

                # Running a Basic program from Assembler

Sometimes it is neccessary to run a Basic program from assembler code. To do this, it's a good idea to do a full [Kernal/Basic initialization](https://codebase.c64.org/doku.php?id=base:kernalbasicinit) before.

```
PRGEND = $1234    ; end of the Basic program
    LDA #<PRGEND
    STA $2D
    STA $AE
    LDA #>PRGEND
    STA $2E
    STA $AF
    JSR $A659    ; Reset execute point...
