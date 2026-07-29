---
title: o SAVE Vector F5DD/F675-F5EC/F684
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/compute!'s_tool_kit:_kernal.txt
category: reference
topics:
- kernal-api
- system-routines
- jumps
difficulty: intermediate
language: assembly
hardware:
- C64
related:
- f5ed-save
- jmp
- lda
- sta
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $F5DD
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: JMP from Kernal SAVE vector at FFD8.'
---

# $F5DD — o SAVE Vector F5DD/F675-F5EC/F684 ($F5DD)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F5DD`
- **Chiamata**: `JSR None` o `SYS 62941`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal SAVE vector at FFD8.

e pointer to the end of the save area + 1, (AE),
he X and Y registers.

cumulator value at entry is transferred to the X reg-
and is used as an index into page zero for the location of
tes that specify the starting address for the save. Set the
r to the start address of the save area, (C1), from these
ge-zero bytes.

o the address in the vector at (0322), normally
685.

ation**:

 AE, the low byte of the address of the end of the save
a + 1.
 AF, the high byte of the address of the end of the save
a + 1.
 and LDA 00,X to get the low byte of the address of the
rt of the save area, and STA in C1.
 01,X to get the high byte of the address of the start of
 save area, and STA in C2.
 (0322) to the save routine. The default address in the
tor is F5ED/F685.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*