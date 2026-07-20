---
title: Inverse Subtraction
source_url: https://codebase.c64.org/doku.php?id=base%3Ainverse_subtraction
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Inverse Subtraction

### Table of Contents

# Inverse Subtraction

by White Flame

To subtract A from a number, or “number - .A”, we transform it to the doable “-.A + number”:

eor #$ff sec adc number

and that's it.

## Further elaboration

by Frantic

One may think that the following two pieces of code would produce exactly the same result:

;Variant 1 - Subtract XX by YY using clc/adc lda #XX clc adc #YY ;E.g. to subtract with 1, use $ff here

;Variant 2 - Subtract $XX by $YY using sec/adc lda #XX sec adc #YY-1 ;E.g. to subtract with 1, use $ff-1=$fe here

The resulting byte in the A register will indeed be the same for all possible values (0-255) of value XX and YY in each of the two variants. However, the carry flag will be set differently after executing these two pieces of code for various values of XX and YY.

This means that if the value of the carry after the “subtraction” matters to you, you can't use standard addition form (clc/adc) to do the “subtraction”. White Flame's code above is obviously using the correct version of inverse subtraction (e.g. sec/adc).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
eor #$ff
 sec
 adc number
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
;Variant 1 - Subtract XX by YY using clc/adc
  lda #XX
  clc
  adc #YY  ;E.g. to subtract with 1, use $ff here
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
;Variant 2 - Subtract $XX by $YY using sec/adc
  lda #XX
  sec
  adc #YY-1  ;E.g. to subtract with 1, use $ff-1=$fe here
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ainverse_subtraction](https://codebase.c64.org/doku.php?id=base%3Ainverse_subtraction)*
