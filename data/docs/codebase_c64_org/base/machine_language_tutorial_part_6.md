---
title: Part 6 - The Stack
source_url: https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_6
category: tutorial
topics:
- assembly
- sprite programming
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CPU
related:
- memory-map
- sprite-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Part 6 - The Stack

### Table of Contents

# Part 6 - The Stack

The stack, located at $0100-$01FF, is a helpful place to store temporary values. It can be imagined as a stack of paper, with each sheet holding one byte of information. You can push a sheet on top of the stack, or pull the topmost sheet off the stack. This principle is formally known as last-in, first-out (LIFO).

## The Stack Pointer

The stack pointer is an index from $0100 that tells the CPU where to push the next stack value to.

The PHA instruction pushes the value in A to the address pointed to by the stack pointer, and then decrements the stack pointer. The PLA instruction increments the stack pointer, and then loads the value pointed to by the stack pointer to A.

A general principle of the stack is that you should always leave it as clean as you found it. Never push a value to the stack and then never pull it.

There are also a few more instructions relating to the stack:

TSX - Transfer stack pointer to X TXS - Transfer X to stack pointer

I've never used TSX, so I can't provide an example for that. However, TXS can be used to reset the stack pointer:

LDX #$FF TXS

A stack overflow happens when the stack pointer rolls over. Don't push when SP is $00, or pull when SP is $FF.

## The Example

So, let's imagine we have a value in $6000 in A that we need to preserve.

LDA $6000

But, we have a loop right after that trashes all registers.

LDA #$00 LDX #$18 TAY LDY $4000,X <- pretend this is at $1000 :) STA $5000,Y DEX BNE $1000

To preserve the value in A, we must push the value to the stack and pull it back after the loop.

LDA $6000 PHA LDA #$00 LDX #$18 TAY LDY $4000,X <- still $1000... STA $5000,Y DEX BNE $1000 PLA

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
TSX - Transfer stack pointer to X
TXS - Transfer X to stack pointer
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDX #$FF
TXS
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA $6000
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA #$00
LDX #$18
TAY
LDY $4000,X <- pretend this is at $1000 :)
STA $5000,Y
DEX
BNE $1000
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA $6000
PHA
LDA #$00
LDX #$18
TAY
LDY $4000,X <- still $1000...
STA $5000,Y
DEX
BNE $1000
PLA
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_6](https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_6)*
