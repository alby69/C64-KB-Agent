---
title: Machine Language Tutorial Part 1 - Preparations
source_url: https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_1
category: tutorial
topics:
- assembly
- sprite programming
difficulty: beginner
language: assembly
hardware:
- BASIC ROM
- KERNAL
- CPU
- SID
related:
- sid-registers
- memory-map
- music-player
- sprite-programming
- sound-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Machine Language Tutorial Part 1 - Preparations

### Table of Contents

# Machine Language Tutorial Part 1 - Preparations

## Introduction

This is a document whose purpose is to teach you 6510 machine language. While I will be showing off some visual effects, this document will be more about the language itself. You won't be a professional democoder after this (even I'm not), but you'll be a step forward to being one!

## What is Machine Language?

Machine language is the programming language that computers can read directly. Like this:

AD 34 12 8D 21 43 60

This is a very inefficient way of writing code, so most people will view and write code in assembly language, which is a lot easier to read. For example, the previous bit of code would be this in assembly.

LDA $1234 STA $4321 RTS

The process of converting assembly to machine language is called “assembly”, so of course it would be “disassembly” vice versa.

Let's compare some lines side by side.

AD 34 12 LDA $1234

The first byte of the line is called an opcode. This is what tells the 6510 what to do. The abbreviations in assembly language are called mnemonics. The next two bytes in this line are the operand. This specifies where to do the operation. You may notice that in the assembly example that the operand was “$1234”. But in the machine example, it's 34 12! What is going on? The 6510 uses reverse byte order. Get used to it, every part of the 6510 is this way.

Some opcodes have no operand, like the RTS.

60 RTS

## Using a Machine Language Monitor

Machine language monitors are programs that freeze the machine and allow you to view memory, and all sorts of other stuff. These things apply to most monitors.

When you open the monitor up you'll get something like this:

ADDR AR XR YR SP 01 NV-BDIZC .;E37B FF FF FF FB 37 00000000

ADDR/PC - Program counter. Tells the 6510 where to get the next instruction from.

AR, XR, YR - Contents of the three registers.

SP - Stack pointer. More on this later.

NV-BDIZC - Status register in binary.

N - Negative flag

V - Overflow flag

- - Unused bit

B - Reached current position from a break.

D - Decimal mode.

I - Interrupt disable flag.

Z - Zero flag.

C - Carry flag.

### Disassembly

To disassemble in a monitor you type:

D ADD1 ADD2

where ADD1 is the address you'd like to disassemble from, and ADD2 is the address where disassembly ends. Typing just D will continuously disassemble from where you left off. You'll get output like this:

.> 1000 AD 34 12 LDA $1234 .> 1003 8D 21 43 STA $4321 .> 1006 60 RTS .> 1007 00 BRK

So we have the address of the instruction, and the instruction in machine language and then assembly language. You can type over a disassembly listing to change the code.

### Assembly

To assemble in a monitor you type:

A ADDR OPC OPER

where ADDR is where you assemble to, then opcode, then operand if one. After you enter in the command, the monitor will have the next assembly line ready for you. All you have to type now is the opcode and operand. Exit this mode by just pressing return with nothing else in the line.

So to assemble LDA $1234 to $1000 we type:

A 1000 LDA $1234

### Memory Listing

To list memory we type:

M ADD1 ADD2

where ADD1 is the address you'd like to list from, and ADD2 is the address where listing ends. Typing just M will continuously list from where you left off. So imagine we want to see 5 bytes by typing M 1000 1004. We'd get this:

.:1000 AD 34 12 8D 21 43 60 00 -4..!C..

So we have the address of the first byte, the bytes, and then the PETSCII-codes of the bytes. Wait, but we only asked for 1000 to 1004! The M command will always fill out a line, even if you don't ask it to. You can type over memory listings to modify them.

To exit the monitor type X.

Stay tuned for more parts, next time we learn what some instructions do!

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
AD 34 12 8D 21 43 60
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA $1234
STA $4321
RTS
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
AD 34 12
LDA $1234
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
60
RTS
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ADDR AR XR YR SP 01 NV-BDIZC
.;E37B FF FF FF FB 37 00000000
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
D ADD1 ADD2
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.> 1000 AD 34 12  LDA $1234
.> 1003 8D 21 43  STA $4321
.> 1006 60        RTS
.> 1007 00        BRK
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A ADDR OPC OPER
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A 1000 LDA $1234
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
M ADD1 ADD2
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.:1000 AD 34 12 8D 21 43 60 00 -4..!C..
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_1](https://codebase.c64.org/doku.php?id=base%3Amachine_language_tutorial_part_1)*
