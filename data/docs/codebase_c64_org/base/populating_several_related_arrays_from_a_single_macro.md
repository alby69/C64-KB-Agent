---
title: base:populating_several_related_arrays_from_a_single_macro [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Apopulating_several_related_arrays_from_a_single_macro
category: reference
topics: []
difficulty: beginner
language: none
hardware:
- KERNAL
- CIA
related:
- keyboard-handling
- cia-registers
- memory-map
- kernal-routines
- joystick-reading
scraped_at: '2026-07-14'
---

# base:populating_several_related_arrays_from_a_single_macro [Codebase64 wiki]

Often, you have set of data, you need to put in several arrays. For example, in a demo, for each effect you could have init address (2 bytes), run address (2 bytes), and number of frames to run.

One easy way to group these together is by using segments.

First, add segments to your config file, as usual:

```
SEGMENTS
{
	INITLO: load=RAM1, type=ro;
	...
}
```
Secondly, add labels at the beginning of each segment. NOTE: It's critical this is done before putting any data in them!

.segment "INITLO" InitLo: .segment "INITHI" InitHi: .segment "RUNLO" RunLo: .segment "RUNHI" RunHi: .segment "NUMFRAMES" NumFrames:

Thirdly, create a macro, that takes all related information as arguments:

.macro RegisterEffect init, run, numframes .segment "INITLO" .byte <init .segment "INITHI" .byte >init .segment "RUNLO" .byte <run .segment "RUNHI" .byte >run .segment "NUMFRAMES" .byte numframes ;.segment "EMPTY" .endmacro

This becomes more powerful, when you use given information to automatically calculate entries for other arrays.

NOTE: It's adviced to add [Safeguard against putting data in wrong segment](https://codebase.c64.org/doku.php?id=base:safeguard_against_putting_data_in_wrong_segment) at the end of macro!

Then fourthly, populate your arrays:

RegisterEffect plasmainit, plasmarun, 200 RegisterEffect invaderinit, invaderrun, 50 RegisterEffect realtimeraytraceinit, realtimeraytracerun, 250

Oh, and fifthly, use array contents in your code. The entries will be in the order they were linked in.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`INITLO`** (unknown): No description available

```assembly
SEGMENTS
{
	INITLO: load=RAM1, type=ro;
	...
}
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`InitLo`** (unknown): No description available
- **`InitHi`** (unknown): No description available
- **`RunLo`** (unknown): No description available
- **`RunHi`** (unknown): No description available
- **`NumFrames`** (unknown): No description available

```assembly
.segment "INITLO"
InitLo:
.segment "INITHI"
InitHi:
.segment "RUNLO"
RunLo:
.segment "RUNHI"
RunHi:
.segment "NUMFRAMES"
NumFrames:
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.macro RegisterEffect init, run, numframes
	.segment "INITLO"
	.byte <init
	.segment "INITHI"
	.byte >init
	.segment "RUNLO"
	.byte <run
	.segment "RUNHI"
	.byte >run
	.segment "NUMFRAMES"
	.byte numframes
	;.segment "EMPTY"
.endmacro
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
RegisterEffect plasmainit, plasmarun, 200
	RegisterEffect invaderinit, invaderrun, 50
	RegisterEffect realtimeraytraceinit, realtimeraytracerun, 250
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Apopulating_several_related_arrays_from_a_single_macro](https://codebase.c64.org/doku.php?id=base%3Apopulating_several_related_arrays_from_a_single_macro)*
