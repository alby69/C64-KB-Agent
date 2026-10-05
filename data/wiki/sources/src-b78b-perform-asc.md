---
id: src-b78b-perform-asc
type: source
title: 'Source Summary: perform ASC()'
aliases:
- perform ASC()
- b78b-perform-asc.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b78b-perform-asc.md
  sha256: 9177b2c17e2654c671e20309591157d6d39bdf68107d2aca00a13df6b00153b9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform ASC()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b78b-perform-asc.md`
**SHA256**: `9177b2c17e2654c671e20309591157d6d39bdf68107d2aca00a13df6b00153b9`

## Summary



# $B78B — perform ASC()

## Disassemblatura
```assembly
.B78B  20 82 B7 JSR $B782   ; evaluate string, get length in A (and Y)
.B78E  F0 08    BEQ $B798   ; if null do illegal quantity error then warm start
.B790  A0 00    LDY #$00   ; set index to first character
.B792  B1 22    LDA ($22),Y   ; get byte
.B794  A8       TAY   ; copy to Y
.B795  4C A2 B3 JMP $B3A2   ; convert Y to byte in FAC1 and return
```


## Commenti

### Original Disassembly (—)
- **$B78B**: evaluate string, get length in...
