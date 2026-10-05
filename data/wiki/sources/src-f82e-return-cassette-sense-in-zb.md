---
id: src-f82e-return-cassette-sense-in-zb
type: source
title: 'Source Summary: return cassette sense in Zb'
aliases:
- return cassette sense in Zb
- f82e-return-cassette-sense-in-zb.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f82e-return-cassette-sense-in-zb.md
  sha256: 27ea403da9cd892e6daa30ca8f02b43bbf1ab0ff2923c35547371c9d0c62c1f8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: return cassette sense in Zb

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f82e-return-cassette-sense-in-zb.md`
**SHA256**: `27ea403da9cd892e6daa30ca8f02b43bbf1ab0ff2923c35547371c9d0c62c1f8`

## Summary



# $F82E — return cassette sense in Zb

## Disassemblatura
```assembly
.F82E  A9 10    LDA #$10   ; set the mask for the cassette switch
.F830  24 01    BIT $01   ; test the 6510 I/O port
.F832  D0 02    BNE $F836   ; branch if cassette sense high
.F834  24 01    BIT $01   ; test the 6510 I/O port
.F836  18       CLC
.F837  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F82E**: set the mask for the cassette switch
- **$F830**: test the 6510 I/O port
- **$F832**: branch if cas...
