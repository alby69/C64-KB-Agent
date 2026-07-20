---
title: Shift-and-add multiplication
source_url: https://elite.bbcelite.com/deep_dives/shift-and-add_multiplication.html
category: manual
topics:
- memory management
- assembly
- basic
difficulty: beginner
language: assembly
hardware:
- SID
- CIA
related:
- sid-registers
- sound-programming
- joystick-reading
- keyboard-handling
- music-player
- cia-registers
scraped_at: '2026-07-20'
---

# Shift-and-add multiplication

## The main algorithm behind Elite's many multiplication routines

Elite implements multiplication using the shift-and-add algorithm. One such example is the [MULT1](https://elite.bbcelite.com/cassette/main/subroutine/mult1.html) routine, which multiplies two 8-bit numbers to give a 16-bit result). Let's take a look at how it does it, as this same technique is used in lots of different multiplication routines throughout the game code (such as [FMLTU](https://elite.bbcelite.com/cassette/main/subroutine/fmltu.html) and [MU11](https://elite.bbcelite.com/cassette/main/subroutine/mu11.html)).

Consider multiplying two example numbers, which we'll call p and a (as this makes it easier to map the following explanation to the code in MULT1):

p * a = %00101001 * a

This is the same as:

p * a = (%00100000 + %00001000 + %00000001) * a

or:

p * a = %00100000 * a + %00001000 * a + %00000001 * a

or:

p * a = a << 5 + a << 3 + a << 0

or, to lay this out in the way we're used to seeing it in school books on long multiplication, if a is made up of binary digits aaaaaaaa, it's the same as:

```
         00101001         p
         aaaaaaaa x       * a
  ---------------
         aaaaaaaa
        00000000
       00000000
      aaaaaaaa
     00000000
    aaaaaaaa
   00000000
  00000000        +
  ---------------
  xxxxxxxxxxxxxxx         -> the result of p * a
```
						In other words, we can work our way through the digits in the first number p and every time there's a 1, we add an a to the result, shifted to the left by the position of that digit.

We could code this into assembly relatively easily, but Elite takes a rather more optimised route. Instead of shifting the number aaaaaaaa to the left for each addition, we can instead shift the entire result to the right, saving the bit that falls off the right end, and add an unshifted value of a. If you think of one of the sums in our longhand version like this:

```
    a7a6a5a4a3a2a1a0
  a7a6a5a4a3a2a1a0   +
```
						then instead of shifting the second number to the left, we can shift the first number to the right and save the rightmost bit, like this:

```
    a7a6a5a4a3a2a1        -> result bit 0 is a0
  a7a6a5a4a3a2a1a0 +
```
						So the routine's approach is to work our way through the digits in the first number p, shifting the result right every time and saving the rightmost bit in the final result, and every time there's a 1 in p, we add another a to the sum.

This is essentially what Elite does in the MULT1 routine, but there is one more tweak that makes the process even more efficient (and even more confusing, especially when you first read through the code). Instead of saving the result bits out into a separate location, we can stick them onto the left end of p, because every time we shift p to the right, we gain a spare bit on the left end of p that we no longer use.

For a simpler version of the above algorithm, take a look at MU11, which multiplies two unsigned numbers.

## Optimised multiplication

													 ------------------------

						The above approach is used in all the multiplication routines in Elite, though sometimes it can be a bit hard to follow. Let look at a particularly knotty example.

The FMLTU routine uses the same basic algorithm as MU11, but because we are only interested in the high byte of the result, we can optimise away a few instructions. Instead of having a loop counter to count the 8 bits in the multiplication, we can instead invert one of the arguments (A in this case, which we then store in P to pull bits off), and then reverse the logic so that ones get skipped and zeroes cause an addition.

Also, when we do the first shift right, we can stick a one into bit 7, so we can keep looping and shifting right until we run out of ones, which is an easy BNE test. This works because we don't have to store the low byte of the result anywhere, so we can just shift P to the right, rather than ROR'ing it as we do in MULT1 - and that lets us do the BNE test, saving few precious instructions in the process.

The result is a really slick, optimised multiplication routine that does a specialised job, at the expense of clarity. To understand the FMLTU routine, first try to understand MULT1, then look at MU11, and finally try FMLTU (I have kept the comments similar so they are easier to compare). And if your eyes aren't crossed by that point, then hats off to you, because this is properly gnarly stuff.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
p * a = %00101001 * a
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
p * a = (%00100000 + %00001000 + %00000001) * a
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
p * a = %00100000 * a + %00001000 * a + %00000001 * a
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
p * a = a << 5 + a << 3 + a << 0
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
00101001         p
         aaaaaaaa x       * a
  ---------------
         aaaaaaaa
        00000000
       00000000
      aaaaaaaa
     00000000
    aaaaaaaa
   00000000
  00000000        +
  ---------------
  xxxxxxxxxxxxxxx         -> the result of p * a
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
a7a6a5a4a3a2a1a0
  a7a6a5a4a3a2a1a0   +
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
a7a6a5a4a3a2a1        -> result bit 0 is a0
  a7a6a5a4a3a2a1a0 +
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/shift-and-add_multiplication.html](https://elite.bbcelite.com/deep_dives/shift-and-add_multiplication.html)*
