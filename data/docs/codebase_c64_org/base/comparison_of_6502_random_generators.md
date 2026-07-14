---
title: Comparison of 6502 pseudo random generators
source_url: https://codebase.c64.org/doku.php?id=base%3Acomparison_of_6502_random_generators
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- CPU
related: []
scraped_at: '2026-07-14'
---

# Comparison of 6502 pseudo random generators

# Comparison of 6502 pseudo random generators

This is an overview of the main properties of eight algorithms here on codebase.

Each algorithm was implemented as stated in the linked articles. Code size, execution time was measured. Execution times do not include the RTS command. Many PRNGs have a problem when the internal state becomes 0. Since this might be an important feature, it was stated which algorithms can also eventually output and handle a 0.

The quality was assessed by a test if the low byte hits all 256 numbers for 2000 random numbers and by a graphical check of the plot of 51200 random values. In every line n, the n&7-th bit of the result was plotted. For the results annotated with high quality, I could not identify any patterns in the plot. For good quality, some slight patterns or imbalances were visible. For low quality a direct repetition of values was visible.

| result size | execution cycles | size (bytes) | seeding | quality | plot | |
|---|---|---|---|---|---|---|
| [798 Xorshift](https://codebase.c64.org/doku.php?id=base:16bit_xorshift_random_generator) | 16bit | 30 | 21 | all except 0 | high | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=767528&media=base:rand_798xorshift.png)  | 
| [X ABC](https://codebase.c64.org/doku.php?id=6502_6510_maths:x_abc_random_number_generator_8_16_bit) | 16bit | 38 | 28 | risk of short cycle | high | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=8b1673&media=base:rand_x_abc.png)  | 
| [Whiteflame16](https://codebase.c64.org/doku.php?id=base:small_fast_16-bit_prng) | 16bit | 30* | 35 | all values | medium (some horizontal dashes visible) | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=ddac4b&media=base:rand_wf16.png)  | 
| [Galois LFSR](https://codebase.c64.org/doku.php?id=base:32bit_galois_lfsr) | 32bit | 60 | 50 | all except 0 | medium (too many 0s) | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=df7ba8&media=base:rand32_galois.png)  | 
| [Two16 PRG LSFR](https://codebase.c64.org/doku.php?id=base:two_very_fast_16bit_pseudo_random_generators_as_lfsr) | 16bit | 108 | 66 | all except 0 | high | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=aa750a&media=base:rand16_2.png)  | 
| [another 16bit PRG](https://codebase.c64.org/doku.php?id=base:another_16bit_pseudo_random_generator) | 16bit | 30 | 21 | all except 0 | low | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=ba096e&media=base:rand16_another.png)  | 
| [16bit PRG](https://codebase.c64.org/doku.php?id=base:16bit_pseudo_random_generator) | 16bit | 69 | 49 | all except 0 | low | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=2b28a7&media=base:rand16_1.png)  | 
| [Whiteflame8](https://codebase.c64.org/doku.php?id=base:small_fast_8-bit_prng) | 8bit | 16* | 14 | all values, 0-255 | low | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=38c7dc&media=base:rand_wf8.png)  | 
| [AX+ Tinyrand8](https://codebase.c64.org/doku.php?id=base:ax_tinyrand8) | 8bit | 18 | 15+ | all values, 0-255 | high | ![](https://codebase.c64.org/lib/exe/fetch.php?w=200&tok=572d9c&media=base:rand_ax_.png)  | 

* implementation has branches, execution time varies

+ not including separate 13 byte function for setting an 8bit seed

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Acomparison_of_6502_random_generators](https://codebase.c64.org/doku.php?id=base%3Acomparison_of_6502_random_generators)*
