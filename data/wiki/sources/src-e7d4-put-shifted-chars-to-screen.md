---
id: src-e7d4-put-shifted-chars-to-screen
type: source
title: 'Source Summary: put shifted chars to screen'
aliases:
- put shifted chars to screen
- e7d4-put-shifted-chars-to-screen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e7d4-put-shifted-chars-to-screen.md
  sha256: 87c16a167e3c6a8c23c6b55d4e1dd3a33281075f8ba1e2fc48dfaeb620edc6c5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: put shifted chars to screen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e7d4-put-shifted-chars-to-screen.md`
**SHA256**: `87c16a167e3c6a8c23c6b55d4e1dd3a33281075f8ba1e2fc48dfaeb620edc6c5`

## Summary



# $E7D4 — put shifted chars to screen

## Disassemblatura
```assembly
.E7D4  29 7F    AND #$7F   ; remove shift bit
.E7D6  C9 7F    CMP #$7F   ; code for PI
.E7D8  D0 02    BNE $E7DC
.E7DA  A9 5E    LDA #$5E   ; screen PI
.E7DC  C9 20    CMP #$20
.E7DE  90 03    BCC $E7E3
.E7E0  4C 91 E6 JMP $E691
.E7E3  C9 0D    CMP #$0D   ; shift return
.E7E5  D0 03    BNE $E7EA
.E7E7  4C 91 E8 JMP $E891
.E7EA  A6 D4    LDX $D4
.E7EC  D0 3F    BNE $E82D
.E7EE  C9 14    CMP #$14   ; insert
.E7F0  D0 37    BNE...
