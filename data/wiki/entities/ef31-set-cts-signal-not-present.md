---
id: ef31-set-cts-signal-not-present
type: entity
title: set CTS signal not present
aliases:
- set CTS signal not present
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef31-set-cts-signal-not-present.md
  sha256: 3aee3827f5341ec770455039c24d9925266f4f6d5371becff567ccb9d3c3da26
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ef31-set-cts-signal-not-present
---

# set CTS signal not present



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
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ef31-set-cts-signal-not-present]]
