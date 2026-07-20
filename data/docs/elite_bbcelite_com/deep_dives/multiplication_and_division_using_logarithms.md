---
title: Multiplication and division using logarithms
source_url: https://elite.bbcelite.com/deep_dives/multiplication_and_division_using_logarithms.html
category: deep-dive
topics: []
difficulty: intermediate
language: none
hardware:
- CPU
related: []
scraped_at: '2026-07-20'
---

# Multiplication and division using logarithms

## Faster multiplication and division routines by using logarithm lookup tables

This deep dive is a work in progress. It covers the logarithm version of the multiplication routines in the advanced versions of Elite, specifically the [FMLTU](https://elite.bbcelite.com/6502sp/main/subroutine/fmltu.html) and [LL28](https://elite.bbcelite.com/6502sp/main/subroutine/ll28.html) routines.

Let's look at the following multiplication of two unsigned 8-bit numbers, returning only the high byte of the result, as implemented in the 6502 Second Processor version of [FMLTU](https://elite.bbcelite.com/6502sp/main/subroutine/fmltu.html):

(A ?) = A * Q

or, to put it another way:

A = A * Q / 256

Let La be the a-th entry in the 16-bit [log](https://elite.bbcelite.com/6502sp/main/variable/log.html)/[logL](https://elite.bbcelite.com/6502sp/main/variable/log.html) (high byte/low byte) table, which means that it has this value:

La = 32 * log(a) * 256

Let Ar be the r-th entry in the [antilog](https://elite.bbcelite.com/6502sp/main/variable/antilog.html) table, which means that it has this value:

Ar = 2^(r / 32 + 8) / 256

These are all logarithms to base 2, so this is true:

a * q = 2 ^ (log(a) + log(q))

Let's reduce this. First, we have the following:

```
  log(a) + log(q) = (log(a) + log(q)) * 1
                  = (log(a) + log(q)) * (32 * 256) / (32 * 256)
                  = (32 * log(a) * 256 + 32 * log(q) * 256) / (32 * 256)
                  = (La + Lq) / (32 * 256)
```
						Now we calculate La + Lq.

1. If La + Lq < 256, then:

```
    log(a) + log(q) < 256 / (32 * 256)
                    = 1 / 32
```
						So:

```
    a * q = 2 ^ (log(a) + log(q))
          < 2 ^ (1 / 32)
          < 1
```
						so, because this routine returns A = a * q / 256, we return A = 0.

2. If La + Lq >= 256, then:

La + Lq >= 256

so:

La + Lq = r + 256

for some value of r > 0. Plugging this into the above gives:

```
    log(a) + log(q) = (La + Lq) / (32 * 256)
                    = (r + 256) / (32 * 256)
                    = (r / 32 + 8) / 256
```
						and plugging this into the above gives:

```
    x * y = 2 ^ (log(a) + log(q))
          = 2 ^ ((r / 32 + 8) / 256)
          = Ar
```
						so we return A = Ar.

In summary, given two numbers A and Q, we can calculate A * Q / 256 by adding La and Lq, and then either returning 0, or using the result to look up the correct result in Ar.

Division can be done in the same way, but we subtract the logarithms instead of adding them - see the [LL28](https://elite.bbcelite.com/6502sp/main/subroutine/ll28.html) routine for an example.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(A ?) = A * Q
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A = A * Q / 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
La = 32 * log(a) * 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Ar = 2^(r / 32 + 8) / 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
a * q = 2 ^ (log(a) + log(q))
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
log(a) + log(q) = (log(a) + log(q)) * 1
                  = (log(a) + log(q)) * (32 * 256) / (32 * 256)
                  = (32 * log(a) * 256 + 32 * log(q) * 256) / (32 * 256)
                  = (La + Lq) / (32 * 256)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
log(a) + log(q) < 256 / (32 * 256)
                    = 1 / 32
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
a * q = 2 ^ (log(a) + log(q))
          < 2 ^ (1 / 32)
          < 1
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
La + Lq >= 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
La + Lq = r + 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
log(a) + log(q) = (La + Lq) / (32 * 256)
                    = (r + 256) / (32 * 256)
                    = (r / 32 + 8) / 256
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
x * y = 2 ^ (log(a) + log(q))
          = 2 ^ ((r / 32 + 8) / 256)
          = Ar
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/multiplication_and_division_using_logarithms.html](https://elite.bbcelite.com/deep_dives/multiplication_and_division_using_logarithms.html)*
