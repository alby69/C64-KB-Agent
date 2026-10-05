---
id: src-f838-wait-for-playrecord
type: source
title: 'Source Summary: wait for PLAY/RECORD'
aliases:
- wait for PLAY/RECORD
- f838-wait-for-playrecord.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f838-wait-for-playrecord.md
  sha256: dc9d57077e8a36156f0cb1abcfeb90d40f7a0d265eff12b896189a814bdd3b82
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: wait for PLAY/RECORD

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f838-wait-for-playrecord.md`
**SHA256**: `dc9d57077e8a36156f0cb1abcfeb90d40f7a0d265eff12b896189a814bdd3b82`

## Summary



# $F838 — wait for PLAY/RECORD

## Disassemblatura
```assembly
.F838  20 2E F8 JSR $F82E   ; return the cassette sense in Zb
.F83B  F0 F9    BEQ $F836   ; exit if switch closed cassette switch was open
.F83D  A0 2E    LDY #$2E   ; index to "PRESS RECORD & PLAY ON TAPE"
.F83F  D0 DD    BNE $F81E   ; display message and wait for switch, branch always
```


## Commenti

### Original Disassembly (—)
- **$F838**: return the cassette sense in Zb
- **$F83B**: exit if switch closed cassette switch was...
