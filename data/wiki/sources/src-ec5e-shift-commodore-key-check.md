---
id: src-ec5e-shift-commodore-key-check
type: source
title: 'Source Summary: shift + commodore key check'
aliases:
- shift + commodore key check
- ec5e-shift-commodore-key-check.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ec5e-shift-commodore-key-check.md
  sha256: 2ba20a4faf5377fbe302d1ca70865c7bde8a8abc1958028a9291627b594ec64e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: shift + commodore key check

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ec5e-shift-commodore-key-check.md`
**SHA256**: `2ba20a4faf5377fbe302d1ca70865c7bde8a8abc1958028a9291627b594ec64e`

## Summary



# $EC5E — shift + commodore key check

## Disassemblatura
```assembly
.EC5E  C9 08    CMP #$08
.EC60  D0 07    BNE $EC69
.EC62  A9 80    LDA #$80
.EC64  0D 91 02 ORA $0291
.EC67  30 09    BMI $EC72
.EC69  C9 09    CMP #$09
.EC6B  D0 EE    BNE $EC5B
.EC6D  A9 7F    LDA #$7F
.EC6F  2D 91 02 AND $0291
.EC72  8D 91 02 STA $0291
.EC75  4C A8 E6 JMP $E6A8
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate...
