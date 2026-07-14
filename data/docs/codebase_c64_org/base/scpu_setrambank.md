---
title: SetRAMBank
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_setrambank
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---

# SetRAMBank

base:scpu_setrambank

                # SetRAMBank

Set's the active RAM Bank used by the 658C16 CPU.

Requires the function: “SwitchEndian16”

| SYNTAX: | :SetRAMBank val | ||
| EXAMPLE: | :SetRAMBank $100000 | ||
| PARAMETERS: | Type | Minimum | Maximum | 
| val | U8 | $00 | $ff | 

```
    .pseudocommand SetRAMBank val {
        lda #SwitchEndian16(val.getValue())
        pha
        plb
        plb
    }
```
base/scpu_setrambank.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand SetRAMBank val {
        lda #SwitchEndian16(val.getValue())
        pha
        plb
        plb
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_setrambank](https://codebase.c64.org/doku.php?id=base%3Ascpu_setrambank)*
