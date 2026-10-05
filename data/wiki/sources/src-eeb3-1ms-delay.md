---
id: src-eeb3-1ms-delay
type: source
title: 'Source Summary: 1ms delay'
aliases:
- 1ms delay
- eeb3-1ms-delay.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eeb3-1ms-delay.md
  sha256: 621a847bef771a5c2293e99719c9c9aed5c071cfea9b6530935015f860636f9b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 1ms delay

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/eeb3-1ms-delay.md`
**SHA256**: `621a847bef771a5c2293e99719c9c9aed5c071cfea9b6530935015f860636f9b`

## Summary



# $EEB3 — 1ms delay

## Disassemblatura
```assembly
.EEB3  8A       TXA   ; save X
.EEB4  A2 B8    LDX #$B8   ; set the loop count
.EEB6  CA       DEX   ; decrement the loop count
.EEB7  D0 FD    BNE $EEB6   ; loop if more to do
.EEB9  AA       TAX   ; restore X
.EEBA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEB3**: save X
- **$EEB4**: set the loop count
- **$EEB6**: decrement the loop count
- **$EEB7**: loop if more to do
- **$EEB9**: restore X

### Commodore-64-inte...
