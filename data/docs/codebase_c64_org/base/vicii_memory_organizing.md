---
title: The VIC banks
source_url: https://codebase.c64.org/doku.php?id=base%3Avicii_memory_organizing
category: reference
topics:
- graphics
- memory management
- assembly
- sprite programming
- basic
difficulty: beginner
language: assembly
hardware:
- SID
- VIC-II
- CIA
- KERNAL
- BASIC ROM
related:
- sprite-programming
- keyboard-handling
- sound-programming
- cia-registers
- memory-map
- raster-interrupts
- sid-registers
- music-player
- kernal-routines
- vic-ii-registers
- joystick-reading
scraped_at: '2026-07-14'
---


# The VIC banks

### Table of Contents

# The VIC banks

By Oswald/Resource.

The first important thing is that the VICII can only adress 16k ram at once. This means that the 64k memory is divided into four 16k VIC banks. $DD00's lowmost 2 bits controls that which bank is seen by the VIC:

$DD00 = %xxxxxx11 -> bank0: $0000-$3fff $DD00 = %xxxxxx10 -> bank1: $4000-$7fff $DD00 = %xxxxxx01 -> bank2: $8000-$bfff $DD00 = %xxxxxx00 -> bank3: $c000-$ffff

$DD00 should be handled with care when also loading while changing VIC bank, because the other bits in it are controlling the serial transfer. If speed is not critical its generally a good idea to change vic bank like this:

lda $DD00 and #%11111100 ora #%000000xx ;<- your desired VIC bank value, see above sta $DD00

the above will only change the bits controlling the VIC bank position.

*A little tip from Nitro/Black Sun: *
If you are using Krill's loader to change the banks, just do

lda #%000000xx ;<- your desired VIC bank value, see above sta $dd00

Otherwise it won't work.

*It is important to note that all the other memory settings are relative to the start of the current VIC bank.*

# Screen, Character memory and Bitmap adresses

These are controlled by $D018.

The Screen dimensions are 40×25 = 1000 bytes of data. When telling the C64 where you want to put your screen data, this is rounded up to 1024 = $400, so you can put screen data on each multiple of $400 bytes in memory. $0400, $0800, $0c00, $1000, $1400, and so on.

Char mem is made up of 256x8 byte chars: 256*8= 2048 -> $0800 Bitmap is (40x8)x25 = 8000, rounded up to 8192 -> $2000

The following table is taken from AAY64:

$D018/53272/VIC+24: Memory Control Register +----------+---------------------------------------------------+ | Bits 7-4 | Video Matrix Base Address (inside VIC) | | Bit 3 | Bitmap-Mode: Select Base Address (inside VIC) | | Bits 3-1 | Character Dot-Data Base Address (inside VIC) | | Bit 0 | Unused | +----------+---------------------------------------------------+

for starters: this register controls the adress of the bitmap or screen (this depends on the screenmode used) and character memory _relative_ to the VIC bank, so all adresses given from now on should be looked at like: VIC bank adress+adress

## Bitmap

$D018 = %xxxx0xxx -> bitmap is at $0000 $D018 = %xxxx1xxx -> bitmap is at $2000

## Character memory

$D018 = %xxxx000x -> charmem is at $0000 $D018 = %xxxx001x -> charmem is at $0800 $D018 = %xxxx010x -> charmem is at $1000 $D018 = %xxxx011x -> charmem is at $1800 $D018 = %xxxx100x -> charmem is at $2000 $D018 = %xxxx101x -> charmem is at $2800 $D018 = %xxxx110x -> charmem is at $3000 $D018 = %xxxx111x -> charmem is at $3800

## Screen memory

$D018 = %0000xxxx -> screenmem is at $0000 $D018 = %0001xxxx -> screenmem is at $0400 $D018 = %0010xxxx -> screenmem is at $0800 $D018 = %0011xxxx -> screenmem is at $0c00 $D018 = %0100xxxx -> screenmem is at $1000 $D018 = %0101xxxx -> screenmem is at $1400 $D018 = %0110xxxx -> screenmem is at $1800 $D018 = %0111xxxx -> screenmem is at $1c00 $D018 = %1000xxxx -> screenmem is at $2000 $D018 = %1001xxxx -> screenmem is at $2400 $D018 = %1010xxxx -> screenmem is at $2800 $D018 = %1011xxxx -> screenmem is at $2c00 $D018 = %1100xxxx -> screenmem is at $3000 $D018 = %1101xxxx -> screenmem is at $3400 $D018 = %1110xxxx -> screenmem is at $3800 $D018 = %1111xxxx -> screenmem is at $3c00

“x” means that the value of that bit is irrevelant from the viewpoint of setting the given memory area's address.

# Sprites

Sprites read their data based on the value of their corresponding Sprite Pointer. Sprite Pointers are located always at the _given_ screen memory's last 8 bytes. ie: screen_memory+$03f8 = sprite pointer0. As everything sprite adresses are also _relative_ to the start of the VIC bank.

for dummies:

screen_memory_start+$03f8 = sprite pointer0 screen_memory_start+$03f9 = sprite pointer1 screen_memory_start+$03fa = sprite pointer2 screen_memory_start+$03fb = sprite pointer3 screen_memory_start+$03fc = sprite pointer4 screen_memory_start+$03fd = sprite pointer5 screen_memory_start+$03fe = sprite pointer6 screen_memory_start+$03ff = sprite pointer7

