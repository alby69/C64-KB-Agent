---
title: Machine Language Tutorial Part 4 - Logical Operations and Math
source_url: https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_4
category: tutorial
topics:
- assembly
- memory management
difficulty: intermediate
language: assembly
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Machine Language Tutorial Part 4 - Logical Operations and Math

### Table of Contents

# Machine Language Tutorial Part 4 - Logical Operations and Math

Logical operations are simply operations that have to do with the logic circuits of the computer. Therefore we will be dealing with bits in this part.

## The Operations

All of these commands can only be used on the A register. The commands are applied to A with a mask, which is the operand.

### ORA - Logical OR to A

This command will turn bits in A on. If the mask is zero, the bit will be left alone. If the mask is one, the bit will be turned on.

Bit in accumulator | Mask = Resulting A bit. 0 | 0 = 0 0 | 1 = 1 1 | 0 = 1 1 | 1 = 1

Let's see this in action. If A was %00110101 and we ORA %01010011, what would happen?

```
A = 00110101
ORA 01010110 <- masks
    vvvvvvvv
A = 01110111
```
### AND - Logical AND to A

This command will turn bits in A off. If the mask is zero, the bit will be turned off. If the mask is one, the bit will be left alone.

Bit in accumulator & Mask = Resulting A bit. 0 & 0 = 0 0 & 1 = 0 1 & 0 = 0 1 & 1 = 1

```
A = 00110101
AND 01010011 <- masks
    vvvvvvvv
A = 00010001
```
### EOR - Exclusive OR to A

This command flips bits around. If the mask is zero, the bit is left alone. If the mask is 1, the bit is flipped.

Bit in accumulator ^ Mask = Resulting A bit. 0 ^ 0 = 0 0 ^ 1 = 1 1 ^ 0 = 1 1 ^ 1 = 0

```
A = 00110101
EOR 01010011 <- masks
    vvvvvvvv
A = 01100110
```
## Math

### Addition

To add to A, we use ADC. The carry bit is used to link different ADCs together for multi-byte addition. Therefore we must clear carry before any new addition to prevent any previous carry from being added.

So to add a two byte value at $3000 to a value at $2000 and store that to $4000, we'd do:

CLC LDA $2000 <- handle low byte ADC $3000 STA $4000 LDA $2001 <- handle high byte ADC $3001 STA $4001

By the way, it doesn't matter if you CLC or LDA first.

### Subtraction

To subtract from A, we use SBC. The carry bit is used as a borrow for multi-byte subtraction. We need to set the carry to prevent anything extra from being subtracted.

SEC LDA $2000 SBC $3000 STA $4000 LDA $2001 SBC $3001 STA $4001

For both subtraction and addition, if the carry flag is on after addition, that means that the number overflowed and you will need to use another byte depending on what you're trying to do.

### Multiplication

To multiply by two we need to shift the bytes back. We use ASL (arithmetic shift left) or ROL (rotate left). You can use these on memory or A.

ASL does this:

```
     +-+-+-+-+-+-+-+-+
C <- |7|6|5|4|3|2|1|0| <- 0
     +-+-+-+-+-+-+-+-+
```
It shifts bit 7 into carry, all other bits left, and 0 goes in bit 0.

ROL does this:

```
+------------------------------+
|                              |
|   +-+-+-+-+-+-+-+-+    +-+   |
+-< |7|6|5|4|3|2|1|0| <- |C| <-+
    +-+-+-+-+-+-+-+-+    +-+
```
It shifts carry into zero, all other bits left, and bit 7 goes into the new carry.

To multiply by non-powers of two, we must use other ways to get there. So to multiply by 6:

LDA #$01 ASL A <- multiply by 2 STA $xxxx <- store A*2 into some location ASL A <- now we have A*4 CLC ADC $xxxx <- and add A*2 to get A*6

To multiply a two-byte value we need to use ASL and ROL in sequence.

ASL $2000 <- x*2 ROL $2001 ASL $2000 <- x*4 ROL $2001 ...and so on.

### Division

To divide by two we use LSR (logical shift right) and ROR (rotate right). These work similarly to their “left” counterparts.

LSR does this:

```
     +-+-+-+-+-+-+-+-+
0 -> |7|6|5|4|3|2|1|0| -> C
     +-+-+-+-+-+-+-+-+
```
And ROR does this:

```
+------------------------------+
|                              |
|   +-+    +-+-+-+-+-+-+-+-+   |
+-> |C| -> |7|6|5|4|3|2|1|0| >-+
    +-+    +-+-+-+-+-+-+-+-+
```
Note that the ASL/LSR/ROL/ROR can be used for more than just addition, since they work with the bits of a memory address/accumulator.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Bit in accumulator | Mask = Resulting A bit.
0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
1 | 1 = 1
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A = 00110101
ORA 01010110 <- masks
    vvvvvvvv
A = 01110111
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Bit in accumulator & Mask = Resulting A bit.
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A = 00110101
AND 01010011 <- masks
    vvvvvvvv
A = 00010001
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Bit in accumulator ^ Mask = Resulting A bit.
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A = 00110101
EOR 01010011 <- masks
    vvvvvvvv
A = 01100110
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CLC
LDA $2000 <- handle low byte
ADC $3000
STA $4000
LDA $2001 <- handle high byte
ADC $3001
STA $4001
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
SEC
LDA $2000
SBC $3000
STA $4000
LDA $2001
SBC $3001
STA $4001
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+-+-+-+-+-+-+-+-+
C <- |7|6|5|4|3|2|1|0| <- 0
     +-+-+-+-+-+-+-+-+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+------------------------------+
|                              |
|   +-+-+-+-+-+-+-+-+    +-+   |
+-< |7|6|5|4|3|2|1|0| <- |C| <-+
    +-+-+-+-+-+-+-+-+    +-+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA #$01
ASL A <- multiply by 2
STA $xxxx <- store A*2 into some location
ASL A <- now we have A*4
CLC
ADC $xxxx <- and add A*2 to get A*6
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ASL $2000 <- x*2
ROL $2001
ASL $2000 <- x*4
ROL $2001
...and so on.
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+-+-+-+-+-+-+-+-+
0 -> |7|6|5|4|3|2|1|0| -> C
     +-+-+-+-+-+-+-+-+
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+------------------------------+
|                              |
|   +-+    +-+-+-+-+-+-+-+-+   |
+-> |C| -> |7|6|5|4|3|2|1|0| >-+
    +-+    +-+-+-+-+-+-+-+-+
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_4](https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_4)*
