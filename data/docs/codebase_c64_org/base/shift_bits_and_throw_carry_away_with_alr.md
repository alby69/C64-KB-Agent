---
title: Shift bits and throw carry away with ALR
source_url: https://codebase.c64.org/doku.php?id=base%3Ashift_bits_and_throw_carry_away_with_alr
category: reference
topics: []
difficulty: intermediate
language: none
hardware: []
related: []
scraped_at: '2026-07-20'
---

# Shift bits and throw carry away with ALR

base:shift_bits_and_throw_carry_away_with_alr

                # Shift bits and throw carry away with ALR

In many cases when you shift/roll a byte to the right with LSR, you don't need the bits that are rolled out. So if you're planning on doing an ADC afterwards, you need a CLC inbetween.

lsr clc adc #$47

But with ALR you can AND the A register before it's shifted. So if you choose $fe (%11111110) as the AND mask, you set the bit that is rolled out to 0, and thereby making sure the carry is cleared, at no extra cost cyclewise.

alr #$fe adc #$47

Unfortunately there is no equivalent for shifting the bits left. There is however a version for ROR called ARR. But this works more like ANC since it's setting the carry to the value of bit 7. So beware of the confusion this might cause.

base/shift_bits_and_throw_carry_away_with_alr.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
lsr
clc
adc #$47
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
alr #$fe
adc #$47
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ashift_bits_and_throw_carry_away_with_alr](https://codebase.c64.org/doku.php?id=base%3Ashift_bits_and_throw_carry_away_with_alr)*
