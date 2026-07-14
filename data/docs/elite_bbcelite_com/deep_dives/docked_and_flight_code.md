---
title: Swapping between the docked and flight code
source_url: https://elite.bbcelite.com/deep_dives/docked_and_flight_code.html
category: manual
topics:
- basic
- raster interrupts
- assembly
- graphics
difficulty: beginner
language: mixed
hardware:
- BASIC ROM
- SID
- KERNAL
related:
- sound-programming
- music-player
- raster-interrupts
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Swapping between the docked and flight code

## Using a disc drive to swap out the game binaries when launching and docking

For BBC Micro users, the launch of Elite drew a line in the sand: you either had a disc drive, or you missed out. Prior to the game's launch in late 1984, games on the BBC Micro were pretty much the same whether they came on floppy disc or cassette, bar the obvious difference that games loaded in seconds from disc while they took minutes to load from tape. But waiting aside, the gaming experience was typically the same.

Elite blew all of this out of the water. The cassette version of Elite was great, and squeezed every ounce of performance out of the BBC's 32K of RAM (leaving almost no free memory in its wake - see the [BBC Micro cassette Elite memory map](https://elite.bbcelite.com/the_elite_memory_map.html) for details). I started on the cassette version, and I fell in love with it. But for those of us poring over the manual and control guide, it hurt to be a lowly tape user, because a noticeable number of features had asterisks next to them, indicating that they were only present in the disc version.

