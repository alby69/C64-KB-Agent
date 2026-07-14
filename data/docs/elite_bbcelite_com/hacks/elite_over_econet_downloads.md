---
title: Playing Elite over Econet
source_url: https://elite.bbcelite.com/hacks/elite_over_econet_downloads.html
category: reference
topics:
- basic
- assembly
- input handling
difficulty: beginner
language: mixed
hardware:
- CPU
- SID
- KERNAL
- CIA
related:
- keyboard-handling
- music-player
- sound-programming
- joystick-reading
- memory-map
- kernal-routines
- sid-registers
- cia-registers
scraped_at: '2026-07-14'
---

# Playing Elite over Econet

## How to play Elite over an Econet network

You can play Elite over Econet on the following networked machines:

- BBC Micro Model B
- BBC Micro Model B+
- BBC Micro Model B+128
- BBC Micro with 6502 Second Processor
- BBC Master 128
- BBC Master ET
- BBC Master Turbo
- BBC Master with external 6502 Second Processor
- Acorn Electron with 16K sideways RAM
- Acorn Archimedes
- Risc PC

For details of how to play Elite over Econet via the TNMoC Econet Cloud, see below.

For details of how to download and install Elite over Econet for the 8-bit machines on your own network (i.e. the BBC Micro, BBC Master and Acorn Electron), see the instructions for [installing Elite over Econet](https://elite.bbcelite.com/elite_over_econet_installing.html).

For more information about the 32-bit version, see [Elite over Econet on the Acorn Archimedes](https://elite.bbcelite.com/elite_over_econet_acorn_archimedes.html).


													 --------------------------------------------

						If you have a PiEconetBridge that is connected to the TNMoC Cloud (the community Econet service from the National Museum of Computing's Acorn team), then you can play Elite over Econet without installing a thing.

To play on a networked BBC Micro or BBC Master, enable Econet and enter the following:

*I AM 63.13 BOOT

This will load a friendly menu from which you can choose various options:

![Loading BBC Micro Elite over the TNMoC Econet Cloud](https://elite.bbcelite.com/images/elite_over_econet/fileserver_menu.png) 

						To run Elite on a networked Acorn Electron, enable Econet and enter the following:

*I AM 63.13 ELITE

This will run Elite without showing a menu, as there is only one version for the Electron.

The cloud can be a bit slow at times and you will be sharing the commander file space with other players, but it's a good way to get started if you don't want to install Elite on your own fileserver. You're also guaranteed to be playing the very latest version of the game, as the 63.13 server is hosted by me and lives just beneath the desk where I do all my Elite hacking.


													 -------------------------

						If you have installed Elite on your own fileserver, then the rest of this page is for you.

Once the game is installed on the fileserver, you can play Elite on a BBC Micro, BBC Master or Acorn Electron by typing:

*Elite

This will load the correct version of Elite for the machine you are using to access your network. The command is case insensitive, so *ELITE and *elite will also work.

If you are running the game on a BBC Micro Model B or B+, then the loading process may try to free up enough memory, in which case you should follow the on-screen instructions. See the BBC Micro section below for details.

If Elite has only been installed for specific users (as opposed to all users), then they will need to *DIR into their own EliteCmdrs directory first, like this:

*DIR *DIR EliteCmdrs *Elite

You can also pass parameters to the *Elite command, as follows:

| Command | Effect | 
|---|---|
| *Elite V | Show the version details and build date for the installed game | 
| *Elite X | Run the Executive version of 6502 Second Processor Elite (see [secrets of the Executive version](https://elite.bbcelite.com/deep_dives/secrets_of_the_executive_version.html)for more details) | 
| *Elite S | Run the Elite over Econet scoreboard (see [the Elite multiplayer scoreboard](https://elite.bbcelite.com/elite_over_econet_scoreboard.html)) | 
| *Elite D | Run the Elite over Econet debugger (see [the Elite multiplayer scoreboard](https://elite.bbcelite.com/elite_over_econet_scoreboard.html)) | 

If you are playing the game on an Archimedes and want to send scores to a multiplayer scoreboard over Econet, then you should load Elite as usual, and run the EliteNet application alongside it (see [Elite over Econet on the Acorn Archimedes](https://elite.bbcelite.com/elite_over_econet_acorn_archimedes.html) for details). You can install both Elite and EliteNet on an Econet fileserver if you want, but this isn't essential; it's probably quicker to load them from a hard disc.

## Versions included in Elite over Econet

													 --------------------------------------

						Elite over Econet contains updated versions of Acornsoft Elite that work when loaded from a fileserver over Econet (unlike the originals). The *Elite loader will load the correct version for the system it is being run on. Here's a summary of which versions run on which hardware:

- The cut-down BBC Micro version works on the unexpanded Model B and Model B+.
- The full-featured BBC Micro sideways RAM version works on the Model B with 16K sideways RAM, the Model B+ with 16K sideways RAM, and the Model B+128.
- The Acorn Electron version works on the Electron with 16K sideways RAM.
- The 6502 Second Processor version works on the BBC Master Turbo, the BBC Master with an external 6502 Second Processor, and the BBC Micro with an external 6502 Second Processor.
- The Executive version works on the same range of machines as the 6502 Second Processor version.
- The Master version works on the Master 128, Master ET and Master Compact. It is based on the Superior Software release, so it supports digital joysticks on the latter.
- The EliteNet application runs on an Archimedes with RISC OS 3 or Risc PC. It runs alongside Archimedes Elite to send scores to an Econet scoreboard, and to allow you to save your scores if you want to take a break from a multiplayer competition.

The game experience is unchanged - this is the same Elite game as always - but these versions load over Econet and let you load and save commander files to your network account.

That said, the version for the unexpanded BBC Micro Model B and B+ does have two features missing from the original, which had to be removed to make room for Econet. First, the docking computer now instantly docks on pressing "C", just like the BBC Micro cassette and Acorn Electron versions of Elite; and second, the planets are simple circles, without meridians, equators or craters, like the Electron version (and in the flicker-free variant, the planet circles still flicker). Gameplay is otherwise unaffected.

The Acorn Electron version of Elite over Econet has a number of extra features that are missing from the original game, and which I have added to make it fairer when competing with the BBC and Archimedes versions. The extra features are: faster graphics, full save/load menu, military lasers, improved cargo selling, extended system descriptions, system search and planetary details (meridians and craters).

As noted above, the *Elite loader will load the correct version for the system it is being run on. For the BBC Micro version, the loader looks for 16K of sideways RAM, and if it finds it, it loads the fully featured sideways RAM variant of BBC Micro disc Elite. If there is no sideways RAM, it loads the cut-down version of BBC Micro disc Elite that is missing the docking computer animation and detailed planets.


													 -------------------------

						Here are some notes on playing Elite over Econet:

- Commander files will be saved into each individual user's EliteCmdrs directory.
- Each user has access to a commander file called MAX that they can load from the game menu. This contains a maxed-out commander, to give players a head start.
- If a user tries to run Elite but doesn't have a directory called EliteCmdrs in their main user directory, i.e. $.<user>.EliteCmdrs, then the game will not load.
- The BBC Micro version loads data every time you launch or dock. This shouldn't take too long, but if the network is slow, you might have to wait a bit longer. You can tell when the game is loading data as the top part of the dashboard tends to flicker.

On top of this, Elite over Econet supports multiplayer scoreboards, which lets you run live Elite competitions between groups of players. The following changes have been made to make multiplayer games fairer between the different versions:

- Docking with the docking computer is instant in the standard BBC Micro and Acorn Electron versions of Elite over Econet. To make things fair in multiplayer competitions, all other versions of Elite over Econet support instant docking (as otherwise BBC Micro players would have a time advantage). You can activate this by pressing "C" to activate the normal docking sequence, and then tapping "J" to insta-dock. This feature is backported from the NES version of Elite, so it's an authentic part of the Elite canon.
- The flicker-free 6502 Second Processor and Executive versions have been tweaked to run at the same speed as the other versions. This makes them much more playable and brings them in line with the single-processor versions. The original, non-flicker-free versions have been left to run at the same speed.

See [the Elite multiplayer scoreboard](https://elite.bbcelite.com/elite_over_econet_scoreboard.html) for more details on multiplayer games.

## The BBC Micro version

													 ---------------------

						Because memory is really tight, the BBC Micro version needs to configure the machine correctly for Elite to work. Specifically, the value of PAGE has to be &1200 or less for the game to work, as otherwise the Econet OSWORD calls will corrupt the game code. The BBC Master and 6502 Second Processor versions are much more forgiving - this is only an issue on the BBC Micro.

To make it easier to set up your BBC Micro for playing Elite over Econet, the loader tries to free up enough free memory by disabling all ROMs except for NFS and BASIC. This should bring PAGE down to the correct level. If you try to run Elite and PAGE is too high, then follow the on-screen instructions:

![Freeing up enough memory in BBC Micro Elite over Econet](https://elite.bbcelite.com/images/elite_over_econet/fixpage.png) 

						This should bring PAGE down to &1200, ready for you to run Elite. The loader might not be able to disable all ROMs, but it should work for most setups (in particular, DFS 0.9 can't be disabled, so you won't be able run Elite over Econet with this version).

Note that even with the loader trying to free up memory, Elite will not work with ANFS on a BBC Micro, as it is too memory-hungry; for the BBC Micro version, you need to use NFS or DNFS. ANFS is fine on a BBC Master or a BBC Micro with 6502 Second Processor, it's just the standard BBC Micro that has problems. If you have both ANFS and NFS fitted to your BBC Micro, then the loader will try to disable ANFS and use NFS, which should work.

If your BBC Micro has sideways RAM, then a full version of the game will be loaded. This stores ship blueprints and network code in sideways RAM, leaving enough free memory for Elite to work alongside Econet. Most sideways RAM systems will work automatically, but if you run into difficulties or you want to store the ROM in a specific ROM bank, then you can pre-load the Elite ROM yourself, and the loader should identify this and won't try to load it again.

If you want to do this, then the ROM image is the ELTBR file in $.EliteGame. You can either load it into sideways RAM yourself, or you can burn it into an EPROM or EEPROM (it works equally well in ROM or RAM).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*I AM 63.13 BOOT
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*I AM 63.13 ELITE
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*Elite
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*DIR
  *DIR EliteCmdrs
  *Elite
```



---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_over_econet_downloads.html](https://elite.bbcelite.com/hacks/elite_over_econet_downloads.html)*
