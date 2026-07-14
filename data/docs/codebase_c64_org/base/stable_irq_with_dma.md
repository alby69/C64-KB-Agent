---
title: Stable IRQ with DMA
source_url: https://codebase.c64.org/doku.php?id=base%3Astable_irq_with_dma
category: reference
topics:
- raster interrupts
- basic
- assembly
difficulty: advanced
language: assembly
hardware:
- VIC-II
- CIA
- KERNAL
related:
- sprite-programming
- keyboard-handling
- cia-registers
- memory-map
- raster-interrupts
- kernal-routines
- vic-ii-registers
- joystick-reading
scraped_at: '2026-07-14'
---


# Stable IRQ with DMA

base:stable_irq_with_dma

                # Stable IRQ with DMA

ChristopherJam's stable IRQ routine using DMA, posted on [http://noname.c64.org/csdb/forums/?roomid=11&topicid=88971](http://noname.c64.org/csdb/forums/?roomid=11&topicid=88971) (cleaned up and converted to ca65 syntax).

.segment "STARTUP" .word basicstub ; load address basicstub: .word @nextline .word 1970 + (.time / 31557600) .byte $9e .byte <(((init / 1000) .mod 10) + $30) .byte <(((init / 100 ) .mod 10) + $30) .byte <(((init / 10 ) .mod 10) + $30) .byte <(((init ) .mod 10) + $30) .byte 0 @nextline: .word 0 init: lda #$04 sta $d021 sta 646 lda #147 jsr $ffd2 lda #0 sta $d021 lda #1 ; something to see sta $0400 lda #2 sta $0428 lda #$7f ; kill CIA irq sta $dc0d sei lda #$35 ; disable ROM sta $01 lda #$01 ; enable VIC irq sta $d01a lda #$1b ; clear high bit of irq rasterline sta $d011 lda #$32 ; last invisible line sta $d012 lda #<irq1 ; set irq vector sta $fffe lda #>irq1 sta $ffff cli loop: inc $07e7 ; a nice untidy main loop to ensure instability! bpl loop jmp loop irq1: pha lda $d019 sta $d019 txa pha tya pha lda #$0f ; this is unstable! sta $d020 lda #$1a ; force partial badline before screen starts sta $d011 lda #$0b ; this is stable ^_^ sta $d020 lda #$1b ; trigger normal re-fetch of first row of chars sta $d011 lda #$ff ; set end-of-screen irq sta $d012 lda #<irq2 sta $fffe lda #>irq2 sta $ffff pla tay pla tax pla rti irq2: pha lda $d019 sta $d019 txa pha tya pha ;ensure first row of chars is already being displayed when badline forced by irq1 lda #$18 sta $d011 lda #$32 sta $d012 lda #<irq1 sta $fffe lda #>irq1 sta $ffff pla tay pla tax pla rti

base/stable_irq_with_dma.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`basicstub`** (unknown): No description available
- **`init`** (unknown): No description available
- **`loop`** (unknown): No description available
- **`irq1`** (unknown): No description available
- **`irq2`** (unknown): No description available

```assembly
.segment "STARTUP"
 
	.word basicstub		; load address
 
basicstub:
	.word @nextline
	.word 1970 + (.time / 31557600)
	.byte $9e
	.byte <(((init / 1000) .mod 10) + $30)
	.byte <(((init / 100 ) .mod 10) + $30)
	.byte <(((init / 10  ) .mod 10) + $30)
	.byte <(((init       ) .mod 10) + $30)
	.byte 0
@nextline:
	.word 0
 
init:
	lda #$04
	sta $d021
	sta 646
	lda #147
	jsr $ffd2
	lda #0
	sta $d021
	lda #1		; something to see
	sta $0400
	lda #2
	sta $0428
 
	lda #$7f	; kill CIA irq
	sta $dc0d
 
	sei
 
	lda #$35	; disable ROM
	sta $01
 
	lda #$01	; enable VIC irq
	sta $d01a
	lda #$1b	; clear high bit of irq rasterline
	sta $d011
	lda #$32	; last invisible line
	sta $d012
 
	lda #<irq1	; set irq vector
	sta $fffe
	lda #>irq1
	sta $ffff
 
	cli
 
loop:
	inc $07e7	; a nice untidy main loop to ensure instability!
	bpl loop
	jmp loop
 
irq1:
	pha
	lda $d019
	sta $d019
	txa
	pha
	tya
	pha
 
	lda #$0f   ; this is unstable!
	sta $d020
	lda #$1a   ; force partial badline before screen starts
	sta $d011
	lda #$0b   ; this is stable ^_^
	sta $d020
	lda #$1b   ; trigger normal re-fetch of first row of chars
	sta $d011
	lda #$ff   ; set end-of-screen irq
	sta $d012
 
	lda #<irq2
	sta $fffe
	lda #>irq2
	sta $ffff
 
	pla
	tay
	pla
	tax
	pla
	rti
 
irq2:
	pha
	lda $d019
	sta $d019
	txa
	pha
	tya
	pha
 
	;ensure first row of chars is already being displayed when badline forced by irq1
	lda #$18
	sta $d011
	lda #$32
	sta $d012
 
	lda #<irq1
	sta $fffe
	lda #>irq1
	sta $ffff
 
	pla
	tay
	pla
	tax
	pla
	rti
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Astable_irq_with_dma](https://codebase.c64.org/doku.php?id=base%3Astable_irq_with_dma)*


### Collegamenti e Riferimenti Hardware
- **$D020 (Border Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d020).
- **$D021 (Background Color)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d021).
- **$D011 (VIC Control Register 1)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d011).
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).
- **$FFD2 (CHROUT (Output Character))**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#ffd2).
