---
id: src-cbm64scrtopet
type: source
title: 'Source Summary: Commodore 64 screen code to PETSCII code conversion'
aliases:
- Commodore 64 screen code to PETSCII code conversion
- cbm64scrtopet.md
tags:
- basic
sources:
- path: data/docs/sta_c64_org/cbm64scrtopet.md
  sha256: dc63a1b48c4f503ec6cfac96811dc4f569c891afeb94f42b35720fd2f90beee5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 screen code to PETSCII code conversion

**Raw Source File**: `data/docs/sta_c64_org/cbm64scrtopet.md`
**SHA256**: `dc63a1b48c4f503ec6cfac96811dc4f569c891afeb94f42b35720fd2f90beee5`

## Summary



# Commodore 64 screen code to PETSCII code conversion

| Screen code (dec, hex) |  | Change (dec, hex) |  | PETSCII code (dec, hex) |  | 
|---|---|---|---|---|---|
| 0-31 | $00-$1F | +64 | $40 | 64-95 | $40-$5F | 
| 32-63 | $20-$3F | 0 | $00 | 32-63 | $20-$3F | 
| 64-93 | $40-$5D | +128 | $80 | 192-221 | $C0-$DD | 
| 94 | $5E |  |  | 255 | $FF | 
| 95 | $5F | +128 | $80 | 223 | $DF | 
| 96-127 | $60-$7F | +64 | $40 | 160-191 | $A0-$BF | 
| 128-159 | $80-$9F | -128 | $80 | 0-31 | $00-$1F | 
| 1...
