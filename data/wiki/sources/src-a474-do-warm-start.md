---
id: src-a474-do-warm-start
type: source
title: 'Source Summary: do warm start'
aliases:
- do warm start
- a474-do-warm-start.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a474-do-warm-start.md
  sha256: 6b400db2775367aea8d41b1fdab9b2eb71df1fa85a5c08a0d7805599ddf7dd0b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do warm start

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a474-do-warm-start.md`
**SHA256**: `6b400db2775367aea8d41b1fdab9b2eb71df1fa85a5c08a0d7805599ddf7dd0b`

## Summary



# $A474 — do warm start

## Disassemblatura
```assembly
.A474  A9 76    LDA #$76   ; set "READY." pointer low byte
.A476  A0 A3    LDY #$A3   ; set "READY." pointer high byte
.A478  20 1E AB JSR $AB1E   ; print null terminated string
.A47B  A9 80    LDA #$80   ; set for control messages only
.A47D  20 90 FF JSR $FF90   ; control kernal messages
.A480  6C 02 03 JMP ($0302)   ; do BASIC warm start
```


## Commenti

### Original Disassembly (—)
- **$A474**: set "READY." pointer low byte
- **$A47...
