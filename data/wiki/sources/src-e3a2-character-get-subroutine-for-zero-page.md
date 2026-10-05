---
id: src-e3a2-character-get-subroutine-for-zero-page
type: source
title: 'Source Summary: character get subroutine for zero page'
aliases:
- character get subroutine for zero page
- e3a2-character-get-subroutine-for-zero-page.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e3a2-character-get-subroutine-for-zero-page.md
  sha256: 3a392760e761494051792cef83a07471273946e14a2e9b1f7068397226022f05
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: character get subroutine for zero page

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e3a2-character-get-subroutine-for-zero-page.md`
**SHA256**: `3a392760e761494051792cef83a07471273946e14a2e9b1f7068397226022f05`

## Summary



# $E3A2 — character get subroutine for zero page

## Disassemblatura
```assembly
.E3A2  E6 7A    INC $7A   ; increment BASIC execute pointer low byte
.E3A4  D0 02    BNE $E3A8   ; branch if no carry else
.E3A6  E6 7B    INC $7B   ; increment BASIC execute pointer high byte page 0 initialisation table from $0079 scan memory
.E3A8  AD 60 EA LDA $EA60   ; get byte to scan, address set by call routine
.E3AB  C9 3A    CMP #$3A   ; compare with ":"
.E3AD  B0 0A    BCS $E3B9   ; exit if>= page 0 init...
