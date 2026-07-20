---
title: Interrupts and timing
source_url: https://codebase.c64.org/doku.php?id=base%3Ainterrupts
category: reference
topics:
- raster interrupts
- assembly
- sprite programming
difficulty: beginner
language: assembly
hardware:
- CPU
- KERNAL
- CIA
- VIC-II
related:
- keyboard-handling
- memory-map
- joystick-reading
- sprite-programming
- kernal-routines
- cia-registers
- vic-ii-registers
- raster-interrupts
scraped_at: '2026-07-20'
---

# Interrupts and timing

base:interrupts

                ### Table of Contents

# Interrupts and timing

Interrupts can be trigged by the CIA chips and the VIC chip, and they are mostly used to trig specific pieces of code at regular intervals. In demo and game coding, timing is often crucial, and programmers may need to use cycle exact timing to achieve things like stable rasterbars. However, timing is not only about setting up interrupts. It can also be achieved through delay loops and simply by keeping track of exactly how many cycles it takes for a certain code snippet to execute.

## IRQ's and timing in general

- [Introduction to raster irqs](https://codebase.c64.org/doku.php?id=base:introduction_to_raster_irqs)- by Oswald / Resource
- [Introduction to timer interrupts](https://codebase.c64.org/doku.php?id=base:timerinterrupts)- A listing
- [Handling IRQs with some simple macros](https://codebase.c64.org/doku.php?id=base:handling_irqs_with_some_simple_macros)- How to handle all IRQ stuff easy - by rambones/Ancients
- [NMI Lock](https://codebase.c64.org/doku.php?id=base:nmi_lock)“disable” NMI - by Ninja/The Dreams
- ["Disable" NMI wihout use of kernal](https://codebase.c64.org/doku.php?id=base:nmi_lock_without_kernal)- by Sokrates
- [Surviving Restore key presses while using CIA2 timer NMIs](https://codebase.c64.org/doku.php?id=base:restore_and_cia_2)- by White Flame
- [Quick exit from interrupt](https://codebase.c64.org/doku.php?id=base:quick_exit_from_interrupt)- Neat trick to save one cycle when quitting an interrupt - text by Frantic, trick invented by someone else.
- [cycle exact measuring of routine execution times](https://codebase.c64.org/doku.php?id=base:cycle_exact_measuring_of_routine_execution_times)- when coloring the border won't do - by tfg, inspired by M. Abrash

## Stable timing

- [Making stable raster routines](https://codebase.c64.org/doku.php?id=interrupts:making_stable_raster_routines)- By Marko Mäkelä (for C64 and Vic-20)
- [Missing Cycles](https://codebase.c64.org/doku.php?id=magazines:chacking3#the_demo_cornermissing_cycles)- Syncing with a sprite by Pasi 'Albert' Ojala (C=Hacking 3)
- ["Stable timing approaches"](https://codebase.c64.org/doku.php?id=base:stable_timing_-_jackasser)- Article series by Jackasser/Instinct
- [Stable Raster Routine](https://codebase.c64.org/doku.php?id=base:stable_raster_routine)- Non cryptic explination by TWW / Creators
- [Improved Clock Slide](https://codebase.c64.org/doku.php?id=base:improved_clockslide)by lft
- [Stable Raster with Lightpen](https://codebase.c64.org/doku.php?id=base:stable_raster_with_lightpen)- Kruthers
- [Shortest Stable Raster (PAL/NTSC)](https://codebase.c64.org/doku.php?id=base:shortest_stable_raster)by Erhan

### Routines

- [Double IRQ stable interrupt](https://codebase.c64.org/doku.php?id=base:double_irq)- Sourcecode by Fungus
- [Delay](https://codebase.c64.org/doku.php?id=base:delay)- subroutine to delay a variable amount of cycles via branch and nops - by Yago.
- [Using a Timer as an Inverted Raster X-Pos Register](https://codebase.c64.org/doku.php?id=base:using_a_timer_as_an_inverted_raster_x-pos_register_method)- by Hermit Soft
- [Detecting 6526 vs 6526A CIA chips](https://codebase.c64.org/doku.php?id=base:detecting_6526_vs_6526a_cia_chips)- since they have a timer phase difference of 1 cycle - by White Flame
- [a_fffe_irq.zip](https://codebase.c64.org/lib/exe/fetch.php?media=sourcecode:airqfffeb.zip:a_fffe_irq.zip)- (An $fffe timed irq by Terric/Meta. Rev 2) Need fix or should be deleted
- [Stable IRQ with DMA](https://codebase.c64.org/doku.php?id=base:stable_irq_with_dma)- by ChristopherJam
- [Frame skipping](https://codebase.c64.org/doku.php?id=base:frame_skipping)- by Mace
- [Double irq explained](https://codebase.c64.org/doku.php?id=base:double_irq_explained)- Double interrupts by TheHighlander 2015
- [The Ninja-Method: NMIs and distributed jitter-correction routines](https://codebase.c64.org/doku.php?id=base:nmis_and_distributed_jitter-correction_routines)- by St0fF/Neoplasia^theObsessedManiacs

## Advanced program flow

About complex execution flow such as multiple interrupt handlers at the same time, threaded code, and similar. This usually involves interrupts in one way or another.

- [Launching long tasks from IRQ handler](https://codebase.c64.org/doku.php?id=base:launching_long_tasks_from_irq_handler)- by Bitbreaker/Oxyron^Nuance
- [Threads on the 6502](https://codebase.c64.org/doku.php?id=base:threads_on_the_6502)- an example on how threads can be used efficiently on the 6502 processor.

base/interrupts.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ainterrupts](https://codebase.c64.org/doku.php?id=base%3Ainterrupts)*
