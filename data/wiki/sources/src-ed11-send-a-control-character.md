---
id: src-ed11-send-a-control-character
type: source
title: 'Source Summary: send a control character'
aliases:
- send a control character
- ed11-send-a-control-character.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ed11-send-a-control-character.md
  sha256: c447cb83f0133a7dfd788d017ef86fe5fbba4f7a8badf4e50c85a22efcf0d070
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: send a control character

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ed11-send-a-control-character.md`
**SHA256**: `c447cb83f0133a7dfd788d017ef86fe5fbba4f7a8badf4e50c85a22efcf0d070`

## Summary



# $ED11 — send a control character

## Disassemblatura
```assembly
.ED11  48       PHA   ; save device address
.ED12  24 94    BIT $94   ; test deferred character flag
.ED14  10 0A    BPL $ED20   ; if no deferred character continue
.ED16  38       SEC   ; else flag EOI
.ED17  66 A3    ROR $A3   ; rotate into EOI flag byte
.ED19  20 40 ED JSR $ED40   ; Tx byte on serial bus
.ED1C  46 94    LSR $94   ; clear deferred character flag
.ED1E  46 A3    LSR $A3   ; clear EOI flag
.ED20  68       PLA  ...
