---
id: src-f20e
type: source
title: 'Source Summary: ;'
aliases:
- ;
- f20e.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f20e.md
  sha256: c5094a1e644e4ab49283b68092240f7d2b26244dc83c781118319fef12583324
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f20e.md`
**SHA256**: `c5094a1e644e4ab49283b68092240f7d2b26244dc83c781118319fef12583324`

## Summary



# $F20E — ;

## Disassemblatura
```assembly
.F20E  20 0F F3 JSR $F30F   ; NCHKIN JSR LOOKUP      ;SEE IF FILE KNOWN
.F211  F0 03    BEQ $F216   ; BEQ    JX310           ;YUP... ;
.F213  4C 01 F7 JMP $F701   ; JMP    ERROR3          ;NO...FILE NOT OPEN ;
.F216  20 1F F3 JSR $F31F   ; JX310  JSR JZ100       ;EXTRACT FILE INFO ;
.F219  A5 BA    LDA $BA   ; LDA    FA
.F21B  F0 16    BEQ $F233   ; BEQ    JX320           ;IS KEYBOARD...DONE. ; ;COULD BE SCREEN, KEYBOARD, OR SERIAL ;
.F21D  C9 03    ...
