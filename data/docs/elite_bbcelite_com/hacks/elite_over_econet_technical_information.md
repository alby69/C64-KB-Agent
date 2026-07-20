---
title: Technical information for Elite over Econet
source_url: https://elite.bbcelite.com/hacks/elite_over_econet_technical_information.html
category: source-code
topics:
- memory management
- basic
- graphics
- assembly
- sound generation
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

# Technical information for Elite over Econet

## Details of how Elite over Econet works

For the most part, Elite over Econet is pretty much the same as the original disc-based version of the game. The main difference is a rearrangement of the code to work with Econet's more stringent memory requirements, along with some tweaks to make the game work with the hierarchical directory system that NFS provides.

This page examines the technical aspects of all these changes, and we also examine a brand new feature, multiplayer scoreboards. This is the scoreboard from the 2024 Econet LAN Party at the National Museum of Computing:

![The Elite scoreboard at the National Museum of Computing](https://elite.bbcelite.com/images/elite_over_econet/tnmoc_scoreboard.jpg) 

						Joining in the fun are players from across the UK, mainland Europe and north America. There are five test accounts in the above, but the other 11 entries are real humans, all playing Elite at the same time on the same Econet network.

We'll take a look at multiplayer Elite in a moment, but let's start with the loading process and preventing memory clash.

## Loading Elite over Econet

													 -------------------------

						On the BBC Micro, BBC Master and Acorn Electron, Elite doesn't normally load from an Econet fileserver; the Archimedes version works fine (see [Elite over Econet on the Acorn Archimedes](https://elite.bbcelite.com/elite_over_econet_acorn_archimedes.html) for details), but the 8-bit versions simply hang. The main reason is that Econet uses various blocks of memory in the BBC's memory map, and Elite uses the same blocks of memory. It's therefore no surprise that trying to load the standard version of Elite over an Econet network causes memory clashes that crash the computer.

The solution to getting Elite to run over Econet is to prevent this memory clash. Very few versions of Econet allow you to change the memory locations that it uses, so instead we have to update Elite so it avoids using the memory that Econet needs to use.

On top of this, the BBC Master version needs to deal with NMIs from Econet, as otherwise network activity can fatally interrupt the game. Also, the interface for loading and saving commander files needs to work with the hierarchical filing system used by Econet (NFS), which is quite different to the standard disc filing system (DFS) that Elite normally uses.

And for the BBC Micro and Electron versions of Elite, there's an even more pressing issue: Econet steals so much memory that there simply isn't enough room to fit both the game and the Econet workspace into main memory.

We'll take a look at the solutions to these challenges below, but if you want to follow along, then the accompanying repository contains all of the changes that I've made to Elite to make it work over Econet. Specifically, the [elite-over-econet repository](https://github.com/markmoxon/elite-over-econet) includes the updated code as submodules, so to find all the changes, search the source files for "Mod:" in these repositories:

- The econet-flicker-free branch of [elite-source-code-bbc-micro-disc](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/tree/econet-flicker-free/1-source-files/main-sources)
- The econet-flicker-free branch of [elite-source-code-acorn-electron](https://github.com/markmoxon/elite-source-code-acorn-electron/tree/econet-flicker-free/1-source-files/main-sources)
- The econet-flicker-free branch of [elite-source-code-6502-second-processor](https://github.com/markmoxon/elite-source-code-6502-second-processor/tree/econet-flicker-free/1-source-files/main-sources)
- The econet-flicker-free branch of [elite-source-code-bbc-master](https://github.com/markmoxon/elite-source-code-bbc-master/tree/econet-flicker-free/1-source-files/main-sources)

Let's take a look at what these mods do to enable Elite to load over Econet.

## Preventing memory clash

													 -----------------------

						The first challenge when getting Elite to load over Econet is to prevent Elite from using memory locations that are reserved for Econet. Elite already avoids using memory that is reserved for the MOS, such as pages &2 and &D, but the following Econet-specific memory blocks clash with the game:

- On all machines, the 16 zero page locations from &90 to &9F are reserved for Econet.
- On the Master, pages &B and &C are reserved for Econet, so that's &0B00 to &0CFF.
- On the BBC Micro and Acorn electron, Econet pushes PAGE up by rather more than DFS (PAGE being the start of user memory). On standard disc systems PAGE gets set to &1900 by default, but it's possible to reduce this to &1100 in typical usage (which is the level that BBC Micro disc Elite expects). However, on Econet systems with DFS still available, PAGE rises two pages higher to &1B00, and the lowest Econet can get is &1200 (when DFS is not being used). This is &100 bytes higher than the lowest value for DFS, and it's &100 bytes higher than the value that Elite expects.

For the first one - freeing up 16 bytes in zero page - this is an easy fix in the 6502 Second Processor version of Elite. In this version, it's the I/O Processor (i.e. the BBC Micro) that deals with file operations, so it's the memory map of the I/O Processor code that we need to check for clashes, rather than the Parasite code that runs in the co-processor. 6502 Second Processor Elite hardly uses any of zero page in the I/O Processor, so all that needs doing there is to move the variables so they don't clash with &90 to &9F.

Freeing up 16 bytes in zero page in the BBC Micro and BBC Master versions is a lot trickier, but a lot of the hard work was already done when I added music to Elite, as the music player requires ten bytes in zero page to work properly (see the [technical information for musical Acornsoft Elite](https://elite.bbcelite.com/bbc_elite_with_music_technical_information.html) for details). Finding a further six bytes on the Master version isn't too hard, as there are some zero page locations that aren't used at all, and there's also plenty of spare memory in the WP workspace at &0E41, so we can move some of the less-used zero page variables there, at the expense of an extra byte in each instruction that accesses these variables (memory we can easily spare). On the BBC Micro space is a bit tighter, but there are still savings to be made, and there is some extra space at the end of the UP workspace that can be used to rehouse some of the less-used variables.

Interestingly, the Electron version of Elite already avoids using addresses &90 to &9F, so that makes life a bit easier. That said, we also need to avoid using any zero page locations that are used for handling NMIs, so that we can support the NMI-based NFS instead of the cassette filing system of the original. It turns out that the simplest solution is to apply the zero page structure from the disc version of Elite over Econet to the Electron version, which involves relocating the keyboard buffer from zero page into main memory. This is pretty easy as in the Electron version, we have an extra 16K of sideways RAM to play with.

Freeing up &0B00 to &0CFF on the BBC Master is pretty easy too. On the standard Master version, &0B00 to &0CFF is only used by the ship heap for the ship hangar, and as we don't use pages &9 and &A, it's an easy change to move the hanger heap to &0900 to &0AFF instead. And if we're running the 6502 Second Processor version on a Master, then this part of the I/O processor's memory is only used for the [TINA hook](https://elite.bbcelite.com/deep_dives/the_tina_hook.html), which we can safely ignore as it's unused anyway.

But what about the high value of PAGE on the BBC Micro? For the 6502 Second Processor version running on a BBC Micro, there is nothing to fix; the I/O Processor code loads at &2300 anyway, which is well above the value of PAGE with Econet fitted, so there is nothing to do here. But for the standard BBC Micro there is hardly any spare memory at all, so instead we have to make some compromises...

## Running Elite on the BBC Micro

													 ------------------------------

						In standard BBC Micro disc Elite, the main docked and flight game binaries live at address &1100, which is the first usable part of user memory under DFS. The first block of memory at &1100 is used for storing common variables, and the docked and flight game code binaries both load at &11E3. Econet pushes up the start of user memory to &1200, so the first thing we have to do is relocate the entire game from &1100 to &1200.

However, Elite uses almost all available memory, so this process will push the game code into the bottom of screen memory unless we do something radical (see the [BBC Micro disc Elite memory map](https://elite.bbcelite.com/deep_dives/the_elite_memory_map_disc.html) for details). Luckily the docked code is easy to fix; it turns out that the docked binary contains lots of routines that are only used during flight, so it's a relatively easy job to remove these from the source, leaving a smaller game binary that fits into memory when moved to address &1200.

The flight code is another matter altogether, as there are very few savings to be had - certainly not enough to add up to &100 bytes. If our BBC Micro has sideways RAM fitted, then there is an obvious solution: we can use the [sideways RAM variant of Elite](https://elite.bbcelite.com/disc/releases.html#sideways-ram), which moves the ship blueprints from the flight code into sideways RAM, thus freeing up lots of spare memory. The flight code stores ship blueprints between &5600 and &6000, so moving this into sideways RAM easily frees up enough memory for us to move the game code up to &1200.

But what about BBC Micros without sideways RAM? Alas, the only solution is to drop enough flight features to enable the flight binary to fit in memory along with the Econet workspace and the ship blueprints. I chose to drop the docking computer sequence (so docking is instant), and planetary details (so there are no craters, meridians or equators), as these do not affect gameplay. This approach saves enough memory for a standard BBC Micro to be able to load Elite over Econet.

There is one more issue. The majority of BBC Micros that have Econet fitted include the network code in a DNFS ROM, which combines the disc filing system and net filing system ROMs in one chip. To get PAGE down to &1200 on these systems, we need to disable just the DFS part of the DNFS ROM, leaving the NFS part to load Elite. This can be done, but it requires poking memory locations, depending on the bank number containing the DNFS ROM, so Elite over Econet comes with a built-in utility program, FixPAGE, that does the hard work for us. This utility disables all ROMs except for BASIC and NFS, even if the NFS comes as part of the DNFS ROM, and this brings the start of user memory down to a level where Elite can successfully run. It is automatically run by the loading process when required.

So we now have versions of Elite that shouldn't clash with Econet, at least in terms of memory. Let's look at what else needs to be done.

## Playing nicely with NFS and NMIs

													 --------------------------------

						Now that Elite should run happily without clashing with Econet, we need to update any DFS-specific code to work with the hierarchical NFS (or, in the case of the Electron, backport the entire disc access menu to the game). We also need to ensure that the BBC Master version deals with NMIs correctly, as otherwise the Master will get interrupted by network traffic while we're trying to play Elite (the BBC Micro doesn't appear to have the same issue with NMIs, so thay remain enabled in the Econet version).

The good news is that the [BBC Master Compact variant](https://elite.bbcelite.com/master/releases.html#compact), released by Superior Software in 1987, contains most of what we need. This is BBC Master 128 Elite, updated to work with ADFS, which is also hierarchical. As part of this, the disc access menu was changed to make more sense with the single ADFS drive on the Compact - so things like "drive number" were removed and replaced by a request for a directory name, and the catalogue code was updated to display files in a single column and across multiple pages, as there's too much information to fit two columns on one screen. Finally, routines were added to claim and release the NMI workspace before and after file access, which is exactly what we need to implement for Econet.

It turns out that the Compact's updates work nicely with NFS, with just a few tweaks needed to the OS commands for switching to the commander file directory (which is $.E in the ADFS version, but we want to switch to EliteCmdrs in the user's main directory for Elite over Econet). The code changes are also suitable for porting to the I/O Processor code in the 6502 Second Processor version, to update the file menu for NFS. A few OS command strings need the drive number removing in the Parasite code, but that's about it.

## Loader programs

													 ---------------

						We're almost there, but there is one more area where Elite clashes with Econet, and that's in the file structure. Econet uses a hierarchical directory structure like ADFS, but most versions of Elite were built to run on DFS. Not only that, but they rely on all of the game files being on the same disc, and that's a problem for Econet.

In an ideal world, players would load Elite from a central library on the fileserver, but would be able to save their commander files locally into their own main user directories. We can achieve this by creating loader programs in the Econet library directories, while keeping the game binaries out of the library and in a separate game folder (to avoid filling the library with too many files). If we then switch directory to the user's main directory once the game is loaded, then loading and saving commander files will work as required.

To achieve this, there are two loader programs that go into the Econet library, which are built by the [elite-over-econet repository](https://github.com/markmoxon/elite-over-econet): they are called Elite and EliteB, and they go in the $.Library and $.Library1 folders on the server. This means that if a user types a *Elite command, then the Elite loader gets executed, irrespective of the current directory. When run without a parameter, the loader does some basic platform checks, and runs the correct game binary depending on the machine type: if this is a Master then it runs ELTME, if this is a 6502 Second Processor then it runs ELTSE, if this is an Electron then it runs ELTEE, and if this is a BBC Micro then it runs EliteB (see the next section).

The Elite loader can also take four parameters, which do the following rather than running the game:

| Command | Effect | 
|---|---|
| *Elite V | Show the version details and build date for the installed game | 
| *Elite X | Run the Executive version of 6502 Second Processor Elite (see [secrets of the Executive version](https://elite.bbcelite.com/deep_dives/secrets_of_the_executive_version.html)for more details) | 
| *Elite S | Run the Elite over Econet scoreboard (see [the Elite multiplayer scoreboard](https://elite.bbcelite.com/elite_over_econet_scoreboard.html)) | 
| *Elite D | Run the Elite over Econet debugger (see [the Elite multiplayer scoreboard](https://elite.bbcelite.com/elite_over_econet_scoreboard.html)) | 

The various game binaries have a consistent naming convention to make them easier to manage in NFS. Files called ELTA* are for the standard BBC Micro version, ELTB* files are for the sideways RAM version, ELTS* files are for the 6502 Second Processor version, ELTE* files are for the Acorn Electron version, and ELTM* files are for the BBC Master version. This convention gets around issues with the original games, which have files called T.CODE, D.CODE and so on, which would need lots of nested directories in NFS. There is one nested directory, however: alongside the game binaries are the ship blueprint files for the standard disc version, which all live in the sub-directory $.EliteGame.D (as in the original discs they have names D.MOA to D.MOP, and it's a bit tidier to group them together in one place).

## The EliteB loader program

													 -------------------------

						The EliteB loader for the BBC Micro is a bit more complicated than the Elite loader. Once the BBC Master and 6502 Second Processor versions have loaded the game binaries, they don't need to do it again - there is enough memory to load the entire game, so from this point onwards they only need to access the filing system to load and save commander files. So in these versions, the game binaries have one extra step when they load for the first time: they switch directory to the user's main directory, like this:

*DIR *DIR EliteCmdrs

This changes the current directory to the individual user's EliteCmdrs directory, so from this point on, commander files can be loaded and saved locally (the *DIR with no argument switches to the user's main directory, and then *DIR EliteCmdrs switches to the EliteCmdrs directory).

The disc version also changes to the EliteCmdrs directory when it loads, but there's a problem with this. When you launch from the space station, the disc version goes looking for the flight code and (in the standard version) the ship blueprint files. But these aren't in the EliteCmdrs directory, so we need a way of flipping between the game binary folder in $.EliteGame and the commander files in EliteCmdrs.

Simply doing a *DIR $.EliteGame won't do, though. Because we want users to be able to install the Elite binaries wherever they want to, we can't be sure that the binaries are actually in $.EliteGame, so we can't simply switch to that folder. Instead, if there is an EliteConf file present alongside the Elite loader (typically in the library), then the loader will fetch the new location from EliteConf, so if we're on, say, a BBC Master, *Elite will *DIR into the correct game binary folder before running the ELTME executable for the BBC Master version of Elite. In the same vein, *EliteB will *DIR into the game binary folder before running the relevant executable for the BBC Micro, and this means we can extend *EliteB to take a parameter that lets us load a specific binary from the correct directory, without the game itself having to know where that binary is.

These are the various commands that the *EliteB loader supports:

| Command | Details | 
|---|---|
| *EliteB | Load the game for the first time (*RUN ELTAB) | 
| *EliteB A to P | Load a ship blueprints file for the standard version, with the file letter as the parameter (*LOAD D.MOA to *LOAD D.MOP) | 
| *EliteB Q | Run the docked code for the standard version and dock with the station (*RUN T.CODE in the original, *RUN ELTAT in the Econet version) | 
| *EliteB R | Run the docked code for the sideways RAM version and dock with the station (*RUN T.CODE in the original, *RUN ELTBT in the Econet version) | 
| *EliteB S | Load the docked code for the standard version and restart the game (*LOAD T.CODE in the original, *LOAD ELTAT in the Econet version) | 
| *EliteB T | Load the docked code for the sideways RAM version and restart the game (*LOAD T.CODE in the original, *LOAD ELTBT in the Econet version) | 
| *EliteB U | Run the flight code for the standard version (*RUN D.CODE in the original, *RUN ELTAD in the Econet version) | 
| *EliteB V | Run the flight code for the sideways RAM version (*RUN D.CODE in the original, *RUN ELTBD in the Econet version) | 

So when we launch from the station in the standard version of BBC Micro Elite over Econet, it executes *EliteB U to run the flight code for the standard version, and because EliteB is in the Econet library and it knows the correct location of the Elite binary directory, then this *EliteB command will work for everyone, and it can switch to the correct directory and run the required binary. In this way we can support the disc version's need to keep loading binaries and blueprints, and if the network manager wants to move the game binaries, then they simply need to set up an EliteConf file, as before.

If there is no argument to *EliteB, then it loads the game from scratch by running the ELTAB binary in the game binary folder. This checks the value of PAGE and runs FixPAGE if it is too high, so we can try to reduce it to the right level. If PAGE is already low enough, then it performs a sideways RAM check and runs the correct version of disc Elite depending on what it finds:

- *RUN ELTAI for the standard version (*RUN ELITE4 in the original)
- *RUN ELTBI for the sideways RAM version (*RUN INTRO in the original)

And there you have it - BBC Micro Elite loading over Econet.

## Multiplayer scoreboards

													 -----------------------

						Elite over Econet also supports multiplayer scoreboards - see [the Elite multiplayer scoreboard](https://elite.bbcelite.com/elite_over_econet_scoreboard.html) for details. Individual instances of Elite can be configured to send score information to another machine on the network, which can then display a live scoreboard showing the status of multiple players across the net.

The core of this functionality is the TransmitCmdrData routine, which transmits a 20-byte block of data containing the player's status. The data block contains the following information:

| Byte | Details | 
|---|---|
| #0-7 | Player's name, terminated by a carriage return (maximum seven characters plus CR) | 
| #8 | Player's legal status: 0 = clean 1 = offender 2 = fugitive | 
| #9 | Player's status condition: 0 = docked 1 = green 2 = yellow 3 = red | 
| #10 | Player's kill count (low byte) | 
| #11 | Player's death count | 
| #12-15 | Player's credits (low byte first) | 
| #16 | Machine type: 0 = BBC Micro with sideways RAM, B+ or B+128 1 = Master 2 = 6502 Second Processor 3 = BBC Micro 4 = Archimedes 5 = Acorn Electron | 
| #17 | Player's station number (when data is being forwarded): 0 = this transmission is coming directly from Elite and the player's station number can be found in the transmission itself Non-zero = this data packet is being forwarded, so bytes #17 and #18 contain the player's station and network numbers, and the transmission itself will contain the address of the forwarding machine | 
| #18 | Player's network number (when data is being forwarded): If byte #17 is zero then this transmission is coming directly from Elite and the player's network number can be found in the transmission itself If byte #17 is non-zero then this data packet is being forwarded, so bytes #17 and #18 contain the player's station and network numbers, and the transmission itself will contain the address of the forwarding machine | 
| #19 | Player's kill count (high byte) | 

To prevent a slow network from affecting gameplay, the data is transmitted by the TransmitCmdrData routine, but we don't poll to check whether there has been a response. This means that sometimes data doesn't get through, but this isn't a big problem as data is sent regularly, especially during flight, when it is transmitted every 256 iterations of the main loop.

One point to note is that in the BBC Micro sideways RAM version, the Econet transmission routines are included in the sideways RAM image, after the end of the ship blueprints. This means that instead of calling the TransmitCmdrData routine directly, we have to use the extended vectors, which are like the normal vectors, but they switch to the specified ROM bank before calling the address in the vector (and switch back afterwards). Specifically, we use the extended IND2 vector to call TransmitCmdrData, and the extended IND3 vector to call GetNetworkDetails from the docked code (the latter implements the network configuration screen). The extended IND1 vector is already used by the sideways RAM code to call the file handler that loads ship blueprints from sideways RAM rather than disc.

## Files on the Elite over Econet disc

													 -----------------------------------

						Because the Elite over Econet disc contains multiple versions of Elite, the game binaries have been renamed to avoid clashes, and to implement a consist naming convention for Econet (removing DFS directories, for example).

The Elite over Econet disc image contains the following general files:

| File | Details | 
|---|---|
| ReadMe | Installation instructions and build date | 
| ElScore | The scoreboard program | 
| ElDebug | The debugger for the scoreboard | 
| FixPAGE | A utility to set PAGE at the correct level on the BBC Micro | 

It also contains the following loader files that are deployed to the network library:

| File | Details | 
|---|---|
| Elite | An Econet loader that runs the correct version of Elite over Econet, depending on the machine type, so users can just type *Elite to play the game; also supports parameters to show the version details or run the scoreboard, debugger or Executive version | 
| EliteB | The Econet loader for the BBC Micro version, which also loads the docked and flight binaries and ship blueprints when docking or launching | 

The 2024 version of Elite over Econet also contained EliteM, EliteSP and EliteX loader files, but these were rolled into the Elite binary in 2025, so if you are upgrading, these files can be removed from the library.

These are the files for the standard BBC Micro version of Elite over Econet (note that the game binaries all start with ELTA, while the ship blueprints live in subdirectory D):

| File | Details | 
|---|---|
| ELTAB | A loader that runs FixPAGE if required, and then runs either ELTAI or ELTBI, depending on the status of sideways RAM. | 
| ELTAI | ELITE4 from the disc version, which runs the game | 
| ELTAT | T.CODE from the disc version, which contains the docked code, updated for Econet | 
| ELTAD | D.CODE from the disc version, which contains the flight code, updated for Econet | 
| D.MOA to D.MOP | The ship blueprint files from the disc version | 

These are the files for the BBC Micro sideways RAM version of Elite over Econet (note that the game binaries all start with ELTB):

| File | Details | 
|---|---|
| ELTBI | INTRO from the sideways RAM variant, which runs the game | 
| ELTBR | A ROM image that contains all the ship blueprints, assembled to support the XX21 lookup table at &5700 rather than &5600 | 
| ELTBM | MNUCODE from the sideways RAM variant, which contains the sideways RAM loading routines | 
| ELTBS | SCREEN from the sideways RAM variant, which displays the mode 7 Acornsoft loading screen | 
| ELTBT | T.CODE from the disc version, which contains the docked code, updated for Econet | 
| ELTBD | D.CODE from the disc version, which contains the flight code, updated for Econet | 

These are the files for the BBC Master version of Elite over Econet (note that the game binaries all start with ELTM):

| File | Details | 
|---|---|
| ELTME | M128Elt from the original disc, updated for Econet | 
| ELTMD | BDATA from the original disc, which contains the game data, updated for Econet | 
| ELTMC | BCODE from the original disc, which contains the game code, updated for Econet | 

These are the files for the Acorn Electron version of Elite over Econet (note that the game binaries all start with ELTE):

| File | Details | 
|---|---|
| ELTEL | A loader for the sideways RAM image in ELTER | 
| ELTER | The speed-critical code for Electron Elite, to load into sideways RAM | 
| ELTEE | ELITE from the original disc, which displays the mode 7 Acornsoft loading screen | 
| ELTED | ELITEDA from the original disc, which displays the Saturn loading screen | 
| ELTEC | ELITECO from the original disc, which contains the game code, updated for Econet | 

These are the files for the 6502 Second Processor version of Elite over Econet (note that the game binaries all start with ELTS):

| File | Details | 
|---|---|
| ELTSE | ELITE from the original disc, updated for Econet | 
| ELTSA | ELITEa from the original disc, updated for Econet | 
| ELTSI | I.CODE from the original disc, which contains the I/O Processor code, updated for Econet | 
| ELTSP | P.CODE from the original disc, which contains the Parasite code, updated for Econet | 

These are the files for the Executive version of Elite over Econet (note that the game binaries all start with ELTX):

| File | Details | 
|---|---|
| ELTXE | ELITE from the original disc, updated for Econet | 
| ELTXA | ELITEa from the original disc, updated for Econet | 
| ELTXI | I.CODE from the original disc, which contains the I/O Processor code, updated for Econet | 
| ELTXP | P.CODE from the original disc, which contains the Parasite code, updated for Econet | 

By default, all the game binaries and scoreboard programs live in $.EliteGame, while the loaders are deployed to the $.Library and $.Library1 folders.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*DIR
  *DIR EliteCmdrs
```



---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_over_econet_technical_information.html](https://elite.bbcelite.com/hacks/elite_over_econet_technical_information.html)*
