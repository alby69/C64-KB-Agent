---
title: The elusive Cougar
source_url: https://elite.bbcelite.com/deep_dives/the_elusive_cougar.html
category: deep-dive
topics: []
difficulty: intermediate
language: basic
hardware:
- KERNAL
- CPU
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# The elusive Cougar

## They say it is vanishingly rare... but just how rare is the mysterious Cougar?

The BBC Master, 6502 Second Processor, Commodore 64 and NES versions of Elite have a ship that doesn't appear in the early versions at all, and which you only see in the wild in those later versions if you are very lucky indeed. Sure, it makes an appearance on the Master's title screen, rotating above the "Press Fire or Space, Commander" prompt, but out in the black? That's another story, because the [Cougar](https://elite.bbcelite.com/6502sp/main/variable/ship_cougar.html) is a rare beast indeed.

But just how rare is she? Let's see if we can work it out mathematically...

![The Cougar in the BBC Master version of Elite](https://elite.bbcelite.com/images/master/cougar.png) 

						During the main game loop's spawning routine (which happens in [1 out of 256 main loop iterations](https://elite.bbcelite.com/6502sp/main/subroutine/main_game_loop_part_2_of_6.html)), all the following have to happen in sequence:

- [Skip asteroid spawning](https://elite.bbcelite.com/6502sp/main/subroutine/main_game_loop_part_2_of_6.html)(87% chance)
- [Skip cop spawning](https://elite.bbcelite.com/6502sp/main/subroutine/main_game_loop_part_3_of_6.html)(0.4% chance)
- [Skip Thargoid spawning](https://elite.bbcelite.com/6502sp/main/subroutine/main_game_loop_part_4_of_6.html)(3.2% chance)

This means that there is a 0.011% chance of spawning a Cougar during each ship spawning routine, which is around 1 in 9000 ship spawnings.

To put this in context, it takes 6400 kills to become Elite, so it is quite possible to go all the way to Elite without seeing a Cougar... though if you're in the 6502 Second Processor version, you can at least capture the event with a screenshot.

## Cloaking device

													 ---------------

						The Cougar is not only vanishingly rare, it's also vanishing... literally. There is some debate about whether the Cougar appears on the scanner, as there are rumours that it has a cloaking device that hides it from prying eyes. In the 6502 Second Processor version, the Cougar does appear on the scanner, in very obvious cyan, but in the later Commodore 64 and BBC Master versions, it does indeed have a cloaking device that hides it from the 3D ellipse.

Whether or not this is intentional is an interesting question, as the cloaking-device effect is caused by a change in ship type between the two versions. In the 6502 Second Processor version, the Elite logo is ship type 32 and the Cougar is ship type 33, and the entries in the [scacol](https://elite.bbcelite.com/6502sp/main/variable/scacol.html) table ensure that the logo is hidden from the scanner, while the Cougar is visible. In the Commodore 64 and BBC Master versions, there is no Elite logo as it's only used in the [demo mode](https://elite.bbcelite.com/6502sp_demo_mode.html) that is unique to the Second Processor version, so the gap closes up, with the Cougar inheriting the logo's old type of 32. The [scacol](https://elite.bbcelite.com/master/main/variable/scacol.html) table, however, remains unchanged, so the Cougar inherits the logo's scanner colour, and gets hidden from the scanner. Was this intentional, or just a happy accident of removing the Elite logo? Presumably only the scientists of Her Majesty's Space Navy know the answer...

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elusive_cougar.html](https://elite.bbcelite.com/deep_dives/the_elusive_cougar.html)*
