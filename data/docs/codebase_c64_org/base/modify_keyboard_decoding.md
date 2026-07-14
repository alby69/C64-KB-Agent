---
title: Modify Keyboard Decoding
source_url: https://codebase.c64.org/doku.php?id=base%3Amodify_keyboard_decoding
category: reference
topics:
- sprite programming
- assembly
difficulty: beginner
language: assembly
hardware:
- KERNAL
- CIA
related:
- sprite-programming
- keyboard-handling
- cia-registers
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
- joystick-reading
scraped_at: '2026-07-14'
---

# Modify Keyboard Decoding

# Modify Keyboard Decoding

The Kernal calls a routine for checking the keyboard in the interrupt routine. The mapping of keyboard code to PETSCII character is done via tables, which are stored in ROM at addresses $EB81 for unshifted keys, $EBC2 for shifted keys, $EC03 for keys pressed together with the CBM key, and $EC78 for keys pressed together with the control key.

The tables are in ROM, but their selection based on the currently pressed Shift/CBM/Ctrl keys is vectored over $28f, so it is rather easy to replace the decoding.

For example, to switch Y and Z to emulate the common layout on German keyboards, a minimally invasive approach would be:

1. Select some piece of RAM where you want to out your new decoding table. For the following steps, I have chosen the area of $2a7-$2ff, which is unused by the Kernal and on of the lesser-used addresses of typical programs

2. Copy the decoding table from the Kernal into that area:

t eb81 ebc1 2a7 in VICE monitor

3. Switch the decoding of Y and Z:

>2c0 5a >2b3 59

4. write a new routine selecting the new decoding and put it right after your table:

a 2e8 .02e8 lda $28d .02eb beq 2f0 .02ed jmp $eb4b .02f0 lda #$a7 .02f2 sta $f5 .02f4 lda #$02 .02f6 sta $f6 .02f8 jmp $eae0

5. Change the pointer in $28f to your new routine:

> 28f e8 02

That's it, Y and Z are now switched. If you also want to switch the shifted values, you need to copy and modify another table (see $EBC2 in Kernal)

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
t eb81 ebc1 2a7 in VICE monitor
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
>2c0 5a
 >2b3 59
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
a 2e8
 .02e8  lda $28d
 .02eb  beq 2f0
 .02ed  jmp $eb4b
 .02f0  lda #$a7
 .02f2  sta $f5
 .02f4  lda #$02
 .02f6  sta $f6
 .02f8  jmp $eae0
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
> 28f e8 02
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Amodify_keyboard_decoding](https://codebase.c64.org/doku.php?id=base%3Amodify_keyboard_decoding)*
