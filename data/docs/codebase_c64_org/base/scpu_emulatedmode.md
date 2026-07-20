---
title: EmulatedMode
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_emulatedmode
category: reference
topics:
- basic
difficulty: intermediate
language: none
hardware:
- CPU
related: []
scraped_at: '2026-07-20'
---

# EmulatedMode

base:scpu_emulatedmode

                # EmulatedMode

Sets the processor into 6502/6510 Emulated mode.

| SYNTAX: | EmulatedMode | 
| EXAMPLE: | EmulatedMode | 
| PARAMETERS: | N/A | 

```
    .pseudocommand EmulatedMode {
        sec
        xce
    }
```
base/scpu_emulatedmode.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand EmulatedMode {
        sec
        xce
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_emulatedmode](https://codebase.c64.org/doku.php?id=base%3Ascpu_emulatedmode)*
