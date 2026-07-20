---
title: Threads on the 6502
source_url: https://codebase.c64.org/doku.php?id=base%3Athreads_on_the_6502
category: manual
topics:
- raster interrupts
- assembly
- sprite programming
difficulty: beginner
language: assembly
hardware:
- KERNAL
- CPU
- VIC-II
related:
- memory-map
- sprite-programming
- kernal-routines
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---


# Threads on the 6502

# Threads on the 6502

By Gregg.

Threads on the 6502, at first this might sound to be a little useless on the 6502 or inefficient to implement. But in fact, utilizing the stack, it is really easy, and has quite a few uses. Sometimes it can make code more elegant too.

In this example two threads will be initiated which will use different stack areas. Using a round-robin scheduler running in an irq (context_switch) these threads are ran one after the other. The thread data is stored on the stack, suitably for RTI, so you only need to manually push the register (A, X, Y) values. In the end it comes down to adjusting the stack pointer for each thread. The stack pointer of each thread is stored starting at thread_data.

num_threads = 2 thread_num = $fd ; current thread number ;-------------------------------------------------------------------------- *= $0801 !byte <.eol,>.eol,0,0,$9e !text "2061" .eol: !byte 0,0,0 *= $080d init: sei lda #<context_switch ldx #>context_switch sta $0314 stx $0315 ; initialize threads ldx #0 stx thread_num ; main thread is automatically setup by first irq ; we only need to setup further threads ; split stack tsx txa tay sec sbc #$20 tax txs ; push thread data ; program counter, status register, a, x, y lda #>thread2 pha lda #<thread2 pha lda #0 pha pha pha pha ; save stack pointer tsx txa sta thread_data+1 ; restore old stack pointer tya tax txs cli ; go to main thread jmp thread1 ;-------------------------------------------------------------------------- ; if you're not using the kernal don't forget to save/restore A, X, Y *using the stack*! context_switch: ; save stack pointer ldy thread_num tsx txa sta thread_data,y ; next thread, wraparound iny cpy #num_threads bne nowrap ldy #0 nowrap: sty thread_num ; restore thread lda thread_data,y tax txs jmp $ea31 ;-------------------------------------------------------------------------- ; thread 1 switches the border color thread1: inc $d020 ldy #$01 jsr wait2 jmp thread1 ; thread 2 displays a text message thread2: lda #<msg1 ldy #>msg1 jsr $ab1e ldy #0 jsr wait2 jmp thread2 ; delay a shitload of cycles wait2: - ldx #0 dex bne *-1 dey bne - rts ;-------------------------------------------------------------------------- msg1: !pet "hello, here is thread 2!",13,0 thread_data:

If you don't want to split the stack area (maybe a routine will use lots of stack or you want to use lots of threads) then it's possible to store and refresh the stack area for each thread context.

Using the NMI can also free up the normal IRQ.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
num_threads = 2
thread_num = $fd		; current thread number

;--------------------------------------------------------------------------
		*= $0801
		!byte <.eol,>.eol,0,0,$9e
		!text "2061"
.eol:	!byte 0,0,0


*= $080d

init:	sei
		
		lda #<context_switch
		ldx #>context_switch
		sta $0314
		stx $0315
		
		; initialize threads
		ldx #0
		stx thread_num
		
		; main thread is automatically setup by first irq
		; we only need to setup further threads
		; split stack
		tsx
		txa
		tay
		sec
		sbc #$20
		tax
		txs
		
		; push thread data
		; program counter, status register, a, x, y
		lda #>thread2
		pha
		lda #<thread2
		pha
		lda #0
		pha
		pha
		pha
		pha
		
		; save stack pointer
		tsx
		txa
		sta thread_data+1
		
		; restore old stack pointer
		tya
		tax
		txs

		cli
		; go to main thread
		jmp thread1

;--------------------------------------------------------------------------
; if you're not using the kernal don't forget to save/restore A, X, Y *using the stack*!
context_switch:
		; save stack pointer
		ldy thread_num
		tsx
		txa
		sta thread_data,y
		
		; next thread, wraparound
		iny
		cpy #num_threads
		bne nowrap
		ldy #0
nowrap:
		sty thread_num
		
		; restore thread
		lda thread_data,y
		tax
		txs

		jmp $ea31

;--------------------------------------------------------------------------
; thread 1 switches the border color
thread1:
		inc $d020
		ldy #$01
		jsr wait2
		jmp thread1


; thread 2 displays a text message
thread2:
		lda #<msg1
		ldy #>msg1
		jsr $ab1e
		ldy #0
		jsr wait2
		jmp thread2

; delay a shitload of cycles
wait2:
-		ldx #0
		dex
		bne *-1
		dey
		bne -
		rts

;--------------------------------------------------------------------------
msg1:	!pet "hello, here is thread 2!",13,0
thread_data:
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Athreads_on_the_6502](https://codebase.c64.org/doku.php?id=base%3Athreads_on_the_6502)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).
- **$0314 (IRQ Vector)**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#0314).
