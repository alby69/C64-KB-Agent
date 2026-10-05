---
id: src-ae58-do-functions
type: source
title: 'Source Summary: do functions'
aliases:
- do functions
- ae58-do-functions.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae58-do-functions.md
  sha256: 1e4066f2eea1cad4b498fa1921bfcbf360244680679073ae0d5eb9eb6a9ddac4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do functions

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ae58-do-functions.md`
**SHA256**: `1e4066f2eea1cad4b498fa1921bfcbf360244680679073ae0d5eb9eb6a9ddac4`

## Summary



# $AE58 — do functions

## Disassemblatura
```assembly
.AE58  A0 FF    LDY #$FF   ; flag function
.AE5A  68       PLA   ; pull precedence byte
.AE5B  F0 23    BEQ $AE80   ; exit if done
.AE5D  C9 64    CMP #$64   ; compare previous precedence with $64
.AE5F  F0 03    BEQ $AE64   ; branch if was $64 (< function)
.AE61  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.AE64  84 4B    STY $4B   ; save precedence stacked flag pop FAC2 and return
.AE66  68       PLA   ; pop ...
