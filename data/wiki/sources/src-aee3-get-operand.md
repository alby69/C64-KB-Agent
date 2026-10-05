---
id: src-aee3-get-operand
type: source
title: 'Source Summary: GET operand'
aliases:
- GET operand
- aee3-get-operand.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aee3-get-operand.md
  sha256: 53e4e455d1464ce00fac6993cc4ebf5518b1126b2fbb908a0c6abe540ee97d42
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: GET operand

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aee3-get-operand.md`
**SHA256**: `53e4e455d1464ce00fac6993cc4ebf5518b1126b2fbb908a0c6abe540ee97d42`

## Summary



# $AEE3 — GET operand

## Disassemblatura
```assembly
.AEE3  C9 A5    CMP #$A5
.AEE5  D0 03    BNE $AEEA
.AEE7  4C F4 B3 JMP $B3F4
.AEEA  C9 B4    CMP #$B4   ; SGN code or higher
.AEEC  90 03    BCC $AEF1
.AEEE  4C A7 AF JMP $AFA7
.AEF1  20 FA AE JSR $AEFA
.AEF4  20 9E AD JSR $AD9E
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$AEEA**: SGN code or higher

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) ...
