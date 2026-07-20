---
title: Using a byte as bitcounter and value container simultaneously
source_url: https://codebase.c64.org/doku.php?id=base%3Ausing_a_byte_as_bitcounter_and_value_container_at_the_same_time
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Using a byte as bitcounter and value container simultaneously

base:using_a_byte_as_bitcounter_and_value_container_at_the_same_time

                # Using a byte as bitcounter and value container simultaneously

This code was posted by Enthusi on the CSDb forum. Inventor uknown. The idea is to use the byte (in $bd in this case) as a “counter” counting eight times at the same time as it is filled with each of the bits of a byte value. This way you don't need to use extra registers to keep track of the eight iterations.

The getbit routine is not included here since this article is intended to demonstrate a general concept, regardless of how the actual getbit routine is designed in each actual case. For a more elaborate example, see [Decoding bitstreams](https://codebase.c64.org/doku.php?id=base:decoding_bitstreams).

getbyte: lda #$01 ;This bit will be rotated to carry when a complete byte is read. sta $bd loop: jsr getbit ;This subroutine reads one bit from the datastream and stores it in the carry flag. rol $bd bcc loop ;As long as the bit doesn't roll off the byte (after 8 loops), do the loop lda $bd rts

From IRC: Krillye: franticHT: that “trick” is pretty common with serial transfer routines as well [in addition to tape loading routines], and some maths routines

base/using_a_byte_as_bitcounter_and_value_container_at_the_same_time.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`getbyte`** (unknown): No description available
- **`loop`** (unknown): No description available

```assembly
getbyte:
	lda #$01   ;This bit will be rotated to carry when a complete byte is read.
	sta $bd

loop:
	jsr getbit ;This subroutine reads one bit from the datastream and stores it in the carry flag.
	rol $bd
	bcc loop   ;As long as the bit doesn't roll off the byte (after 8 loops), do the loop
	lda $bd
	rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ausing_a_byte_as_bitcounter_and_value_container_at_the_same_time](https://codebase.c64.org/doku.php?id=base%3Ausing_a_byte_as_bitcounter_and_value_container_at_the_same_time)*
