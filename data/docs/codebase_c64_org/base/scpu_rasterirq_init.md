---
title: RasterIRQ
source_url: https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_init
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
- CPU
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

# RasterIRQ

base:scpu_rasterirq_init

                # RasterIRQ

Raster Interrupt initialisation code. Grounds NMI and disable IRQ's from CIA Timers.

After all initialisation is completed, the routine clears the interrupt flag and allows an interrupt to occurr once a raster IRQ is triggered by the raster compare value passed to the routine.

Standard Memoryconfiguration set to RAM+IO

| SYNTAX: | :RasterIRQ RasterCompareValue : VectorIRQ | ||
| EXAMPLE: | :RasterIRQ 52 : #IRQ | ||
| cli | |||
| jmp * | |||
| IRQ: rti | |||
| PARAMETERS: | Type | Minimum | Maximum | 
| RasterCompareValue | U9 | 0 | 312 | 
| VectorIRQ | Label | N/A | N/A | 

```
    .pseudocommand RasterIRQ RasterCompareValue : IRQVector {
        sei
        :NativeMode            // Switch to 658C16 Native CPU mode
        :BitMode16             // Switch to 16 bit registers
        :lda #$007f
        sta $dc0d              // Disable CIA #1 Interrupts
        lda $dc0d              // Acknowledge pending CIA #1 Interrupts
        :RasterCompare RasterCompareValue.getValue()
        :lda #$0101
        sta $d019              // Ack. Raster IRQ and enable Raster IRQ
        :lda #$352f
        sta $00                // Bank all RAM except IO
        :lda #IRQVector.getValue()
        sta $ffee              // Set IRQ Vector.
        cli                    // Clear Interrupt Flag - Allow IRQs to trigger
                               // IRQ Interrupt Handler.
    }
```
base/scpu_rasterirq_init.txt · Last modified:  by 127.0.0.1

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.pseudocommand RasterIRQ RasterCompareValue : IRQVector {
        sei
        :NativeMode            // Switch to 658C16 Native CPU mode
        :BitMode16             // Switch to 16 bit registers
        :lda #$007f
        sta $dc0d              // Disable CIA #1 Interrupts
        lda $dc0d              // Acknowledge pending CIA #1 Interrupts
        :RasterCompare RasterCompareValue.getValue()
        :lda #$0101
        sta $d019              // Ack. Raster IRQ and enable Raster IRQ
        :lda #$352f
        sta $00                // Bank all RAM except IO
        :lda #IRQVector.getValue()
        sta $ffee              // Set IRQ Vector.
        cli                    // Clear Interrupt Flag - Allow IRQs to trigger
                               // IRQ Interrupt Handler.
    }
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_init](https://codebase.c64.org/doku.php?id=base%3Ascpu_rasterirq_init)*
