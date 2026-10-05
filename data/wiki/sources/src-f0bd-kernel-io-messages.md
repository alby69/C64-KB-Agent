---
id: src-f0bd-kernel-io-messages
type: source
title: 'Source Summary: kernel I/O messages'
aliases:
- kernel I/O messages
- f0bd-kernel-io-messages.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f0bd-kernel-io-messages.md
  sha256: 665b8ce12a15688edacf5b715e625568ed9cee99dba99dbdee9cfb22a2229bab
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: kernel I/O messages

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f0bd-kernel-io-messages.md`
**SHA256**: `665b8ce12a15688edacf5b715e625568ed9cee99dba99dbdee9cfb22a2229bab`

## Summary



# $F0BD — kernel I/O messages

## Disassemblatura
```assembly
.F0BD  0D 49 2F 4F 20 45 52 52   ; I/O ERROR #
.F0C5  4F 52 20 A3
.F0C9  0D 53 45 41 52 43 48 49   ; SEARCHING
.F0D1  4E 47 A0
.F0D4  46 4F 52 A0   ; FOR
.F0D8  0D 50 52 45 53 53 20 50   ; PRESS PLAY ON TAPE
.F0E0  4C 41 59 20 4F 4E 20 54
.F0E8  41 50 C5
.F0EB  50 52 45 53 53 20 52 45   ; PRESS RECORD & PLAY ON TAPE
.F0F3  43 4F 52 44 20 26 20 50
.F0FB  4C 41 59 20 4F 4E 20 54
.F103  41 50 C5
.F106  0D 4C 4F 41 44 49 4E C7   ; LOADI...
