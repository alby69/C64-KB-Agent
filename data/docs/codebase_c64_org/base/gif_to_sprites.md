---
title: GIF to sprites
source_url: https://codebase.c64.org/doku.php?id=base%3Agif_to_sprites
category: tool
topics:
- assembly
- sprite programming
difficulty: intermediate
language: none
hardware:
- VIC-II
related:
- vic-ii-registers
- raster-interrupts
- sprite-programming
scraped_at: '2026-07-20'
---

# GIF to sprites

# GIF to sprites

By Mace

This is a Kick Assembler script that turns a GIF into separate sprites. The order is represented by strings that contain letters, enabling you to make a sprite font with only the letters that you use, but distributed into memory where the sprite pointers have screen code offset.

To clearify: if you have the A as your first letter in the top left of your GIF, it will be transfered to spriteMemory + 1*64 (where 1 is the screencode of the letter A). So if spriteMemory is $4000, the 64×21 top left pixels will be transfered to $4040.

The GIF could look something like the one below. The script assumes black letters on a white background. Compare the content of the GIF with the strings in lines 13 and 14 of the script and you'll see the resemblance.

![](https://codebase.c64.org/lib/exe/fetch.php?w=400&tok=73413f&media=base:halloweed_sprite_set_single_color.gif)


```
.label spriteMemory = $4000
* = spriteMemory // spriteMemory is where you want your sprites
// Load the GIF with the sprite font, each letter in a 64x21 grid
.var spriteFont = LoadPicture("spritefont.gif",List().add($ffffff,$000000))
// Create a List() that contains the letters in your font
//  in the order as they appear in the GIF
.var fontMap = List()
// Add strings that contains all the letters for each line in the GIF
.eval fontMap.add("abcdefghijklmnopqrstuvwxyz")	// content of 1st line
.eval fontMap.add(@"0123456789\$27-+?!,.")	// content of 2nd line
                                                // (@ indicates escape code)
// Parse the strings (var l = lines) in the fontMap List()
.for (var l=0; l<fontMap.size(); l++){		// loop through lines
// Parse each string (var p = position)
.for (var p=0; p<fontMap.get(l).size(); p++){	// loop through letters
// The location in memory is determined by the value of the letter
* = spriteMemory + fontMap.get(l).charAt(p)*64 	// determine memory location
// Transfer the graphics in the GIF to the sprite
.fill 63, spriteFont.getSinglecolorByte((p*3)+mod(i,3), l*21+floor(i/3))
} // for-loop p
} // for-loop l
```

## Codice Estratto

### Snippet Codice (BASIC)

```basic
.label spriteMemory = $4000

* = spriteMemory // spriteMemory is where you want your sprites

// Load the GIF with the sprite font, each letter in a 64x21 grid
.var spriteFont = LoadPicture("spritefont.gif",List().add($ffffff,$000000))

// Create a List() that contains the letters in your font
//  in the order as they appear in the GIF
.var fontMap = List()

// Add strings that contains all the letters for each line in the GIF
.eval fontMap.add("abcdefghijklmnopqrstuvwxyz")	// content of 1st line
.eval fontMap.add(@"0123456789\$27-+?!,.")	// content of 2nd line
                                                // (@ indicates escape code)

// Parse the strings (var l = lines) in the fontMap List()
.for (var l=0; l<fontMap.size(); l++){		// loop through lines

// Parse each string (var p = position)
.for (var p=0; p<fontMap.get(l).size(); p++){	// loop through letters

// The location in memory is determined by the value of the letter
* = spriteMemory + fontMap.get(l).charAt(p)*64 	// determine memory location

// Transfer the graphics in the GIF to the sprite
.fill 63, spriteFont.getSinglecolorByte((p*3)+mod(i,3), l*21+floor(i/3))

} // for-loop p
} // for-loop l
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Agif_to_sprites](https://codebase.c64.org/doku.php?id=base%3Agif_to_sprites)*
