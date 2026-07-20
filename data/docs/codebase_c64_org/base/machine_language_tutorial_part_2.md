---
title: Machine Language Tutorial Part 2 - Memory Manipulation
source_url: https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_2
category: tutorial
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- CPU
- KERNAL
- CIA
- SID
related:
- sid-registers
- keyboard-handling
- memory-map
- joystick-reading
- music-player
- sound-programming
- kernal-routines
- cia-registers
scraped_at: '2026-07-20'
---

# Machine Language Tutorial Part 2 - Memory Manipulation

### Table of Contents

# Machine Language Tutorial Part 2 - Memory Manipulation

The 6510 has three registers that can all hold 8 bits of data (this is why the C64 is called an 8-bit computer): A, X, and Y. The proper name for the A register is the accumulator because of its ability to do math, and X & Y are called index registers. You cannot transfer data directly between two memory addresses, so these must pass through the registers.

To load a byte into registers, use these commands:

LDA - load into A LDX - load into X LDY - load into Y

So the “LDA $1234” example from last part would load whatever was in $1234 into A.

To store registers into memory, use these commands:

STA - store A into STX - store X into STY - store Y into

So the “STA $4321” example from last part would store whatever was in A into $4321.

To transfer data between registers, use these commands:

TAX - transfer A to X TAY - transfer A to Y TXA - transfer X to A TYA - transfer Y to A

These commands have no operand, so just “TAX” would be sufficient.

To increment or decrement registers or memory, use these commands:

INC - increment memory INX - increment X INY - increment Y DEC - decrement memory DEX - decrement X DEY - decrement Y

So “INC $1111” would increment $1111. INX and INY have no operand. You'll use INX/DEX/INY/DEY a lot, so remember them!

## A Little Tangent

Alright, so we have a question that still needs to be answered: where do we put our programs? The cassette buffer, $033C-$03FB is a good spot to put these short example programs. But in the future, you're going to need to use different spots of memory. There's a completely free block of RAM in $C000-$CFFF, but that's still only 4K. $0800-$9FFF is the normal spot if you're not using BASIC at all, but usually you're going to include a SYS-line, so you'll need to start at $080D if so. If you have the BASIC and Kernal-ROMs turned off entirely, you've also got almost all of $A000-$BFFF and $E000-$FFFF. Don't use $D000-$DFFF, that's where the I/O (SID, VIC, CIA) lies.

## The Example

Objective: We want to get $46 into A, transfer that to X, increase it, put it back into A, and then store that into $CFFF.

The first problem comes right away: how do we get the specific value $46 into A? We can't do LDA $46, or else it would load from the zeropage $46.

The solution is that we have to add a number sign preceding the value. This is called immediate addressing. Using a full address (LDA $FFFF) is called absolute addressing, and zeropage access (LDA $FF) is called zeropage addressing. We'll learn about more addressing modes later.

So type this into the monitor:

A 033C LDA #$46

Remember what this means? It means that we're Assembling LDA #$46 to $033C.

So now we see that the monitor has prepared the next line, now all we must type to transfer is:

TAX

And now we increment it:

INX

Put it back into A:

TXA

And store it (absolute addressing):

STA $CFFF

But now there's another issue: how do we tell the computer to stop execution? If we didn't, it would just go into a random series of commands that would inevitably crash it.

To tell the computer to quit this program, we use:

BRK

This breaks the program and jumps to the address at $0316. In this case, it returns to the monitor.

Note: Using BRK to end a program is generally a bad idea for actual programs. We're only using it in this example.

We're done, now just press return on the next line to exit assembly mode.

To start the program, we could do two things: go back to BASIC and type SYS828 ($033C in decimal), or type in the monitor:

G 033C

This command (goto) changes the Program Counter so the next thing it executes is your program (the instruction at $033C).

Now type R into the monitor to view the registers, and type M CFFF. See anything different?

End of part 2…

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA - load into A
LDX - load into X
LDY - load into Y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
STA - store A into
STX - store X into
STY - store Y into
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
TAX - transfer A to X
TAY - transfer A to Y
TXA - transfer X to A
TYA - transfer Y to A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
INC - increment memory
INX - increment X
INY - increment Y
DEC - decrement memory
DEX - decrement X
DEY - decrement Y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A 033C LDA #$46
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
TAX
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
INX
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
TXA
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
STA $CFFF
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
BRK
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
G 033C
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_2](https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_2)*
