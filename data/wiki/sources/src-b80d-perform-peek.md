---
id: src-b80d-perform-peek
type: source
title: 'Source Summary: perform PEEK()'
aliases:
- perform PEEK()
- b80d-perform-peek.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b80d-perform-peek.md
  sha256: 0874aa8abfd113a37461de6ba12011031a3abcc8967782109362a796d427ebe4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform PEEK()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b80d-perform-peek.md`
**SHA256**: `0874aa8abfd113a37461de6ba12011031a3abcc8967782109362a796d427ebe4`

## Summary



# $B80D — perform PEEK()

## Disassemblatura
```assembly
.B80D  A5 15    LDA $15   ; get line number high byte
.B80F  48       PHA   ; save line number high byte
.B810  A5 14    LDA $14   ; get line number low byte
.B812  48       PHA   ; save line number low byte
.B813  20 F7 B7 JSR $B7F7   ; convert FAC_1 to integer in temporary integer
.B816  A0 00    LDY #$00   ; clear index
.B818  B1 14    LDA ($14),Y   ; read byte
.B81A  A8       TAY   ; copy byte to A
.B81B  68       PLA   ; pull byte
....
