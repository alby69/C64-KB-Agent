---
id: src-ab47-print-character
type: source
title: 'Source Summary: print character'
aliases:
- print character
- ab47-print-character.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab47-print-character.md
  sha256: f719ac37fde0aed7edc7dca369b07d9b19e9750ba009d0f6681aaa719d9a1a8a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print character

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ab47-print-character.md`
**SHA256**: `f719ac37fde0aed7edc7dca369b07d9b19e9750ba009d0f6681aaa719d9a1a8a`

## Summary



# $AB47 — print character

## Disassemblatura
```assembly
.AB47  20 0C E1 JSR $E10C   ; output character to channel with error check
.AB4A  29 FF    AND #$FF   ; set the flags on A
.AB4C  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$AB47**: output character to channel with error check
- **$AB4A**: set the flags on A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
