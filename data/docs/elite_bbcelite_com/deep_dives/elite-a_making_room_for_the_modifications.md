---
title: Making room for the modifications in Elite-A
source_url: https://elite.bbcelite.com/deep_dives/elite-a_making_room_for_the_modifications.html
category: deep-dive
topics:
- memory management
- assembly
- basic
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
- CIA
- BASIC ROM
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

# Making room for the modifications in Elite-A

## How Angus Duggan found enough spare memory for Elite-A's modifications

Elite is famous for using practically all of the available memory in the BBC Micro, and a quick glance at the [memory usage for the BBC Micro cassette version](https://elite.bbcelite.com/the_elite_memory_map.html) shows just how tight things are. Angus Duggan's Elite-A is an extended version of the BBC Micro disc version, where the only way of fitting in all the enhanced features was to split the main codebase into two separate files, only one of which is loaded at any one time (one for when were are docked, and the other for when we are flying in space).

For example, Angus had to find a way of adding our current ship type to the Status Mode screen, and extra functionality takes up extra space:

![The Elite-A Status Mode screen](https://elite.bbcelite.com/images/elite-a/status_mode.png) 

						So how did he manage to squeeze so many new features and changes into an already chock-full codebase? Here's a run-down of how he did it.

## Removing unused code

													 --------------------

						The main savings come from stripping out any unused code, of which there is a surprisingly large amount, particularly in the docked code. The original disc version retains a lot of flight-specific code in the docked code that is never actually called, so Angus removed the following routines to free up quite a bit of memory:

- [ABORT](https://elite.bbcelite.com/elite-a/docked/subroutine/abort_removed.html),- [ABORT2](https://elite.bbcelite.com/elite-a/docked/subroutine/abort2_removed.html),- [BAD](https://elite.bbcelite.com/elite-a/docked/subroutine/bad_removed.html),- [BULB](https://elite.bbcelite.com/elite-a/docked/subroutine/bulb_removed.html),- [BUMP2](https://elite.bbcelite.com/elite-a/docked/subroutine/bump2_removed.html),- [CIRCLE](https://elite.bbcelite.com/elite-a/docked/subroutine/circle_removed.html),- [cntr](https://elite.bbcelite.com/elite-a/docked/subroutine/cntr_removed.html),- [CPIX2](https://elite.bbcelite.com/elite-a/docked/subroutine/cpix2_removed.html),- [CPIX4](https://elite.bbcelite.com/elite-a/docked/subroutine/cpix4_removed.html),- [DEEOR](https://elite.bbcelite.com/elite-a/docked/subroutine/deeor_removed.html),- [DENGY](https://elite.bbcelite.com/elite-a/docked/subroutine/dengy_removed.html),- [DET1](https://elite.bbcelite.com/elite-a/docked/subroutine/det1_removed.html),- [DKJ1](https://elite.bbcelite.com/elite-a/docked/subroutine/dkj1_removed.html),- [DOEXP](https://elite.bbcelite.com/elite-a/docked/subroutine/doexp_removed.html),- [DV41](https://elite.bbcelite.com/elite-a/docked/subroutine/dv41_removed.html),- [DV42](https://elite.bbcelite.com/elite-a/docked/subroutine/dv42_removed.html),- [DVID3B2](https://elite.bbcelite.com/elite-a/docked/subroutine/dvid3b2_removed.html),- [EXNO](https://elite.bbcelite.com/elite-a/docked/subroutine/exno_removed.html),- [EXNO2](https://elite.bbcelite.com/elite-a/docked/subroutine/exno2_removed.html),- [EXNO3](https://elite.bbcelite.com/elite-a/docked/subroutine/exno3_removed.html),- [FLIP](https://elite.bbcelite.com/elite-a/docked/subroutine/flip_removed.html),- [Ghy](https://elite.bbcelite.com/elite-a/docked/subroutine/ghy_removed.html),- [GTNMES](https://elite.bbcelite.com/elite-a/docked/subroutine/gtnmes_removed.html),- [hyp](https://elite.bbcelite.com/elite-a/docked/subroutine/hyp_removed.html),- [LAUN](https://elite.bbcelite.com/elite-a/docked/subroutine/laun_removed.html),- [LL164](https://elite.bbcelite.com/elite-a/docked/subroutine/ll164_removed.html),- [MLS2](https://elite.bbcelite.com/elite-a/docked/subroutine/mls2_removed.html),- [MLTU2](https://elite.bbcelite.com/elite-a/docked/subroutine/mltu2_removed.html),- [MLU1](https://elite.bbcelite.com/elite-a/docked/subroutine/mlu1_removed.html),- [MLU2](https://elite.bbcelite.com/elite-a/docked/subroutine/mlu2_removed.html),- [MU5](https://elite.bbcelite.com/elite-a/docked/subroutine/mu5_removed.html),- [MU6](https://elite.bbcelite.com/elite-a/docked/subroutine/mu6_removed.html),- [MUT1](https://elite.bbcelite.com/elite-a/docked/subroutine/mut1_removed.html),- [MUT2](https://elite.bbcelite.com/elite-a/docked/subroutine/mut2_removed.html),- [MUT3](https://elite.bbcelite.com/elite-a/docked/subroutine/mut3_removed.html),- [MVT1](https://elite.bbcelite.com/elite-a/docked/subroutine/mvt1_removed.html),- [MVT3](https://elite.bbcelite.com/elite-a/docked/subroutine/mvt3_removed.html),- [MVT6](https://elite.bbcelite.com/elite-a/docked/subroutine/mvt6_removed.html),- [NwS1](https://elite.bbcelite.com/elite-a/docked/subroutine/nws1_removed.html),- [PIX1](https://elite.bbcelite.com/elite-a/docked/subroutine/pix1_removed.html),- [PIXEL2](https://elite.bbcelite.com/elite-a/docked/subroutine/pixel2_removed.html),- [plf2](https://elite.bbcelite.com/elite-a/docked/subroutine/plf2_removed.html),- [REDU2](https://elite.bbcelite.com/elite-a/docked/subroutine/redu2_removed.html),- [refund](https://elite.bbcelite.com/elite-a/docked/subroutine/refund_removed.html),- [SHD](https://elite.bbcelite.com/elite-a/docked/subroutine/shd_removed.html),- [SIGHT](https://elite.bbcelite.com/elite-a/docked/subroutine/sight_removed.html),- [SPBLB](https://elite.bbcelite.com/elite-a/docked/subroutine/spblb_removed.html),- [SPBT](https://elite.bbcelite.com/elite-a/docked/variable/spbt_removed.html),- [SPS1](https://elite.bbcelite.com/elite-a/docked/subroutine/sps1_removed.html),- [SPS3](https://elite.bbcelite.com/elite-a/docked/subroutine/sps3_removed.html),- [stack](https://elite.bbcelite.com/elite-a/docked/variable/stack_removed.html),- [TAS2](https://elite.bbcelite.com/elite-a/docked/subroutine/tas2_removed.html),- [TAS3](https://elite.bbcelite.com/elite-a/docked/subroutine/tas3_removed.html),- [TT147](https://elite.bbcelite.com/elite-a/docked/subroutine/tt147_removed.html),- [TT214](https://elite.bbcelite.com/elite-a/docked/subroutine/tt214_removed.html),- [TTX110](https://elite.bbcelite.com/elite-a/docked/subroutine/ttx110_removed.html),- [Ze](https://elite.bbcelite.com/elite-a/docked/subroutine/ze_removed.html),- [Unused block](https://elite.bbcelite.com/elite-a/docked/variable/unused_block_removed.html),- [Unused duplicate of MULTU](https://elite.bbcelite.com/elite-a/docked/subroutine/unused_duplicate_of_multu_removed.html),- [WP1](https://elite.bbcelite.com/elite-a/docked/subroutine/wp1_removed.html),- [WPLS](https://elite.bbcelite.com/elite-a/docked/subroutine/wpls_removed.html),- [wW](https://elite.bbcelite.com/elite-a/docked/subroutine/ww_removed.html)

Not all of these routines are completely unused in the original, so in some cases there's also a bit of associated refactoring to enable the original routine to be removed. For example, the [stack](https://elite.bbcelite.com/elite-a/docked/variable/stack_removed.html) variable can only be removed because of some clever tweaking in the [MEBRK](https://elite.bbcelite.com/elite-a/docked/subroutine/mebrk.html) and [SVE](https://elite.bbcelite.com/elite-a/docked/subroutine/sve.html) routines, but in general, the routines removed from the docked code are flight-specific, doing things like updating the dashboard or processing galactic hyperdrive jumps, none of which are needed when we're docked.

There are also some savings to be made in the flight code, though there are fewer opportunities for pruning unused code there. Here's a list of the routines that Angus removed from the flight code:

- [BAD](https://elite.bbcelite.com/elite-a/flight/subroutine/bad_removed.html),- [DEEOR](https://elite.bbcelite.com/elite-a/flight/subroutine/deeor_removed.html),- [FLKB](https://elite.bbcelite.com/elite-a/flight/subroutine/flkb_removed.html),- [GCASH](https://elite.bbcelite.com/elite-a/flight/subroutine/gcash_removed.html),- [Main flight loop (Part 5 of 16)](https://elite.bbcelite.com/elite-a/flight/subroutine/main_flight_loop_part_5_of_16_removed.html),- [MUT3](https://elite.bbcelite.com/elite-a/flight/subroutine/mut3_removed.html),- [ou2](https://elite.bbcelite.com/elite-a/flight/subroutine/ou2_removed.html),- [ou3](https://elite.bbcelite.com/elite-a/flight/subroutine/ou3_removed.html),- [PX3](https://elite.bbcelite.com/elite-a/flight/subroutine/px3_removed.html),- [SP1](https://elite.bbcelite.com/elite-a/flight/subroutine/sp1_removed.html),- [SPS4](https://elite.bbcelite.com/elite-a/flight/subroutine/sps4_removed.html),- [tnpr1](https://elite.bbcelite.com/elite-a/flight/subroutine/tnpr1_removed.html),- [TTX110](https://elite.bbcelite.com/elite-a/flight/subroutine/ttx110_removed.html),- [Unused block](https://elite.bbcelite.com/elite-a/flight/variable/unused_block_removed.html)

These removals are less to do with removing unused code, and more to do with streamlining. For example, [ou2](https://elite.bbcelite.com/elite-a/flight/subroutine/ou2_removed.html) and [ou3](https://elite.bbcelite.com/elite-a/flight/subroutine/ou3_removed.html) can be removed because their logic has been cleverly rolled into the [OUCH](https://elite.bbcelite.com/elite-a/flight/subroutine/ouch.html) routine, and [part 5 of the main flight loop](https://elite.bbcelite.com/elite-a/flight/subroutine/main_flight_loop_part_5_of_16_removed.html) can be removed as it deals with the energy bomb, a feature that isn't present in Elite-A (the energy bomb is replaced by the hyperspace unit in Elite-A).

Interestingly, there is a routine that is unused in the original code that is still present in Elite-A (well, half of it is), so this one not only managed to slip past the original authors, but it also managed to slip past Angus. It's the [Unused duplicate of MULTU](https://elite.bbcelite.com/elite-a/flight/subroutine/unused_duplicate_of_multu.html), which Angus identified and removed from the docked code, while leaving the second half of the routine in the flight code. I make it 11 bytes, which might not sound like a lot to have missed, but in the flight code every single byte saved is a big win, so those 11 bytes represent quite a bit of effort.

## Saving with subroutines

													 -----------------------

						Another way to save a few bytes is to identify any commonly repeated code - such as the code to switch text tokens between Sentence Case and ALL CAPS - and see if any of these repeated blocks could be called as a subroutine, if we gave it a label (i.e. we're looking for an occurrence that ends with an RTS instruction). We can then replace all the other instances of this code with JSR calls to that single block. As long as the subroutine is longer than three bytes (i.e. the number of bytes in a JSR instruction), this will save us a small amount of memory for every conversion to a subroutine call.

There are quite a few routines in Elite-A that save bytes using this approach. Here's a selection:

Let's look at an example. The most popular of these is vdu_80, which switches to Sentence Case. This code appears ten times in the original docked code and 6 times in the original flight code, where it looks like this:

LDA #%10000000 STA QQ17

In Elite-A, this code is replaced by a call to the newly added label at [vdu_80](https://elite.bbcelite.com/elite-a/flight/subroutine/tt27.html#vdu_80), like this:

JSR vdu_80

You can see an example of this modification in the [TT69](https://elite.bbcelite.com/elite-a/flight/subroutine/tt69.html) routine in the flight code, for example.

This represents a saving of just one byte for each conversion to a JSR, as the first version takes up four bytes (QQ17 is in zero page), while the second version takes up three bytes. However, this still saves us nine bytes in the docked code and five bytes in the flight code, as we convert all but one occurrence of the repeated code to a JSR, and this is a significant amount when every single byte counts.

## One byte here and another byte there

													 ------------------------------------

						There are also some savings to be had from bolting extra instructions onto the start of existing routines. For example, Angus bolted a CLC instruction onto the start of the [pr2](https://elite.bbcelite.com/elite-a/flight/subroutine/pr2.html) routine in the flight code, and then replaced four occurrences of this code:

CLC JSR pr2

with this:

JSR pr2-1

So that's one extra byte for the new CLC instruction at pr2-1, and four bytes saved in the four calls, giving a total saving of three bytes.

Other examples of tiny savings that all contribute are:

- Converting two STA/LDA pairs to TAY/TYA saves four bytes in the flight version of [NORM](https://elite.bbcelite.com/elite-a/flight/subroutine/norm.html).
- The [UNWISE](https://elite.bbcelite.com/elite-a/docked/subroutine/unwise.html)routine in the docked code is quite a lot tighter than the version in the original version, saving an impressive 15 bytes.
- The [SPS2](https://elite.bbcelite.com/elite-a/flight/subroutine/sps2.html)routine in the flight code has been moved, so the[COMPAS](https://elite.bbcelite.com/elite-a/flight/subroutine/compas.html)routine is now just before the[SP2](https://elite.bbcelite.com/elite-a/flight/subroutine/sp2.html)routine. This means we can drop the JSR SP2 instruction that was at the end of COMPAS, thus saving three precious bytes by letting COMPAS fall through into SP2 instead.

There are plenty of other little tweaks that save a byte here and there, eventually adding up to enough free space to support Elite-A's new features.

## Three programs in one

													 ---------------------

						The most visually obvious feature in Elite-A is the Encyclopedia Galactica, which shows in-game information on ships, controls and equipment if you press CTRL-f6 when docked (see the deep dive on [the Encyclopedia Galactica](https://elite.bbcelite.com/elite-a_the_encyclopedia_galactica.html) for more details). This is implemented as a totally separate program, so while the original disc version has two code files for docked and flight, Elite-A also has a third for the encyclopedia.

This means the encyclopedia doesn't have to worry about the limited memory in the docked and flight code, and the only impact on the rest of the codebase is an additional bit of code at the start of the docked code's [TT25](https://elite.bbcelite.com/elite-a/docked/subroutine/tt25.html) routine, which shows the Data on System screen when F6 is pressed. The additional code checks to see whether CTRL is being held down, and if so, it loads the encyclopedia code by calling the [encyclopedia](https://elite.bbcelite.com/elite-a/docked/subroutine/encyclopedia.html) routine.

## Replacing CATD

													 --------------

						In the original disc version, the [CATD](https://elite.bbcelite.com/disc/loader_3/subroutine/catd.html) routine lives at &0D7A, and is one of the few persistent routines that lives in the same place, irrespective of whichever main code file is loaded (docked or flight). This routine refreshes the disc catalogue from sectors 0 and 1 on disc, which makes sure it's always up to date.

Elite-A, however, ditches the CATD routine altogether, and instead it locates the [iff_index](https://elite.bbcelite.com/elite-a/loader/subroutine/iff_index.html) routine at the same address. This routine forms part of the I.F.F. system which upgrades the 3D scanner with more ship information, so it's only needed during flight and is therefore a strange candidate for using up this persistent space, but it does have the advantage of being very close to the size of the CATD routine, so that's presumably why it ended up here.

There is a downside to removing the CATD routine, however, as CATD is there to fix a bug when swapping between the flight and docked code. If we launch and immediately pause the game with COPY and then press ESCAPE to restart the game before the disc has stopped spinning in the drive, then in Elite-A, this will crash the game with a "Not found" error. This is because the disc catalogue has been corrupted, so when Elite-A goes to load the the T.CODE file containing the docked code, it can't find it. In the original version, CATD is called first to reconstruct the catalogue in memory, so the load command works.

Still, replacing CATD did enable Angus to shoehorn more functionality into the flight code without having to eat into the flight code itself, so there is an upside.

See the deep dive on [the I.F.F. system](https://elite.bbcelite.com/elite-a_the_iff_system.html) for more information on the iff_index routine.

## Adding new code

													 ---------------

						With the above savings, Angus managed to find enough spare memory to add the following new routines into the docked code:

- [confirm](https://elite.bbcelite.com/elite-a/docked/subroutine/confirm.html),- [count_offs](https://elite.bbcelite.com/elite-a/docked/variable/count_offs.html),- [cour_buy](https://elite.bbcelite.com/elite-a/docked/subroutine/cour_buy.html),- [cour_dock](https://elite.bbcelite.com/elite-a/docked/subroutine/cour_dock.html),- [encyclopedia](https://elite.bbcelite.com/elite-a/docked/subroutine/encyclopedia.html),- [n_buyship](https://elite.bbcelite.com/elite-a/docked/subroutine/n_buyship.html),- [n_load](https://elite.bbcelite.com/elite-a/docked/subroutine/n_load.html),- [n_name](https://elite.bbcelite.com/elite-a/docked/subroutine/n_name.html),- [n_price](https://elite.bbcelite.com/elite-a/docked/subroutine/n_price.html),- [new_details](https://elite.bbcelite.com/elite-a/docked/variable/new_details.html),- [new_offsets](https://elite.bbcelite.com/elite-a/docked/variable/new_offsets.html),- [new_ships](https://elite.bbcelite.com/elite-a/docked/variable/new_ships.html),- [sell_jump](https://elite.bbcelite.com/elite-a/docked/subroutine/sell_jump.html),- [sell_yn](https://elite.bbcelite.com/elite-a/docked/subroutine/sell_yn.html),- [stay_here](https://elite.bbcelite.com/elite-a/docked/subroutine/stay_here.html)

and the following routines into the flight code:

Together with the encyclopedia code and numerous other small modifications to the existing routines, this is how Angus managed to squeeze Elite-A into the already crowded memory map of the original Elite. It's impressive stuff!

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA #%10000000
  STA QQ17
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
JSR vdu_80
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CLC
  JSR pr2
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
JSR pr2-1
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/elite-a_making_room_for_the_modifications.html](https://elite.bbcelite.com/deep_dives/elite-a_making_room_for_the_modifications.html)*
