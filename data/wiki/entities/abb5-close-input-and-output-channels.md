---
id: abb5-close-input-and-output-channels
type: entity
title: close input and output channels
aliases:
- close input and output channels
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/abb5-close-input-and-output-channels.md
  sha256: e71c3f6b4ea39215f620cc21f8c56252e50575cfa78c43b68304b5c2d6d05a2d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-abb5-close-input-and-output-channels
---

# close input and output channels



# $ABB5 — close input and output channels

## Disassemblatura
```assembly
.ABB5  A5 13    LDA $13   ; get current I/O channel
.ABB7  20 CC FF JSR $FFCC   ; close input and output channels
.ABBA  A2 00    LDX #$00   ; clear X
.ABBC  86 13    STX $13   ; clear current I/O channel, flag default
.ABBE  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$ABB5**: get current I/O channel
- **$ABB7**: close input and output channels
- **$ABBA**: clear X
- **$ABBC**: clear current I/O channel, flag default

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-abb5-close-input-and-output-channels]]
