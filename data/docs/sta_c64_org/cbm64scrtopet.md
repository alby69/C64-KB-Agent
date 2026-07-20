---
title: Commodore 64 screen code to PETSCII code conversion
source_url: https://sta.c64.org/cbm64scrtopet.html
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware:
- KERNAL
- BASIC ROM
related:
- kernal-routines
- memory-map
scraped_at: '2026-07-20'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---

# Commodore 64 screen code to PETSCII code conversion

| Screen code (dec, hex) | Change (dec, hex) | PETSCII code (dec, hex) | |||
|---|---|---|---|---|---|
| 0-31 | $00-$1F | +64 | $40 | 64-95 | $40-$5F | 
| 32-63 | $20-$3F | 0 | $00 | 32-63 | $20-$3F | 
| 64-93 | $40-$5D | +128 | $80 | 192-221 | $C0-$DD | 
| 94 | $5E | 255 | $FF | ||
| 95 | $5F | +128 | $80 | 223 | $DF | 
| 96-127 | $60-$7F | +64 | $40 | 160-191 | $A0-$BF | 
| 128-159 | $80-$9F | -128 | $80 | 0-31 | $00-$1F | 
| 160-191 | $A0-$BF | -128 | $80 | 32-63 | $20-$3F | 
| 192-223 | $C0-$DF | -64 | $C0 | 128-159 | $80-$9F | 
| 224-254 | $E0-$FE | -64 | $C0 | 160-191 | $A0-$BF | 

Notes:

- PETSCII code $5E belongs to the π (pi) symbol. It is converted internally to the the BASIC token $FF when fetched from the screen.

---
*Fonte originale: [https://sta.c64.org/cbm64scrtopet.html](https://sta.c64.org/cbm64scrtopet.html)*
