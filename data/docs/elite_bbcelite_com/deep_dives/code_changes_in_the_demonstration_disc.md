---
title: Code changes in the Demonstration Disc
source_url: https://elite.bbcelite.com/deep_dives/code_changes_in_the_demonstration_disc.html
category: source-code
topics:
- basic
- assembly
- input handling
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CIA
- BASIC ROM
related:
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- cia-registers
scraped_at: '2026-07-20'
---

# Code changes in the Demonstration Disc

## The differences between the cassette version and the demonstration disc

The Elite Demonstration Disc is a fork of the BBC Micro cassette version of Elite, with a number of routines removed to make room for the self-flying features, and other routines copied over from the BBC Micro disc version to implement the combat autopilot. See the deep dive on [the Elite Demonstration Disc](https://elite.bbcelite.com/the_elite_demonstration_disc.html) for details.

![The Elite Demomstration Disc](https://elite.bbcelite.com/images/demo/demo_disc.jpg) 

						This article contains a complete list of all the code modifications made to the BBC Micro cassette version in order to produce the Demonstration Disc. In the following, the modified routines are shown in the order in which they are run while the demo is progressing, so you might find it useful to refer to the deep dive on [program flow of the main game loop](https://elite.bbcelite.com/program_flow_of_the_main_game_loop.html), as that covers the entire program flow in the standard cassette version, while the following only covers the modifications.

Links will take you through to the modified code in the Demonstration Disc source code, where all the modifications are shown, along with any code that has been removed. This lets you see exactly what the authors changed to convert the cassette version into the demo.

Note that the code on this site has been extracted from the Demonstration Disc, but it doesn't include the disc protection, which only works on the 8271 disc interface. The version on this site will work on all disc interfaces, including the 1770, as the copy protection is not included.

## Variable modifications

													 ----------------------

						The following variables have been updated or added for the demonstration:

| Name | Modification details | 
|---|---|
| [QQ18](https://elite.bbcelite.com/demo/main/variable/qq18.html) | Update the text tokens as follows: Replace token 123 ("COMMANDER'S NAME") with "DEMONSTRATION", to be shown during flightReplace token 142 ("DANGEROUS") with "-"Replace token 143 ("DEADLY") with "-"Replace token 147 ("PRESS FIRE OR SPACE,COMMANDER.") with "BBC TAPE VERSION DEMONSTRATION" for the second title screenMove two carriage returns from the end of token 128 ("LOAD NEW COMMANDER (Y/N)?") into the start of token 147 ("(C) ACORNSOFT 1984")
 | 
| [WP](https://elite.bbcelite.com/demo/main/workspace/wp.html) | Add five new variables for use by the combat autopilot: [targetShip](https://elite.bbcelite.com/demo/main/workspace/wp.html#targetship)contains the slot number of the target ship, if any[attackingShip](https://elite.bbcelite.com/demo/main/workspace/wp.html#attackingship)contains the slot number of the ship that is firing its lasers at us[hyperspaceDone](https://elite.bbcelite.com/demo/main/workspace/wp.html#hyperspacedone)indicates whether we have done the hyperspace jump to Riedquat[launchedMissile](https://elite.bbcelite.com/demo/main/workspace/wp.html#launchedmissile)gets set to the slot number of the most recently spawned ship, so that if an enemy has launched a missile at us, we can set our target to this slot number so we start hunting for the missile[enableLasers](https://elite.bbcelite.com/demo/main/workspace/wp.html#enablelasers)determines whether our lasers are enabled, so they can be disabled for a while when we get a missile lock
 | 
| [NA%](https://elite.bbcelite.com/demo/main/variable/na_per_cent.html) | Update the commander for the demo: Set the commander name to "DISPLAY"Set the cash level to 500 creditsSet the fuel level to 2.0 light yearsAdd a rear pulse laser
 | 
| [CHK2](https://elite.bbcelite.com/demo/main/variable/chk2.html) | Add the correct second checksum for the updated commander | 
| [CHK](https://elite.bbcelite.com/demo/main/variable/chk.html) | Add the correct checksum for the updated commander | 

## Code modifications when docked

													 ------------------------------

						These are the code modifications that are run when the demo first loads and the ship is still in the station:

| Name | Modification details | 
|---|---|
| [Elite loader](https://elite.bbcelite.com/demo/loader/subroutine/elite_loader_part_4_of_6.html)(Part 4 of 6) | Remove the long wait for a key press on the Acornsoft loading screen | 
| [BR1 (Part 1 of 2)](https://elite.bbcelite.com/demo/main/subroutine/br1_part_1_of_2.html) | Remove the "Y/N" key press detection code for the first title screen | 
| [TITLE](https://elite.bbcelite.com/demo/main/subroutine/title.html) | Show each of the title screens for 255 loop iterations and disable the joystick detection code | 
| [RESET](https://elite.bbcelite.com/demo/main/subroutine/reset.html) | Set [hyperspaceDone](https://elite.bbcelite.com/demo/main/workspace/wp.html#hyperspacedone)to zero to indicate that we have not yet performed the hyperspace to Riedquat | 
| [QU5](https://elite.bbcelite.com/demo/main/subroutine/qu5.html) | Remove the commander file checksum code | 
| [BAY](https://elite.bbcelite.com/demo/main/subroutine/bay.html) | Add code to do the following: Show the Status Mode screen for five seconds (the latter is implemented by the new [DelayFiveSeconds](https://elite.bbcelite.com/demo/main/subroutine/delayfiveseconds.html)routine throughout the following)Show the Market Price screen for five secondsShow the Data on System screen for five secondsCall [EQSHP](https://elite.bbcelite.com/demo/main/subroutine/eqshp.html)to trigger the equipment-buying part of the demo, which then calls[TT219](https://elite.bbcelite.com/demo/main/subroutine/tt219.html)to do the cargo-buying demo, the Long-range Chart demo and the launch from the station, with the latter triggering the hyperspace demo in[TT110](https://elite.bbcelite.com/demo/main/subroutine/tt110.html)Switch to the front space view to wait for the hyperspace countdown
 | 
| [DELAY](https://elite.bbcelite.com/demo/main/subroutine/delay.html) | Add a call to the new [ProcessDemoKeys](https://elite.bbcelite.com/demo/main/subroutine/processdemokeys.html)routine to check for the supported key presses in the demo | 
| [TT102](https://elite.bbcelite.com/demo/main/subroutine/tt102.html) | Add a five second delay to the Status Mode screen, disable the code for the "@" key so it doesn't save commander files | 
| [TT167](https://elite.bbcelite.com/demo/main/subroutine/tt167.html) | Add a five-second delay after showing the Market Price screen | 
| [TT25](https://elite.bbcelite.com/demo/main/subroutine/tt25.html) | Add a five-second delay after showing the Data on System screen | 
| [EQSHP](https://elite.bbcelite.com/demo/main/subroutine/eqshp.html) | Add code to demonstrate buying of equipment: Restrict the available equipment to the smallest rangeIf we do not have four missiles already then buy a missileIf we do not have a full fuel tank, buy some fuelIf we already have four missiles and a full fuel tank, buy a random item of equipment (though in practice this is limited to fuel or missiles)Wait for five seconds and show the Buy Cargo screen in TT219, to trigger the cargo-buying part of the demo
 | 
| [gnum](https://elite.bbcelite.com/demo/main/subroutine/gnum.html) | Return a random number in the correct range instead of waiting for the player to enter one | 
| [TT219](https://elite.bbcelite.com/demo/main/subroutine/tt219.html) | Add code to do the following after displaying the Inventory screen following the cargo-buying part of the demo: Display the Long-range ChartChoose a random destinationShow the Data on System screenRepeat the above a random number of timesShow the Status Mode screen for five secondsLaunch from the station to trigger the hyperspace code in TT110
 | 
| [TT210](https://elite.bbcelite.com/demo/main/subroutine/tt210.html) | Add a five-second delay after showing the cargo list | 

## Code modifications following launch

													 -----------------------------------

						These are the code modifications that are run when the ship has launched but has not yet performed the hyperspace jump to Riedquat:

| Name | Modification details | 
|---|---|
| [TT110](https://elite.bbcelite.com/demo/main/subroutine/tt110.html) | Add code so as soon as we launch, we show the Short-range Chart, which will then trigger the hyperspace process in TT17 to set up a hyperspace to Riedquat | 
| [TT17](https://elite.bbcelite.com/demo/main/subroutine/tt17.html) | Remove joystick support from the chart screens and add code to automatically move the crosshairs from Lave to Riedquat before initiating a hyperspace and switching to the front space view | 
| [U%](https://elite.bbcelite.com/demo/main/subroutine/u_per_cent.html) | Add code to clear KL when clearing the key logger | 
| [LOOK1](https://elite.bbcelite.com/demo/main/subroutine/look1.html) | Remove support for views other than the front view | 
| [TTX66](https://elite.bbcelite.com/demo/main/subroutine/ttx66.html) | Remove support for views other than the front view | 
| [TT18](https://elite.bbcelite.com/demo/main/subroutine/tt18.html) | Remove support for making a manual mis-jump by holding down CTRL | 

## Code modifications for combat

													 -----------------------------

						These are the code modifications that are run once we have reached Riedquat and are on combat alert:

| Name | Modification details | 
|---|---|
| [SOLAR](https://elite.bbcelite.com/demo/main/subroutine/solar.html) | Set the value of [hyperspaceDone](https://elite.bbcelite.com/demo/main/workspace/wp.html#hyperspacedone)to non-zero indicate that we have hyperspaced to Riedquat | 
| [DOKEY](https://elite.bbcelite.com/demo/main/subroutine/dokey.html) | Add code to do the following after displaying the Inventory screen following the cargo-buying part of the demo: Contains code copied from the disc version to apply the docking computer code to ship flyingContains new code to ensure that missile-launching takes precedence over flyingCalls the new [AttackTarget](https://elite.bbcelite.com/demo/main/subroutine/attacktarget.html)routine to implement combat tactics
 | 
| [DK4](https://elite.bbcelite.com/demo/main/subroutine/dk4.html) | Replace the original game's pause key processing code with a call to the new [ProcessDemoKeys](https://elite.bbcelite.com/demo/main/subroutine/processdemokeys.html)routine | 
| [cntr](https://elite.bbcelite.com/demo/main/subroutine/cntr.html) | Force keyboard damping to be used | 
| [REDU2](https://elite.bbcelite.com/demo/main/subroutine/redu2.html) | Force keyboard auto-recentre to be used | 
| [Main flight loop](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_3_of_16.html)(Part 3 of 16) | Disable our lasers via [enableLasers](https://elite.bbcelite.com/demo/main/workspace/wp.html#enablelasers)when missile lock is achieved, and remove the code for processing the energy bomb, escape pod, in-system jump, E.C.M. and docking computer | 
| [LASLI](https://elite.bbcelite.com/demo/main/subroutine/lasli.html) | Minor label change (has no effect) | 
| [TACTICS](https://elite.bbcelite.com/demo/main/subroutine/tactics_part_2_of_7.html)(Part 2 of 7) | Initialise the [RAT](https://elite.bbcelite.com/demo/main/workspace/zp.html#rat),[RAT2](https://elite.bbcelite.com/demo/main/workspace/zp.html#rat2)and[CNT2](https://elite.bbcelite.com/demo/main/workspace/zp.html#cnt2)variables used by the docking computer code | 
| [TACTICS](https://elite.bbcelite.com/demo/main/subroutine/tactics_part_5_of_7.html)(Part 5 of 7) | If a ship fires a missile at us, immediately switch our target to be that missile by setting [targetShip](https://elite.bbcelite.com/demo/main/workspace/wp.html#targetship)to[launchedMissile](https://elite.bbcelite.com/demo/main/workspace/wp.html#launchedmissile) | 
| [TACTICS](https://elite.bbcelite.com/demo/main/subroutine/tactics_part_6_of_7.html)(Part 6 of 7) | If a ship starts firing lasers at us, store its slot in [attackingShip](https://elite.bbcelite.com/demo/main/workspace/wp.html#attackingship), and if we don't have a target, set[targetShip](https://elite.bbcelite.com/demo/main/workspace/wp.html#targetship)to the attacking ship and call the new[PressMissileKey](https://elite.bbcelite.com/demo/main/subroutine/pressmissilekey.html)routine to arm a missile | 
| [TACTICS](https://elite.bbcelite.com/demo/main/subroutine/tactics_part_7_of_7.html)(Part 7 of 7) | Add in code from the enhanced versions to enable the docking computer code to steer the ship | 
| [NWSHP](https://elite.bbcelite.com/demo/main/subroutine/nwshp.html) | Store the new ship's slot in [launchedMissile](https://elite.bbcelite.com/demo/main/workspace/wp.html#launchedmissile)so that if this is an enemy launching a missile at us in the tactics routine, we can switch targets to start hunting down the missile | 
| [KILLSHP](https://elite.bbcelite.com/demo/main/subroutine/killshp.html) | If we just removed our target ship, clear the [targetShip](https://elite.bbcelite.com/demo/main/workspace/wp.html#targetship)variable | 
| [Main flight loop](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_7_of_16.html)(Part 7 of 16) | Remove the code for scooping of cargo using the fuel scoops | 
| [Main flight loop](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_8_of_16.html)(Part 8 of 16) | Remove the code for scooping of cargo using the fuel scoops | 
| [Main flight loop](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_9_of_16.html)(Part 9 of 16) | If we docked successfully, restart from the title screen and configure the author's names to be displayed | 
| [Main flight loop](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_11_of_16.html)(Part 11 of 16) | Various combat-related changes: Disable support for targeting missile lock in the left, right and rear viewsIf a missile lock has been achieved, fire the missile by calling the new [PressMissileKey](https://elite.bbcelite.com/demo/main/subroutine/pressmissilekey.html)routine (with a 61% chance of firing on each iteration of the main loop)If we have destroyed our target ship, clear the [targetShip](https://elite.bbcelite.com/demo/main/workspace/wp.html#targetship)variable
 | 
| [Main flight loop](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_13_of_16.html)(Part 13 of 16) | Various combat-related changes: Remove the energy bomb explosion codeOn main loop iteration 200 only: print "DEMONSTRATION" as an in-flight message, enable our lasers to be fired via [enableLasers](https://elite.bbcelite.com/demo/main/workspace/wp.html#enablelasers)(so this reverses any disabling done during missile lock), and 39% of the time on this iteration, change our target ship to the last ship to fire its lasers at us; then jump to part 16 to skip the space station and altitude checks
 | 
| [FAROF2](https://elite.bbcelite.com/demo/main/subroutine/farof2.html) | Minor label change (has no effect) | 
| [Main flight loop](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_15_of_16.html)(Part 15 of 16) | Minor changes only to fix branches that would otherwise be too long with the added code | 
| [Main flight loop](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_16_of_16.html)(Part 16 of 16) | Minor change to jump straight to the stardust routines for the front view without testing for the other three views | 

## New routines

													 ------------

						The following brand new routines have been added to support the above process:

| Name | Details | 
|---|---|
| [AttackTarget](https://elite.bbcelite.com/demo/main/subroutine/attacktarget.html) | Turn towards the specified enemy target and fire lasers when we are pointing in the right direction | 
| [DelayFiveSeconds](https://elite.bbcelite.com/demo/main/subroutine/delayfiveseconds.html) | Wait for 5.1 seconds | 
| [PressMissileKey](https://elite.bbcelite.com/demo/main/subroutine/pressmissilekey.html) | "Press" a key by populating the key logger directly (used for pressing the "T" and "M" missile keys only) | 
| [ProcessDemoKeys](https://elite.bbcelite.com/demo/main/subroutine/processdemokeys.html) | Process the key presses that are supported in the demo (COPY to pause, DELETE to unpause, ESCAPE to quit, "Q" to disable sound, "S" to enable sound) | 

## Code from the disc version

													 --------------------------

						The following routines contain code that has been copied directly from the disc version to implement the autopilot:

| Name | Details | 
|---|---|
| [DOKEY](https://elite.bbcelite.com/demo/main/subroutine/dokey.html) | The code added to DOKEY from the disc version implements the automatic flight controls for the demo, so that the ship turns towards either the planet in [DOCKIT](https://elite.bbcelite.com/demo/main/subroutine/dockit.html)or the target in[AttackTarget](https://elite.bbcelite.com/demo/main/subroutine/attacktarget.html), depending on whether there is a target in[targetShip](https://elite.bbcelite.com/demo/main/workspace/wp.html#targetship) | 
| [RefineApproach](https://elite.bbcelite.com/demo/main/subroutine/refineapproach.html) | Refine our approach using pitch and roll to aim for the target; the code is copied from the DOCKIT routine in the disc version, and has been extracted into a separate routine so it can be called by both the [DOCKIT](https://elite.bbcelite.com/demo/main/subroutine/dockit.html)and[AttackTarget](https://elite.bbcelite.com/demo/main/subroutine/attacktarget.html)routines | 
| [DOCKIT](https://elite.bbcelite.com/demo/main/subroutine/dockit.html) | Apply docking manoeuvres to the ship in INWK (this routine contains some minor refactoring that doesn't affect the functionality but which supports manoeuvring towards enemy ships as well as the planet/station) | 
| [GOPL](https://elite.bbcelite.com/demo/main/subroutine/gopl.html) | Make the ship head towards the planet | 
| [VCSU1](https://elite.bbcelite.com/demo/main/subroutine/vcsu1.html) | Vector calculations for the vector towards the station or planet | 
| [VCSUB](https://elite.bbcelite.com/demo/main/subroutine/vcsub.html) | Vector calculations for the vector towards the station or planet | 
| [TAS4](https://elite.bbcelite.com/demo/main/subroutine/tas4.html) | Calculate the dot product of XX15 and one of the station or planet's orientation vectors | 
| [TAS6](https://elite.bbcelite.com/demo/main/subroutine/tas6.html) | Negate the vector in XX15 so it points in the opposite direction | 
| [DCS1](https://elite.bbcelite.com/demo/main/subroutine/dcs1.html) | Calculate the vector from the ideal docking position to the ship | 

## Removed code

													 ------------

						The following routines have been removed, either fully or partially; in either case, they aren't used in the demo. They are listed in the order in which they appear in the source.

| Name | Details of removed code | 
|---|---|
| [Main flight loop (Part 5 of 16)](https://elite.bbcelite.com/demo/main/subroutine/main_flight_loop_part_5_of_16_removed.html) | If an energy bomb has been set off, potentially kill this ship | 
| [FLIP](https://elite.bbcelite.com/demo/main/subroutine/flip_removed.html) | Reflect the stardust particles in the screen diagonal and redraw the stardust field | 
| [STARS](https://elite.bbcelite.com/demo/main/subroutine/stars_removed.html) | The main routine for processing the stardust | 
| [STARS6](https://elite.bbcelite.com/demo/main/subroutine/stars6_removed.html) | Process the stardust for the rear view | 
| [ESCAPE](https://elite.bbcelite.com/demo/main/subroutine/escape_removed.html) | Launch our escape pod | 
| [STARS2](https://elite.bbcelite.com/demo/main/subroutine/stars2_removed.html) | Process the stardust for the left or right view | 
| [WARP](https://elite.bbcelite.com/demo/main/subroutine/warp_removed.html) | Perform an in-system jump | 
| [PLUT](https://elite.bbcelite.com/demo/main/subroutine/plut_removed.html) | Flip the coordinate axes for the four different views | 
| [MJP](https://elite.bbcelite.com/demo/main/subroutine/mjp_removed.html) | Process a mis-jump into witchspace | 
| [CHECK](https://elite.bbcelite.com/demo/main/subroutine/check_removed.html) | Calculate the checksum for the last saved commander data block | 
| [TRNME](https://elite.bbcelite.com/demo/main/subroutine/trnme_removed.html) | Copy the last saved commander's name from INWK to NA% | 
| [TR1](https://elite.bbcelite.com/demo/main/subroutine/tr1_removed.html) | Copy the last saved commander's name from NA% to INWK | 
| [GTNME](https://elite.bbcelite.com/demo/main/subroutine/gtnme_removed.html) | Fetch the name of a commander file to save or load | 
| [RLINE](https://elite.bbcelite.com/demo/main/variable/rline_removed.html) | The OSWORD configuration block used to fetch a line of text from the keyboard | 
| [SVE](https://elite.bbcelite.com/demo/main/subroutine/sve.html) | Save the commander file | 
| [QUS1](https://elite.bbcelite.com/demo/main/subroutine/qus1_removed.html) | Save or load the commander file | 
| [LOD](https://elite.bbcelite.com/demo/main/subroutine/lod_removed.html) | Load a commander file | 
| [DKS3](https://elite.bbcelite.com/demo/main/subroutine/dks3_removed.html) | Toggle a configuration setting and emit a beep | 
| [TT217](https://elite.bbcelite.com/demo/main/subroutine/tt217.html) | Scan the keyboard until a key is pressed | 
| [RDKEY](https://elite.bbcelite.com/demo/main/subroutine/rdkey.html) | Scan the keyboard for key presses |

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/code_changes_in_the_demonstration_disc.html](https://elite.bbcelite.com/deep_dives/code_changes_in_the_demonstration_disc.html)*
