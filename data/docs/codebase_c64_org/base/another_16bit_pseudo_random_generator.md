---
title: base:another_16bit_pseudo_random_generator [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Aanother_16bit_pseudo_random_generator
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---

# base:another_16bit_pseudo_random_generator [Codebase64 wiki]

base:another_16bit_pseudo_random_generator

                
Better use this one, which is more evolved: [Two very fast 16bit pseudo random generators as LFSR](https://codebase.c64.org/doku.php?id=base:two_very_fast_16bit_pseudo_random_generators_as_lfsr)

sr=$FD lda sr+1 asl asl eor sr+1 asl eor sr+1 asl asl eor sr+1 asl rol sr rol sr+1 rts

base/another_16bit_pseudo_random_generator.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
sr=$FD

lda sr+1
asl
asl
eor sr+1
asl
eor sr+1
asl
asl
eor sr+1
asl
rol sr
rol sr+1
rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aanother_16bit_pseudo_random_generator](https://codebase.c64.org/doku.php?id=base%3Aanother_16bit_pseudo_random_generator)*
