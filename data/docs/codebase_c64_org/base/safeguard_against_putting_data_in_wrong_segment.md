---
title: base:safeguard_against_putting_data_in_wrong_segment [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Asafeguard_against_putting_data_in_wrong_segment
category: reference
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- CIA
related:
- keyboard-handling
- cia-registers
- joystick-reading
scraped_at: '2026-07-20'
---

# base:safeguard_against_putting_data_in_wrong_segment [Codebase64 wiki]

base:safeguard_against_putting_data_in_wrong_segment

                Especially in macros, you often want to put data into a specific segments. After that is done, afaik, there's no way to go back to “previous segment” automatically. The next best thing would be to make current segment “undefined”, which isn't possible either.

One good safeguard for this is to create an empty segment.

Add to your config file:

```
MEMORY
{
	EMPTY: start=$07FF,  size=$0000, file=%O;
	...
}
SEGMENTS
{
	EMPTY:             load=EMPTY, type=ro;
	...
}
```
Then, whenever you want to make sure that developer HAS to define a segment, do:

.segment "EMPTY"

If you don't:

ld65: Warning: config.cfg(4): Memory area overflow in `EMPTY', segment `EMPTY' (1 bytes) ld65: Error: Cannot generate output due to memory area overflow Makefile:62: recipe for target 'example' failed

base/safeguard_against_putting_data_in_wrong_segment.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`EMPTY`** (unknown): No description available
- **`EMPTY`** (unknown): No description available

```assembly
MEMORY
{
	EMPTY: start=$07FF,  size=$0000, file=%O;
	...
}
SEGMENTS
{
	EMPTY:             load=EMPTY, type=ro;
	...
}
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.segment "EMPTY"
```

### Snippet Codice (BASIC)

```basic
ld65: Warning: config.cfg(4): Memory area overflow in `EMPTY', segment `EMPTY' (1 bytes)
ld65: Error: Cannot generate output due to memory area overflow
Makefile:62: recipe for target 'example' failed
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asafeguard_against_putting_data_in_wrong_segment](https://codebase.c64.org/doku.php?id=base%3Asafeguard_against_putting_data_in_wrong_segment)*
