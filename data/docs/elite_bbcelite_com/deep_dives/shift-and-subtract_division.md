---
title: Shift-and-subtract division
source_url: https://elite.bbcelite.com/deep_dives/shift-and-subtract_division.html
category: manual
topics:
- basic
difficulty: intermediate
language: basic
hardware: []
related: []
scraped_at: '2026-07-20'
---

# Shift-and-subtract division

## The main algorithm behind Elite's many division routines

Elite implements division in routines like [TIS2](https://elite.bbcelite.com/cassette/main/subroutine/tis2.html) using the shift-and-subtract algorithm (an approach which is used in other division routines, such as [TIS1](https://elite.bbcelite.com/cassette/main/subroutine/tis1.html) and [DVID4](https://elite.bbcelite.com/cassette/main/subroutine/dvid4.html)). This is similar in concept to the shift-and-add algorithm used to implement multiplication in routines like [MULT1](https://elite.bbcelite.com/cassette/main/subroutine/mult1.html), but it's essentially the reverse of that algorithm.

In the same way that shift-and-add implements a binary version of the manual long multiplication process, shift-and-subtract implements long division. We shift bits out of the left end of the number being divided (A), subtracting the largest possible multiple of the divisor (Q) after each shift; each bit of A where we can subtract Q gives a 1 the answer to the division, otherwise it gives a 0.

In pseudo-code, the algorithm to calculate T = P / Q (with remainder A) looks like this:

```
  T = 0
  A = 0
  for x = 7 to 0
    A = A << 1
    A(bit 0) = P(bit x)
    if A >= Q then
      A = A - Q
      T(bit x) = 1
```
						This is the algorithm implemented in TIS2, except we save space (and make things much more confusing) by using A for both the number being divided and the remainder, building the answer in T instead of P, and using set bits in T to implement the loop counter. The basic idea of shifting and subtracting is the same, though.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
T = 0
  A = 0
  for x = 7 to 0
    A = A << 1
    A(bit 0) = P(bit x)
    if A >= Q then
      A = A - Q
      T(bit x) = 1
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/shift-and-subtract_division.html](https://elite.bbcelite.com/deep_dives/shift-and-subtract_division.html)*
