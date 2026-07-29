---
title: Read Current Raster Scan Line/Write Line to Compare for Raster IRQ
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- vic-ii-registers
difficulty: intermediate
language: assembly
hardware:
- VIC-II
related:
- 00d7-data
- 0286-color
- ab45-print
- d011
- d01a
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $D012
  symbol: RASTE
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Read Raster/Write Raster Value for Compare IRQ
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The Raster Compare register has two different functions, depending
      on
---

# RASTE — Read Current Raster Scan Line/Write Line to Compare for Raster IRQ ($D012)

## Panoramica
Il registro o area di memoria RASTE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D012` (`53266` decimale)
- **Range**: `$D012`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
Read Raster/Write Raster Value for Compare IRQ

### Mapping the Commodore 64 (Sheldon Leemon)
The Raster Compare register has two different functions, depending on
     whether you are reading from it or writing to it.  When this register
     is read, it tells which screen line the electron beam is currently
     scanning.

     There are 262 horizontal lines which make up the American (NTSC)
     standard display screen (312 lines in the European or PAL standard
     screen).  Every one of these lines is scanned and updated 60 times per
     second.  Only 200 of these lines (numbers 50-249) are part of the
     visible display.

     It is sometimes helpful to know just what line is being scanned,
     because changing screen graphics on a particular line while that line
     is being scanned may cause a slight disruption on the screen.  By
     reading this register, it is possible for a machine language program
     to wait until the scan is off the bottom of the screen before changing
     the graphics display.

     It is even possible for a machine language program to read this
     register, and change the screen display when a certain scan line is
     reached.  The program below uses this technique to change the
     background color in midscreen, in order to show all 256 combinations
     of foreground and background text colors at once.

         40 FOR I=49152 TO 49188:READ A:POKE I,A:NEXT:POKE 53280,11
         50 PRINT CHR$(147):FOR I=1024 TO I+1000:POKE I,160:POKE I+54272,11:NEXT I
         60 FOR I=0 TO 15:FOR J=0 TO 15
         70 P=1196+(48*I)+J:POKE P,J+I:POKE P+54272,J:NEXT J,I
         80 PRINT TAB(15)CHR$(5)"COLOR CHART":FOR I=1 TO 19:PRINT:NEXT
         85 PRINT "THIS CHART SHOWS ALL COMBINATIONS OF   "
         86 PRINT "FOREGROUND AND BACKGROUND COLORS.      "
         87 PRINT "FOREGROUND INCREASES FROM LEFT TO RIGHT"
         88 PRINT "BACKGROUND INCREASES FROM TOP TO BOTTOM"
         90 SYS 12*4096
         100 DATA 169,90,133,251,169,0,141,33,208,162,15,120,173,17,208,48
         105 DATA 251,173,18,208
         110 DATA 197,251,208,249,238,33,208,24,105,8,133,251,202,16,233,48,219

     Writing to this register designates the comparison value for the
     Raster Compare Interrupt.  When that interrupt is enabled, a maskable
     interrupt request will be issued every time the electron beam scan
     reaches the scan line whose number was written here.  This is a much
     more flexible technique for changing the display in midscreen than
     reading this register as the sample program above does.  That
     technique requires that the program continuously watch the Raster
     Register, while the interrupt method will call the program when the
     time is right to act.  For more information on raster interrupts, see
     the entry for the Interrupt Mask Register (53274, $D01A).

     It is very important to remember that this register requires nine
     bits, and that this location only holds eight of those bits (the ninth
     is Bit 7 of 53265 ($D011)).  If you forget to read or write to the
     ninth bit, your results could be in error by a factor of 256.

     For example, some early programs written to demonstrate the raster
     interrupt took for granted that the ninth bit of this register would
     be set to 0 on power-up.  When a later version of the Kernal changed
     this initial value to a 1, their interrupt routines, which were
     supposed to set the raster interrupt to occur at scan line number 150,
     ended up setting it for line number 406 instead.  Since the scan line
     numbers do not go up that high, no interrupt request was ever issued
     and the program did not work.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*