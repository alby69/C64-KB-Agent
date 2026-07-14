---
title: Generating system names
source_url: https://elite.bbcelite.com/deep_dives/generating_system_names.html
category: deep-dive
topics:
- memory management
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- BASIC ROM
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# Generating system names

## Producing system names from twisted seeds and two-letter tokens

There are 256 systems in each of the eight galaxies in Elite, and each of those 2048 systems has a unique name, as shown in the system charts like this one from the start of the game:

![The Short-range Chart in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/short-range_chart.png) 

						System names aren't stored as plain text, as there simply isn't enough memory in Elite. Instead they are generated from the three 16-bit seeds for that system, and in the case of the selected system, those seeds live at [QQ15](https://elite.bbcelite.com/cassette/main/workspace/zp.html#qq15). See the deep dive on [galaxy and system seeds](https://elite.bbcelite.com/galaxy_and_system_seeds.html) for more information about the seeds.

The process of printing the system name is done by the [cpl](https://elite.bbcelite.com/cassette/main/subroutine/cpl.html) routine. It works as follows, where s0, s1, s2 are the seeds for the system in question:

- Check bit 6 of s0_lo. If it is set then we will generate four two-letter pairs for the name (8 characters in total), otherwise we will generate three pairs (6 characters).
- Generate the first two letters by taking bits 0-4 of s2_hi. If this is zero, jump to the next step, otherwise we have a number in the range 1-31. Add 128 to get a number in the range 129-159, and convert this to a two-letter token (see variable [QQ16](https://elite.bbcelite.com/cassette/main/variable/qq16.html)for the list of two-letter tokens).
- Twist the seeds by calling [TT54](https://elite.bbcelite.com/cassette/main/subroutine/tt54.html)and repeat the previous step, until we have processed three or four pairs, depending on step 1. The results of the final twist are ignored.

See the deep dive on [twisting the system seeds](https://elite.bbcelite.com/twisting_the_system_seeds.html) for an explanation of the twisting process.

As the process above involves twisting the seeds three or four times, they will be changed, so we also need to back up the original seeds before starting the above process, and restore them afterwards. Also, the C flag is changed by the twisting process, and the C flag that results from the final twist feeds into the calculation of the system's star size on the Short-range Chart (with a clear C flag producing either a small or medium star, and a set C flag producing either a medium or large star).

Probably the best way to understand the process is to run through some examples, so let's do that now.

## Two-letter system name: Ra

													 --------------------------

						There is only one system in the whole game with a two-letter name: Ra in the first galaxy.

To generate the letter pairs, we start with the system's seeds and twist them twice to generate three letter pairs. The twists are as follows:

| Twist | s0_hi | s0_lo | s1_hi | s1_lo | s2_hi | s2_lo | 
|---|---|---|---|---|---|---|
| - | %10000111 | %10101010 | %00001100 | %00111000 | %10000000 | %01010011 | 
| 1 | %00001100 | %00111000 | %10000000 | %01010011 | %00010100 | %00110101 | 
| 2 | %10000000 | %01010011 | %00010100 | %00110101 | %10100000 | %11000000 | 

And this gives us the following result:

| Twist | Seed bits | Bits | Calculation | Result | 
|---|---|---|---|---|
| - | s0_lo bit 6 | %0 | - | Three pairs | 
| - | s2_hi bits 0-4 | %00000 | 0 | Pair 1: Skip | 
| 1 | s2_hi bits 0-4 | %10100 | 128 + %10100 = 148 | Pair 2: "RA" | 
| 2 | s2_hi bits 0-4 | %00000 | 0 | Pair 3: Skip | 

## Three-letter system name: Ara

													 -----------------------------

						There are two system in the whole game with three-letter names: Ara in the first galaxy and Rea in the third galaxy. Let's look at Ara here.

To generate the letter pairs, we start with the system's seeds and twist them twice to generate three letter pairs. The twists are as follows:

| Twist | s0_hi | s0_lo | s1_hi | s1_lo | s2_hi | s2_lo | 
|---|---|---|---|---|---|---|
| - | %00101000 | %00000000 | %00011100 | %11000000 | %01001111 | %01001101 | 
| 1 | %00011100 | %11000000 | %01001111 | %01001101 | %10010100 | %00001101 | 
| 2 | %01001111 | %01001101 | %10010100 | %00001101 | %00000000 | %00011010 | 

And this gives us the following result:

| Twist | Seed bits | Bits | Calculation | Result | 
|---|---|---|---|---|
| - | s0_lo bit 6 | %0 | - | Three pairs | 
| - | s2_hi bits 0-4 | %01111 | 128 + %01111 = 143 | Pair 1: "A" | 
| 1 | s2_hi bits 0-4 | %10100 | 128 + %10100 = 148 | Pair 2: "RA" | 
| 2 | s2_hi bits 0-4 | %00000 | 0 | Pair 3: Skip | 

## Four-letter system name: Lave

													 -----------------------------

						Lave is the iconic starting system in Elite, so let's see how this name is generated.

To generate the letter pairs, we start with the system's seeds and twist them twice to generate three letter pairs. The twists are as follows:

| Twist | s0_hi | s0_lo | s1_hi | s1_lo | s2_hi | s2_lo | 
|---|---|---|---|---|---|---|
| - | %10101101 | %00111000 | %00010100 | %10011100 | %00010101 | %00011101 | 
| 1 | %00010100 | %10011100 | %00010101 | %00011101 | %11010110 | %11110001 | 
| 2 | %00010101 | %00011101 | %11010110 | %11110001 | %00000000 | %10101010 | 

And this gives us the following result:

| Twist | Seed bits | Bits | Calculation | Result | 
|---|---|---|---|---|
| - | s0_lo bit 6 | %0 | - | Three pairs | 
| - | s2_hi bits 0-4 | %10101 | 128 + %10101 = 149 | Pair 1: "LA" | 
| 1 | s2_hi bits 0-4 | %10110 | 128 + %10110 = 150 | Pair 2: "VE" | 
| 2 | s2_hi bits 0-4 | %00000 | 0 | Pair 3: Skip | 

## Five-letter system name: Arexe

													 ------------------------------

						Arexe is a key system in the Constrictor mission, as that's where the stolen ship jumps from the first to the second galaxy. The clue appears when you dock at Reesdice:

A STRANGE LOOKING SHIP LEFT HERE A WHILE BACK. LOOKED BOUND FOR AREXE.


To generate the letter pairs, we start with the system's seeds and twist them three times to generate four letter pairs. The twists are as follows:

| Twist | s0_hi | s0_lo | s1_hi | s1_lo | s2_hi | s2_lo | 
|---|---|---|---|---|---|---|
| - | %01011001 | %01111010 | %10100100 | %11110000 | %11101111 | %10110011 | 
| 1 | %10100100 | %11110000 | %11101111 | %10110011 | %11101110 | %00011101 | 
| 2 | %11101111 | %10110011 | %11101110 | %00011101 | %10000010 | %11000000 | 
| 3 | %11101110 | %00011101 | %10000010 | %11000000 | %01100000 | %10010000 | 

And this gives us the following result:

| Twist | Seed bits | Bits | Calculation | Result | 
|---|---|---|---|---|
| - | s0_lo bit 6 | %1 | - | Four pairs | 
| - | s2_hi bits 0-4 | %01111 | 128 + %01111 = 143 | Pair 1: "A" | 
| 1 | s2_hi bits 0-4 | %01110 | 128 + %01110 = 142 | Pair 2: "RE" | 
| 2 | s2_hi bits 0-4 | %00010 | 128 + %00010 = 130 | Pair 3: "XE" | 
| 3 | s2_hi bits 0-4 | %00000 | 0 | Pair 4: Skip | 

## Six-letter system name: Errius

													 ------------------------------

						Also a key player in the Constrictor mission, Errius is the first clue we get when we arrive in the second galaxy - and its hint is certainly the most memorable:

GET YOUR IRON ASS OVER TO ERRIUS.


To generate the letter pairs, we start with the system's seeds and twist them twice to generate three letter pairs. The twists are as follows:

| Twist | s0_hi | s0_lo | s1_hi | s1_lo | s2_hi | s2_lo | 
|---|---|---|---|---|---|---|
| - | %10010101 | %10000000 | %10111000 | %10100000 | %01110000 | %11011010 | 
| 1 | %10111000 | %10100000 | %01110000 | %11011010 | %10111110 | %11111010 | 
| 2 | %01110000 | %11011010 | %10111110 | %11111010 | %11101000 | %01110100 | 

And this gives us the following result:

| Twist | Seed bits | Bits | Calculation | Result | 
|---|---|---|---|---|
| - | s0_lo bit 6 | %0 | - | Three pairs | 
| - | s2_hi bits 0-4 | %10000 | 128 + %10000 = 144 | Pair 1: "ER" | 
| 1 | s2_hi bits 0-4 | %11110 | 128 + %11110 = 158 | Pair 2: "RI" | 
| 2 | s2_hi bits 0-4 | %01000 | 128 + %01000 = 136 | Pair 3: "US" | 

## Seven-letter system name: Geinona

													 ---------------------------------

						Let's look at a seven-letter name now - and how about picking the 42nd system in the first galaxy, as that's an auspicious number?

To generate the letter pairs, we start with the system's seeds and twist them three times to generate four letter pairs. The twists are as follows:

| Twist | s0_hi | s0_lo | s1_hi | s1_lo | s2_hi | s2_lo | 
|---|---|---|---|---|---|---|
| - | %10011001 | %11000000 | %10001111 | %00001000 | %01100011 | %10111101 | 
| 1 | %10001111 | %00001000 | %01100011 | %10111101 | %10001100 | %10000101 | 
| 2 | %01100011 | %10111101 | %10001100 | %10000101 | %01111111 | %01001010 | 
| 3 | %10001100 | %10000101 | %01111111 | %01001010 | %01101111 | %10001100 | 

And this gives us the following result:

| Twist | Seed bits | Bits | Calculation | Result | 
|---|---|---|---|---|
| - | s0_lo bit 6 | %1 | - | Four pairs | 
| - | s2_hi bits 0-4 | %00011 | 128 + %00011 = 131 | Pair 1: "GE" | 
| 1 | s2_hi bits 0-4 | %01100 | 128 + %01100 = 140 | Pair 2: "IN" | 
| 2 | s2_hi bits 0-4 | %11111 | 128 + %11111 = 159 | Pair 3: "ON" | 
| 3 | s2_hi bits 0-4 | %01111 | 128 + %01111 = 143 | Pair 4: "A" | 

## Eight-letter system name: Tibedied

													 ----------------------------------

						Tibedied is the first system in the first galaxy, so these are the only seeds that are hard-coded into the game. They are embedded into the default commander at [NA%](https://elite.bbcelite.com/cassette/main/variable/na_per_cent.html), in bytes #3 to #8.

To generate the letter pairs, we start with the system's seeds and twist them three times to generate four letter pairs. The twists are as follows:

| Twist | s0_hi | s0_lo | s1_hi | s1_lo | s2_hi | s2_lo | 
|---|---|---|---|---|---|---|
| - | %01011010 | %01001010 | %00000010 | %01001000 | %10110111 | %01010011 | 
| 1 | %00000010 | %01001000 | %10110111 | %01010011 | %00010011 | %11100101 | 
| 2 | %10110111 | %01010011 | %00010011 | %11100101 | %11001101 | %10000000 | 
| 3 | %00010011 | %11100101 | %11001101 | %10000000 | %10011000 | %10111000 | 

And this gives us the following result:

| Twist | Seed bits | Bits | Calculation | Result | 
|---|---|---|---|---|
| - | s0_lo bit 6 | %1 | - | Four pairs | 
| - | s2_hi bits 0-4 | %10111 | 128 + %10111 = 151 | Pair 1: "TI" | 
| 1 | s2_hi bits 0-4 | %10011 | 128 + %10011 = 147 | Pair 2: "BI" | 
| 2 | s2_hi bits 0-4 | %01101 | 128 + %01101 = 141 | Pair 3: "DI" | 
| 3 | s2_hi bits 0-4 | %11000 | 128 + %11000 = 152 | Pair 4: "ED" |

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/generating_system_names.html](https://elite.bbcelite.com/deep_dives/generating_system_names.html)*
