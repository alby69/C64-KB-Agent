---
title: base:formatting_a_disk [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Aformatting_a_disk
category: tool
topics:
- raster interrupts
- memory management
- basic
- assembly
difficulty: advanced
language: assembly
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

# base:formatting_a_disk [Codebase64 wiki]

** Formatting a disk **

As pointed out elsewhere, the CBMDOS formats disks well. To activate it we send a command via the command channel as follows:

OPEN 15, 8, 15, “N0:DISKNAME,ID”: CLOSE 15

And that's it if You're doing it from Basic. However from inside a program possibly running IRQ, Memory Configurations and even possibly run from a cartridge (meaning KERNAL is bypassed during start up) we can do it as follows:

```
        //---------------------------
        // Format the disk in Drive 8
    FormatDisk:
        lda $01
        pha                  // Preserve Memory Configuration
        lda #$36
        sta $01              // BANK KERNAL+IO+RAM
        ldx #6
    !:  lda SetParameters,x
        sta $b7,x            // Set SETLFS & SETNAM
        dex
        bpl !-
        jsr $f34a            // OPEN (jumps straight to $f34a instead of $ffc0 (indirectly jumps to $f34a))
        lda #$0f
        jsr $f291            // CLOSE (Same here, straight instead of $ffc3)
        pla
        sta $01
        rts
    SetParameters:
        .byte $14            // Length of Filename
        .byte $0f            // Logical File Number
        .byte $6f            // Channel
        .byte $08            // Device
        .word FormatName
    FormatName:
        .text "N0:DISKNAME,ID"
```
Make sure You have your Vectors at 0314 etc. set up correctly as they will be called since the OPEN command invokes CLI (Set Interrupt flag before modifying the vectors to avoid any accidental IRQ firing while modifying IRQ vectors). Also if you want to maintain compatibility you will have to make sure the KERNAL RAM Vectors are set up correctly and call OPEN and CLOSE from the KERNAL Jump Table and use SETNAM / SETLFS instead of the loop-routine.

I also encountered an issue where I had to initialize the drive before formatting worked. Suspect it was an emulator issue but posting the work-around for sake of good order:

OPEN 15,8,15,“I”: CLOSE 15

TWW/CTR

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`FormatDisk`** (unknown): --------------------------- Format the disk in Drive 8
- **`SetParameters`** (unknown): No description available
- **`FormatName`** (unknown): No description available

```assembly
//---------------------------
        // Format the disk in Drive 8

    FormatDisk:
        lda $01
        pha                  // Preserve Memory Configuration
        lda #$36
        sta $01              // BANK KERNAL+IO+RAM
        ldx #6
    !:  lda SetParameters,x
        sta $b7,x            // Set SETLFS & SETNAM
        dex
        bpl !-
        jsr $f34a            // OPEN (jumps straight to $f34a instead of $ffc0 (indirectly jumps to $f34a))
        lda #$0f
        jsr $f291            // CLOSE (Same here, straight instead of $ffc3)
        pla
        sta $01
        rts

    SetParameters:
        .byte $14            // Length of Filename
        .byte $0f            // Logical File Number
        .byte $6f            // Channel
        .byte $08            // Device
        .word FormatName

    FormatName:
        .text "N0:DISKNAME,ID"
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aformatting_a_disk](https://codebase.c64.org/doku.php?id=base%3Aformatting_a_disk)*
