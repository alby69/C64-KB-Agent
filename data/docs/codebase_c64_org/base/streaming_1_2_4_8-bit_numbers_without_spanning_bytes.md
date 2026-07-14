---
title: Packing bitfields evenly into bytes
source_url: https://codebase.c64.org/doku.php?id=base%3Astreaming_1_2_4_8-bit_numbers_without_spanning_bytes
category: reference
topics:
- memory management
- basic
difficulty: beginner
language: basic
hardware:
- SID
- KERNAL
- BASIC ROM
related:
- sound-programming
- memory-map
- sid-registers
- music-player
- kernal-routines
scraped_at: '2026-07-14'
---

# Packing bitfields evenly into bytes

# Packing bitfields evenly into bytes

(I first used this in my FMV system, around 2005 or so? - White Flame)

As long as you're outputting 1, 2, 4, and 8 bit tokens (not 3 or 5-7 bit), you can keep all the bitfields aligned so they do not span byte boundaries, making the reading simpler. No length tokens need to be added to the stream.

The reader will hold a byte-sized buffer each for reading 1, 2, or 4-bit values. If that buffer is empty upon reading it, pull the next byte from the input stream to refill that particular buffer. Reading 8-bit values comes directly from the input byte stream.

The writer packs only tokens of the same bit length into each byte, creating a new output byte at the end of the stream whenever a new buffer for that bit length is required. The writer remembers where in the stream the various buffer bytes for each bit length resides, adding to it in place until it's full.

Example of writing this arbitrary token stream:

0 1 0 0011 10 1100 10101010 0 11 11 11 0101

0: Allocate a new 1-bit buffer byte in the stream:

.......0

1: Add to the 1-bit buffer byte:

......10

0: And another 0:

.....010

0011: Now we need to output a 4-bit token. Allocate a new buffer byte in the stream for it:

.....010 ....0011

10: Now for a 2-bit token. Alocate a new buffer byte for it:

.....010 ....0011 ......10

1100: Another 4-bit token, goes into its buffer byte:

.....010 11000011 ......10

10101010: Full bytes always go at the end of the stream:

.....010 11000011 ......10 10101010

0: Write into the 1-bit buffer byte:

....0010 11000011 ......10 10101010

11: Write into the 2-bit buffer byte:

....0010 11000011 ....1110 10101010

11: Write into the 2-bit buffer byte:

....0010 11000011 ..111110 10101010

11: Write into the 2-bit buffer byte:

....0010 11000011 11111110 10101010

0101: Since the 4-bit buffer byte is full, create a new byte at the end of the stream for it:

....0010 11000011 11111110 10101010 ....0101

When the specifically 1/2/4/8-bit reads are done in the same order as the writes were, all ordering is preserved.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
0 1 0 0011 10 1100 10101010 0 11 11 11 0101
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.......0
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
......10
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.....010
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.....010 ....0011
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.....010 ....0011 ......10
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.....010 11000011 ......10
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.....010 11000011 ......10 10101010
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
....0010 11000011 ......10 10101010
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
....0010 11000011 ....1110 10101010
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
....0010 11000011 ..111110 10101010
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
....0010 11000011 11111110 10101010
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
....0010 11000011 11111110 10101010 ....0101
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Astreaming_1_2_4_8-bit_numbers_without_spanning_bytes](https://codebase.c64.org/doku.php?id=base%3Astreaming_1_2_4_8-bit_numbers_without_spanning_bytes)*
