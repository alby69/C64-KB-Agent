---
id: src-e6a8-return-from-output-to-the-screen
type: source
title: 'Source Summary: return from output to the screen'
aliases:
- return from output to the screen
- e6a8-return-from-output-to-the-screen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e6a8-return-from-output-to-the-screen.md
  sha256: 947b942e5795e35d0e8bf8c9ba0fa0d90c2138aba5e6b4e823220987ef044271
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: return from output to the screen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e6a8-return-from-output-to-the-screen.md`
**SHA256**: `947b942e5795e35d0e8bf8c9ba0fa0d90c2138aba5e6b4e823220987ef044271`

## Summary



# $E6A8 — return from output to the screen

## Disassemblatura
```assembly
.E6A8  68       PLA
.E6A9  A8       TAY
.E6AA  A5 D8    LDA $D8
.E6AC  F0 02    BEQ $E6B0
.E6AE  46 D4    LSR $D4
.E6B0  68       PLA
.E6B1  AA       TAX
.E6B2  68       PLA
.E6B3  18       CLC
.E6B4  58       CLI
.E6B5  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
