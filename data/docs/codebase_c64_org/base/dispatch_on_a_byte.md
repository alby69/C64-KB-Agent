---
title: Dispatching on a Byte
source_url: https://codebase.c64.org/doku.php?id=base%3Adispatch_on_a_byte
category: reference
topics:
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Dispatching on a Byte

base:dispatch_on_a_byte

                ### Table of Contents

# Dispatching on a Byte

*by White Flame and Krill*

The need to dispatch to one of many possible routines based on the value of a byte comes up regularly if you're doing complex data-oriented routines like decompression or scripting, and most often needs to be as fast as possible.

All but the Stack Dispatch routine use self-modification, which will run 1 cycle faster and 1 byte leaner if the dispatch routine itself is in zeropage.

## General Table Dispatch

### 128 entries or less

sta :+ +1 : jmp (table) table: .word handler0, handler2, handler4, ...

- 9 cycles, 8 if from zeropage
- Align opcodes and table low-word, or use`SBC`/`ASL`to adjust
- Maximum of 128 entries

### More than 128 entries

asl bcs :++ ; Dispatch 0-127 sta :+ +1 : jmp (table) ; Dispatch 128-255 : sta :+ +1 : jmp (table + $0100) table: .word handler0, handler1, ..., handler127, handler128, ...

- 13 cycles for 0-127, 14 cycles for 128-255. Subtract 1 cycle if from zeropage.

## Stack Dispatch

tax txs rts

- 8 or 10 cycles, depending on if`TAX`is necessary
- Table of vectors at $0100
- Maximum of 128 entries
- Handlers cannot use stack, or must reposition it to not trample the table

## Low-Address Dispatch

sta :+ +1 : jmp routine ; Low byte is overwritten, high byte remains

- 7 cycles, 6 if in zeropage
- All handlers start in the same memory page
- Byte codes match specific addresses with little flexibility

## High-Address Dispatch

sta :+ +2 : jmp $0000 ; High byte is overwritten, low byte remains

- 7 cycles, 6 if in zeropage
- All handlers start on their own page, at the same low byte
- Byte codes constrained to ranges based on memory map

## Relative Branch Dispatch

sta :+ +1 : bne * ; If Z corresponds to A, otherwise use appropriate BRA

- 7 cycles, 6 if in zeropage
- Similar to low-address dispatch but allows page-crosses at the cost of one cycle
- Saves one cycle for the fall-through case

base/dispatch_on_a_byte.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`table`** (unknown): No description available

```assembly
sta :+ +1
: jmp (table)
 
table:
  .word handler0, handler2, handler4, ...
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`table`** (unknown): Dispatch 128-255

```assembly
asl
  bcs :++
  ; Dispatch 0-127
  sta :+ +1
: jmp (table)
  ; Dispatch 128-255
: sta :+ +1
: jmp (table + $0100)
 
table: .word handler0, handler1, ..., handler127, handler128, ...
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
tax
  txs
  rts
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sta :+ +1
: jmp routine  ; Low byte is overwritten, high byte remains
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sta :+ +2
: jmp $0000  ; High byte is overwritten, low byte remains
```

### Snippet Codice (BASIC)

```basic
sta :+ +1
: bne *  ; If Z corresponds to A, otherwise use appropriate BRA
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Adispatch_on_a_byte](https://codebase.c64.org/doku.php?id=base%3Adispatch_on_a_byte)*
