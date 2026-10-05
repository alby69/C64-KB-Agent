---
id: src-cbm64pettoscr
type: source
title: 'Source Summary: Commodore 64 PETSCII code to screen code conversion'
aliases:
- Commodore 64 PETSCII code to screen code conversion
- cbm64pettoscr.md
tags:
- basic
sources:
- path: data/docs/sta_c64_org/cbm64pettoscr.md
  sha256: a3460fafec6cbcc7a52a8302e04e6ff97ea75e1e3596f3322cec6545af2fcefc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 PETSCII code to screen code conversion

**Raw Source File**: `data/docs/sta_c64_org/cbm64pettoscr.md`
**SHA256**: `a3460fafec6cbcc7a52a8302e04e6ff97ea75e1e3596f3322cec6545af2fcefc`

## Summary



# Commodore 64 PETSCII code to screen code conversion

| PETSCII code (dec, hex) |  | Change (dec, hex) |  | Screen code (dec, hex) |  | 
|---|---|---|---|---|---|
| 0-31 | $00-$1F | +128 | $80 | 128-159 | $80-$9F | 
| 32-63 | $20-$3F | 0 | $00 | 32-63 | $20-$3F | 
| 64-95 | $40-$5F | -64 | $C0 | 0-31 | $00-$1F | 
| 96-127 | $60-$7F | -32 | $E0 | 64-95 | $40-$5F | 
| 128-159 | $80-$9F | +64 | $40 | 192-223 | $C0-$DF | 
| 160-191 | $A0-$BF | -64 | $C0 | 96-127 | $60-$7F | 
| 192-223 | $C0-$DF |...
