---
id: src-e684-if-open-quote-toggle-cursor-quote-flag
type: source
title: 'Source Summary: if open quote toggle cursor quote flag'
aliases:
- if open quote toggle cursor quote flag
- e684-if-open-quote-toggle-cursor-quote-flag.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e684-if-open-quote-toggle-cursor-quote-flag.md
  sha256: 70e3afbbc08520fcec480305d0ac5bcc64a296f2d1e5176936a06394a4654dc4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: if open quote toggle cursor quote flag

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e684-if-open-quote-toggle-cursor-quote-flag.md`
**SHA256**: `70e3afbbc08520fcec480305d0ac5bcc64a296f2d1e5176936a06394a4654dc4`

## Summary



# $E684 — if open quote toggle cursor quote flag

## Disassemblatura
```assembly
.E684  C9 22    CMP #$22   ; comapre byte with "
.E686  D0 08    BNE $E690   ; exit if not "
.E688  A5 D4    LDA $D4   ; get cursor quote flag, $xx = quote, $00 = no quote
.E68A  49 01    EOR #$01   ; toggle it
.E68C  85 D4    STA $D4   ; save cursor quote flag
.E68E  A9 22    LDA #$22   ; restore the "
.E690  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E684**: comapre byte with "
- **$E686**...
