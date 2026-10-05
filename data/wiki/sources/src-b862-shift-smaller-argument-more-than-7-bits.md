---
id: src-b862-shift-smaller-argument-more-than-7-bits
type: source
title: 'Source Summary: SHIFT SMALLER ARGUMENT MORE THAN 7 BITS'
aliases:
- SHIFT SMALLER ARGUMENT MORE THAN 7 BITS
- b862-shift-smaller-argument-more-than-7-bits.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b862-shift-smaller-argument-more-than-7-bits.md
  sha256: b537f49cd398c2a5b886a4ee8d605e8621b31db047b32d91992c672717609b1e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: SHIFT SMALLER ARGUMENT MORE THAN 7 BITS

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b862-shift-smaller-argument-more-than-7-bits.md`
**SHA256**: `b537f49cd398c2a5b886a4ee8d605e8621b31db047b32d91992c672717609b1e`

## Summary



# $B862 — SHIFT SMALLER ARGUMENT MORE THAN 7 BITS

## Disassemblatura
```assembly
.B862  20 99 B9 JSR $B999   ; ALIGN RADIX BY SHIFTING
.B865  90 3C    BCC $B8A3   ; ...ALWAYS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B862**: ALIGN RADIX BY SHIFTING
- **$B865**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
