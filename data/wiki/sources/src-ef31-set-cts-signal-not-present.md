---
id: src-ef31-set-cts-signal-not-present
type: source
title: 'Source Summary: set CTS signal not present'
aliases:
- set CTS signal not present
- ef31-set-cts-signal-not-present.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef31-set-cts-signal-not-present.md
  sha256: 3aee3827f5341ec770455039c24d9925266f4f6d5371becff567ccb9d3c3da26
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set CTS signal not present

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef31-set-cts-signal-not-present.md`
**SHA256**: `3aee3827f5341ec770455039c24d9925266f4f6d5371becff567ccb9d3c3da26`

## Summary



# $EF31 — set CTS signal not present

## Disassemblatura
```assembly
.EF31  A9 10    LDA #$10   ; set CTS signal not present
.EF33  0D 97 02 ORA $0297   ; OR it with the RS232 status register
.EF36  8D 97 02 STA $0297   ; save the RS232 status register
```


## Commenti

### Original Disassembly (—)
- **$EF31**: set CTS signal not present
- **$EF33**: OR it with the RS232 status register
- **$EF36**: save the RS232 status register

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultim...
