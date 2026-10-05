---
id: src-cbm64scrtopetext
type: source
title: 'Source Summary: Commodore 64 screen code to PETSCII code conversion'
aliases:
- Commodore 64 screen code to PETSCII code conversion
- cbm64scrtopetext.md
tags:
- general
sources:
- path: data/docs/sta_c64_org/cbm64scrtopetext.md
  sha256: 2b249aebb495f3a4574349fff40ceb4645a8fb848f424ff553577e270aab542c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 screen code to PETSCII code conversion

**Raw Source File**: `data/docs/sta_c64_org/cbm64scrtopetext.md`
**SHA256**: `2b249aebb495f3a4574349fff40ceb4645a8fb848f424ff553577e270aab542c`

## Summary



# Commodore 64 screen code to PETSCII code conversion

| Screen code (dec, hex) |  | Change (dec, hex) |  | PETSCII code (dec, hex) |  | 
|---|---|---|---|---|---|
| 0-31 | $00-$1F | +64 | $40 | 64-95 | $40-$5F | 
| 32-63 | $20-$3F | 0 | $00 | 32-63 | $20-$3F | 
| 64-93 | $40-$5F | +128 | $80 | 192-223 | $C0-$DF | 
| 96-127 | $60-$7F | +64 | $40 | 160-191 | $A0-$BF | 
| 128-159 | $80-$9F | -128 | $80 | 0-31 | $00-$1F | 
| 160-191 | $A0-$BF | -64 | $C0 | 96-127 | $60-$7F | 
| 192-223 | $C0-$DF ...