![The docking computer in action in the disc version of BBC Micro Elite](https://elite.bbcelite.com/images/disc/docking_computer.png) 

						More ships! Military lasers! Asteroid mining! Extended system descriptions! Better enemy tactics! Missions! A proper docking computer! Bitstik support! The list went on. And OK, perhaps nobody really cared about the last one, but this exotic menu of extra features was utterly mouthwatering for those of with our noses pressed up against the glass. To see what I mean, check out the [feature comparison table](https://elite.bbcelite.com/compare/feature_comparison.html) for a comprehensive list of all the extra features in the disc version.

I, like many others, starting saving up for a disc drive specifically to play the enhanced disc version of Elite, and although it took ages to get there, it was worth every single penny. The BBC Micro disc version is now regarded as the canonical version of Elite, and quite right too.

In this article, we'll take a look at how Bell and Braben managed to fit so many extra features into the disc version, by splitting the codebase into two parts: the docked code and the flight code.

## T.CODE, D.CODE and the ship blueprint files

													 -------------------------------------------

						If you look at the disc contents for the BBC Micro disc version of Elite, there are an awful lot of files on there:

![The contents of the disc for the BBC Micro disc version of Elite](https://elite.bbcelite.com/images/disc/disc_contents.png) 

						Most of these files - the ones called D.MOA to D.MOP - contain different combinations of ship blueprints, and one of these files gets loaded every time we launch from the station or do a hyperspace jump. These are discussed in the deep dive on [ship blueprints in the BBC Micro disc version](https://elite.bbcelite.com/ship_blueprints_in_the_disc_version.html).

The files we are interested in here are called T.CODE and D.CODE, which contain the docked code and the flight code respectively. The directory prefixes are slightly confusing: the "T" in "T.CODE" presumably stands for "Trade", as that's the code that's loaded when we are docked and you can only trade items when inside the station. But the "D" in "D.CODE" is less obvious, as this is the code that's loaded when we launch into space; whatever the "D" stands for, it definitely doesn't stand for "Docked", so don't get confused by that.

When the game is first run from disc, the game data is loaded and stored in various parts of the memory map; the memory layout is described in detail in the [BBC Micro disc Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_disc.html), but let's cover the most important aspects here.

The process starts by loading the game data, so the text tokens in [QQ18](https://elite.bbcelite.com/disc/text_tokens/variable/qq18.html) go at address &0400, the trigonometry lookup tables at [SNE](https://elite.bbcelite.com/disc/text_tokens/variable/sne.html) go at &07C0, the missile blueprint in [SHIP_MISSILE](https://elite.bbcelite.com/disc/missile_ship_blueprint/variable/ship_missile.html) is stored after screen memory at &7F00, and so on. Next, the following bits of code are loaded between address &1100 to &11E1: the palettes in [TVT1](https://elite.bbcelite.com/disc/loader_3/variable/tvt1.html), the interrupt handler for the split-screen mode in [IRQ1](https://elite.bbcelite.com/disc/loader_3/subroutine/irq1.html), the last saved commander file in [S1%](https://elite.bbcelite.com/disc/loader_3/variable/s1_per_cent.html) and [NA%](https://elite.bbcelite.com/disc/loader_3/variable/na_per_cent.html), and the break handler for the flight code in [BRBR1](https://elite.bbcelite.com/disc/loader_3/subroutine/brbr1.html). The [CATD](https://elite.bbcelite.com/disc/loader_3/subroutine/catd.html) routine is also loaded into the NMI workspace at &0D7A - see below for more about that.

All of this code and data stays in memory for the duration of the game, leaving a gap in the memory map from &11E2 all the way to the start of screen memory at &6000. This is where the main game binary is loaded: when the game first starts, when we dock at a station or when we die in space, the docked code in T.CODE gets loaded at &11E2. When we launch from the space station, the flight code in D.CODE gets loaded at &11E2, which in turn loads one of the D.MOA to D.MOP ship blueprint files to address &5600. And when we hyperspace, the flight code remains in-place and we load a different ship blueprint file to address &5600.

![The launch tunnel in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/launch.png) 

						This approach enables us to cram more functionality into the game, at the expense of a short pause for loading when switching between the station and space. The T.CODE binary contains all the routines that are needed to run the game while docked, so it covers buying and selling cargo, equipping our ship, mission briefings, the ship hangar and so on. Meanwhile the D.CODE binary contains all the flight code, along with the ship blueprints that contain the 3D wireframes.

There is quite a bit of code that appears in both the docked and flight code: the maths routines, the system charts, the Inventory and Status Mode screens, the text-printing routines... all of these are needed by both the docked and flight code, so they appear in both T.CODE and D.CODE (though typically at different addresses, as the docked and flight code binaries are assembled separately).

The docked code doesn't take up the entire block of available memory, and it even contains a number of routines that are never called. As part of his development of Elite-A, Angus Duggan identified and removed almost all of these unused routines, to make room for his improvements; see the deep dive on [making room for the modifications in Elite-A](https://elite.bbcelite.com/elite-a_making_room_for_the_modifications.html) for details.

In contrast, the flight code is absolutely jam-packed, with hardly any spare memory (though Angus still managed to find some spare memory for Elite-A, which is quite a feat). Between them, the main flight code and ship blueprint file take up every single byte between &11E2 and the start of screen memory at &6000. They only manage to fit because the main flight code doesn't contain the two-letter token table at [QQ16](https://elite.bbcelite.com/disc/docked/variable/qq16.html) (unlike the docked code, which does contain this table). This data is still needed during flight, however, so just before it loads the flight code, the docked code moves its own copy of this 64-byte token table to location &0880, so the flight code can access it there (the copying is done in routine [TT110](https://elite.bbcelite.com/disc/docked/subroutine/tt110.html) which gets called when the launch key is pressed). See the [BBC Micro disc Elite memory map](https://elite.bbcelite.com/the_elite_memory_map_disc.html) for more details on how this fits into memory.

Let's take a closer look at the process of swapping the docked and flight code.

## Swapping between the docked and flight code

													 -------------------------------------------

						When we launch from the space station, the game loads and runs the flight code with a simple *RUN D.CODE command in the [RDLI](https://elite.bbcelite.com/disc/docked/variable/rdli.html) variable. The load and execution address of D.CODE are both set to &11E3, and the first instruction in the D.CODE binary at [S%](https://elite.bbcelite.com/disc/flight/workspace/s_per_cent.html) is a jump to [DEEOR](https://elite.bbcelite.com/disc/flight/subroutine/deeor.html) in the flight code, which decrypts the binary and jumps into the flight loop to display the space view.

![The launch view of Lave in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/ellipses/lave.png) 

						Things are slightly more complex when going the other way, as there are two ways to leave the flight code: by docking, or by dying. When docking, we want to load the docked code, display the ship hangar and show the Status Mode screen. When dying, we want to load the docked code and jump to the title screen.

The flight code deals with these two scenarios by editing the command string that we use to load the docked code. The command string lives in the [LTLI](https://elite.bbcelite.com/disc/flight/variable/ltli.html) variable, and by default it contains a *LOAD T.CODE command, which is the command we run when we die in space (we'll look at this below). However, if we execute a successful docking, then the [DOENTRY](https://elite.bbcelite.com/disc/flight/subroutine/doentry.html) routine in the flight code changes this command to *RUN T.CODE instead, which is executed in the flight code's [INBAY](https://elite.bbcelite.com/disc/flight/subroutine/inbay.html) routine. The load and execution address of T.CODE are both set to &11E3, and the first instruction in the T.CODE binary at [S%](https://elite.bbcelite.com/disc/docked/workspace/s_per_cent.html) is a jump to [DOENTRY](https://elite.bbcelite.com/disc/docked/subroutine/doentry.html) in the docked code, which shows the ship hangar, checks for mission progression and shows the Status Mode screen.

![The Status Mode screen in the BBC Micro disc version of Elite](https://elite.bbcelite.com/images/disc/status_mode.png) 

						So what happens if we die in space, with the command still left at *LOAD T.CODE? Well, the docked code in T.CODE gets loaded at its load address of &11E3, and then the CPU continues executing instructions as if nothing had happened. The load command is executed in the flight code's [INBAY](https://elite.bbcelite.com/disc/flight/subroutine/inbay.html) routine, which calls the operating system's OSCLI routine with a JSR, so when the T.CODE file has been loaded, execution continues with the instruction after the JSR OSCLI instruction... which has now been replaced by the docked code.

To make this work, the first few bytes of both the T.CODE and D.CODE files have the exact same structure. At the start of each binary is a workspace called S% that contains the following:

- A JMP instruction to the entry point that is called when this file is *RUN
- A JMP instruction to start the game
- A JMP instruction to the text-printing routine; CHRV points here
- An address for the IRQ1 routine; IRQ1V points here
- A JMP instruction for the break handler; BRKV points here

You can see these two workspaces at [S% in the docked code](https://elite.bbcelite.com/disc/docked/workspace/s_per_cent.html) and [S% in the flight code](https://elite.bbcelite.com/disc/flight/workspace/s_per_cent.html). Putting these five instructions at the start of each binary and in the same structure lets each binary provide different addresses for the entry points, text, interrupt and break handlers. Simply loading the new binary will update the addresses that the vectors point to, so they automatically point to the correct addresses in the newly loaded binary.

Note that the second entry is slightly different: the final step of the [LOAD](https://elite.bbcelite.com/disc/loader_3/subroutine/load.html) routine in the game loader is a JMP S%+3 instruction, which jumps to the second instruction in the docked code's S% workspace to start the game. In the flight code, this second instruction is never used, but is there to ensure all the other addresses line up with the docked code.

The S% workspace is followed by the INBAY routine. [INBAY in the flight code](https://elite.bbcelite.com/disc/flight/subroutine/inbay.html) contains three instructions that run the OS command to load the docked code. [INBAY in the docked code](https://elite.bbcelite.com/disc/docked/subroutine/inbay.html) also contains three instructions with the exact same format, but they are placeholders that are never run, as they simply exist to ensure the next instruction - a JMP SCRAM instruction - appears at the correct place in memory, i.e. just after the three instructions that perform the *LOAD. This ensures that when the JSR OSCLI instruction in the flight code returns after *LOADing the docked code over the top of the currently executing flight code, execution continues with the next instruction, which is now the JMP SCRAM instruction that we just loaded. And the jump to [SCRAM](https://elite.bbcelite.com/disc/docked/subroutine/scram.html) restarts the game, which is what we want to do when we die.

## Saving the disc catalogue with CATD

													 -----------------------------------

						If you look at the [memory map](https://elite.bbcelite.com/the_elite_memory_map_disc.html) for the BBC Micro disc version of Elite, you'll see that the [WP workspace](https://elite.bbcelite.com/disc/docked/workspace/wp.html) from &0E00 to &0FD2 uses the same memory as the DFS disc catalogue. On DFS discs, the disc catalogue takes up sectors 0 and 1, and the Disc Filing System loads these two sectors into pages &E and &F, so it can work with the disc's file catalogue data in-memory before saving it back to disc. Elite uses the same part of memory for the WP workspace, where it stores flight-specific data such as line heaps and stardust coordinates. This is acceptable as the flight code doesn't require disc access (you can only save or load commander files when docked).

![A space station in BBC Micro cassette Elite](https://elite.bbcelite.com/images/cassette/docking_checks.png) 

						The only issue is that using this part of memory for flight data obviously corrupts the disc catalogue that normally lives there, so before doing any disc activity, Elite calls the [CATD](https://elite.bbcelite.com/disc/loader_3/subroutine/catd.html) routine at &0D7A, which reloads sectors 0 and 1 into pages &E and &F. This routine is itself tucked away in the middle of the DFS workspace, this time in a safe spot in the NMI vector workspace that persists between disc operations, so the CATD routine persists throughout the game.

But doesn't the DFS simply reload the catalogue itself from sectors 0 and 1 when it needs to access a disc? It does, but it only does this when necessary; specifically, if the disc is still spinning in the drive, the DFS assumes that the catalogue in memory is still present and correct. It only reloads the catalogue when it spins the disc up again.

So if we didn't have the CATD routine, there's a specific edge-case that would otherwise crash the game. If we launched from the space station without CATD, then the game would load D.CODE and a ship blueprint file into memory, as normal, and we would launch into space. However, if we immediately paused the game and pressed ESCAPE to restart the game, and we did this before the disc had a chance to stop spinning, then the game would try to load the docked code in T.CODE, but by this point we've already corrupted the catalogue in the DFS workspace, so we would get a "Not found" disc error that would hang the game (see the next section for more details). So to fix this issue, the game calls CATD to reload the catalogue before it tries to load T.CODE, which guarantees that it will work.

You can see this in action in Elite-A, as Angus removed the CATD routine to make way for the updated scanner in [iff_index](https://elite.bbcelite.com/elite-a/loader/subroutine/iff_index.html). As a result, Elite-A will crash if you launch, pause and press ESCAPE before the disc has stopped spinning, demonstrating the bug that the disc version of Elite fixes with CATD.

## Handling disc and system errors

													 -------------------------------

						The final thing to mention about this code-swapping process are the three break handlers.

The loader sets up a break handler called [BRBR1](https://elite.bbcelite.com/disc/loader_3/subroutine/brbr1.html), which is loaded into permanent memory just before the docked or flight code (as mentioned above). This break handler is used by the flight code, and it is extremely basic: it simply prints a newline, followed by the system error message in the block pointed to by (&FD &FE), which is where the disc filing system will put any disc errors (such as "Not found", "Disc fault" and so on). After printing the error message, it hangs the computer. This is only used for fatal errors, such as the "Not found" error that's shown if you remove the game disc from drive 0, replace it with a different disc (such as your disc of saved games!) and then try to hyperspace, at which point the flight code will try to load a non-existent ship blueprint file and will hang the game with a "Not found" error at that point. Ask me how I know...

For the docked code, there is a slightly more civilised break handler at [BRBR](https://elite.bbcelite.com/disc/docked/subroutine/brbr.html), which restarts the game to display the title screen, where the error pointed to by (&FD &FE) gets displayed without having to hang the computer.

![The disc access menu in BBC Micro disc Elite](https://elite.bbcelite.com/images/disc/disk_access_menu.png) 

						On top of this, there is a third break handler at [MEBRK](https://elite.bbcelite.com/disc/docked/subroutine/mebrk.html) that is used when saving or loading commander files; this handler makes a beep and prints the system error message in the block pointed to by (&FD &FE). It then waits for a key press and returns to the disc access menu. This ensures that any disc errors in the disc access menu are handled gracefully, in case the user tries to load or delete a non-existent file, for example.

In summary, BRBR is the standard BRKV handler for the docked part of the game, and it's swapped out to MEBRK for disc access operations only. When the flight code loads, it switches to the BRBR1 break handler until the docked code is loaded once more. This ensures that errors are handled as gracefully as possible, depending on which part of the codebase is loaded.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/docked_and_flight_code.html](https://elite.bbcelite.com/deep_dives/docked_and_flight_code.html)*
