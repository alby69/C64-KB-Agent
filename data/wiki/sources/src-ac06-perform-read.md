---
id: src-ac06-perform-read
type: source
title: 'Source Summary: perform READ'
aliases:
- perform READ
- ac06-perform-read.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ac06-perform-read.md
  sha256: ac394a2032ec343eb6b3381dc39006373ddb7eac876288d71a16be7648b3b0b1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform READ

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ac06-perform-read.md`
**SHA256**: `ac394a2032ec343eb6b3381dc39006373ddb7eac876288d71a16be7648b3b0b1`

## Summary



# $AC06 — perform READ

## Disassemblatura
```assembly
.AC06  A6 41    LDX $41   ; get DATA pointer low byte
.AC08  A4 42    LDY $42   ; get DATA pointer high byte
.AC0A  A9 98    LDA #$98   ; set input mode = READ
.AC0C  2C       .BYTE $2C   ; makes next line BIT $00A9
.AC0D  A9 00    LDA #$00   ; set input mode = INPUT
```


## Commenti

### Original Disassembly (—)
- **$AC06**: get DATA pointer low byte
- **$AC08**: get DATA pointer high byte
- **$AC0A**: set input mode = READ
- **$AC0C**: ...
