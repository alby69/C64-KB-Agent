---
title: BitMode16
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_bitmode16
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware:
- CPU
related: []
scraped_at: '2026-07-14'
---

# BitMode16

base:scpu_bitmode16

                # BitMode16

Pseudocommand to set the Accumulator and X/Y Index registers to 16 bit mode on the 658C16.

| SYNTAX: | BitMode16 | 
| EXAMPLE: | BitMode16 | 
| PARAMETERS: | N/A | 

```
    .pseudocommand BitMode16 {
        rep #%00110000
    }
```
base/scpu_bitmode16.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand BitMode16 {
        rep #%00110000
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_bitmode16](https://codebase.c64.org/doku.php?id=base%3Ascpu_bitmode16)*
