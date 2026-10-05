---
id: src-f250
type: source
title: 'Source Summary: ;'
aliases:
- ;
- f250.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f250.md
  sha256: 83ccd654d20b4cb76bf390dcf12611d56f2dc1c9d86dfd14660948ae53ea58f4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f250.md`
**SHA256**: `83ccd654d20b4cb76bf390dcf12611d56f2dc1c9d86dfd14660948ae53ea58f4`

## Summary



# $F250 — ;

## Disassemblatura
```assembly
.F250  20 0F F3 JSR $F30F   ; NCKOUT JSR LOOKUP      ;IS FILE IN TABLE?
.F253  F0 03    BEQ $F258   ; BEQ    CK5             ;YES... ;
.F255  4C 01 F7 JMP $F701   ; JMP    ERROR3          ;NO...FILE NOT OPEN ;
.F258  20 1F F3 JSR $F31F   ; CK5    JSR JZ100       ;EXTRACT TABLE INFO ;
.F25B  A5 BA    LDA $BA   ; LDA    FA              ;IS IT KEYBOARD?
.F25D  D0 03    BNE $F262   ; BNE    CK10            ;NO...SOMETHING ELSE. ;
.F25F  4C 0D F7 JMP $F70...
