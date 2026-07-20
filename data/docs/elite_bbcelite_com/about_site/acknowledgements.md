---
title: Acknowledgements
source_url: https://elite.bbcelite.com/about_site/acknowledgements.html
category: source-code
topics:
- raster interrupts
- assembly
- basic
difficulty: advanced
language: mixed
hardware:
- KERNAL
- SID
- CPU
related:
- sid-registers
- sound-programming
- vic-ii-registers
- memory-map
- kernal-routines
- music-player
- sprite-programming
- raster-interrupts
scraped_at: '2026-07-20'
---

# Acknowledgements

On this page you can find information on copyright, as well as the people whose work has made this project possible.

## Copyright notices

						                             -----------------

						The following copyright notices apply to the contents of this site and the accompanying repositories.

- BBC Micro Elite was written by Ian Bell and David Braben and is copyright © Acornsoft 1984.
- Acorn Electron Elite was written by Ian Bell and David Braben and is copyright © Acornsoft 1984.
- 6502 Second Processor Elite was written by Ian Bell and David Braben and is copyright © Acornsoft 1985.
- Commodore 64 Elite was written by Ian Bell and David Braben and is copyright D. Braben and I. Bell 1985.
- Apple II Elite was written by Ian Bell and David Braben and is copyright D. Braben and I. Bell 1986.
- BBC Master Elite was written by Ian Bell and David Braben and is copyright © Acornsoft 1986.
- Elite-A was written by Angus Duggan, and is an extended version of the BBC Micro disc version of Elite; the extra code is copyright © Angus Duggan.
- NES Elite was written by Ian Bell and David Braben and is copyright © D. Braben and I. Bell 1991/1992.
- The commentary is copyright © Mark Moxon. Any misunderstandings or mistakes in the documentation are entirely my fault.

The code on this site is based on the following sources:

- For the BBC Micro cassette, 6502 Second Processor, Commodore 64 and Apple II versions, the code on this site is identical to the source discs released on [Ian Bell's personal website](http://www.elitehomepage.org/)(it's just been reformatted to be more readable).
- For the Electron, BBC Micro disc, BBC Master and NES versions, the code on this site has been reconstructed from a disassembly of the original game binaries from the same site.
- For Elite-A, the code on this site is identical to Angus Duggan's source discs (it's just been reformatted, and the label names have been changed to be consistent with the sources for the original BBC Micro disc version on which it is based).

## A big thank you to the following

						                             --------------------------------

						Huge thanks are due to the following, without whom this project would simply not exist:

