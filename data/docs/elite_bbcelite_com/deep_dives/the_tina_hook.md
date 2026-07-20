---
title: The TINA hook
source_url: https://elite.bbcelite.com/deep_dives/the_tina_hook.html
category: source-code
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# The TINA hook

## Adding your own custom code to the 6502 Second Processor version using TINA

Programmers of the BBC Micro know all about SHEILA, FRED and JIM, and BBC Master coders are also friendly with LYNNE, HAZEL and ANDY. You don't get far in 6502 assembly language on the Acorn platforms without bumping into one of these important areas of memory, all of which map onto key parts of the system, from the 6522 VIA chips to the Master's shadow RAM. Acorn clearly liked their catchy nicknames.

But the 6502 Second Processor version of Elite introduces a brand new character, TINA, and exactly what she does is a bit of a mystery. Sure, it's easy enough to track her down in the I/O processor's code - she's mentioned at the end of the [STARTUP](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/startup.html#noint) routine, and [TINA](https://elite.bbcelite.com/6502sp/i_o_processor/workspace/tina.html) herself is at &0B00 - but what exactly does TINA do?

It turns out she's quite simple, but quite powerful. If the contents of locations &0B00 to &0B03 contain the string "TINA" (in capital letters), then once the I/O processor code has finished setting up all the handlers for the [Tube communication](https://elite.bbcelite.com/deep_dives/6502sp_tube_communication.html), the code calls location &0B04 with a JSR instruction. This allows us to add a hook to the start-up process by populating page &B with "TINA" plus the code for a subroutine, and it will be called just before the setup code terminates on the I/O processor and the BBC Micro settles into listening for commands from the parasite.

In this way, we could install a driver for some new piece of hardware, or set up an interrupt-driven routine to run in the background on the BBC Micro, all without changing the game code. All we need to do is store the code in &0B00 with the "TINA" header, and it gets run automatically.

I wonder what the original plans were for TINA, as there are no clues in the source code. It's intriguing stuff...

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_tina_hook.html](https://elite.bbcelite.com/deep_dives/the_tina_hook.html)*
