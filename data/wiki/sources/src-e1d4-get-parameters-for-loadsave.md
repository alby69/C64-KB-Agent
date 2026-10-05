---
id: src-e1d4-get-parameters-for-loadsave
type: source
title: 'Source Summary: get parameters for LOAD/SAVE'
aliases:
- get parameters for LOAD/SAVE
- e1d4-get-parameters-for-loadsave.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e1d4-get-parameters-for-loadsave.md
  sha256: 53d0dfa2cdaff16cd05d019e6c3d35b5ea874034c24835f8cf41efc897cf971b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get parameters for LOAD/SAVE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e1d4-get-parameters-for-loadsave.md`
**SHA256**: `53d0dfa2cdaff16cd05d019e6c3d35b5ea874034c24835f8cf41efc897cf971b`

## Summary



# $E1D4 — get parameters for LOAD/SAVE

## Disassemblatura
```assembly
.E1D4  A9 00    LDA #$00   ; clear file name length
.E1D6  20 BD FF JSR $FFBD   ; clear the filename
.E1D9  A2 01    LDX #$01   ; set default device number, cassette
.E1DB  A0 00    LDY #$00   ; set default command
.E1DD  20 BA FF JSR $FFBA   ; set logical, first and second addresses
.E1E0  20 06 E2 JSR $E206   ; exit function if [EOT] or ":"
.E1E3  20 57 E2 JSR $E257   ; set filename
.E1E6  20 06 E2 JSR $E206   ; exit func...
