---
title: Commodore 64 PETSCII code to screen code conversion (extended)
source_url: https://sta.c64.org/cbm64pettoscrext.html
category: reference
topics: []
difficulty: intermediate
language: none
hardware: []
related: []
scraped_at: '2026-07-14'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 PETSCII code to screen code conversion (extended)

| PETSCII code (dec, hex) | Change (dec, hex) | Screen code (dec, hex) | |||
|---|---|---|---|---|---|
| 0-31 | $00-$1F | +128 | $80 | 128-159 | $80-$9F | 
| 32-63 | $20-$3F | 0 | $00 | 32-63 | $20-$3F | 
| 64-95 | $40-$5F | -64 | $C0 | 0-31 | $00-$1F | 
| 96-127 | $60-$7F | +64 | $40 | 160-191 | $A0-$BF | 
| 128-159 | $80-$9F | +64 | $40 | 192-223 | $C0-$DF | 
| 160-191 | $A0-$BF | -64 | $C0 | 96-127 | $60-$7F | 
| 192-223 | $C0-$DF | -128 | $80 | 64-95 | $40-$5F | 
| 224-255 | $E0-$FF | 0 | $00 | 224-255 | $E0-$FF | 

Notes:

- This suggested conversion table is theoritical, created for the sake of a bijective conversion. It has never been actually implemented by Commodore.

---
*Fonte originale: [https://sta.c64.org/cbm64pettoscrext.html](https://sta.c64.org/cbm64pettoscrext.html)*
