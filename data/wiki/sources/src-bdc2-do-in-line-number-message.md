---
id: src-bdc2-do-in-line-number-message
type: source
title: 'Source Summary: do " IN " line number message'
aliases:
- do " IN " line number message
- bdc2-do-in-line-number-message.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bdc2-do-in-line-number-message.md
  sha256: e7f4b68025d2392c9bb519da44e09cac102033717838f803a072cdd071efa31a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: do " IN " line number message

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bdc2-do-in-line-number-message.md`
**SHA256**: `e7f4b68025d2392c9bb519da44e09cac102033717838f803a072cdd071efa31a`

## Summary



# $BDC2 — do " IN " line number message

## Disassemblatura
```assembly
.BDC2  A9 71    LDA #$71   ; set " IN " pointer low byte
.BDC4  A0 A3    LDY #$A3   ; set " IN " pointer high byte
.BDC6  20 DA BD JSR $BDDA   ; print null terminated string
.BDC9  A5 3A    LDA $3A   ; get the current line number high byte
.BDCB  A6 39    LDX $39   ; get the current line number low byte
```


## Commenti

### Original Disassembly (—)
- **$BDC2**: set " IN " pointer low byte
- **$BDC4**: set " IN " pointer ...
