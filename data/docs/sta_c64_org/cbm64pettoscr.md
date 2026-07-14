---
title: Commodore 64 PETSCII code to screen code conversion
source_url: https://sta.c64.org/cbm64pettoscr.html
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware:
- BASIC ROM
related: []
scraped_at: '2026-07-14'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 PETSCII code to screen code conversion

| PETSCII code (dec, hex) | Change (dec, hex) | Screen code (dec, hex) | |||
|---|---|---|---|---|---|
| 0-31 | $00-$1F | +128 | $80 | 128-159 | $80-$9F | 
| 32-63 | $20-$3F | 0 | $00 | 32-63 | $20-$3F | 
| 64-95 | $40-$5F | -64 | $C0 | 0-31 | $00-$1F | 
| 96-127 | $60-$7F | -32 | $E0 | 64-95 | $40-$5F | 
| 128-159 | $80-$9F | +64 | $40 | 192-223 | $C0-$DF | 
| 160-191 | $A0-$BF | -64 | $C0 | 96-127 | $60-$7F | 
| 192-223 | $C0-$DF | -128 | $80 | 64-95 | $40-$5F | 
| 224-254 | $E0-$FE | -128 | $80 | 96-126 | $60-$7E | 
| 255 | $FF | 94 | $5E | ||

Notes:

- PETSCII code $FF is the BASIC token of the π (pi) symbol. It is converted internally to screen code $5E when printed onto the screen.

---
*Fonte originale: [https://sta.c64.org/cbm64pettoscr.html](https://sta.c64.org/cbm64pettoscr.html)*
