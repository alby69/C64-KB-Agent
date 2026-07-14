---
title: Calculating square roots
source_url: https://elite.bbcelite.com/deep_dives/calculating_square_roots.html
category: manual
topics:
- assembly
difficulty: intermediate
language: mixed
hardware:
- CPU
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# Calculating square roots

## The algorithm behind the square root routine

The algorithm used to calculate square roots in routine [LL5](https://elite.bbcelite.com/cassette/main/subroutine/ll5.html) is related to the division algorithm in TIS2 (see the deep dive on [shift-and-subtract division](https://elite.bbcelite.com/shift-and-subtract_division.html) for details), though with a couple of twists. If you think about the division algorithm, it calculates the quotient and remainder from a given dividend and divisor, and the following holds:

dividend = (quotient * divisor) + remainder

The problem of calculating the square root is related to this, except we have the following relationship between the arguments and results, where "number" is the number we want to find the square root of:

number = (root * root) + remainder

So the number we want to find the root of is equivalent to the dividend in the shift-and-subtract algorithm, and instead of the divisor being fixed, we instead build up the root bit by bit and use that in place of the divisor.

When generalised to calculate the n-th root, this approach is called the "shifting nth-root" algorithm, and it is explained in various places on the web by minds more devious than mine. The LL5 routine is an application of the algorithm for n = 2, which is why the number ("dividend") and remainder get shifted by two places in each iteration.

There is a deeper explanation of this exact routine here, though I have to say it makes my head spin more than a little:

[http://6502org.wikidot.com/software-math-sqrt](http://6502org.wikidot.com/software-math-sqrt)

It also turns out that the LL5 routine in Elite is identical to the SQR16 routine from the [March 1983 issue of Personal Computer World](https://archive.org/details/PersonalComputerWorld1983-03/page/186/mode/1up). The same routine also appears in the book [Assembler Routines for the 6502](https://archive.org/details/assembler-routines-for-the-6502/page/126/mode/2up) by Dave Barrow. Thanks to TobyLobster and Rocketeer for some top-tier detective work in tracking this down - see [this thread from Stardot](https://stardot.org.uk/forums/viewtopic.php?p=349165#p349165) for more details.

This algorithm is definitely one for the "must study later" pile...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
dividend = (quotient * divisor) + remainder
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
number = (root * root) + remainder
```

### Snippet Codice (Dialetto: DASM)

#### Routine Identificate:
- **`http`** (unknown): No description available

```assembly
http://6502org.wikidot.com/software-math-sqrt
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/calculating_square_roots.html](https://elite.bbcelite.com/deep_dives/calculating_square_roots.html)*
