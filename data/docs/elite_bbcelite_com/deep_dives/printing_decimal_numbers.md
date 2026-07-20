---
title: Printing decimal numbers
source_url: https://elite.bbcelite.com/deep_dives/printing_decimal_numbers.html
category: deep-dive
topics:
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CPU
related:
- sid-registers
- sound-programming
- memory-map
- kernal-routines
- music-player
scraped_at: '2026-07-20'
---

# Printing decimal numbers

## How to print big decimal numbers with decimal points and padding

Elite prints out a lot of numbers, all of them in decimal (hexadecimal and binary numbers are used internally, but we never see them displayed). The [BPRNT](https://elite.bbcelite.com/cassette/main/subroutine/bprnt.html) routine can print out numbers from 0.1 to 4,294,967,295 (32 set bits), though as the highest figure in the game is the cash pot and that stores the cash amount * 10, the highest figure BPRNT might ever be asked to display is 429,496,729.5 - the biggest cash pot we can have.

As an example, the Market Price screen contains numbers in various formats, some with decimal points and others without:

![The Market Price screen in BBC Micro Elite](https://elite.bbcelite.com/images/cassette/market_prices.png) 

						Let's first look at the algorithm for printing decimal numbers, as all our numbers are stored in binary, and then we'll look at the BPRNT implementation of it.

## Printing decimal numbers

													 ------------------------

						The algorithm is relatively simple, but it looks fairly complicated because we're dealing with 32-bit numbers.

To see how it works, let's first consider a simple example with fewer digits. Let's say we want to print out the following number to three digits:

567

First we subtract 100 repeatedly until we can't do it any more, counting how many times we can do this:

567 - 100 - 100 - 100 - 100 - 100 = 67

Not surprisingly, we can subtract it 5 times, so our first digit is 5. Now we multiply the remaining number by 10 to get 670, and repeat the process:

670 - 100 - 100 - 100 - 100 - 100 - 100 = 70

We subtracted 100 6 times, so the second digit is 6. Now to multiply by 10 again to get 700 and repeat the process:

700 - 100 - 100 - 100 - 100 - 100 - 100 - 100 = 0

So the third digit is 7 and we are done.

## The BPRNT routine

													 -----------------

						The BPRNT subroutine does exactly this in its main loop at TT36, except that instead of having a three-digit number and subtracting 100, we have up to an 11-digit number and subtract 10 billion each time (as 10 billion has 11 digits), using 32-bit arithmetic and an overflow byte, and that's where the complexity comes in.

Let's look at the above algorithm in more detail. We need to implement it with multi-byte subtraction, which we can do byte-by-byte using the C flag, but we also need to be able to multiply a multi-byte number by 10, which is slightly trickier. Multiplying by 10 isn't directly supported the 6502, but multiplying by 2 is, in the guise of shifting and rotating left, so we can do this to multiply K by 10:

```
  K * 10 = K * (2 + 8)
         = (K * 2) + (K * 8)
         = (K * 2) + (K * 2 * 2 * 2)
```
						And that's essentially what we do in the TT35 subroutine, just with 32-bit numbers with an 8-bit overflow. This doubling process is used quite a few times in the following, so let's look at an example, in which we double the number in K(S 0 1 2 3):

ASL K+3 ROL K+2 ROL K+1 ROL K ROL S

First we use ASL K+3 to shift the least significant byte left (so bit 7 goes to the C flag). Then we rotate the next most significant byte with ROL K+2 (so the C flag goes into bit 0 and bit 7 goes into the C flag), and we repeat this with each byte in turn, until we get to the overflow byte S. This has the effect of shifting the entire five-byte number one place to the left, which doubles it in-place.

Finally, there are three variables that are used as counters in the above loop, each of which gets decremented as we go work our way through the digits. Their starting values are:

| Variable | Description | Starting value | 
|---|---|---|
| XX17 | The maximum number of characters to print in total | Hard-coded to 11 | 
| T | The maximum number of digits that we might end up printing | 11 if there's no decimal point, 10 otherwise | 
| U | The loop number at which we should start printing digits or spaces | Calculated from the U argument to BPRNT | 

We do the loop XX11 times, once for each character that we might print. We start printing characters once we reach loop number U (at which point we print a space if there isn't a digit at that point, otherwise we print the calculated digit). As soon as we have printed our first digit we set T to 0 to indicate that we should print characters for all subsequent loops, so T is effectively a flag for denoting that we're switching from spaces to zeroes for zero values, and decrementing T ensures that we always have at least one digit in the number, even if it's a zero.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
567
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
567 - 100 - 100 - 100 - 100 - 100 = 67
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
670 - 100 - 100 - 100 - 100 - 100 - 100 = 70
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
700 - 100 - 100 - 100 - 100 - 100 - 100 - 100 = 0
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
K * 10 = K * (2 + 8)
         = (K * 2) + (K * 8)
         = (K * 2) + (K * 2 * 2 * 2)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ASL K+3
  ROL K+2
  ROL K+1
  ROL K
  ROL S
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/printing_decimal_numbers.html](https://elite.bbcelite.com/deep_dives/printing_decimal_numbers.html)*
