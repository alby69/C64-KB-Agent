---
title: vic ii chip initialisation values
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ecb9-videocontroller
- ece7-load
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $ECB9
  address_end: $ECE6
  symbol: vic-ii-chip-initialisation-values
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ECB9**: sprite 0 x,y'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Nessun commento disponibile.
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$ECB9**: sprite 1 x,y'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$ECB9**: $d000/1, sprite0 - x,y coordinate'
---

# $ECB9 — vic ii chip initialisation values

## Disassemblatura
```assembly
.ECB9  00 00   ; sprite 0 x,y
.ECBB  00 00   ; sprite 1 x,y
.ECBD  00 00   ; sprite 2 x,y
.ECBF  00 00   ; sprite 3 x,y
.ECC1  00 00   ; sprite 4 x,y
.ECC3  00 00   ; sprite 5 x,y
.ECC5  00 00   ; sprite 6 x,y
.ECC7  00 00   ; sprite 7 x,y
.ECC9  00   ; sprites 0 to 7 x bit 8
.ECCA  9B   ; enable screen, enable 25 rows vertical fine scroll and control bit function --- ------- 7  raster compare bit 8 6  1 = enable extended color text mode 5  1 = enable bitmap graphics mode 4  1 = enable screen, 0 = blank screen 3  1 = 25 row display, 0 = 24 row display 2-0 vertical scroll count
.ECCB  37   ; raster compare
.ECCC  00   ; light pen x
.ECCD  00   ; light pen y
.ECCE  00   ; sprite 0 to 7 enable
.ECCF  08   ; enable 40 column display horizontal fine scroll and control bit function --- ------- 7-6 unused 5  1 = vic reset, 0 = vic on 4  1 = enable multicolor mode 3  1 = 40 column display, 0 = 38 column display 2-0 horizontal scroll count
.ECD0  00   ; sprite 0 to 7 y expand
.ECD1  14   ; memory control bit function --- ------- 7-4 video matrix base address 3-1 character data base address 0  unused
.ECD2  0F   ; clear all interrupts interrupt flags 7 1 = interrupt 6-4 unused 3  1 = light pen interrupt 2  1 = sprite to sprite collision interrupt 1  1 = sprite to foreground collision interrupt 0  1 = raster compare interrupt
.ECD3  00   ; all vic IRQs disabled IRQ enable bit function --- ------- 7-4 unused 3  1 = enable light pen 2  1 = enable sprite to sprite collision 1  1 = enable sprite to foreground collision 0  1 = enable raster compare
.ECD4  00   ; sprite 0 to 7 foreground priority
.ECD5  00   ; sprite 0 to 7 multicolour
.ECD6  00   ; sprite 0 to 7 x expand
.ECD7  00   ; sprite 0 to 7 sprite collision
.ECD8  00   ; sprite 0 to 7 foreground collision
.ECD9  0E   ; border colour
.ECDA  06   ; background colour 0
.ECDB  01   ; background colour 1
.ECDC  02   ; background colour 2
.ECDD  03   ; background colour 3
.ECDE  04   ; sprite multicolour 0
.ECDF  00   ; sprite multicolour 1
.ECE0  01   ; sprite 0 colour
.ECE1  02   ; sprite 1 colour
.ECE2  03   ; sprite 2 colour
.ECE3  04   ; sprite 3 colour
.ECE4  05   ; sprite 4 colour
.ECE5  06   ; sprite 5 colour
.ECE6  07   ; sprite 6 colour sprite 7 colour is actually the first character of "LOAD" ($4C)
```


## Commenti

