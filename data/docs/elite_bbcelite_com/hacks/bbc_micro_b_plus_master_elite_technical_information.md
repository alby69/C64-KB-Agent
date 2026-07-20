---
title: Technical information for BBC Master Elite on the BBC Micro B+
source_url: https://elite.bbcelite.com/hacks/bbc_micro_b_plus_master_elite_technical_information.html
category: source-code
topics:
- memory management
- assembly
- graphics
- basic
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CPU
- CIA
related:
- sid-registers
- sound-programming
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- cia-registers
scraped_at: '2026-07-20'
---

# Technical information for BBC Master Elite on the BBC Micro B+

## Squeezing full colour BBC Master Elite into the weird extra memory on the B+

![A transporter in the BBC Master version of Elite](https://elite.bbcelite.com/images/master/transporter_station.png) 

						The BBC Micro B+ has 64K of RAM, double that of the original BBC Micro's 32K. It turns out that this is just enough memory to load the BBC Master version of Elite, but using that extra RAM for program space is not as simple as you might hope. In this article, I'll look at how we can use this extra memory to run the full version of BBC Master Elite on the unexpanded BBC Micro B+.

If you want to see exactly how the code for the Compendium version of Elite differs from the code in the original Acornsoft version, you can check out the compendium-related branches in the accompanying repositories:

- See the [bbc-micro-b-plus branch](https://github.com/markmoxon/elite-source-code-bbc-master/tree/bbc-micro-b-plus/1-source-files/main-sources)for modifications related to the standard version of BBC Master Elite on the BBC Micro B+.
- The [bbc-micro-b-plus-music branch](https://github.com/markmoxon/elite-source-code-bbc-master/tree/bbc-micro-b-plus-music/1-source-files/main-sources)for modifications related to the musical version of BBC Master Elite on the BBC Micro B+.

You can search the source code files in these branches for "Mod:" to see every single modification that I've made to the original code to produce the Compendium version.

## The B+ memory map

													 -----------------

						The B+ memory map is almost identical to the standard BBC Micro, just with 32K tacked onto the side. This extra 32K is split into two parts: 20K of shadow RAM and 12K of so-called "private RAM".

Note that the B+ comes with the MOS 2.00 operating system rather than the MOS 1.20 of the original BBC, but this doesn't affect the memory map in any significant way, and for the purposes of Elite we can ignore any differences between the two.

The original BBC Micro already uses the full 64K address allocation that the 6502 can support; it's split into 32K of user RAM from &0000 to &7FFF and 32K of ROM from &8000 to &FFFF. So it's no surprise that the extra 32K of RAM in the B+ is tacked on "sideways", just like sideways RAM in the standard Beeb. We can then switch the various banks in and out by poking to specific memory-mapped locations.

When you switch on the B+, the memory map is identical to the standard BBC Micro; neither shadow RAM nor private RAM are enabled by default, and instead 32K of RAM is mapped to &0000-&7FFF, where it is split into screen memory, user RAM and operating system workspaces. Let's refer to this standard memory setup as "normal RAM", to distinguish it from the extra shadow RAM and private RAM in the B+.

In this configuration, the B+ behaves exactly like the standard BBC Micro, with screen memory taking up the top part of user RAM. Consider the situation where we turn on our B+ and switch to screen mode 1; the upper part of the memory map will look like this:

+-----------------------------------+ &FFFF | | | Machine Operating System (MOS) | | | +-----------------------------------+ &C000 | | | | | Paged ROMs | | | | | +-----------------------------------+ &8000 | | | | | | | | | | | Screen memory for mode 1 | | | | | | | | | | | +-----------------------------------+ &3000 | | | User RAM | | | +-----------------------------------+ &1100 | | : : : :

The B+ comes with the DFS disc filing system fitted as standard, so memory below &1100 has the same structure as for the BBC Micro, so it's a mixture of DFS workspaces, MOS workspaces, user RAM, the 6502 stack and zero page; see the [BBC Micro disc Elite memory map](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_disc.html) for details.

As for the amount of usable memory, it's pretty small, because screen memory takes up a whopping 20K from &3000 to &7FFF, leaving just 7936 bytes of user RAM from &1100 to &2FFF. This is where the extra memory on the B+ comes in to play, in the form of 20K of shadow RAM and 12K of private RAM.

These two banks can be paged into the memory map independently. When shadow RAM is enabled, screen memory is stored in this extra 20K of RAM, leaving the entire block of normal RAM for the user; when private RAM is enabled, it is paged into the first 12K of sideways RAM space at &8000.

Here's the same part of the B+ memory map when both shadow RAM and private RAM are enabled and we are in shadow screen mode 1:

+-----------------------------------+ &FFFF | | | Machine Operating System (MOS) | | | +-----------------------------------+ &C000 | | | +-- &B000 --------------------------+ | Paged ROMs | | | | Private RAM | | | | +-----------------------------------+-- &8000 --------------------------+ | | | | | | | | | | | | | | | | | Shadow RAM (screen memory) | | | | | User RAM | | | | | | | | | | | | +-- &3000 --------------------------+ | | | | | | +-----------------------------------+ &1100 | | : : : :

For the purposes of Elite, this is great; enabling shadow RAM gives us a huge block of user RAM from &1100 to &7FFF that we can fill with the BBC Master game code, and if we also page in private RAM, that extends user RAM into a continuous block of memory from &1100 to &AFFF. That's just under 40K, which is almost big enough to contain BBC Master Elite.

As you can see, the extra RAM is bolted onto the side of normal RAM, and we can switch banks in and out of the memory map, just as we can with sideways ROM. Not surprisingly, this approach is very similar to the BBC Master, except the Master splits the 12K of private RAM into two chunks that the MOS itself then uses: 8K is allocated to filing system workspace under the name HAZEL, and 4K is used for VDU and function key workspace under the name ANDY. The Master also has an additional four 16K banks of sideways RAM that can be paged into &8000 in the standard way.

On top of this, the Master also adds a lot more fine-grained control over its extra memory. The B+ is rather more limited, so let's look at how we can access the extra memory on the B+ in our attempt to use it for Elite.

## Enabling shadow RAM

													 -------------------

						We can enable shadow RAM on the B+ by simply changing to a screen mode with bit 7 set (so screen mode 128+n is the same as screen mode n, but with shadow RAM enabled). So in the memory maps above, the top map is in screen mode 1, while the bottom map is in screen mode 129. When shadow RAM is enabled, the computer stores screen memory in shadow RAM, leaving normal RAM for the user.

This switching to shadow RAM is typically handled by the MOS operating system. Specifically, when shadow RAM is enabled, any VDU code in the operating system ROM will now write into shadow RAM instead of normal memory, and the hardware displays the contents of shadow RAM on-screen. If your program uses operating system calls or BASIC to draw to the screen, then shadow RAM will "just work"; the fact that screen memory is now in shadow RAM rather than normal RAM is hidden from the user.

Of course, games like Elite don't go anywhere near the operating system's comparatively slow graphics routines; they poke directly into screen memory. The upshot is that if you enable shadow RAM and try running Elite, then the game will appear to do nothing at all, as when it pokes into screen memory, it will actually update normal RAM rather than shadow RAM. And if we try to squeeze the rather large BBC Master version of Elite into our B+ by loading the game code from &1100 to &AFFF, that means Elite will poke the game's graphics into normal RAM *where the game binary lives*, and that will definitely not end well.

So we need some way of poking graphics into shadow RAM instead of normal RAM. A first thought is that there are two operating system OSWORD calls (OSWORD 5 and 6) that support poking into shadow RAM, but just like the operating system's graphics routines, they are far too slow for drawing fast game graphics into screen memory.

The BBC Master version of Elite gets around this using the Access Control Register at SHEILA &34 (i.e. &FE34). Bits 0 to 3 of this register give us fine-grained control over the screen memory structure, so to update the screen we simply need to switch shadow RAM into the memory map from &3000-&7FFF, write to the correct screen memory address, and switch normal RAM back in. We have to ensure that the code doing the switching and drawing isn't within the shadow RAM range, as otherwise we will end up paging out our switching code while it is trying to run, which would crash the computer by trying to execute screen memory instead of program code. But that's the only limitation, and the Access Control Register also lets us control which bank of memory is currently being used to display the screen - normal RAM or shadow RAM - so it's possible to implement double buffering for smooth animation, where we show one screen while updating the hidden screen, and then swap them over with a simple flick of one bit. Elite on the BBC Master doesn't use double buffering, but the hardware does at least support it.

Unfortunately things aren't quite as flexible on the B+. On the B+, SHEILA &34 has just one bit, bit 7, which enables or disables shadow RAM, and that's it. When shadow RAM is enabled, it is used for screen memory and its contents are displayed on-screen, and when it isn't, normal RAM is used for screen memory and its contents are displayed on-screen. On top of this, you can only write to shadow RAM if it is currently enabled and being used to display the screen; you can't write to shadow RAM otherwise. In other words, if shadow RAM is not enabled, it effectively disappears completely; you simply can't access it. This means that shadow RAM on the B+ can't be used for double buffering, as you can't update the hidden screen. Luckily this isn't an issue for Elite, as it doesn't use double-buffering, but it does explain why the extra memory on the B+ isn't particularly useful for gaming.

So we clearly need to enable shadow RAM on the B+ if we're to be able to fit BBC Master Elite into the available memory, but there's another problem, as the B+ doesn't let us switch &3000-&7FFF between normal RAM and shadow RAM. Instead, when shadow RAM is enabled, code in normal RAM between &3000 and &7FFF can't see shadow RAM. The 6502 uses 16-bit addresses, so all addresses in this range are taken to refer to normal RAM, not shadow RAM. This means that code that runs in normal RAM can only see normal RAM, so if Elite tries to write directly to screen memory when shadow RAM is enabled, it will instead overwrite itself, and it will crash horribly.

The solution to this problem lies with the private RAM, so let's look at that next.

## Enabling private RAM

													 --------------------

						Private RAM in the B+ maps into sideways ROM space from &8000 to &AFFF, so it works a bit like a 12K block of sideways RAM. We can enable private RAM using bit 7 of the ROM Select latch at SHEILA &30 (i.e. &FE30).

In the standard BBC Micro, the ROM Select latch is used to page one of the 16K sideways ROMs into address &8000 to &BFFF. We do this by storing the ROM number into bits 0-3 of &FE30 (bit 7 is ignored). There's also a RAM copy of SHEILA &30 in address &00F4 that must be updated as well, just before we write to &FE30, so switching ROMs is actually a two-instruction process, as follows (where A contains the ROM number):

STA &00F4 STA &FE30

In the BBC Micro B+, this ROM-switching process works in exactly the same way, but bit 7 of SHEILA &30 can also be set to page private RAM into &8000 to &AFFF. If bit 7 is set, the ROM number in bits 0-3 determines which ROM is paged into &AFFF to &BFFF, just after the end of private RAM, though only the upper 4K of that ROM is paged in, with private RAM mapping to the first 12K.

This approach has its limitations. Not only is the private RAM space smaller than the standard 16K of normal sideways ROMs, but if we use private RAM to store a language ROM, then the language will not be retained as the current language if BREAK is pressed. And unlike sideways RAM on the B+128 and Master, there are no handy star-commands for loading code into private RAM, so in practice, private RAM isn't much use for sideways ROM images. When the B+128 added 64K of sideways RAM and the associated *SRLOAD star-command, this was the final nail in private RAM's coffin; it remains an overlooked and underused feature of the B+, an afterthought following the much more useful addition of 20K of shadow RAM.

But private RAM has a killer feature - or, at least, the top 4K of it does. When code that lives between &A000 and &AFFF writes to a screen memory address between &3000 and &7FFF, it will always write into the currently displayed screen memory. So if shadow RAM is enabled, code running in the top 4K of private RAM will always write into shadow RAM (and if shadow RAM is disabled, it will write into normal RAM).

This is all part of a hardware-based solution to the challenge of supporting both normal and shadow screen modes. In the B+, certain code in the system is classed as "VDU driver code", depending on the address of that code in memory. Specifically, all code in the region &C000-&DFFF is treated as a VDU driver, and so is the top 4K of private RAM in &A000-&AFFF. Code at the same address in a normal sideways ROM is not classed as VDU driver code; this is a unique property of private RAM.

VDU driver code is special, in that it will access shadow RAM, if selected, when the operand address is in the range &3000-&7FFF. This means that only the top 4K of private RAM (&A000-&AFFF) and the bottom 8K of the MOS operating system ROM (&C000-&DFFF) can write to shadow RAM. No other code has any idea that shadow RAM even exists, so code in &0000-&9FFF and in normal sideways ROMs will always write into normal RAM. And when shadow RAM is disabled, it completely disappears for everyone, even the VDU driver code.

This means that Elite can still update the screen directly even when we have shadow RAM enabled. We just have to make sure the screen-poking is performed by VDU driver code, which we can do by putting the relevant screen-poking routines into the top 4K of private RAM between &A000 and &AFFF.

Let's take a look at that process now.

## Writing VDU driver code for Elite

													 ---------------------------------

						Luckily Elite is reasonably amenable to conversion into VDU driver code. The screen-drawing code is limited to a handful of routines that poke graphics directly into screen memory:

- Pixel-drawing routines: [PIXEL](https://elite.bbcelite.com/master/main/subroutine/pixel.html),[CPIXK](https://elite.bbcelite.com/master/main/subroutine/cpixk.html)
- Line-drawing routines: [LOINQ](https://elite.bbcelite.com/master/main/subroutine/loinq_part_1_of_7.html),[HLOIN](https://elite.bbcelite.com/master/main/subroutine/hloin.html)
- Dashboard routines: [SCAN](https://elite.bbcelite.com/master/main/subroutine/scan.html),[ECBLB](https://elite.bbcelite.com/master/main/subroutine/ecblb.html),[SPBLB](https://elite.bbcelite.com/master/main/subroutine/spblb.html),[MSBAR](https://elite.bbcelite.com/master/main/subroutine/msbar.html),[DILX](https://elite.bbcelite.com/master/main/subroutine/dilx.html),[DIL2](https://elite.bbcelite.com/master/main/subroutine/dil2.html)
- Ship hangar routines: [HANGER](https://elite.bbcelite.com/master/main/subroutine/hanger.html),[HAS2](https://elite.bbcelite.com/master/main/subroutine/has2.html),[HAL3](https://elite.bbcelite.com/master/main/subroutine/hal3.html),[HAS3](https://elite.bbcelite.com/master/main/subroutine/has3.html)
- Text-drawing routines: [CHPR](https://elite.bbcelite.com/master/main/subroutine/chpr.html)
- Screen-clearing routines: [TTX66](https://elite.bbcelite.com/master/main/subroutine/ttx66.html),[ZES2](https://elite.bbcelite.com/master/main/subroutine/zes2.html),[CLYNS](https://elite.bbcelite.com/master/main/subroutine/clyns.html)

One approach would be to move all of these routines into the address range &A000-&AFFF, as they would then update screen memory in shadow RAM. I suspect this would be possible, but it would mean restructuring the game code to a fairly high degree. BBC Master Elite stores all of the game data in the top part of memory above &8000, and as some of these data tables are pretty huge, we'd need to shuffle a lot of code and data if we wanted to squeeze the above routines into the top 4K of private RAM.

A much easier approach is to replace just the screen-poking parts. Examining the above routines, it turns out there are only eight different variations of code that poke into screen memory. The most popular is this snippet:

EOR (SC),Y \ Draw a pixel using EOR logic STA (SC),Y

This draws a byte into screen memory using EOR logic, so it merges the pixels we are drawing with whatever is already on-screen. Other variations include drawing using OR logic, poking directly into screen memory without checking what's already there, drawing to an address in a different zero-page variable to SC(1 0), and so on.

So the easiest solution is to write eight subroutines to implement all eight variations, and place them into the address range &A000-&AFFF so they act as VDU driver code. We can then replace all the original screen pokes with JSR calls to these new routines, so the above code gets changed to the following, for example:

```
   JSR DrawPixelEOR       \ Perform the EOR/STA instructions from &A000-&AFFF
                          \ so they affect screen memory in shadow RAM
```
						The DrawPixelEOR then looks a bit like this:

.DrawPixelEOR EOR (SC),Y \ Draw a pixel using EOR logic STA (SC),Y RTS \ Return from the subroutine

As long as DrawPixelEOR is in the top 4K of private RAM, this will enable Elite to draw directly into screen memory in shadow RAM.

My main concern with this approach was speed. We are effectively wrapping JSR and RTS instructions around every single screen poke, which might not matter much for screen-clearing or text-drawing routines, but surely it slows things down for the line and pixel routines? Luckily Elite is pretty frugal with its screen-poking, and the space view is mostly pure black, so this code-injection approach doesn't noticeably slow down the game. Elite spends most of its time on the complicated maths needed to calculate which pixels to draw, rather than the drawing itself, and the Master contains fast, log-based multiplication and division routines that the original BBC Micro versions didn't have room for. On top of that, a lot of its code is unrolled - the line-drawing routines in particular - and these speed-ups comfortably offset the hit from calling the VDU driver code in this way.

In the end I had to shrink the size of the VDU driver routines to fit them into the top part of private RAM along with all the large text tables (see the next section for more on this). As a result I had to use shared entry points and BIT hacks to reduce the code size, but the concept remains the same. This is what the entire VDU driver looks like for B+ Elite, all 35 bytes of it:

```
  .DrawPixelEOR
  
   EOR (SC),Y             \ Draw a pixel using EOR logic
  
   EQUB &2C               \ Skip the next instruction by turning it into
                          \ &2C &91 &06, or BIT &0691, which does nothing
                          \ apart from affect the flags
  
  .DrawPixelORA
  
   ORA (SC),Y             \ Draw a pixel using OR logic
   STA (SC),Y
  
   RTS                    \ Return from the subroutine
  
  .DrawDialPixels4
  
   STA (SC),Y             \ Draw the shape of the mask on pixel row Y of the
                          \ character block we are processing
  
   INY                    \ Increment Y to draw the next pixel
  
  .DrawDialPixels3
  
   STA (SC),Y             \ Draw the shape of the mask on pixel row Y of the
                          \ character block we are processing
  
   INY                    \ Draw the next pixel row, incrementing Y
   STA (SC),Y
  
   INY                    \ And draw the third pixel row, incrementing Y and
                          \ falling through into DrawPixelSTA
  
  .DrawPixelSTA
  
   STA (SC),Y             \ Draw the pixel into screen memory
  
   RTS                    \ Return from the subroutine
  
  .DrawPixelP2
  
   EOR (P+2),Y            \ EOR this value with the existing screen contents
                          \ of P(3 2), which is equal to SC(1 0) + 8, the
                          \ next four pixels along from the first four pixels
                          \ we just plotted in SC(1 0)
  
   STA (P+2),Y            \ Store the Y-th byte at the screen address for this
                          \ character location
  
   RTS                    \ Return from the subroutine
  
  .DrawPixelAND
  
   AND (SC),Y             \ Check the pixel and set the flags
  
   RTS                    \ Return from the subroutine
  
  .DrawBoxCorners
  
   STA &4000              \ Set locations &4000 and &41F8 to the correct
   STA &41F8              \ colour, as otherwise the top-left and top-right
                          \ corners will be black (as the lines overlap at
                          \ the corners, and the EOR logic used by LOINQ
                          \ will otherwise make them black)
  
   RTS                    \ Return from the subroutine
```
						It took quite a while to track down the last bit of screen-poking code and move it into the DrawBoxCorners routine, as this bit of code is in a different format to the rest of the screen routines. Until I replaced them with VDU driver code, these instructions would corrupt the main game code at addresses &4000 and &41F8, which meant the game randomly did some very strange things as I worked on the squeezing the code into the B+.

Talking of which, let's look at that squeezing process in more detail.

## Fitting Master Elite into the B+

													 --------------------------------

						If you look at the [memory map for BBC Master Elite](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_master.html), it almost feels like the shape of the extra memory on the B+. Unfortunately, "almost" isn't good enough, so we need to break out the shoehorn.

There are three main challenges if we're to fit BBC Master Elite into an unexpanded B+:

- The Master version uses memory from &0E41 to &1100 that the B+ uses for DFS workspace.
- The Master version uses the whole of zero page, even the parts that are used by NMI handlers and filing systems.
- The Master's main game code runs from &1300 to &B1FF, while shadow RAM and private RAM on the B+ cover &1100 to &AFFF. This is an exact match, but some shuffling is required, especially if we want to include any extra features.

In the end, this is how I restructured the memory layout of BBC Master Elite to work on the B+ (address ranges are inclusive in the following):

| Workspace | Master | B+ | 
|---|---|---|
| ZP | &0000-&00E3 | &0000-&008E &00D1-&00E1 &0900-&0910 | 
| K% | &0400-&05BB | Unchanged | 
| LS% | &0800 down | Unchanged | 
| Hangar heap | &0B00 | Unchanged | 
| WP | &0E41-&12A9 | &0932-&0A90 | 
| UP | &2C40-&2C60 | &0911-&0930 | 
| Main code | &1300-&7F47 | &1100-&7FC3 | 
| Data | &8000-&B1FF | &8000-&AFDC | 

Moving memory around is always a complicated process, even with a fully documented and buildable source code, so here are some notes on the above:

- On the BBC Master, Elite uses the whole of zero page, up to and including &00E3. This means Elite uses the filing system and NMI workspaces, amongst others. When the game needs to use the filing system, for example when loading commander files from disc, it uses an approach first developed for the Commodore 64 version of Elite. When it starts up, the game copies the top half of zero page into a buffer in shadow RAM, and when it needs to access the disc, it swaps zero page with this copy, accesses the disc, and swaps it back. This ensures that Elite's variables don't get corrupted by disc activity, and that zero page is in the correct format that the disc filing system expects.
 I started out by reimplementing the Master's[getzp](https://elite.bbcelite.com/master/main/subroutine/getzp.html)and[setzp](https://elite.bbcelite.com/master/main/subroutine/setzp.html)routines, using VDU driver code to copy between zero page and an unused portion at the bottom of shadow RAM, just like the Master. But this proved to be unreliable, so instead I copied the zero page structure from the BBC Micro disc version, which deals with the same challenge by avoiding those parts of zero page that the disc filing system and NMIs use (it frees up enough space by moving the key logger into main memory). This removed the need for a zero page swap process in the B+ version, and as the BBC Micro and BBC Micro B+ are so similar, it works nicely. (Note that the swap system proved unreliable at a point in the development where I still had some rogue screen-poking routines corrupting the main game binary, so this might have been the problem; it's hard to tell!)
- As noted in the previous section, the VDU driver code lives in the top part of private RAM, specifically from &AFDD to &AFFF.
- In moving the UP workspace out of the main game binary and into page 9, I left the last variable ([VOL](https://elite.bbcelite.com/master/main/workspace/up.html#vol)) in-place in the main game code, so it still gets initialised with a value of 7.
- To maintain a tidy split between the game code (below &8000) and the game data (&8000 and above), I moved the [SNE](https://elite.bbcelite.com/master/game_data/variable/sne.html),[ACT](https://elite.bbcelite.com/master/game_data/variable/act.html),[RUGAL](https://elite.bbcelite.com/master/game_data/variable/rugal.html)and[RUPLA](https://elite.bbcelite.com/master/game_data/variable/rupla.html)tables into main memory.
- Moving variables out of zero page is a more complicated process than you might imagine, as the authors of Elite were big fans of offset branching using P%. Offset branching uses the program counter in P% to build the destination for a branch, so BEQ P%+4, for example, will skip over the two bytes following the branch instruction when the Z flag is set (we use P%+4 because the BEQ instruction is two bytes and we want to skip another two). This works fine, unless the next two bytes happen to be an instruction that loads a value from a zero page variable that we have just moved; this is because LDA addr is a two-byte instruction if addr is in zero page, but it's a three-byte instruction if addr is in main memory. So if we just moved addr from zero page to main memory, we have to hunt for any P%+n references that might break as a result. Moving the key logger out of zero page required a lot of changes.
- There's a similar challenge when replacing screen-poking code with JSRs to VDU driver code. In the above section we looked at replacing EOR (SC),Y and STA (SC),Y with a JSR DrawPixelEOR instruction, which is a change from four bytes of code to three bytes of code. It turns out that the unrolled line-drawing routines at [LOINQ](https://elite.bbcelite.com/master/main/subroutine/loinq_part_1_of_7.html)and[HLOIN](https://elite.bbcelite.com/master/main/subroutine/hloin.html)use offset branching to skip the drawing code, but this time using offsets from labels, so there are lots of instructions of the form BEQ LI100+6, which in this case skips the first three two-byte instructions after the label LI100. Unfortunately the second and third instructions are the EOR and STA that we want to replace with a JSR, so BEQ LI100+6 needs to become BEQ LI100+5 to avoid branching one byte too far. Even more insidiously, the fourth instruction after LI100 is a DEX, so leaving the BEQ instruction alone won't crash the game, but it will make line-drawing go noticeably wrong. Tracking down this kind of issue is a whole process in itself!

The only other point to note about converting Elite from the Master to the B+ are the slightly different instruction sets used by the two machines. The B+ has a 6512 CPU, which is almost identical to the original BBC Micro's 6502 CPU (the difference is that the clock is internal in the 6502 but external in the 6512). The Master has a 65SC12 CPU, which supports some very handy extra instructions such as PLX, PLY, STZ and BRA. Elite doesn't go all-in on these new instructions, as the source is very much derived from the original BBC Micro, Commodore 64 and Apple II versions, but there are some examples that need converting into 6502 code that will run on the B+.

Luckily all BBC computers use the same 2MHz clock, including the B+ and the Master, so any speed difference in converting 65SC12 code into 6502 is negligible, and the game runs just as well on a B+ as on a Master.

As a final point, I also had room to fit in all the extra features in the BBC Master version of Compendium Elite, including music for those computers with sideways RAM (such as the BBC Micro B+128). You can read more about these changes in the article on [technical information for the Elite Compendium](https://elite.bbcelite.com/elite_compendium_technical_information.html).

And that is how you squeeze BBC Master Elite into the unexpanded BBC Micro B+. I think it was worth the effort...

## Codice Estratto

### Snippet Codice (BASIC)

```basic
+-----------------------------------+   &FFFF
  |                                   |
  | Machine Operating System (MOS)    |
  |                                   |
  +-----------------------------------+   &C000
  |                                   |
  |                                   |
  | Paged ROMs                        |
  |                                   |
  |                                   |
  +-----------------------------------+   &8000
  |                                   |
  |                                   |
  |                                   |
  |                                   |
  |                                   |
  | Screen memory for mode 1          |
  |                                   |
  |                                   |
  |                                   |
  |                                   |
  |                                   |
  +-----------------------------------+   &3000
  |                                   |
  | User RAM                          |
  |                                   |
  +-----------------------------------+   &1100
  |                                   |
  :                                   :
  :                                   :
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
+-----------------------------------+   &FFFF
  |                                   |
  | Machine Operating System (MOS)    |
  |                                   |
  +-----------------------------------+   &C000
  |                                   |
  |                                   +-- &B000 --------------------------+
  | Paged ROMs                        |                                   |
  |                                   |                       Private RAM |
  |                                   |                                   |
  +-----------------------------------+-- &8000 --------------------------+
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |        Shadow RAM (screen memory) |
  |                                   |                                   |
  | User RAM                          |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   |                                   |
  |                                   +-- &3000 --------------------------+
  |                                   |
  |                                   |
  |                                   |
  +-----------------------------------+   &1100
  |                                   |
  :                                   :
  :                                   :
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
STA &00F4
  STA &FE30
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
EOR (SC),Y             \ Draw a pixel using EOR logic
   STA (SC),Y
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
JSR DrawPixelEOR       \ Perform the EOR/STA instructions from &A000-&AFFF
                          \ so they affect screen memory in shadow RAM
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.DrawPixelEOR

   EOR (SC),Y             \ Draw a pixel using EOR logic
   STA (SC),Y

   RTS                    \ Return from the subroutine
```

### Snippet Codice (BASIC)

```basic
.DrawPixelEOR
  
   EOR (SC),Y             \ Draw a pixel using EOR logic
  
   EQUB &2C               \ Skip the next instruction by turning it into
                          \ &2C &91 &06, or BIT &0691, which does nothing
                          \ apart from affect the flags
  
  .DrawPixelORA
  
   ORA (SC),Y             \ Draw a pixel using OR logic
   STA (SC),Y
  
   RTS                    \ Return from the subroutine
  
  .DrawDialPixels4
  
   STA (SC),Y             \ Draw the shape of the mask on pixel row Y of the
                          \ character block we are processing
  
   INY                    \ Increment Y to draw the next pixel
  
  .DrawDialPixels3
  
   STA (SC),Y             \ Draw the shape of the mask on pixel row Y of the
                          \ character block we are processing
  
   INY                    \ Draw the next pixel row, incrementing Y
   STA (SC),Y
  
   INY                    \ And draw the third pixel row, incrementing Y and
                          \ falling through into DrawPixelSTA
  
  .DrawPixelSTA
  
   STA (SC),Y             \ Draw the pixel into screen memory
  
   RTS                    \ Return from the subroutine
  
  .DrawPixelP2
  
   EOR (P+2),Y            \ EOR this value with the existing screen contents
                          \ of P(3 2), which is equal to SC(1 0) + 8, the
                          \ next four pixels along from the first four pixels
                          \ we just plotted in SC(1 0)
  
   STA (P+2),Y            \ Store the Y-th byte at the screen address for this
                          \ character location
  
   RTS                    \ Return from the subroutine
  
  .DrawPixelAND
  
   AND (SC),Y             \ Check the pixel and set the flags
  
   RTS                    \ Return from the subroutine
  
  .DrawBoxCorners
  
   STA &4000              \ Set locations &4000 and &41F8 to the correct
   STA &41F8              \ colour, as otherwise the top-left and top-right
                          \ corners will be black (as the lines overlap at
                          \ the corners, and the EOR logic used by LOINQ
                          \ will otherwise make them black)
  
   RTS                    \ Return from the subroutine
```



---
*Fonte originale: [https://elite.bbcelite.com/hacks/bbc_micro_b_plus_master_elite_technical_information.html](https://elite.bbcelite.com/hacks/bbc_micro_b_plus_master_elite_technical_information.html)*
