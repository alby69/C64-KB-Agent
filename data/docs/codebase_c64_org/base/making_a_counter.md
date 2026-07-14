---
title: base:making_a_counter [Codebase64 wiki]
source_url: https://codebase.c64.org/doku.php?id=base%3Amaking_a_counter
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# base:making_a_counter [Codebase64 wiki]

base:making_a_counter

                A quite nifty example of how to make an increasing decimal counter with a flexible amount of digits. It's possible to create a counter with up to 255 digits.

Useful for counting scores in games, for example.

```
; Counter code
; [c]2007 Scout/Silicon Ltd.
numdigits = 6
      *=$c000
      ldx #0
      txa         ; A=X=0
-
      sta tellertabel,x   ; erase the countertable
      inx
      cpx #numdigits      ; for the amount of desired digits
      bne -
loop
      ldx #0
-
      lda tellertabel+1,x   ; read the contents of the countertable
      clc
      adc #$30      ; add 48(decimal) -> in petscii, 48=0, 49=1 etc 
      sta $0400,x      ; poke them in the upperleft of the screen (address 1024)
      inx
      cpx #numdigits
      bne -
      jsr teller      ; do the counter
      jmp loop      ; do the loop
;----------------------------------------------------------------
teller
      ldx #numdigits      ; go from back to front in the table
-
      lda tellertabel,x   
      cmp #9         ; is the current digit 9?
      beq +         ; yes, jump to the + branch   
      inc tellertabel,x   ; no, keep on counting
      rts         ; back to the mainroutine
+
      lda #0         ; put current digit to 0
      sta tellertabel,x   ; in the countertable
      dex         ; go 1 back in the table
      bne -         ; and do the rest of the remaining digits
      rts         ; back to the main routine
;-------------------------------------------------------------------
.align 256
tellertabel   ; 256 bytes reserved for the countertable 
```
                    
                                    base/making_a_counter.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (BASIC)

```basic
; Counter code
; [c]2007 Scout/Silicon Ltd.

numdigits = 6


      *=$c000

      ldx #0
      txa         ; A=X=0
-
      sta tellertabel,x   ; erase the countertable
      inx
      cpx #numdigits      ; for the amount of desired digits
      bne -

loop

      ldx #0
-
      lda tellertabel+1,x   ; read the contents of the countertable
      clc
      adc #$30      ; add 48(decimal) -> in petscii, 48=0, 49=1 etc 
      sta $0400,x      ; poke them in the upperleft of the screen (address 1024)
      inx
      cpx #numdigits
      bne -

      jsr teller      ; do the counter

      jmp loop      ; do the loop

;----------------------------------------------------------------

teller
      ldx #numdigits      ; go from back to front in the table
-
      lda tellertabel,x   
      cmp #9         ; is the current digit 9?
      beq +         ; yes, jump to the + branch   
      inc tellertabel,x   ; no, keep on counting
      rts         ; back to the mainroutine
+
      lda #0         ; put current digit to 0
      sta tellertabel,x   ; in the countertable
      dex         ; go 1 back in the table
      bne -         ; and do the rest of the remaining digits
      rts         ; back to the main routine
;-------------------------------------------------------------------

.align 256
tellertabel   ; 256 bytes reserved for the countertable
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Amaking_a_counter](https://codebase.c64.org/doku.php?id=base%3Amaking_a_counter)*
