---
id: src-bc2b-get-fac1-sign
type: source
title: 'Source Summary: get FAC1 sign'
aliases:
- get FAC1 sign
- bc2b-get-fac1-sign.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc2b-get-fac1-sign.md
  sha256: 94bdff8b583a46cf548918e6c641ac2927c137140c87502c849439d95c5672e9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get FAC1 sign

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc2b-get-fac1-sign.md`
**SHA256**: `94bdff8b583a46cf548918e6c641ac2927c137140c87502c849439d95c5672e9`

## Summary



# $BC2B — get FAC1 sign

## Disassemblatura
```assembly
.BC2B  A5 61    LDA $61   ; get FAC1 exponent
.BC2D  F0 09    BEQ $BC38   ; exit if zero (already correct SGN(0)=0)
```


## Commenti

### Original Disassembly (—)
- **$BC2B**: get FAC1 exponent
- **$BC2D**: exit if zero (already correct SGN(0)=0)

### Commodore-64-intern-Buch (Commodore)
- **$BC2B**: wenn null,
- **$BC2D**: dann RTS
- **$BC2F**: FAC-Vorzeichen
- **$BC31**: holen
- **$BC32**: negativ?
- **$BC34**: dann RTS
- **$BC36**: so...
