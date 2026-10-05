---
id: 0311-usradd
type: entity
title: $B248 USR-Vektor
aliases:
- $B248 USR-Vektor
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0311-usradd.md
  sha256: d52b6efa8abd87de82acceabff64e7e7993ec56bfb5d52f9e7a6f77238085155
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0311-usradd
---

# $B248 USR-Vektor



# USRADD — $B248 USR-Vektor ($0311)

## Panoramica
Il registro o area di memoria USRADD è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0311` (`785` decimale)
- **Range**: `$0311`-`$0312`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Commodore-64-intern-Buch (Commodore)
$B248 USR-Vektor

### C64 Programmer's Reference Guide (Commodore)
USR Address Low Byte / High Byte

### Mapping the Commodore 64 (Sheldon Leemon)
These locations contain the target address of the USR command.  They
are initialized by the Operating System to point to the BASIC error
message handler routine, so that if you try to execute a USR call
without changing these values, you will receive an ILLEGAL QUANTITY
error message.

In order to successfully execute a USR call, you must first POKE in
the target address in low-byte, high-byte order.  You can calculate
these two values for any address with the formula:

    HI=INT(AD/256):LO=AD-(HI*256)

For example, if the USR routine started at 49152 ($C000), you would
POKE 786, INT(49152/256):POKE 785,49152-(PEEK(786)*256 before
executing the USR command.

What makes the USR command different from SYS is that you can pass a
parameter into the machine language routine by placing it in
parenthesis after the USR keyword, and you can pass a parameter back
to a variable by assigning its value to the USR function.

In other words, the statement X=USR(50) will first put the number 50
in floating point format into the Floating Point Accumulator (FAC1) at
97-102 ($0061-$0066).  Then, the machine language program designated by
the address at this vector will be executed.  Finally, the variable X
will be assigned the floating point value which ends up in FAC1 after
the user-written routine is finished.

Since floating point representation is difficult to work with, it is
handy to change these floating point parameters into integers before
working with them.  Fortunately, there are vectored routines which
will do the conversions for you.  The routine vectored at locations
3-4 converts the number in FAC1 to a two-byte signed integer, with the
low byte in the .Y register (and location 101 ($0065)) and the high byte
in the Accumulator (.A).  Remember, that number is converted to a
signed integer in the range between 32767 and -32768, with Bit 7 of
the high byte used to indicate the sign.

To pass a value back through the USR function, you need to place the
number into FAC1.  To convert a signed integer to floating point
format, place the high byte into the Accumulator (.A), the low byte
into the .Y register, and jump through the vector at locations 5-6
with a JMP ($0005) instruction.  The floating point result will be
left in FAC1.

### Reference (Joe Forster / STA)
Execution address of USR() function

### 64map (—)
USR Address ($LB,$MB)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0311-usradd]]
