---
title: Commodore 64 screen code to PETSCII code conversion
source_url: https://sta.c64.org/cbm64scrtopetext.html
category: reference
topics: []
difficulty: intermediate
language: none
hardware: []
related: []
scraped_at: '2026-07-20'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 screen code to PETSCII code conversion

| Screen code (dec, hex) | Change (dec, hex) | PETSCII code (dec, hex) | |||
|---|---|---|---|---|---|
| 0-31 | $00-$1F | +64 | $40 | 64-95 | $40-$5F | 
| 32-63 | $20-$3F | 0 | $00 | 32-63 | $20-$3F | 
| 64-93 | $40-$5F | +128 | $80 | 192-223 | $C0-$DF | 
| 96-127 | $60-$7F | +64 | $40 | 160-191 | $A0-$BF | 
| 128-159 | $80-$9F | -128 | $80 | 0-31 | $00-$1F | 
| 160-191 | $A0-$BF | -64 | $C0 | 96-127 | $60-$7F | 
| 192-223 | $C0-$DF | -64 | $C0 | 128-159 | $80-$9F | 
| 224-254 | $E0-$FE | 0 | $00 | 224-255 | $E0-$FF | 

Notes:

- This suggested conversion table is theoritical, created for the sake of a bijective conversion. It has never been actually implemented by Commodore.

---
*Fonte originale: [https://sta.c64.org/cbm64scrtopetext.html](https://sta.c64.org/cbm64scrtopetext.html)*
