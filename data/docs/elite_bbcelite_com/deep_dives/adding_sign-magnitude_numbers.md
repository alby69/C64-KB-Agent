---
title: Adding sign-magnitude numbers
source_url: https://elite.bbcelite.com/deep_dives/adding_sign-magnitude_numbers.html
category: deep-dive
topics:
- memory management
- basic
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
- SID
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Adding sign-magnitude numbers

## Doing basic arithmetic with sign-magnitude numbers

Elite uses a lot of sign-magnitude numbers, where the sign bit is stored separately from an unsigned magnitude. The classic examples are the ship coordinates at INWK, which are stored in 24 bits as (x_sign x_hi x_lo), where bit 7 of x_sign is the sign, and (x_hi x_lo) is the coordinate value.

This means that when we come to do arithmetic on sign-magnitude numbers, we have to write our own routines for everything from addition and subtraction to multiplication and division, as the standard two's complement maths that the 6502 supports won't work.

For example, let's try adding 127 and -1 as sign-magnitude numbers, first using sign-magnitude arithmetic. 127 is 01111111 as a sign-magnitude number, while -1 is 10000001, and:

```
  127 + -1 = 0 1111111 + 1 0000001
           = 0 1111111 - 0 0000001
           = 0 1111110
           = 126
```
						However, if we use the built-in ADC instruction, we get the following:

```
  127 + -1 = 01111111 + 10000001
           = 00000000
```
						which is a completely different result.

Elite's [ADD](https://elite.bbcelite.com/cassette/main/subroutine/add.html) routine implements sign-magnitude addition using the following algorithm. We want to add A and S, so:

- If both A and S are positive, just add them as normal
- If both A and S are negative, then add them and make sure the result is negative
- If A and S have different signs, then we can use the absolute values of A and S to work out the sum, as follows:
								- Subtract the smaller absolute value from the larger absolute value
- Give the answer the same sign as the argument with the larger absolute value
 

To see why this works, try visualising a number line containing the two numbers A and S, with one to the left of zero and one to the right. Adding the numbers is a bit like moving the number with the larger absolute value towards zero on the number line, moving it by the amount of the smaller absolute number; so it's like subtracting the smaller absolute value from the larger one. You can also see that the sum of the two numbers will be on the same side of zero as the number that is furthest from zero, so that's why the answer should have the same sign as the argument with the larger absolute value.

We can implement these steps like this:

- If |A| = |S|, then the result is 0
- If |A| > |S|, then the result is |A| - |S|, with the sign set to the same sign as A
- If |S| > |A|, then the result is |S| - |A|, with the sign set to the same sign as S

So that's what we do in the ADD routine to implement 16-bit sign-magnitude addition. The same basic approach can be found in lots of Elite's arithmetic routines: check the signs of the two operands, then add, subtract, divide or multiply as appropriate, and finally set the sign bit correctly.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
127 + -1 = 0 1111111 + 1 0000001
           = 0 1111111 - 0 0000001
           = 0 1111110
           = 126
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
127 + -1 = 01111111 + 10000001
           = 00000000
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/adding_sign-magnitude_numbers.html](https://elite.bbcelite.com/deep_dives/adding_sign-magnitude_numbers.html)*
