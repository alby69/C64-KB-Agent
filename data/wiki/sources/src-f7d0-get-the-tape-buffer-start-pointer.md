---
id: src-f7d0-get-the-tape-buffer-start-pointer
type: source
title: 'Source Summary: get the tape buffer start pointer'
aliases:
- get the tape buffer start pointer
- f7d0-get-the-tape-buffer-start-pointer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f7d0-get-the-tape-buffer-start-pointer.md
  sha256: 5eb63e8146a9c2559a23e81589cd2981c855fb4c88d2de41f1ffce56f3ad34bc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get the tape buffer start pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f7d0-get-the-tape-buffer-start-pointer.md`
**SHA256**: `5eb63e8146a9c2559a23e81589cd2981c855fb4c88d2de41f1ffce56f3ad34bc`

## Summary



# $F7D0 — get the tape buffer start pointer

## Disassemblatura
```assembly
.F7D0  A6 B2    LDX $B2   ; get tape buffer start pointer low byte
.F7D2  A4 B3    LDY $B3   ; get tape buffer start pointer high byte
.F7D4  C0 02    CPY #$02   ; compare high byte with $02xx
.F7D6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F7D0**: get tape buffer start pointer low byte
- **$F7D2**: get tape buffer start pointer high byte
- **$F7D4**: compare high byte with $02xx

### Commodore...
