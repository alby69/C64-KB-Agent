---
title: Sizecoding
source_url: https://codebase.c64.org/doku.php?id=base%3Asizecoding
category: tool
topics:
- graphics
- sprite programming
- assembly
difficulty: beginner
language: mixed
hardware:
- VIC-II
- CPU
- KERNAL
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---


# Sizecoding

### Table of Contents

# Sizecoding

When you programming using assembler and start optimizing the code, you think it's like Sudoku. But when you sizecode and then optimization, you start to wonder if there is a 3D Sudoku :D


I put some useful tips and tricks here. They were created mainly during my programming work on Lovebyte 2024 and 2025. Most of them use KERNAL.


“Real life” examples you can find at my CSDB profile: [https://csdb.dk/scener/?id=37254](https://csdb.dk/scener/?id=37254)

Have a lot of fun!

Gordian

P.S. To be continued.

## Clearing memory locations/registers

Clearing A and **$99**:

jsr $f345

Clearing A and **$d3**:

jsr $e6fc

Clearing X register and memory at **$13**:

jsr $abba

Clearing X register and memory at **$0d** + TAY:

jsr $b785

Clearing Y register and **$02a1**:

jsr $f498

Swaps value at **$0297** and 0:

jsr $fe0d

This routine puts value from **$0297** into A and clears memory at that address.

Clearing zeropage memory at **$61** and **$66**:

jsr $b8f7

Saves at least 1 byte.

Clearing zeropage memory at **$10** and **$3e**:

jsr $a687

Saves at least 1 byte.

Clearing zeropage memory at **$62**, **$63**, **$64**, **$65**:

lax #0 tay jsr $af87

Saves at least 2 bytes.

Clearing A and zeropage memory at **$9b**, **$a4**, **$a8**, **$a9**:

jsr $fb9b

Saves at least 5 bytes.

## Setting and manipulating A/Y

Store -1 in A and at **$7a**:

jsr $a60e

Store A at **$62**, **$63**, **$64**, **$65** + TAY:

jsr $bce9

Store 0 in A and 1 in Y:

jsr $bf0c

Decrement Y and store at **$42**, store A at **$41**:

jsr $a826

NOT operator for **$66**:

jsr $bfb8

ORA **$90** with A:

jsr $fe1c

EOR **$d1** with 1:

jsr $e688

This routine loads #$22 into A after EORing.

## Copying 2 ZP registers

jsr $fb8e

**$c1** is stored at **$ac** and **$c2** at **$ad**.

## 5/6-bytes "stack"

jsr $bc0f

This routine copies 6 bytes from **$61**-**$66** to **$69**-**$6e**.

If you want pull data, just use:

jsr $bc00

But this routine copies only 5 bytes. From **$6d**-**$69** to **$65**-**$61**.

Depedning on your needs, first routine can be used as “multiple PHA” and the second one as “multiple PLA”, and vice versa.

## 16 bit counter

jsr $b977

Is incremental loop base on **$62**/**$63** value. But remember! **$62** is high byte and **$63** is low byte, so counter is useless when using indirect indexed addressing mode.

jsr $fcdb

This routine increments by 1 16 bit value stored at **$ac**/**$ad**.

## 16 bit addition

jsr $a8fc

Adds 8-byte accumulator value to **$7a** (low byte) and **$7b** (high byte).

jsr $b699

Same as above, but applies to **$35** and **$36** respectively.

jsr $b5f8

Adds 8-byte accumulator value to **$22** (low byte) and **$23** (high byte). Then X register is filled with value from **$23** and Y register becomes empty for free.

jsr $b6cb

Adds 8-byte accumulator value to **$33** (low byte) and **$34** (high byte).
Then X register is filled with value from **$22** and Y register is filled with value from **$23**.

## 16 bit substraction

Substracts 1 from 16 bit value ($5f/$60 - 1 = $7a/$7b):

jsr $a8c5

## Copying memory

ldx #HOW_MANY_PAGES lda #<(Source+(HOW_MANY_PAGES-1)*256) sta $5a lda #>(Source+(HOW_MANY_PAGES-1)*256) sta $5b lda #<(Destination+(HOW_MANY_PAGES-1)*256) sta $58 lda #>(Destination+(HOW_MANY_PAGES-1)*256) sta $59 jsr $a3e8

Another method proposed by [Krill](https://csdb.dk/scener/?id=8104) in [CSDB->Sizecoding section at Codebase64](https://csdb.dk/forums/?roomid=11&topicid=171567&showallposts=1)

lda #<Source sta $22 lda #>Source sta $23 lda #<Dest sta $35 lda #>Dest sta $36 lda #HOW_MANY_HALF_PAGES ; HALF_PAGE=128 bytes sta $02 - lda #$80 jsr $b68c lda #$80 jsr $b5f8 dec $02 bne -

## Clearing/filling memory

jsr $e416

Calling this routines causes clearing single byte at **$2b** (low byte) and **$2c** (high byte), but slight modification:

lda #$00 sta $2b lda #$20 sta $2c - jsr $e416 lda $2c bpl -

and we have cleared memory from $2000 to $7fff.

It is very helpful when we want to clear hires bitmap before drawing, e.g.:

lda #$18 sta $d018 sta $2c - jsr $e416 lda $2c bpl -

Using **#$18** as value we set bitmap mode and bitmap at $2000 and we start clearing from $18xx (who cares it's not $2000 - we sizecode;))

Filling memory from $2000 to $7fff required code as below:

lda #$00 sta $2b lda #$20 sta $2c - ldy #0 lda #VALUE jsr $e419 lda $2c bpl -

## ORing bitmap data

Here is simple example which I used in [New World OR'er](https://csdb.dk/release/?id=239335). It automagically multiplies X by 2 and sets proper bit, so pixels are drawn with 1px horizontal spacing.

ldx #X lda #3 sbx #0 ;x AND 3 eor #$a9 ;A^mask=%x0x0x0x0 ;at bd36 we have ;60 10 0E A9 ;rolled and masked ;80 20 08 02 rla $bd36,x ora (BitmapDataL),y sta (BitmapDataL),y

Another location which give us the same values is placed at **$e736**.

## Aligning sprite and charset data

We know that sprite data pointer must be 64-byte-aligned and charset 2048-byte-aligned. When you sizecode there is often no space for copying data. The best (IMHO) solution is put data at the start of the code. E.g.:

*=$ALIGNED_ADDRESS-2 bvc + Sprite !fill 255,63 + ;the rest of the code

If the data takes more than 127 bytes and relative branch is not possible just use jmp instruction:

*=$ALIGNED_ADDRESS-3 jmp + Sprite !fill 255,63 + ;the rest of the code

## Using single table for chars and colors

When you draw some char-dithered pattern, you can save half the bytes using the same table for chars and colors. Remember that low nibble of the char-byte can be used as a color.

## Drawing chars

Table at **$ecf0** stores low byte of pointers to each screen line address (<row*40).

Table at **$d9** like above, but stores high bytes (>row*40).

Each table has 25 bytes.

Calling routine at **$e9f0** with X register filled by row value we get low pointer in **$d1** and high pointer in **$d2** register:

ldx #row jsr $e9f0

Now via:

lda #char ldy #column sta ($d1),y

we can put certain char at certain screen cell.
Remember that high byte points by default to **$0400**.

## Clearing and filling Color-RAM

If you want to provide backward compability between all ROM versions, instead of:

lda #CHARS_COLOR jsr $e544

you should use:

lda #CHARS_COLOR sta $d021 jsr $e536

Unfortunately you will lost 3 bytes…

## Coloring chars

Now it's easy way to transform screen pointers to color RAM pointers using

jsr $ea24

New pointers are putted in **$f3** (low) and **$f4** (high)

## Clearing line/chars

Clearing one line of the screen is easy by calling:

ldy #39 jsr $ea0a

It's worth to use it if **$d1** and **$d2** registers are filled by proper values.

## Scrolling screen up

It's easy. Just call:

jsr $e9c8

## Fast method for scrolling up screen at $0400

The is the shortest routine I was able to come up with.
It generates unrolled speecode (LDA/STA) and uses $e9f0 calls (see [Drawing chars](https://codebase.c64.org#drawing_chars) section above) and $b699 (also mentioned).
I used it in: [Agricultural fields from above](https://csdb.dk/release/?id=250200)

```
LINES=24
   lda #HIGH_PTR_OF_ROUTINE
   sta $36
   
;number of lines is also
;low byte of routine   
   ldx #LINES-1
   stx $35
---   
   jsr $e9f0 ;get screen pointers at $d1/$d2
   ldy #0
--   
   lda #$ad
   sta ($35),y
   iny
   lda $d1
   sta ($35),y
   iny
   lda $d2
   sta ($35),y
   iny
   
   lda #$8d
   sta ($35),y
   iny   
   lda $d1
   clc
   adc #40
   sta ($35),y
   iny
   lda $d2
   adc #0
   sta ($35),y  
   iny
   
   inc $d1
   bne +
   inc $d2
+   
   cpy #240
   bne --
   tya
   
;increment $35/$36 by 240   
   jsr $b699
  
   dex
   bpl ---
   
   lda #$60
   sta HIGH_PTR_OF_ROUTINE+LINES*40*6+LINES-1
      
```
Now just call:

jsr HIGH_PTR_OF_ROUTINE*256+LINES-1

## Scrolling screen down

Scrolling screen down is a bit more difficult.

ldx #24 - dex ;get screen pointers ;for line 23 ;and store them in $ac/$ad jsr $e9f0 lda $d1 sta $ac lda $d2 sta $ad inx ;get screen pointers ;for line 24 jsr $e9f0 ;copy memory ;chars from $ac/$ad->$d1/$d2 ;colors from $ae/$af->$f3/$f4 jsr $e9cf dex bpl - ;clear bottom line ldy #39 jsr $ea0a

## Scrolling screen left

Let's start real roller-coaster ride!

;copy KERNAL ;from $ffxx to $00xx ;xx means that we don't know ;what values are store at low byte ;pointers ($5b/$59) ldx #-1 stx $5a stx $58 jsr $a3e8 ;put some RTS ;we don't need rest ;of the routine lda #$60 sta $e777 ;now we can disable KERNAL lda #$35 sta $01 ;scroll left ldx #24 - ldy #0 ;get screen pointers jsr $e9f0 ;get color pointers jsr $ea24 ;copy memory backwards jsr $e762 dex bpl -

## Scrolling screen right

Now we should change direction and start another roller-coaster right, I mean ride:)

;copy KERNAL ;from $ffxx to $00xx ;xx means that we don't know ;what values are store at low byte ;pointers ($5b/$59) ldx #-1 stx $5a stx $58 jsr $a3e8 ;put some RTS ;we don't need rest ;of the routine lda #$60 sta $e81f ;now we can disable KERNAL lda #$35 sta $01 ;scroll left ldx #24 - ldy #0 ;get screen pointers jsr $e9f0 ;get color pointers jsr $ea24 ;column 38 is ;the first cell ;which copy starts ldy #38 ;copy memory forwards jsr $e80a dex bpl -

I used theses scrolling routines in: [Undersea Adventures](https://csdb.dk/release/?id=250194) and [Leaf ain't a game](https://csdb.dk/release/?id=250204).

## Delays

1 ms delay:

jsr $eeb3

2 s delay (source: [http://www.sizecoding.org/wiki/Commodore_64#Delay_.7E_2_Seconds](http://www.sizecoding.org/wiki/Commodore_64#Delay_.7E_2_Seconds)):

jsr $fd68

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $f345
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $e6fc
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $abba
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $b785
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $f498
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $fe0d
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $b8f7
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $a687
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lax #0
   tay
   jsr $af87
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $fb9b
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $a60e
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $bce9
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $bf0c
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $a826
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $bfb8
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $fe1c
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $e688
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $fb8e
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $bc0f
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $bc00
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $b977
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $fcdb
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $a8fc
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $b699
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $b5f8
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $b6cb
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $a8c5
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldx #HOW_MANY_PAGES
   lda #<(Source+(HOW_MANY_PAGES-1)*256)
   sta $5a
   lda #>(Source+(HOW_MANY_PAGES-1)*256)
   sta $5b
   lda #<(Destination+(HOW_MANY_PAGES-1)*256)
   sta $58
   lda #>(Destination+(HOW_MANY_PAGES-1)*256)
   sta $59  
   jsr $a3e8
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda #<Source
   sta $22
   lda #>Source
   sta $23

   lda #<Dest
   sta $35
   lda #>Dest
   sta $36

   lda #HOW_MANY_HALF_PAGES ; HALF_PAGE=128 bytes
   sta $02
-
   lda #$80
   jsr $b68c
   lda #$80
   jsr $b5f8
   dec $02
   bne -
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $e416
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda #$00
   sta $2b
   lda #$20
   sta $2c
- 
   jsr $e416
   lda $2c
   bpl -
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda #$18
   sta $d018
   sta $2c
- 
   jsr $e416
   lda $2c
   bpl -
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda #$00
   sta $2b
   lda #$20
   sta $2c
- 
   ldy #0
   lda #VALUE
   jsr $e419
   lda $2c
   bpl -
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldx #X
   lda #3
   sbx #0      ;x AND 3
   eor #$a9    ;A^mask=%x0x0x0x0
;at bd36 we have
;60 10 0E A9
;rolled and masked
;80 20 08 02
   rla $bd36,x 
   ora (BitmapDataL),y
   sta (BitmapDataL),y
```

### Snippet Codice (Dialetto: ACME)

```assembly
*=$ALIGNED_ADDRESS-2
   bvc +

Sprite
!fill 255,63   

+
;the rest of the code
```

### Snippet Codice (Dialetto: ACME)

```assembly
*=$ALIGNED_ADDRESS-3
   jmp +

Sprite
!fill 255,63   

+
;the rest of the code
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldx #row
   jsr $e9f0
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda #char
   ldy #column
   sta ($d1),y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda #CHARS_COLOR
   jsr $e544
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lda #CHARS_COLOR
   sta $d021
   jsr $e536
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $ea24
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldy #39
   jsr $ea0a
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $e9c8
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LINES=24

   lda #HIGH_PTR_OF_ROUTINE
   sta $36
   
;number of lines is also
;low byte of routine   

   ldx #LINES-1
   stx $35
---   
   jsr $e9f0 ;get screen pointers at $d1/$d2

   ldy #0
--   
   lda #$ad
   sta ($35),y
   iny
   lda $d1
   sta ($35),y
   iny
   lda $d2
   sta ($35),y
   iny
   
   lda #$8d
   sta ($35),y
   iny   
   lda $d1
   clc
   adc #40
   sta ($35),y
   iny
   lda $d2
   adc #0
   sta ($35),y  
   iny
   
   inc $d1
   bne +
   inc $d2
+   
   cpy #240
   bne --

   tya
   
;increment $35/$36 by 240   
   jsr $b699
  
   dex
   bpl ---
   
   lda #$60
   sta HIGH_PTR_OF_ROUTINE+LINES*40*6+LINES-1
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr HIGH_PTR_OF_ROUTINE*256+LINES-1
```

### Snippet Codice (BASIC)

```basic
ldx #24
-   
   dex

;get screen pointers
;for line 23
;and store them in $ac/$ad

   jsr $e9f0

   lda $d1
   sta $ac
   lda $d2
   sta $ad 
   inx

;get screen pointers
;for line 24

   jsr $e9f0

;copy memory
;chars from $ac/$ad->$d1/$d2
;colors from $ae/$af->$f3/$f4

   jsr $e9cf
   dex
   bpl -
   
;clear bottom line   

   ldy #39
   jsr $ea0a
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
;copy KERNAL
;from $ffxx to $00xx
;xx means that we don't know
;what values are store at low byte
;pointers ($5b/$59) 

   ldx #-1
   stx $5a
   stx $58
   jsr $a3e8
   
;put some RTS
;we don't need rest
;of the routine

   lda #$60
   sta $e777
   
;now we can disable KERNAL   

   lda #$35
   sta $01

;scroll left   

   ldx #24
-   
   ldy #0

;get screen pointers   

   jsr $e9f0

;get color pointers   

   jsr $ea24

;copy memory backwards

   jsr $e762  

   dex 
   bpl -
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
;copy KERNAL
;from $ffxx to $00xx
;xx means that we don't know
;what values are store at low byte
;pointers ($5b/$59) 

   ldx #-1
   stx $5a
   stx $58
   jsr $a3e8
   
;put some RTS
;we don't need rest
;of the routine

   lda #$60
   sta $e81f
   
;now we can disable KERNAL   

   lda #$35
   sta $01

;scroll left   

   ldx #24
-   
   ldy #0

;get screen pointers   

   jsr $e9f0

;get color pointers   

   jsr $ea24

;column 38 is
;the first cell
;which copy starts

   ldy #38
 
;copy memory forwards  

   jsr $e80a  

   dex 
   bpl -
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $eeb3
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
jsr $fd68
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asizecoding](https://codebase.c64.org/doku.php?id=base%3Asizecoding)*


### Collegamenti e Riferimenti Hardware
- **$D021 (Background Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d021).
- **$D018 (Memory Setup Register)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d018).
