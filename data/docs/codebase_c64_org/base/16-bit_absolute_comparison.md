---
title: 16-Bit Absolute Value Comparison
source_url: https://codebase.c64.org/doku.php?id=base%3A16-bit_absolute_comparison
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

# 16-Bit Absolute Value Comparison

base:16-bit_absolute_comparison

                ### Table of Contents

# 16-Bit Absolute Value Comparison

## Skate & Eins Method

N1 = 16-bit signed number at zeropage

N2 = 16-bit signed number at zeropage

Here we compare;

|N1| and |N2|

in other representation

abs(N1) and abs(N2)

So, if N1 = 2000, N2 = -3000, N2 should be bigger since we compare the distance from zero.

Please note that equality is neglected here. Equal absolute values may end up in any of the two conditions.

lda N1+1 eor N2+1 bmi differentSigns // sameSigns: lda N1 cmp N2 lda N1+1 sbc N2+1 eor N1+1 bmi num1IsBigger jmp num2IsBigger differentSigns: clc lda N1 adc N2 lda N1+1 adc N2+1 eor N1+1 bmi num1IsBigger num2IsBigger: // ...add your code here for |N1| < |N2|... jmp endOfAbsCompare num1IsBigger: //...add your code here for |N1| > |N2|... endOfAbsCompare:

base/16-bit_absolute_comparison.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
lda N1+1
	eor N2+1
	bmi differentSigns
 
// sameSigns:
	lda N1
	cmp N2
	lda N1+1
	sbc N2+1
	eor N1+1
	bmi num1IsBigger
	jmp num2IsBigger
 
differentSigns:
	clc
	lda N1
	adc N2
	lda N1+1
	adc N2+1
	eor N1+1
	bmi num1IsBigger
 
num2IsBigger:
	// ...add your code here for |N1| < |N2|...
	jmp endOfAbsCompare
 
num1IsBigger:
	//...add your code here for |N1| > |N2|...
 
endOfAbsCompare:
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3A16-bit_absolute_comparison](https://codebase.c64.org/doku.php?id=base%3A16-bit_absolute_comparison)*
