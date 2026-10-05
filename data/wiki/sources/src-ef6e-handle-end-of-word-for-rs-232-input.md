---
id: src-ef6e-handle-end-of-word-for-rs-232-input
type: source
title: 'Source Summary: handle end of word for RS-232 input'
aliases:
- handle end of word for RS-232 input
- ef6e-handle-end-of-word-for-rs-232-input.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef6e-handle-end-of-word-for-rs-232-input.md
  sha256: 4648acd85fbb81974f93c5f389910867ab8368c6710f8949c6ef19d9c36263b3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: handle end of word for RS-232 input

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef6e-handle-end-of-word-for-rs-232-input.md`
**SHA256**: `4648acd85fbb81974f93c5f389910867ab8368c6710f8949c6ef19d9c36263b3`

## Summary



# $EF6E — handle end of word for RS-232 input

## Disassemblatura
```assembly
.EF6E  C6 A8    DEC $A8
.EF70  A5 A7    LDA $A7
.EF72  F0 67    BEQ $EFDB
.EF74  AD 93 02 LDA $0293
.EF77  0A       ASL
.EF78  A9 01    LDA #$01
.EF7A  65 A8    ADC $A8
.EF7C  D0 EF    BNE $EF6D
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