### Original Disassembly (—)
- **$ECB9**: sprite 0 x,y
- **$ECBB**: sprite 1 x,y
- **$ECBD**: sprite 2 x,y
- **$ECBF**: sprite 3 x,y
- **$ECC1**: sprite 4 x,y
- **$ECC3**: sprite 5 x,y
- **$ECC5**: sprite 6 x,y
- **$ECC7**: sprite 7 x,y
- **$ECC9**: sprites 0 to 7 x bit 8
- **$ECCA**: enable screen, enable 25 rows vertical fine scroll and control bit function --- ------- 7  raster compare bit 8 6  1 = enable extended color text mode 5  1 = enable bitmap graphics mode 4  1 = enable screen, 0 = blank screen 3  1 = 25 row display, 0 = 24 row display 2-0 vertical scroll count
- **$ECCB**: raster compare
- **$ECCC**: light pen x
- **$ECCD**: light pen y
- **$ECCE**: sprite 0 to 7 enable
- **$ECCF**: enable 40 column display horizontal fine scroll and control bit function --- ------- 7-6 unused 5  1 = vic reset, 0 = vic on 4  1 = enable multicolor mode 3  1 = 40 column display, 0 = 38 column display 2-0 horizontal scroll count
- **$ECD0**: sprite 0 to 7 y expand
- **$ECD1**: memory control bit function --- ------- 7-4 video matrix base address 3-1 character data base address 0  unused
- **$ECD2**: clear all interrupts interrupt flags 7 1 = interrupt 6-4 unused 3  1 = light pen interrupt 2  1 = sprite to sprite collision interrupt 1  1 = sprite to foreground collision interrupt 0  1 = raster compare interrupt
- **$ECD3**: all vic IRQs disabled IRQ enable bit function --- ------- 7-4 unused 3  1 = enable light pen 2  1 = enable sprite to sprite collision 1  1 = enable sprite to foreground collision 0  1 = enable raster compare
- **$ECD4**: sprite 0 to 7 foreground priority
- **$ECD5**: sprite 0 to 7 multicolour
- **$ECD6**: sprite 0 to 7 x expand
- **$ECD7**: sprite 0 to 7 sprite collision
- **$ECD8**: sprite 0 to 7 foreground collision
- **$ECD9**: border colour
- **$ECDA**: background colour 0
- **$ECDB**: background colour 1
- **$ECDC**: background colour 2
- **$ECDD**: background colour 3
- **$ECDE**: sprite multicolour 0
- **$ECDF**: sprite multicolour 1
- **$ECE0**: sprite 0 colour
- **$ECE1**: sprite 1 colour
- **$ECE2**: sprite 2 colour
- **$ECE3**: sprite 3 colour
- **$ECE4**: sprite 4 colour
- **$ECE5**: sprite 5 colour
- **$ECE6**: sprite 6 colour sprite 7 colour is actually the first character of "LOAD" ($4C)

### Commodore-64-intern-Buch (Commodore)
Nessun commento disponibile.

### Marko Mäkelä (Marko Mäkelä)
- **$ECB9**: sprite 1 x,y
- **$ECBB**: sprite 2 x,y
- **$ECBD**: sprite 3 x,y
- **$ECBF**: sprite 4 x,y
- **$ECC1**: sprite 5 x,y
- **$ECC3**: sprite 6 x,y
- **$ECC5**: sprite 7 x,y
- **$ECC7**: sprite 8 x,y
- **$ECD0**: sprite Y expand
- **$ECD5**: sprite multi-colour
- **$ECD6**: sprite X expand
- **$ECD9**: boarder colour
- **$ECDA**: background colour
- **$ECDF**: sprite colour
- **$ECE0**: sprite colour
- **$ECE1**: sprite colour
- **$ECE2**: sprite colour
- **$ECE3**: sprite colour
- **$ECE4**: sprite colour
- **$ECE5**: sprite colour
- **$ECE6**: sprite colour

### Magnus Nyman (Magnus Nyman)
- **$ECB9**: $d000/1, sprite0 - x,y coordinate
- **$ECBB**: $d002/3, sprite1 - x,y coordinate
- **$ECBD**: $d004/5, sprite2 - x,y coordinate
- **$ECBF**: $d006/7, sprite3 - x,y coordinate
- **$ECC1**: $d008/9, sprite4 - x,y coordinate
- **$ECC3**: $d00a/b, sprite5 - x,y coordinate
- **$ECC5**: $d00c/d, sprite6 - x,y coordinate
- **$ECC7**: $d00e/f, sprite7 - x,y coordinate
- **$ECC9**: $d010, sprite MSB
- **$ECCA**: $d011, VIC control register
- **$ECCB**: $d012,
- **$ECCC**: $d013/4, light pen x/y position
- **$ECCE**: $d015, sprite enable
- **$ECCF**: $d016, VIC control register 2
- **$ECD0**: $d017, sprite y-expansion
- **$ECD1**: $d018, VIC memory control register
- **$ECD2**: $d019, VIC irq flag register
- **$ECD3**: $d01a, VIC irq mask register
- **$ECD4**: $d01b, sprite/background priority
- **$ECD5**: $d01c, sprite multicolour mode
- **$ECD6**: $d01d, sprite x-expansion
- **$ECD7**: $d01e, sprite/sprite collision
- **$ECD8**: $d01f, sprite/background collision
- **$ECD9**: $d020, border colour (light blue)
- **$ECDA**: $d021, background colour 0 (blue)
- **$ECDB**: $d022, background colour 1
- **$ECDC**: $d023, background colour 2
- **$ECDD**: $d024, background colour 3
- **$ECDE**: $d025, sprite multicolour register 0
- **$ECDF**: $d026, sprite multicolour register 1
- **$ECE0**: $d027, sprite0 colour
- **$ECE1**: $d028, sprite1 colour
- **$ECE2**: $d029, sprite2 colour
- **$ECE3**: $d02a, sprite3 colour
- **$ECE4**: $d02b, sprite4 colour
- **$ECE5**: $d02c, sprite5 colour
- **$ECE6**: $d02d, sprite6 colour

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*