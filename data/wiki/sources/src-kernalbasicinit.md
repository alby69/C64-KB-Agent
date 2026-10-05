---
id: src-kernalbasicinit
type: source
title: 'Source Summary: Initialization of Kernal and Basic system variables'
aliases:
- Initialization of Kernal and Basic system variables
- kernalbasicinit.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/kernalbasicinit.md
  sha256: 134de887c7721a7bd403fe589d0a918f807fc319155e3a6e9f294a9f6bb6e538
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Initialization of Kernal and Basic system variables

**Raw Source File**: `data/docs/codebase_c64_org/base/kernalbasicinit.md`
**SHA256**: `134de887c7721a7bd403fe589d0a918f807fc319155e3a6e9f294a9f6bb6e538`

## Summary



# Initialization of Kernal and Basic system variables

base:kernalbasicinit

                # Initialization of Kernal and Basic system variables

The following code does a software reset.

```
systeminit
    SEI
    CLD
    LDX #$FF
    TXS
    JSR $FF84    ; IOINIT - Initialize I/O
    ; Initialize SID registers (not done by Kernal reset routine):
    LDX #$17
    LDA #$00
lp1 STA $D400,X
    DEX
    BPL lp1
    ; RAMTAS (JSR $FF87) - Initialize System Constants
    ; $FF87 is not actually ...
