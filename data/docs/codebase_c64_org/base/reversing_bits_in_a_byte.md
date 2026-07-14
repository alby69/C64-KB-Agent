---
title: Reversing bits in a byte
source_url: https://codebase.c64.org/doku.php?id=base%3Areversing_bits_in_a_byte
category: tool
topics:
- basic
- assembly
difficulty: intermediate
language: assembly
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# Reversing bits in a byte

base:reversing_bits_in_a_byte

                # Reversing bits in a byte

If you quickly need to flip the bits in a byte in reverse (turning bits from 01234567 to 76543210) you can use this unrolled loop.

```
        ldx #0
.for(var i=0;i<8;i++)
{
        lsr // shift A down, bit 0 to C
        tay // copy to Y doesn't change C
        txa // pull x to a, doesn't change C
        rol // shift left, C to bit 0
        tax // stash a in x
        tya // get start a back from y
}
        txa
```
(kickassembler loop syntax)

This takes a byte in A, reverses the bits and exits with the reversed bits in A again, using X and Y for temporary storage and only short 2-cycle instructions in the loop. Of course a table lookup will be faster if you do this a lot in your code.

– this would be equally fast, at 100cycl +rts (enter with the value in .A, result in .A, .X will be 0)

```
        ldx #8
loop    asl 
        ror $2
        dex
        bne loop
        lda $2
        rts
```
or unrolled (56 cycl +rts):

```
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        lda $2
        ror
        rts
```
– Optimized version, at 84cycl +rts (enter with the value in .A, result in .A)

sta $02 ; 3 lda #1 ; 2 lp: ror $02 ; 5 rol ; 2 bcc lp ; 3(2) ; =84 rts

or slightly unrolled:

sta $02 ; 3 lda #1 ; 2 lp: ror $02 ; 5 rol ; 2 ror $02 ; 5 rol ; 2 bcc lp ; 3(2) ; =72 rts

base/reversing_bits_in_a_byte.txt · Last modified:  by cz

## Codice Estratto

### Snippet Codice (BASIC)

```basic
ldx #0
.for(var i=0;i<8;i++)
{
        lsr // shift A down, bit 0 to C
        tay // copy to Y doesn't change C
        txa // pull x to a, doesn't change C
        rol // shift left, C to bit 0
        tax // stash a in x
        tya // get start a back from y
}
        txa
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`loop`** (unknown): No description available

```assembly
ldx #8
loop    asl 
        ror $2
        dex
        bne loop
        lda $2

        rts
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        ror $2
        asl 
        lda $2
        ror
        rts
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`lp`** (unknown): No description available

```assembly
sta	$02	; 3
	lda	#1	; 2
lp:
	ror	$02	; 5
	rol		; 2
	bcc	lp	; 3(2)
			; =84
	rts
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`lp`** (unknown): No description available

```assembly
sta	$02	; 3
	lda	#1	; 2
lp:
	ror	$02	; 5
	rol		; 2
	ror	$02	; 5
	rol		; 2
	bcc	lp	; 3(2)
			; =72
	rts
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Areversing_bits_in_a_byte](https://codebase.c64.org/doku.php?id=base%3Areversing_bits_in_a_byte)*