- Ian Bell and David Braben, the original authors of Elite, for not only creating such an important piece of my childhood, but also for releasing [the source code](http://www.elitehomepage.org/)for us to play with.
- Kieran Connell for his [BeebAsm version of the source code](https://github.com/kieranhj/elite-beebasm), which I forked as the original basis for this project. Also, I owe a huge thank you to Kieran for being the inspiration for[musical Elite](https://elite.bbcelite.com/hacks/bbc_elite_with_music.html),[Teletext Elite](https://elite.bbcelite.com/hacks/teletext_elite.html)and[Elite 3D](https://elite.bbcelite.com/hacks/elite_3d.html)- without his algorithms, code suggestions and thoughtful testing, these wonderful hacks would never have happened.
- Paul Brink for his annotated disassembly of the BBC Micro disc version's [docked code](http://www.elitehomepage.org/archive/a/d4090010.txt)and[flight code](http://www.elitehomepage.org/archive/a/d4090012.txt).
- Martin Ling for his [commentary script](https://github.com/martinling/elite-beebasm/commits/apply-brink-commentary), which gave me a massive head start by merging Paul's comments into Kieran's repository.
- Angus Duggan for sending me his Elite-A source discs and giving me permission to analyse his code.
- Christian Pinder for lots of expertise from the coalface of Elite disassembly, and for [Elite: The New Kind](http://www.new-kind.com/), whose[source](https://github.com/fesh0r/newkind)helped me out on more than one occasion.
- Chris Jordan for help and feedback on all sorts of Elite-related matters.
- Kroc Camen for his excellent [Elite Harmless](https://github.com/Kroc/elite-harmless)project, which is an invaluable resource when working with the Commodore 64 version of Elite.
- Mark Usher for loads of Econet-related help and support, without which the [multiplayer scoreboard](https://elite.bbcelite.com/hacks/elite_over_econet_scoreboard.html)in Elite over Econet probably wouldn't work.
- Matt Godbolt for the wonderful online BBC Micro emulator [JSBeeb](https://bbc.xania.org/).
- 0xC0DE for the equally wonderful online Acorn Electron emulator [Electroniq](https://0xc0de6502.github.io/electroniq/)and his hugely impressive[Electron development environment](https://stardot.org.uk/forums/viewtopic.php?t=30087&start=60).
- Tom Seddon for the amazing [b2 emulator](https://github.com/tom-seddon/b2), which is the best emulator I have used on any platform, period. It is a work of art!
- Diminished for the UEF scripts that I use in the BBC Micro cassette and Acorn Electron builds, which are part of the excellent [Quadbike 2](https://stardot.org.uk/forums/viewtopic.php?t=26669)tape transcriber.
- Jarod Nash for helping improve Elite over Econet's [FixPAGE utility](https://elite.bbcelite.com/hacks/elite_over_econet_downloads.html), and for setting up the amazing TNMoC Econet Cloud service that enables Elite competitions to span the whole planet.
- Wouter Hobers for creating [sideways RAM Electron Elite](https://www.stardot.org.uk/forums/viewtopic.php?p=406189#p406189), which opened the door for my own version.
- Mark Keates for many things, including inspiring me to look at the Elite Demonstration Disc, doing amazing things with the Atari conversions (as [Wrathchild on AtariAge](https://forums.atariage.com/profile/1822-wrathchild/)), and being so supportive of my efforts over the years.

You can find out more in the [about this project](https://elite.bbcelite.com/about_this_project.html) page.

Also, thank you to everyone who has written in with comments, and particularly these kind souls who spotted things that I missed or explained things I didn't understand:


- Mike Standing for pointing out the hidden message in the [disc version's loader](https://elite.bbcelite.com/disc/loader_3/subroutine/load.html), where the authors ask "Does your mother know you do this?" - I can't believe I missed that one! Thanks Mike.
- TobyLobster for discovering a bug in the [LOIN](https://elite.bbcelite.com/cassette/main/subroutine/loin_part_3_of_7.html)routine in the original versions of Elite, where some lines omit the pixel from the wrong end of the line; and for help in working out the[FAROF2](https://elite.bbcelite.com/nes/bank_7/subroutine/farof2.html)algorithm in the NES version. Thanks Toby! (Incidentally, if you enjoy high-quality BBC Micro disassemblies, I highly recommend Toby's[Manic Miner 2021](https://github.com/TobyLobster/ManicMiner2021)and[Jet Set Willy 2021](https://github.com/TobyLobster/jsw2021)projects; they are simply brilliant.)
- SteveF for pointing out a mistake in the [BBC Master memory map](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_master.html), where I'd got my MOS ROM addresses mixed up. Thank you, Steve.
- Michael Fairbank for spotting a really neat way to speed up circle drawing in [Teletext Elite](https://elite.bbcelite.com/hacks/teletext_elite.html), and for his analysis into[ellipses](https://elite.bbcelite.com/deep_dives/drawing_ellipses.html),[craters](https://elite.bbcelite.com/deep_dives/drawing_craters.html),[meridians and equators](https://elite.bbcelite.com/deep_dives/drawing_meridians_and_equators.html)and[the loading screen's Saturn](https://elite.bbcelite.com/deep_dives/drawing_saturn_on_the_loading_screen.html). Thanks Michael.
- Chris Evans for help tracking down a really gnarly bug in [Teletext Elite](https://elite.bbcelite.com/hacks/teletext_elite.html)(and also for the awesome[beebjit](https://github.com/scarybeasts/beebjit)emulator, which I've found particularly useful when analysing the original releases of all the games I've disassembled). Thank you, Chris.
- Wouter Hobers for explaining the Electron's [IRQ1](https://elite.bbcelite.com/electron/main/subroutine/irq1.html)routine properly (which I hadn't!) and for spotting that it clears all interrupts and not just the RTC. Thanks Wouter.
- Timothy Muller for spotting a number of incorrect cargo capacity figures in the original Elite-A encyclopedia, and for sending me the correct values to add to the [bug-fix release of Elite-A](https://elite.bbcelite.com/elite-a/releases.html#bug-fix). Thank you, Timothy.
- Peter Mackay for suggesting a much cleaner build process for NES Elite that removes the need to declare cross-bank label addresses in the [common variables](https://elite.bbcelite.com/nes/all/common.html)source. Thanks Peter.
- Roman for pointing out that the Moray never gets spawned in any version of Elite (except Elite-A, which has a different spawning system). I had no idea, but looking at the spawning code in [part 4 of the main flight loop](https://elite.bbcelite.com/disc/flight/subroutine/main_game_loop_part_4_of_6.html#label_2), it's absolutely true! Thank you, Roman.
- Stardot user cola5pandex for explaining the subtleties behind 6845 register 10, which we use to disable the cursor in [B%](https://elite.bbcelite.com/cassette/loader/variable/b_per_cent.html). Thanks cola5pandex.
- Michael Bellamy for spotting that my kill calculations for the [combat ranks](https://elite.bbcelite.com/deep_dives/combat_rank.html)were off by a factor of two - whoops! Thank you, Michael.
- Flavio Machado for kindly pointing out an error in my summary of the NES docking fee system. Thanks, Flavio.
- Stardot user TheCiscoKid for spotting a number of subtle issues with the commentary, and for inspiring me to document [aggression and hostility](https://elite.bbcelite.com/deep_dives/aggression_and_hostility_in_ship_tactics.html)properly. Thank you, TheCiscoKid.
- James Sargent for letting me know the correct clock speed for the [ARM Evaluation System](https://elite.bbcelite.com/deep_dives/6502sp_tube_communication.html), and for sending me down a[fascinating rabbit hole](https://groups.google.com/g/comp.arch/c/hPsDLEPf2eo/m/nvJR_d7nnyYJ?pli=1)in the process. Thanks, James.

Thanks to everyone who has contributed.

## A note on licences, copyright etc.

						                             ----------------------------------

						This site and the accompanying repositories are not provided with a licence, and there is intentionally no LICENSE file provided in the repositories.

According to GitHub's licensing documentation, this means that "the default copyright laws apply, meaning that you retain all rights to your source code and no one may reproduce, distribute, or create derivative works from your work".

The reason for this is that my commentary is intertwined with the original source code for Elite, and the original source code is copyright. The whole site is therefore covered by default copyright law, to ensure that this copyright is respected.

Under GitHub's rules, you have the right to read and fork the repositories... but that's it. No other use is permitted, I'm afraid.

My hope is that the educational and non-profit intentions of this repository will enable it to stay hosted and available, but the original copyright holders do have the right to ask for it to be taken down, in which case I will comply without hesitation. I do hope, though, that along with the various other disassemblies and commentaries of this source, it will remain viable.

---
*Fonte originale: [https://elite.bbcelite.com/about_site/acknowledgements.html](https://elite.bbcelite.com/about_site/acknowledgements.html)*
