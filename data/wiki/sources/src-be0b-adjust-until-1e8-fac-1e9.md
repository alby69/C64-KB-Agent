---
id: src-be0b-adjust-until-1e8-fac-1e9
type: source
title: 'Source Summary: ADJUST UNTIL 1E8 <= (FAC) <1E9'
aliases:
- ADJUST UNTIL 1E8 <= (FAC) <1E9
- be0b-adjust-until-1e8-fac-1e9.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/be0b-adjust-until-1e8-fac-1e9.md
  sha256: 3e093364c8771e7e0a084d8585d4986a2f0aec8edffc660b82a6683ee8afbe4b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ADJUST UNTIL 1E8 <= (FAC) <1E9

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/be0b-adjust-until-1e8-fac-1e9.md`
**SHA256**: `3e093364c8771e7e0a084d8585d4986a2f0aec8edffc660b82a6683ee8afbe4b`

## Summary



# $BE0B — ADJUST UNTIL 1E8 <= (FAC) <1E9

## Disassemblatura
```assembly
.BE0B  A9 B8    LDA #$B8
.BE0D  A0 BD    LDY #$BD
.BE0F  20 5B BC JSR $BC5B   ; COMPARE TO 1E9-1
.BE12  F0 1E    BEQ $BE32   ; (FAC) = 1E9-1
.BE14  10 12    BPL $BE28   ; TOO LARGE, DIVIDE BY TEN
.BE16  A9 B3    LDA #$B3   ; COMPARE TO 1E8-.1
.BE18  A0 BD    LDY #$BD
.BE1A  20 5B BC JSR $BC5B   ; COMPARE TO 1E8-.1
.BE1D  F0 02    BEQ $BE21   ; (FAC) = 1E8-.1
.BE1F  10 0E    BPL $BE2F   ; IN RANGE, ADJUSTMENT FINISHED
.BE2...
