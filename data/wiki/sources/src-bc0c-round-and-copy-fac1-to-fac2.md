---
id: src-bc0c-round-and-copy-fac1-to-fac2
type: source
title: 'Source Summary: round and copy FAC1 to FAC2'
aliases:
- round and copy FAC1 to FAC2
- bc0c-round-and-copy-fac1-to-fac2.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc0c-round-and-copy-fac1-to-fac2.md
  sha256: 3faa34105f84267f1e44d762f97470d9df071bb2bdec15347c40ede52530bf19
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: round and copy FAC1 to FAC2

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc0c-round-and-copy-fac1-to-fac2.md`
**SHA256**: `3faa34105f84267f1e44d762f97470d9df071bb2bdec15347c40ede52530bf19`

## Summary



# $BC0C — round and copy FAC1 to FAC2

## Disassemblatura
```assembly
.BC0C  20 1B BC JSR $BC1B   ; round FAC1 copy FAC1 to FAC2
.BC0F  A2 06    LDX #$06   ; 6 bytes to copy
.BC11  B5 60    LDA $60,X   ; get byte from FAC1,X
.BC13  95 68    STA $68,X   ; save byte at FAC2,X
.BC15  CA       DEX   ; decrement count
.BC16  D0 F9    BNE $BC11   ; loop if not all done
.BC18  86 70    STX $70   ; clear FAC1 rounding byte
.BC1A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BC0C**...
