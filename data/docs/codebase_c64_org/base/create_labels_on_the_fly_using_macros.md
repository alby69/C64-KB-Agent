---
title: Create labels on the fly using macros (in ca65)
source_url: https://codebase.c64.org/doku.php?id=base%3Acreate_labels_on_the_fly_using_macros
category: tool
topics:
- assembly
difficulty: intermediate
language: assembly
hardware: []
related: []
scraped_at: '2026-07-14'
---

# Create labels on the fly using macros (in ca65)

base:create_labels_on_the_fly_using_macros

                # Create labels on the fly using macros (in ca65)

This was written by RadiantX on [CSDb](http://noname.c64.org/csdb/forums/?roomid=11&topicid=74546#74692), and put on Codebase by me (FTC). 

It is a description of how to create labels on the fly in the ca65 assembler by using macros. In this particular example, the labels are generated using a repeat counter in a loop. The macro that is used goes like this:

```
.macro makeident lname, count
    .ident(.concat(lname,.sprintf("%d", count))):
.endmacro
```
Using a macro like this it's possible to create labels using a repeat counter.

```
.repeat $100, I
    makeident "foo", I
    lda $1000 + I
    sta $2000 + I
.endrepeat
```
This produces the following code:

```
foo0:
    lda $1000
    sta $2000
foo1:
    lda $1001
    sta $2001
foo2:
    [...]
```
base/create_labels_on_the_fly_using_macros.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.macro makeident lname, count
    .ident(.concat(lname,.sprintf("%d", count))):
.endmacro
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.repeat $100, I
    makeident "foo", I
    lda $1000 + I
    sta $2000 + I
.endrepeat
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`foo0`** (unknown): No description available
- **`foo1`** (unknown): No description available
- **`foo2`** (unknown): No description available

```assembly
foo0:
    lda $1000
    sta $2000
foo1:
    lda $1001
    sta $2001
foo2:
    [...]
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Acreate_labels_on_the_fly_using_macros](https://codebase.c64.org/doku.php?id=base%3Acreate_labels_on_the_fly_using_macros)*
