---
id: src-ff48-irq-vector
type: source
title: 'Source Summary: IRQ vector'
aliases:
- IRQ vector
- ff48-irq-vector.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff48-irq-vector.md
  sha256: 3f9d947442d75d5a53e9917a5b663eaf99174695ccedbb12c456dc39989a5675
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: IRQ vector

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ff48-irq-vector.md`
**SHA256**: `3f9d947442d75d5a53e9917a5b663eaf99174695ccedbb12c456dc39989a5675`

## Summary



# $FF48 — IRQ vector

## Disassemblatura
```assembly
.FF48  48       PHA   ; save A
.FF49  8A       TXA   ; copy X
.FF4A  48       PHA   ; save X
.FF4B  98       TYA   ; copy Y
.FF4C  48       PHA   ; save Y
.FF4D  BA       TSX   ; copy stack pointer
.FF4E  BD 04 01 LDA $0104,X   ; get stacked status register
.FF51  29 10    AND #$10   ; mask BRK flag
.FF53  F0 03    BEQ $FF58   ; branch if not BRK
.FF55  6C 16 03 JMP ($0316)   ; else do BRK vector (iBRK)
.FF58  6C 14 03 JMP ($0314)   ; do IRQ...
