---
id: src-f817-wait-for-play
type: source
title: 'Source Summary: wait for PLAY'
aliases:
- wait for PLAY
- f817-wait-for-play.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f817-wait-for-play.md
  sha256: 1655a19503abe0caa12f4be450e780026e9310b64ffccd3fd295194b03653051
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: wait for PLAY

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f817-wait-for-play.md`
**SHA256**: `1655a19503abe0caa12f4be450e780026e9310b64ffccd3fd295194b03653051`

## Summary



# $F817 — wait for PLAY

## Disassemblatura
```assembly
.F817  20 2E F8 JSR $F82E   ; return cassette sense in Zb
.F81A  F0 1A    BEQ $F836   ; if switch closed just exit cassette switch was open
.F81C  A0 1B    LDY #$1B   ; index to "PRESS PLAY ON TAPE"
.F81E  20 2F F1 JSR $F12F   ; display kernel I/O message
.F821  20 D0 F8 JSR $F8D0   ; scan stop key and flag abort if pressed note if STOP was pressed the return is to the routine that called this one and not here
.F824  20 2E F8 JSR $F82E   ...
