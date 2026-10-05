---
id: src-fb97-new-tape-byte-setup
type: source
title: 'Source Summary: new tape byte setup'
aliases:
- new tape byte setup
- fb97-new-tape-byte-setup.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fb97-new-tape-byte-setup.md
  sha256: 80bce4874d7ccfd81045055cfd3ef0f01059db6ec73a0613a9985481759ddc39
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: new tape byte setup

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fb97-new-tape-byte-setup.md`
**SHA256**: `80bce4874d7ccfd81045055cfd3ef0f01059db6ec73a0613a9985481759ddc39`

## Summary



# $FB97 — new tape byte setup

## Disassemblatura
```assembly
.FB97  A9 08    LDA #$08   ; eight bits to do
.FB99  85 A3    STA $A3   ; set bit count
.FB9B  A9 00    LDA #$00   ; clear A
.FB9D  85 A4    STA $A4   ; clear tape bit cycle phase
.FB9F  85 A8    STA $A8   ; clear start bit first cycle done flag
.FBA1  85 9B    STA $9B   ; clear byte parity
.FBA3  85 A9    STA $A9   ; clear start bit check flag, set no start bit yet
.FBA5  60       RTS
```


## Commenti

### Original Disassembly (—)...
