---
id: src-a883-perform-gosub
type: source
title: 'Source Summary: perform GOSUB'
aliases:
- perform GOSUB
- a883-perform-gosub.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a883-perform-gosub.md
  sha256: 2a6a8e77fcd5c9f694b52cb846cf6e9c6779f4f13049b3a1086cf5c3dd60bfef
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform GOSUB

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a883-perform-gosub.md`
**SHA256**: `2a6a8e77fcd5c9f694b52cb846cf6e9c6779f4f13049b3a1086cf5c3dd60bfef`

## Summary



# $A883 — perform GOSUB

## Disassemblatura
```assembly
.A883  A9 03    LDA #$03   ; need 6 bytes for GOSUB
.A885  20 FB A3 JSR $A3FB   ; check room on stack for 2*A bytes
.A888  A5 7B    LDA $7B   ; get BASIC execute pointer high byte
.A88A  48       PHA   ; save it
.A88B  A5 7A    LDA $7A   ; get BASIC execute pointer low byte
.A88D  48       PHA   ; save it
.A88E  A5 3A    LDA $3A   ; get current line number high byte
.A890  48       PHA   ; save it
.A891  A5 39    LDA $39   ; get current l...
