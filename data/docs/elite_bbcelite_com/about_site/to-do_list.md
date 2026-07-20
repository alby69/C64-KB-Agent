---
title: To-do list
source_url: https://elite.bbcelite.com/about_site/to-do_list.html
category: reference
topics:
- raster interrupts
- assembly
- basic
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
- CPU
- CIA
related:
- sid-registers
- sound-programming
- vic-ii-registers
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- sprite-programming
- raster-interrupts
- cia-registers
scraped_at: '2026-07-20'
---

# To-do list

I have documented every byte of the Elite game code, but that doesn't mean that I've fully *understood* every byte (though it's close). Almost every single aspect of the code is explained, but there are a few issues that could benefit from another look.

This page lists all of the outstanding issues of which I am aware. These are the notes I made as I analysed the source, so they are fairly terse and might not be terribly clear.

## Pitch and roll angles, signs

						                             ----------------------------

						- [STARS1](https://elite.bbcelite.com/cassette/main/subroutine/stars1.html): What is pitch calculation 7? Also, the explanation of the projection maths is shaky
- [STARS2](https://elite.bbcelite.com/cassette/main/subroutine/stars2.html): The maths behind roll calculations 5 and 6 (up/down) is unclear
- [MV40](https://elite.bbcelite.com/cassette/main/subroutine/mv40.html): Don't understand the sign stuff for result 3, particularly EOR at .MV2
- [TACTICS (Part 4 of 7)](https://elite.bbcelite.com/cassette/main/subroutine/tactics_part_4_of_7.html): Update comments on pitch and roll counters to explain what the manoeuvres actaully are, given that 44 * 1/16 radians = 2.75 radians = 158 degrees, and positive direction is clockwise (use style from DEMON)
- [PIXEL2](https://elite.bbcelite.com/cassette/main/subroutine/pixel2.html): Stardust plotting, why make the x-coordinate -X1? Could it be a -128+128 thing like in SLIDE?

## Vector calculations

						                             -------------------

						- [Main flight loop (Part 15 of 16)](https://elite.bbcelite.com/cassette/main/subroutine/main_flight_loop_part_15_of_16.html): Q doesn't get set to 0 for altitude calc - why isn't this a problem?
- [WARP](https://elite.bbcelite.com/cassette/main/subroutine/warp.html): What is &81-based maths to make the jump, is it -1 while preserving sign? (DEX works)
- [MVEIT (Part 5 of 9)](https://elite.bbcelite.com/cassette/main/subroutine/mveit_part_5_of_9.html): Note that Minsky is applied to x-coord not z here. Why is this different to MVS40?

## Maths

						                             -----

						- [ADD](https://elite.bbcelite.com/cassette/main/subroutine/add.html): If result is positive but overflows, can sign bit still be wrong?
- [MULT1](https://elite.bbcelite.com/cassette/main/subroutine/mult1.html),- [FMLTU](https://elite.bbcelite.com/cassette/main/subroutine/fmltu.html),- [MLTU2](https://elite.bbcelite.com/cassette/main/subroutine/mltu2.html),- [MULT3](https://elite.bbcelite.com/cassette/main/subroutine/mult3.html): Algorithms are still slightly mysterious
- [LL5](https://elite.bbcelite.com/cassette/main/subroutine/ll5.html): Try to understand the linked square root algorithm and put into comments

## Other

						                             -----

						- [IRQ1](https://elite.bbcelite.com/cassette/main/subroutine/irq1.html): The exact maths behind the split-screen timer value isn't clear
- [IRQ1](https://elite.bbcelite.com/cassette/main/subroutine/irq1.html): Why do we read an unused value, e.g. LDA VIA+&41, before RTI?
- [BPRNT](https://elite.bbcelite.com/cassette/main/subroutine/bprnt.html): Meaning of U is still confusing me, also see SVE and competition number
- [KYTB](https://elite.bbcelite.com/cassette/main/variable/kytb.html): Why do important flight keys have the top bit set? Works OK without it
- [Main game loop (Part 5 of 6)](https://elite.bbcelite.com/cassette/main/subroutine/main_game_loop_part_5_of_6.html): What's with the delay by 8/50s? And what about QQ11 and PATG? (Looks like cheating with PATG also slows down the gameplay - check this)
- [TT18](https://elite.bbcelite.com/cassette/main/subroutine/tt18.html): Why switch the view to 1, only to have it switch back to the space view?
- [Ghy](https://elite.bbcelite.com/cassette/main/subroutine/ghy.html): We jump in at (96,96), but where is this converted to the nearest system?
- [LOIN](https://elite.bbcelite.com/cassette/main/subroutine/loin_part_1_of_7.html): Logic for not plotting end points is confusing
- [LL9 (Part 3 of 12)](https://elite.bbcelite.com/cassette/main/subroutine/ll9_part_3_of_12.html): Division code to normalise orientation vectors is unclear
- [Elite loader (Part 4 of 6)](https://elite.bbcelite.com/cassette/loader/subroutine/elite_loader_part_4_of_6.html): What's the keyboard bit about if we have checksums enabled?

## Enhanced versions

						                             -----------------

						- [SHIP_SPLINTER](https://elite.bbcelite.com/disc/ship_blueprints_c/variable/ship_splinter.html): Why do we need to add 24 to the Faces data offset (low)? Do splinters work properly in 6502 SP, disc, Master Elite?

## BBC Master version

						                             ------------------

						- [Dials part 1](https://elite.bbcelite.com/master/main/subroutine/dials_part_1_of_4.html): what's the STA &DDEB for?
- [NOISE](https://elite.bbcelite.com/master/main/subroutine/noise.html),- [SOINT](https://elite.bbcelite.com/master/main/subroutine/soint.html),- [SFXBT](https://elite.bbcelite.com/master/main/variable/sfxbt.html),- [SFXVC](https://elite.bbcelite.com/master/main/variable/sfxvc.html),- [SOFLG](https://elite.bbcelite.com/master/main/workspace/sound_variables.html#soflg): This is based on the C64 code, but for the Master's sound chip, so document accordingly (see- [this page](https://mansfield-devine.com/speculatrix/2019/11/fun-with-chips-2-sn76489-sound-generator-ic/))

## Disc version

						                             ------------

						- [Elite loader (Part 1 of 2)](https://elite.bbcelite.com/disc/loader_2/subroutine/elite_loader_part_1_of_2.html): Tube code JMP &5A00 is odd
- [TestBBC (Sideways RAM loader)](https://elite.bbcelite.com/disc/sideways_ram_loader/subroutine/testbbc.html): Why do we set the top four bits of the first byte in banks that don't contain ROM images?

## 6502 Second Processor version

						                             -----------------------------

						- [DOFE21](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dofe21.html): Energy bomb effect doesn't appear to work?
- [DOCKIT](https://elite.bbcelite.com/6502sp/main/subroutine/dockit.html): K3+10 - what on earth is this check for?
- [HATB](https://elite.bbcelite.com/6502sp/main/variable/hatb.html): Ship hanger, Viper/Krait is repeated - test this against reality
- [HANGER](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/hanger.html): Why is S 60 rather than 15 for yaw rotations?
- [newosrdch](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/newosrdch.html): Why is key press 21 allowed through?
- [Elite loader](https://elite.bbcelite.com/6502sp/loader_1/subroutine/elite_loader.html): Machine detection logic is very odd
- [DEATH](https://elite.bbcelite.com/6502sp/main/subroutine/death.html): The logic behind showing plates on death seems weird
- [DEATH](https://elite.bbcelite.com/6502sp/main/subroutine/death.html): The number of canisters shown doesn't seem to match what the code says
- [DOKEY](https://elite.bbcelite.com/6502sp/main/subroutine/dokey.html): Why is the roll key "pressing" logic different to pitch?
- [DVID4](https://elite.bbcelite.com/6502sp/main/subroutine/dvid4.html): This returns different values to cassette?
- [FMLTU](https://elite.bbcelite.com/6502sp/main/subroutine/fmltu.html): Explanation of logs is... dodgy throughout all log routines
- [TACTICS (Part 7 of 7)](https://elite.bbcelite.com/6502sp/main/subroutine/tactics_part_7_of_7.html): RAT, RAT2, CNT2 logic is a bit unclear, see part 3 as well
- [B% variable](https://elite.bbcelite.com/6502sp/loader_1/variable/b_per_cent.html): Why is register 7 set using &87?
- Inventory is one line higher in Tube version only - why? JSR INCYC in TTX69?

## Apple II version

						                             ----------------

						- [seek](https://elite.bbcelite.com/apple/main/subroutine/seek.html): Why is the track number doubled?

## Elite-A

						                             -------

						- [CATS](https://elite.bbcelite.com/elite-a/docked/subroutine/cats.html): The mode in &0355 gets set to 1 before *CAT, then reset afterwards: why?
- Source discs: B.SHIP vs B.FILES, where does S.T come from, how do CSV ship files get converted to assembly?

---
*Fonte originale: [https://elite.bbcelite.com/about_site/to-do_list.html](https://elite.bbcelite.com/about_site/to-do_list.html)*
