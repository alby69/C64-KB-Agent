---
title: base:sign_extension [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Asign_extension
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-20'
---

# base:sign_extension [Codebase64 wiki]

base:sign_extension

                Convert a signed 8-bit number to a signed 16-bit number, with .Y holding the high byte:

ldy #$00 lda value bpl :+ dey :

base/sign_extension.txt · Last modified:  by 127.0.0.1

                
                base:sign_extension

                Convert a signed 8-bit number to a signed 16-bit number, with .Y holding the high byte:

ldy #$00 lda value bpl :+ dey :

base/sign_extension.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldy #$00
 lda value
 bpl :+
  dey
:
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asign_extension](https://codebase.c64.org/doku.php?id=base%3Asign_extension)*
