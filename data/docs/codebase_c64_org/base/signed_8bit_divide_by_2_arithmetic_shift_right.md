---
title: Arithmetic shift right
source_url: https://codebase.c64.org/doku.php?id=base%3Asigned_8bit_divide_by_2_arithmetic_shift_right
category: reference
topics:
- assembly
difficulty: beginner
language: assembly
hardware:
- CPU
related: []
scraped_at: '2026-07-14'
---

# Arithmetic shift right

### Table of Contents

# Arithmetic shift right

By Bitbreaker

If we want to divide by the power of 2 we usually shift right. That is fine with unsigned numbers, but for signed numbers we would need a arithemtic shift right, that we have no opcode for. So we need a trick to preserve bit 7 in another way:

```
    cmp #$80 ;copy bit 7 to carry (i love that trick also for other situations where A should not be clobbered)
    ror      ;now rotate and we successfully preserved bit 7
```
Easy like that, done in 4 cycles! However keep in mind that this way the result is rounded down and not up when dealing with negative numbers. So for more accuracy you might prefer:

bpl + ;positive number? eor #$ff ;a = 0 - a to get a positive number clc adc #$01 lsr ;shift right eor #$ff ;make it negative again clc adc #$01 jmp ++ + lsr ++

This would need 13 cycles in average, but it can be done faster as well using the first method:

cmp #$80 ;copy bit 7 to carry ror ;shift right as before bpl + ;if positive number then skip adc #$00 ;else round up + ...

Then we would need 7,5 cycles in average. Still pretty nice. If you need it even faster (6 cycles) and use a lot of div by 2, then a lookup table might also be an option:

tax lda divtable,x

When using illegal op-codes you might also want to use this version that gives you always a cleared carry afterwards:

anc #$fe ;copy N to C and mask out bit 0 ror ;rotate, carry will now be clear

## And how's about shifting left?

If you intend to multiply a signed number by two, just do a = a + a and you are fine.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
cmp #$80 ;copy bit 7 to carry (i love that trick also for other situations where A should not be clobbered)
    ror      ;now rotate and we successfully preserved bit 7
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
bpl +     ;positive number?
   eor #$ff  ;a = 0 - a to get a positive number
   clc
   adc #$01
   lsr       ;shift right
   eor #$ff  ;make it negative again
   clc
   adc #$01
   jmp ++
+
   lsr
++
```

### Snippet Codice (BASIC)

```basic
cmp #$80  ;copy bit 7 to carry
   ror       ;shift right as before
   bpl +     ;if positive number then skip
   adc #$00  ;else round up
+  ...
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
tax
   lda divtable,x
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
anc #$fe  ;copy N to C and mask out bit 0
   ror       ;rotate, carry will now be clear
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asigned_8bit_divide_by_2_arithmetic_shift_right](https://codebase.c64.org/doku.php?id=base%3Asigned_8bit_divide_by_2_arithmetic_shift_right)*
