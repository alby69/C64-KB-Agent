---
title: BitMode8
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_bitmode8
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

# BitMode8

base:scpu_bitmode8

                # BitMode8

Pseudocommand to set the Accumulator and X/Y Index registers to 8 bit mode on the 658C16.

| SYNTAX: | BitMode8 | 
| EXAMPLE: | BitMode8 | 
| PARAMETERS: | N/A | 

```
    .pseudocommand BitMode8 {
        sep #%00110000
    }
```
base/scpu_bitmode8.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand BitMode8 {
        sep #%00110000
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_bitmode8](https://codebase.c64.org/doku.php?id=base%3Ascpu_bitmode8)*
