---
id: src-cbm64pettoscrext
type: source
title: 'Source Summary: Commodore 64 PETSCII code to screen code conversion (extended)'
aliases:
- Commodore 64 PETSCII code to screen code conversion (extended)
- cbm64pettoscrext.md
tags:
- general
sources:
- path: data/docs/sta_c64_org/cbm64pettoscrext.md
  sha256: bf780592550f1178e56a50c17737b647d46f0e3b5c663ac20870959a2f9f25aa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 PETSCII code to screen code conversion (extended)

**Raw Source File**: `data/docs/sta_c64_org/cbm64pettoscrext.md`
**SHA256**: `bf780592550f1178e56a50c17737b647d46f0e3b5c663ac20870959a2f9f25aa`

## Summary



# Commodore 64 PETSCII code to screen code conversion (extended)

| PETSCII code (dec, hex) |  | Change (dec, hex) |  | Screen code (dec, hex) |  | 
|---|---|---|---|---|---|
| 0-31 | $00-$1F | +128 | $80 | 128-159 | $80-$9F | 
| 32-63 | $20-$3F | 0 | $00 | 32-63 | $20-$3F | 
| 64-95 | $40-$5F | -64 | $C0 | 0-31 | $00-$1F | 
| 96-127 | $60-$7F | +64 | $40 | 160-191 | $A0-$BF | 
| 128-159 | $80-$9F | +64 | $40 | 192-223 | $C0-$DF | 
| 160-191 | $A0-$BF | -64 | $C0 | 96-127 | $60-$7F | 
| 192-22...
