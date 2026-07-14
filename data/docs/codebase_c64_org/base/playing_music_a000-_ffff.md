---
title: Playing music at $A000 - $FFFF "behind" kernal
source_url: https://codebase.c64.org/doku.php?id=base%3Aplaying_music_a000-_ffff
category: reference
topics:
- raster interrupts
- basic
- assembly
- sound generation
difficulty: beginner
language: mixed
hardware:
- SID
- KERNAL
related:
- sprite-programming
- sound-programming
- memory-map
- raster-interrupts
- sid-registers
- music-player
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---


# Playing music at $A000 - $FFFF "behind" kernal

base:playing_music_a000-_ffff

                # Playing music at $A000 - $FFFF "behind" kernal

Ok, you saw the simple IRQ music player I added previously, now let's play some music inside the IRQ that is outside the $0400-$9fff area. How do we come about it? Well, simple really. We need to turn off the kernal (SET #$35 to $01) initialize the tune and then turn the kernal back on (SET #$37 to $01). You do the same to play the music as well. This is an example for a JCH/DMC tune at $A000.

```
      !to "musplr+.prg",cbm
      *=$0810
      SEI
      LDA #<IRQ
      LDX #>IRQ
      STA $0314
      STX $0315
      LDA #$7F
      STA $DC0D
      LDA #$1B
      STA $D01B
      LDA #$01
      STA $D01A
      LDA #$35 ;TURN OFF BASIC KERNAL
      STA $01
      LDA #$00
      JSR $A000 
      LDA #$37 ;TURN BASIC KERNAL BACK ON
      STA $01
      CLI
      JMP *
IRQ   INC $D019
      LDA #$00
      STA $D012
      LDA #$35
      STA $01
      JSR $A003
      LDA #$37
      STA $01
      JMP $EA31
      *=$a000-2   ;-2 to remove the load adress
      !binary "music.prg"
```
base/playing_music_a000-_ffff.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: ACME)

#### Routine Identificate:
- **`IRQ`** ($0810): No description available

```assembly
!to "musplr+.prg",cbm

      *=$0810
      SEI
      LDA #<IRQ
      LDX #>IRQ
      STA $0314
      STX $0315
      LDA #$7F
      STA $DC0D
      LDA #$1B
      STA $D01B
      LDA #$01
      STA $D01A
      LDA #$35 ;TURN OFF BASIC KERNAL
      STA $01
      LDA #$00
      JSR $A000 
      LDA #$37 ;TURN BASIC KERNAL BACK ON
      STA $01
      CLI
      JMP *
IRQ   INC $D019
      LDA #$00
      STA $D012
      LDA #$35
      STA $01
      JSR $A003
      LDA #$37
      STA $01
      JMP $EA31

      *=$a000-2   ;-2 to remove the load adress
      !binary "music.prg"
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aplaying_music_a000-_ffff](https://codebase.c64.org/doku.php?id=base%3Aplaying_music_a000-_ffff)*


### Collegamenti e Riferimenti Hardware
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).
- **$0314 (IRQ Vector)**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#0314).