Sprites are made up of 3 bytes horizontally, and 21 lines vertically giving the size 21*3=63 bytes. As in the binary world living with 2's squares is easyer that is rounded up to 64. Giving: VIC Bank size → $4000/$40 = 256 (16384/64 in decimal) available sprite shapes per VIC bank. It's easy to see that the data that holds the given sprite's gfx starts at spritepointer*64.

Also see the article named [Sprites](https://codebase.c64.org/doku.php?id=base:sprites) written/collected by Oswald.

# The specially handled character ROM

The character rom consists of two character sets being uppercase/lowercase set. $0800×2=$1000 thus the char ram is 4k in size.

## from the viewpoint of VICII

Now dont ask me how this mechanism works but there are two memory areas handled differently where for the VIC the character ROM is mapped in. Unless Ultimax mode is selected by an expansion port cartridge, at these areas the VIC will _always_ 'see' the char rom instead of the RAM. If you set a sprite/bitmap/screen/character memory to read its data from $1000-$2000 or $9000-$a000 the read will be always done from the character rom. These areas are:

$1000-$2000 $9000-$a000

While the cpu will always handle these areas as RAM, the VIC (once again) will always see the character rom. This was done so you can use the RAM freely for the CPU, but at the same time the VIC can read its characters without the need to have them stored in RAM.

## from the viewpoint of the CPU

Now if you want to read the char ROM with the CPU, you have to 'turn' on it. When turned on the char ROM will be visible _for_ the CPU at $D000-$E000. lda #$33 sta $01 will turn the char rom on for you. Be careful, as this value will turn the kernal/basic roms off, also you wont see the vic/sid/cia regs, at $d000 since the char rom will overlap that area.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
$DD00 = %xxxxxx11 -> bank0: $0000-$3fff
$DD00 = %xxxxxx10 -> bank1: $4000-$7fff
$DD00 = %xxxxxx01 -> bank2: $8000-$bfff
$DD00 = %xxxxxx00 -> bank3: $c000-$ffff
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda $DD00
and #%11111100
ora #%000000xx ;<- your desired VIC bank value, see above
sta $DD00
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda #%000000xx ;<- your desired VIC bank value, see above
sta $dd00
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`Char`** (unknown): No description available

```assembly
Char mem is made up of 256x8 byte chars: 256*8= 2048 -> $0800
Bitmap is (40x8)x25 = 8000, rounded up to 8192 -> $2000
```

### Snippet Codice (BASIC)

```basic
$D018/53272/VIC+24:   Memory Control Register

   +----------+---------------------------------------------------+
   | Bits 7-4 |   Video Matrix Base Address (inside VIC)          |
   | Bit  3   |   Bitmap-Mode: Select Base Address (inside VIC)   |
   | Bits 3-1 |   Character Dot-Data Base Address (inside VIC)    |
   | Bit  0   |   Unused                                          |
   +----------+---------------------------------------------------+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
$D018 = %xxxx0xxx -> bitmap is at $0000
$D018 = %xxxx1xxx -> bitmap is at $2000
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
$D018 = %xxxx000x -> charmem is at $0000
$D018 = %xxxx001x -> charmem is at $0800
$D018 = %xxxx010x -> charmem is at $1000
$D018 = %xxxx011x -> charmem is at $1800
$D018 = %xxxx100x -> charmem is at $2000
$D018 = %xxxx101x -> charmem is at $2800
$D018 = %xxxx110x -> charmem is at $3000
$D018 = %xxxx111x -> charmem is at $3800
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
$D018 = %0000xxxx -> screenmem is at $0000
$D018 = %0001xxxx -> screenmem is at $0400
$D018 = %0010xxxx -> screenmem is at $0800
$D018 = %0011xxxx -> screenmem is at $0c00
$D018 = %0100xxxx -> screenmem is at $1000
$D018 = %0101xxxx -> screenmem is at $1400
$D018 = %0110xxxx -> screenmem is at $1800
$D018 = %0111xxxx -> screenmem is at $1c00
$D018 = %1000xxxx -> screenmem is at $2000
$D018 = %1001xxxx -> screenmem is at $2400
$D018 = %1010xxxx -> screenmem is at $2800
$D018 = %1011xxxx -> screenmem is at $2c00
$D018 = %1100xxxx -> screenmem is at $3000
$D018 = %1101xxxx -> screenmem is at $3400
$D018 = %1110xxxx -> screenmem is at $3800
$D018 = %1111xxxx -> screenmem is at $3c00
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
screen_memory_start+$03f8 = sprite pointer0
screen_memory_start+$03f9 = sprite pointer1
screen_memory_start+$03fa = sprite pointer2
screen_memory_start+$03fb = sprite pointer3
screen_memory_start+$03fc = sprite pointer4
screen_memory_start+$03fd = sprite pointer5
screen_memory_start+$03fe = sprite pointer6
screen_memory_start+$03ff = sprite pointer7
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
$1000-$2000
$9000-$a000
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Avicii_memory_organizing](https://codebase.c64.org/doku.php?id=base%3Avicii_memory_organizing)*


### Collegamenti e Riferimenti Hardware
- **$D018 (Memory Setup Register)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d018).
