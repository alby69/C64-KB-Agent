---
title: Commodore 64 display modes
source_url: https://sta.c64.org/cbm64disp.html
category: reference
topics:
- graphics
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- VIC-II
related:
- vic-ii-registers
- memory-map
- raster-interrupts
- kernal-routines
- sprite-programming
scraped_at: '2026-07-20'
last_modified: Fri, 13 Feb 2015 23:00:00 GMT
---


# Commodore 64 display modes

Screen based on:

- Screen RAM ($0400-$07FF, configurable) 
- Character ROM ($D000-$DFFF) 

Colors based on:

- Background Color ($D021) 
- Color RAM ($D800-$DBFF) 

Character shape and color:

- Fetch screen byte from Screen RAM, multiply it by 8. 
- If charset is in lowercase/uppercase mode, add 2048 ($0800). 
- Fetch 8 bytes from this offset of the Character ROM and use it as a bitmap: - Bit = 0: Pixel has background color. 
- Bit = 1: Pixel color is determined by the corresponding color byte in Color RAM. 
 

Screen based on:

- Screen RAM ($0400-$07FF, configurable) 
- Character ROM ($D000-$DFFF) 
- Color RAM ($D800-$DBFF) 

Colors based on:

- Background color ($D021) 
- Extra Background Color #1 ($D022) 
- Extra Background Color #2 ($D023) 
- Color RAM ($D800-$DBFF) 

Character shape and color:

- Fetch color byte from Color RAM. If bit #3 = 0, the character is single color, see "Standard character mode". 
- If color byte bit #3 = 1, the character is multicolor. Fetch screen byte, multiply it by 8. 
- If charset is in lowercase/uppercase mode, add 2048 ($0800). 
- Fetch 8 bytes from this offset of the Character ROM and use it as a bitmap: - Bit pair = %00: Pixel has background color. 
- Bit pair = %01: Pixel has extra background color #1. 
- Bit pair = %02: Pixel has extra background color #2. 
- Bit pair = %11: Pixel color is determined by bits #0-#2 of the color byte. 
 

Screen based on:

- Screen RAM ($0400-$07FF, configurable) 
- Character ROM ($D000-$DFFF) 

Colors based on:

- Screen RAM ($0400-$07FF, configurable) 
- Background Color ($D021) 
- Extra Background Color #1 ($D022) 
- Extra Background Color #2 ($D023) 
- Extra Background Color #3 ($D024) 
- Color RAM ($D800-$DBFF) 

Character shape and color:

- Fetch screen byte from Screen RAM, keep only bits #0-#5, multiply it by 8. 
- If charset is in lowercase/uppercase mode, add 2048 ($0800). 
- Fetch 8 bytes from this offset of the Character ROM and use it as a bitmap: - Bit = 0: Pixel has background color which is determined by bits #6-#7 of the screen byte: - Bit pair = %00: Pixel has Background Color. 
- Bit pair = %01: Pixel has Extra Background Color #1. 
- Bit pair = %10: Pixel has Extra Background Color #2. 
- Bit pair = %11: Pixel has Extra Background Color #3. 
 
- Bit = 1: Pixel color is determined by the corresponding color byte in Color RAM. 
 

Screen based on:

- Bitmap RAM ($2000-$3FFF, configurable) 

Colors based on:

- Screen RAM ($0400-$07FF, configurable) 

Bitmap shape and color:

- Fetch bitmap byte from Bitmap RAM: - Bit = 0: Pixel color is determined by bits #0-#3 of the corresponding screen byte in Screen RAM. 
- Bit = 1: Pixel color is determined by bits #4-#7 of the corresponding screen byte in Screen RAM. 
 

Screen based on:

- Bitmap RAM ($2000-$3FFF, configurable) 

- Screen RAM ($0400-$07FF, configurable) 
- Background Color ($D021) 
- Color RAM ($D800-$DBFF) 

Bitmap shape and color:

- Fetch bitmap byte from Bitmap RAM: - Bit pair = %00: Pixel has Background Color. 
- Bit pair = %01: Pixel color is determined by bits #4-#7 of the corresponding screen byte in Screen RAM. 
- Bit pair = %10: Pixel color is determined by bits #0-#3 of the corresponding screen byte in Screen RAM. 
- Bit pair = %11: Pixel color is determined by the corresponding color byte in Color RAM.

---
*Fonte originale: [https://sta.c64.org/cbm64disp.html](https://sta.c64.org/cbm64disp.html)*


### Collegamenti e Riferimenti Hardware
- **$D021 (Background Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d021).
