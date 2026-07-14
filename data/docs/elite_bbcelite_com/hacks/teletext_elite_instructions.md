---
title: Instructions for Teletext Elite
source_url: https://elite.bbcelite.com/hacks/teletext_elite_instructions.html
category: manual
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CIA
related:
- keyboard-handling
- joystick-reading
- memory-map
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
---

# Instructions for Teletext Elite

## Full instructions for Teletext Elite on the BBC Micro

![Teletext Elite Status Mode screen](https://elite.bbcelite.com/images/teletext_elite/status.png) 

						Teletext Elite is the full disc version of BBC Micro Elite, and it uses the same keys and has the same playing experience as the original - all changes are purely cosmetic. For details of the controls, check out the [original game manual on Ian Bell's website](http://www.elitehomepage.org/manual.htm).

That said, some very minor differences that enable the game to work in teletext:

- In the Long-range and Short-range Charts, the jump-range circle and system names are initially hidden (as it's almost impossible in teletext to combine moving graphics like the crosshair with colours and text). Instead, you can hold down the reveal button ("R") to reveal more information, just like in Ceefax and Oracle.
- Unlike in the original game, the dashboard in Teletext Elite is not always visible, so using a palette change to indicate an escape pod being fitted wouldn't work very well. To get around this, I have used the same approach as the Acorn Electron version, so the escape pod is listed along with the other equipment in the Status Mode screen, rather than changing the colour of the dashboard.
- When targeting missiles, all the missiles change colour to reflect the current status rather than just the left-hand missile, as there isn't enough room to support individually coloured missiles. Only one missile is actually targeted, though.

Also provided on the disc are four commander files that you can load in the usual way:

- MAX contains a maxed out commander, which makes life a lot easier than using the default commander.
- MISS1 and MISS2 were saved at the points where missions 1 and 2 are about to be triggered; simply launch and re-dock to get the relevant mission's "INCOMING MESSAGE" screen.
- FIGHT was saved just before the Constrictor fight in mission 1; you just have to hyperspace to Orarra to trigger the showdown.

If you are using an emulator, note that modern keyboards don't have the same range of keys as the BBC Micro, or the same layout. In particular, f0 and COPY don't tend to exist anymore, so you may have to check the documentation to see which keys you should press instead.

For example, in JSBeeb, BeebEm and b2, you should press f10 instead of f0 to launch from the station, while in B-em you should press f1 to launch instead. In all these emulators you should press End instead of COPY to pause the game, and while some emulators will emulate the BBC Micro's DELETE key using both Delete and backspace, others may only recognise backspace if you want to unpause again. And as for the "@" key, for the disc access menu, it may be mapped to backtick, it may be mapped to backslash, or it may even be mapped to the "@" key on your keyboard; experimentation pays off here.


													 -----------

						If you pause the game by pressing COPY, then press "X" (you will hear a beep), and then press DELETE to unpause, then not only does this show the authors' names on the title screen (as with the standard game), but if you now visit the Market Prices screen by pressing f7, you will see an homage to Ceefax ticking away in the page header. If you are already looking at the Market Prices screen when you pause and toggle the "X" option, you can see the change happen in front of you.

Page 131 of Ceefax was where the index page of share prices lived, so it seemed like a good page to choose the same page for Galfax, the equivalent in Elite. Incidentally, if you're at all interested in the Ceefax experience, you can explore a genuine set of Ceefax pages from 1983 with the brilliant [An Evening with Ceefax](http://teletext.mb21.co.uk/gallery/ceefax/evening/19831003/index.shtml) - it's highly recommended.

![Teletext Elite with Galfax](https://elite.bbcelite.com/images/teletext_elite/galfax.png) 

						On the subject of TV-based teletext, the system charts make use of the teletext reveal button, to get around the difficulties of combining moving graphics like the crosshair with colours and text. I guess you could say I'm aiming for maximum nostalgia with Teletext Elite - after all, it's a 1984 game, running on a 1981 BBC Micro, using authentic Ceefax page numbers from 1983. Ah, the memories!

---
*Fonte originale: [https://elite.bbcelite.com/hacks/teletext_elite_instructions.html](https://elite.bbcelite.com/hacks/teletext_elite_instructions.html)*
