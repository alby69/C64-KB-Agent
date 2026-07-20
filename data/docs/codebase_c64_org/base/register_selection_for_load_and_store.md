---
title: Register selection for load and store
source_url: https://codebase.c64.org/doku.php?id=base%3Aregister_selection_for_load_and_store
category: reference
topics: []
difficulty: intermediate
language: none
hardware:
- CPU
related: []
scraped_at: '2026-07-20'
---

# Register selection for load and store

base:register_selection_for_load_and_store

                # Register selection for load and store

```
   bit1 bit0     A  X  Y
    0    0             x
    0    1          x
    1    0       x
    1    1       x  x
So, A and X are selected by bits 1 and 0 respectively, while
 ~(bit1|bit0) enables Y.
Indexing is determined by bit4, even in relative addressing mode,
which is one kind of indexing.
Lines containing opcodes xxx000x1 (01 and 03) are treated as absolute
after the effective address has been loaded into CPU.
Zeropage,y and Absolute,y (codes 10x1 x11x) are distinguished by bit5.
```
base/register_selection_for_load_and_store.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`after`** (unknown): No description available

```assembly
bit1 bit0     A  X  Y
    0    0             x
    0    1          x
    1    0       x
    1    1       x  x

So, A and X are selected by bits 1 and 0 respectively, while
 ~(bit1|bit0) enables Y.

Indexing is determined by bit4, even in relative addressing mode,
which is one kind of indexing.

Lines containing opcodes xxx000x1 (01 and 03) are treated as absolute
after the effective address has been loaded into CPU.

Zeropage,y and Absolute,y (codes 10x1 x11x) are distinguished by bit5.
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aregister_selection_for_load_and_store](https://codebase.c64.org/doku.php?id=base%3Aregister_selection_for_load_and_store)*
