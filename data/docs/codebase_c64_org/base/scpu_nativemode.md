---
title: NativeMode
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_nativemode
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

# NativeMode

base:scpu_nativemode

                # NativeMode

Sets the processor into 65C816 native mode.

| SYNTAX: | NativeMode | 
| EXAMPLE: | NativeMode | 
| PARAMETERS: | N/A | 

```
    .pseudocommand NativeMode {
        clc
        xce
    }
```
base/scpu_nativemode.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand NativeMode {
        clc
        xce
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_nativemode](https://codebase.c64.org/doku.php?id=base%3Ascpu_nativemode)*
