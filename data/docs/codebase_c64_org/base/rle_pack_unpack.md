---
title: RLE Toolkit for CC65 v 1.0
source_url: https://codebase.c64.org/doku.php?id=base%3Arle_pack_unpack
category: tool
topics:
- sprite programming
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
related:
- sprite-programming
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# RLE Toolkit for CC65 v 1.0

### Table of Contents

# RLE Toolkit for CC65 v 1.0

By MagerValp.

The homepage and sources to this Toolkit is available [here](http://www.paradroid.net/rle/). Check that page for potential updates to this code. A copy of the source package (of v1.0) is also available for download right here from [codebase64](https://codebase.c64.org/lib/exe/fetch.php?media=base:rle-toolkit-1.0.zip). 

RLE Toolkit consists of:

- a small RLE compression library for CC65
- commandline utilities to pack and unpack files
- sample code that shows you how to use it

# Compression API

There are two functions, rle_pack and rle_unpack, that can be called from both C and assembler.

C interface:

unsigned int __fastcall__ rle_pack(unsigned char *dest, unsigned char *src, unsigned int length); unsigned int __fastcall__ rle_unpack(unsigned char *dest, unsigned char *src);

Assembler interface:

.import rle_pack .importzp src, dest .import srclen, destlen ; set source pointer lda #<sourcedata sta src lda #>sourcedata sta src + 1 ; set destination pointer lda #<destbuffer sta dest lda #>destbuffer sta dest + 1 ; set length of source data when packing ; parameter is ignored when unpacking lda #<datalen sta srclen lda #>datalen sta srclen + 1 jsr rle_pack or jsr rle_unpack ; length of output is returned in destlen

# Packed stream format

When two or more consecutive bytes are identical, they are replaced by <BYTE> <BYTE> <COUNT>. A COUNT of 0 indicates End Of Stream. A COUNT of 1 indicates that two bytes should be written, a COUNT of 2 indicates three bytes, and so on.

# Commandline tools

rlepack infile outfile rleunpack infile outfile

Self explanatory. Right?

# The Routines

## rle.h

/* Pack data. Returns the number of bytes written to destination. */ unsigned int __fastcall__ rle_pack(unsigned char *dest, const unsigned char *src, unsigned int length); /* Unpack data. Returns the number of unpacked bytes. */ unsigned int __fastcall__ rle_unpack(unsigned char *dest, const unsigned char *src);

## rle.s

; Routines for packing and unpacking run length encoded byte streams ; ; When two or more consecutive bytes are identical, they are replaced by ; <BYTE> <BYTE> <COUNT>. A COUNT of 0 indicates End Of Stream. A COUNT ; of 1 indicates that two bytes should be written, a COUNT of 2 indicates ; three bytes, and so on. .export rle_read, rle_store .exportzp src, dest .export lastbyte .export destlen .importzp ptr1, ptr2 .zeropage src = ptr1 ; borrow cc65's temp pointers dest = ptr2 .bss lastbyte: .res 1 ; last byte read destlen: .res 2 ; number of bytes written .code ; read a byte and increment source pointer rle_read: lda (src),y inc src bne :+ inc src + 1 : rts ; write a byte and increment destination pointer rle_store: sta (dest),y inc dest bne :+ inc dest + 1 : inc destlen bne :+ inc destlen + 1 : rts

## rlepack.s

.export _rle_pack, rle_pack .import rle_store, rle_read .importzp src, dest .import lastbyte .import destlen .import popax .bss srclen: .res 2 ; length of source data .code ; cc65 interface to rle_pack ; unsigned int __fastcall__ rle_pack(unsigned char *dest, unsigned char *src, unsigned int length); _rle_pack: sta srclen ; save length arg stx srclen + 1 jsr popax ; get src arg sta src stx src + 1 jsr popax ; get dest arg sta dest stx dest + 1 jsr rle_pack ; execute lda destlen ; return length ldx destlen + 1 rts ; run length encode a stream rle_pack: ldy #0 sty destlen ; reset the byte counter sty destlen + 1 jsr rle_read ; read the first byte sta lastbyte ; save for reference jsr rle_store ; store it jsr @decsrclen ; decrease source count beq @end ; if you're trying to pack a single byte, this the end @pack: jsr rle_read ; grab a byte cmp lastbyte ; same as last byte? beq @rle ; then count bytes and store run length sta lastbyte ; save for reference jsr rle_store ; store byte jsr @decsrclen ; decrease source count bne @pack ; next @end: lda lastbyte ; store last byte... jsr rle_store lda #0 ; ...with a 0 count as the terminator jsr rle_store rts ; done @rle: ldx #1 ; start with a count of 1 jsr @decsrclen beq @rleend @rlenext: jsr rle_read ; grab a byte cmp lastbyte ; make sure it's the same bne @newbyte ; no, then terminate inx ; inc counter beq @stop ; overflow? jsr @decsrclen ; check for end of data bne @rlenext @rleend: ; end of data lda lastbyte ; store double byte jsr rle_store txa ; and counter jsr rle_store jmp @end @stop: ; overflow lda lastbyte ; store the double byte jsr rle_store lda #$ff ; $ff as the byte count jsr rle_store inx ; start over with a counter of 1 jsr @decsrclen beq @rleend bne @rlenext @newbyte: ; new byte detected pha ; save lda lastbyte ; store double byte jsr rle_store txa ; and counter jsr rle_store pla ; restore new byte sta lastbyte ; save for reference jsr rle_store ; store it jsr @decsrclen ; data left? bne @pack ; yep, pack beq @end ; nope, end ; decrease number of bytes left, return 0 when done @decsrclen: lda srclen bne :+ dec srclen + 1 : sec sbc #1 sta srclen ora srclen + 1 rts

## rleunpack.s

.export _rle_unpack, rle_unpack .import rle_store, rle_read .importzp src, dest .import lastbyte .import destlen .import popax .code ; cc65 interface to rle_unpack ; unsigned int __fastcall__ rle_unpack(unsigned char *dest, unsigned char *src); _rle_unpack: sta src ; save src arg stx src + 1 jsr popax ; get dest arg sta dest stx dest + 1 jsr rle_unpack ; execute lda destlen ; return length ldx destlen + 1 rts ; unpack a run length encoded stream rle_unpack: ldy #0 sty destlen ; reset byte counter sty destlen + 1 jsr rle_read ; read the first byte sta lastbyte ; save as last byte jsr rle_store ; store @unpack: jsr rle_read ; read next byte cmp lastbyte ; same as last one? beq @rle ; yes, unpack sta lastbyte ; save as last byte jsr rle_store ; store jmp @unpack ; next @rle: jsr rle_read ; read byte count tax beq @end ; 0 = end of stream lda lastbyte @read: jsr rle_store ; store X bytes dex bne @read beq @unpack ; next @end: rts

## test.c

And finally, a test program (for the cc65 compiler).

```
/*
Pack data to a buffer, unpack and compare with original. If source and
destination are identical, everything works. Simple.
*/
#include <stdio.h>
#include <string.h>
#include "rle.h"
// number of bytes to pack
#define DATASIZE 1000
// source
#define SRC 0x0400
// destination
#define DEST 0x4400
// buffer, worst case should be DATASIZE * 1.5 + 2
#define BUFFER 0xc000
#define BUFSIZE 0x1000
void main(void) {
  unsigned int packlen, unpacklen, diffcount, i;
  unsigned char *src, *dest, *buffer;
  src = (unsigned char *) SRC;
  dest = (unsigned char *) DEST;
  buffer = (unsigned char *) BUFFER;
  // fill with 0x55 to see what gets written
  memset(buffer, 0x55, BUFSIZE);
  memset(dest, 0x55, DATASIZE);
  // pack src to buffer
  packlen = rle_pack(buffer, src, DATASIZE);
  // unpack buffer to dest
  unpacklen = rle_unpack(dest, buffer);
  // check differences
  diffcount = 0;
  for (i = 0; i < DATASIZE; ++i) {
    if (*src++ != *dest++) {
      ++diffcount;
    }
  }
  // print statistics
  printf("Packed %d bytes to %d bytes\n", DATASIZE, packlen);
  printf("Unpacked to %d bytes\n", unpacklen);
  printf("%d bytes differ\n", diffcount);
}
```
## Makefile

Example makefile just to show how this stuff can be built. In any case, don't forget that you can download the whole package at MagerValp's site - [http://www.paradroid.net/rle/](http://www.paradroid.net/rle/).

ARGET=c64 CC=cl65 AS=ca65 LD=cl65 AR=ar65 C1541=c1541 CFLAGS=-Oirs -t $(TARGET) AFLAGS= %.o: %.c $(CC) -c $(CFLAGS) $< %.o: %.s $(AS) $(AFLAGS) $< all: rle.lib test.prg RLEOBJS = \ rle.o \ rlepack.o \ rleunpack.o TESTOBJS= \ test.o \ rle.lib rle.lib: $(RLEOBJS) $(AR) a $@ $^ test.prg: $(TESTOBJS) $(LD) -m test.map -Ln test.lab -t $(TARGET) -o test.prg $(AFLAGS) $^ .PHONY: clean distclean clean: rm -f *.o rle.lib rm -f test.prg test.map test.lab distclean: clean rm -f *~

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`unsigned`** (unknown): No description available

```assembly
unsigned int __fastcall__ rle_pack(unsigned char *dest, unsigned char *src, unsigned int length);


  unsigned int __fastcall__ rle_unpack(unsigned char *dest, unsigned char *src);
```

### Snippet Codice (BASIC)

```basic
.import rle_pack
	.importzp src, dest
	.import srclen, destlen

	; set source pointer
	lda #<sourcedata
	sta src
	lda #>sourcedata
	sta src + 1

	; set destination pointer
	lda #<destbuffer
	sta dest
	lda #>destbuffer
	sta dest + 1

	; set length of source data when packing
	; parameter is ignored when unpacking
	lda #<datalen
	sta srclen
	lda #>datalen
	sta srclen + 1

	jsr rle_pack

	  or

	jsr rle_unpack


	; length of output is returned in destlen
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
rlepack infile outfile

  rleunpack infile outfile
```

### Snippet Codice (BASIC)

```basic
/* Pack data. Returns the number of bytes written to destination. */
unsigned int __fastcall__ rle_pack(unsigned char *dest, const unsigned char *src, unsigned int length);

/* Unpack data. Returns the number of unpacked bytes. */
unsigned int __fastcall__ rle_unpack(unsigned char *dest, const unsigned char *src);
```

### Snippet Codice (BASIC)

```basic
; Routines for packing and unpacking run length encoded byte streams
;
; When two or more consecutive bytes are identical, they are replaced by
; <BYTE> <BYTE> <COUNT>. A COUNT of 0 indicates End Of Stream. A COUNT
; of 1 indicates that two bytes should be written, a COUNT of 2 indicates
; three bytes, and so on.


  	.export rle_read, rle_store
  	.exportzp src, dest
	.export lastbyte
	.export destlen


	.importzp ptr1, ptr2


	.zeropage

src		= ptr1		; borrow cc65's temp pointers
dest		= ptr2


	.bss

lastbyte:	.res 1		; last byte read
destlen:	.res 2		; number of bytes written


	.code


; read a byte and increment source pointer
rle_read:
	lda (src),y
	inc src
	bne :+
	inc src + 1
:	rts


; write a byte and increment destination pointer
rle_store:
	sta (dest),y
	inc dest
	bne :+
	inc dest + 1
:	inc destlen
	bne :+
	inc destlen + 1
:	rts
```

### Snippet Codice (BASIC)

```basic
.export _rle_pack, rle_pack


	.import rle_store, rle_read
	.importzp src, dest
	.import lastbyte
	.import destlen

	.import popax


	.bss

srclen:		.res 2		; length of source data


	.code


; cc65 interface to rle_pack
; unsigned int __fastcall__ rle_pack(unsigned char *dest, unsigned char *src, unsigned int length);
_rle_pack:
	sta srclen		; save length arg
	stx srclen + 1
	jsr popax		; get src arg
	sta src
	stx src + 1
	jsr popax		; get dest arg
	sta dest
	stx dest + 1
	jsr rle_pack		; execute
	lda destlen		; return length
	ldx destlen + 1
	rts


; run length encode a stream
rle_pack:
	ldy #0
	sty destlen		; reset the byte counter
	sty destlen + 1
	jsr rle_read		; read the first byte
	sta lastbyte		; save for reference
	jsr rle_store		; store it
	jsr @decsrclen		; decrease source count
	beq @end		; if you're trying to pack a single byte, this the end
@pack:
	jsr rle_read		; grab a byte
	cmp lastbyte		; same as last byte?
	beq @rle		; then count bytes and store run length
	sta lastbyte		; save for reference
	jsr rle_store		; store byte
	jsr @decsrclen		; decrease source count
	bne @pack		; next
@end:
	lda lastbyte		; store last byte...
	jsr rle_store
	lda #0			; ...with a 0 count as the terminator
	jsr rle_store
	rts			; done
@rle:
	ldx #1			; start with a count of 1
	jsr @decsrclen
	beq @rleend
@rlenext:
	jsr rle_read		; grab a byte
	cmp lastbyte		; make sure it's the same
	bne @newbyte		; no, then terminate
	inx 			; inc counter
	beq @stop		; overflow?
	jsr @decsrclen		; check for end of data
	bne @rlenext
@rleend:			; end of data
	lda lastbyte		; store double byte
	jsr rle_store
	txa			; and counter
	jsr rle_store
	jmp @end
@stop:	    			; overflow
	lda lastbyte		; store the double byte
	jsr rle_store
	lda #$ff		; $ff as the byte count
	jsr rle_store
	inx			; start over with a counter of 1
	jsr @decsrclen
	beq @rleend
	bne @rlenext
@newbyte:			; new byte detected
	pha			; save
	lda lastbyte		; store double byte
	jsr rle_store
	txa			; and counter
	jsr rle_store
	pla			; restore new byte
	sta lastbyte		; save for reference
	jsr rle_store		; store it
	jsr @decsrclen		; data left?
	bne @pack		; yep, pack
	beq @end		; nope, end
; decrease number of bytes left, return 0 when done
@decsrclen:
	lda srclen
	bne :+
	dec srclen + 1
:	sec
	sbc #1
	sta srclen
	ora srclen + 1
	rts
```

### Snippet Codice (BASIC)

```basic
.export _rle_unpack, rle_unpack


	.import rle_store, rle_read
	.importzp src, dest
	.import lastbyte
	.import destlen

	.import popax


	.code


; cc65 interface to rle_unpack
; unsigned int __fastcall__ rle_unpack(unsigned char *dest, unsigned char *src);
_rle_unpack:
	sta src			; save src arg
	stx src + 1
	jsr popax		; get dest arg
	sta dest
	stx dest + 1
	jsr rle_unpack		; execute
	lda destlen		; return length
	ldx destlen + 1
	rts


; unpack a run length encoded stream
rle_unpack:
	ldy #0
	sty destlen		; reset byte counter
	sty destlen + 1
	jsr rle_read		; read the first byte
	sta lastbyte		; save as last byte
	jsr rle_store		; store
@unpack:
	jsr rle_read		; read next byte
	cmp lastbyte		; same as last one?
	beq @rle		; yes, unpack
	sta lastbyte		; save as last byte
	jsr rle_store		; store
	jmp @unpack		; next
@rle:
	jsr rle_read		; read byte count
	tax
	beq @end		; 0 = end of stream
	lda lastbyte
@read:
	jsr rle_store		; store X bytes
	dex
	bne @read
	beq @unpack		; next
@end:
	rts
```

### Snippet Codice (BASIC)

```basic
/*

Pack data to a buffer, unpack and compare with original. If source and
destination are identical, everything works. Simple.

*/

#include <stdio.h>
#include <string.h>
#include "rle.h"


// number of bytes to pack
#define DATASIZE 1000
// source
#define SRC 0x0400
// destination
#define DEST 0x4400
// buffer, worst case should be DATASIZE * 1.5 + 2
#define BUFFER 0xc000
#define BUFSIZE 0x1000


void main(void) {
  unsigned int packlen, unpacklen, diffcount, i;
  unsigned char *src, *dest, *buffer;

  src = (unsigned char *) SRC;
  dest = (unsigned char *) DEST;
  buffer = (unsigned char *) BUFFER;

  // fill with 0x55 to see what gets written
  memset(buffer, 0x55, BUFSIZE);
  memset(dest, 0x55, DATASIZE);

  // pack src to buffer
  packlen = rle_pack(buffer, src, DATASIZE);
  // unpack buffer to dest
  unpacklen = rle_unpack(dest, buffer);

  // check differences
  diffcount = 0;
  for (i = 0; i < DATASIZE; ++i) {
    if (*src++ != *dest++) {
      ++diffcount;
    }
  }

  // print statistics
  printf("Packed %d bytes to %d bytes\n", DATASIZE, packlen);
  printf("Unpacked to %d bytes\n", unpacklen);
  printf("%d bytes differ\n", diffcount);
}
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`all`** (unknown): No description available
- **`clean`** (unknown): No description available
- **`distclean`** (unknown): No description available

```assembly
ARGET=c64
CC=cl65
AS=ca65
LD=cl65
AR=ar65
C1541=c1541
CFLAGS=-Oirs -t $(TARGET)
AFLAGS=


%.o: %.c
	$(CC) -c $(CFLAGS) $<

%.o: %.s
	$(AS) $(AFLAGS) $<


all: rle.lib test.prg


RLEOBJS = \
	rle.o \
	rlepack.o \
	rleunpack.o

TESTOBJS= \
	test.o \
	rle.lib


rle.lib: $(RLEOBJS)
	$(AR) a $@ $^


test.prg: $(TESTOBJS)
	$(LD) -m test.map -Ln test.lab -t $(TARGET) -o test.prg $(AFLAGS) $^


.PHONY: clean distclean

clean:
	rm -f *.o rle.lib
	rm -f test.prg test.map test.lab


distclean: clean
	rm -f *~
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Arle_pack_unpack](https://codebase.c64.org/doku.php?id=base%3Arle_pack_unpack)*
