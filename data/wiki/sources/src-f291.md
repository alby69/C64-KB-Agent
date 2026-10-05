---
id: src-f291
type: source
title: 'Source Summary: ;'
aliases:
- ;
- f291.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f291.md
  sha256: c92e9d010a8bc911fe85b9466f0a5b2d1fbcc9201f5cf1cb2055f06b84304d08
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f291.md`
**SHA256**: `c92e9d010a8bc911fe85b9466f0a5b2d1fbcc9201f5cf1cb2055f06b84304d08`

## Summary



# $F291 — ;

## Disassemblatura
```assembly
.F291  20 14 F3 JSR $F314   ; NCLOSE JSR JLTLK       ;LOOK FILE UP
.F294  F0 02    BEQ $F298   ; BEQ    JX050           ;OPEN...
.F296  18       CLC   ; CLC                    ;ELSE RETURN
.F297  60       RTS   ; RTS ;
.F298  20 1F F3 JSR $F31F   ; JX050  JSR JZ100       ;EXTRACT TABLE DATA
.F29B  8A       TXA   ; TXA                    ;SAVE TABLE INDEX
.F29C  48       PHA   ; PHA ;
.F29D  A5 BA    LDA $BA   ; LDA    FA              ;CHECK DEVICE NU...
