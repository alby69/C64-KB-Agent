---
title: Installing Elite over Econet
source_url: https://elite.bbcelite.com/hacks/elite_over_econet_installing.html
category: manual
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
- SID
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# Installing Elite over Econet

## How to install Elite on an Econet fileserver

To play Elite on your Econet network, you'll either need a PiEconetBridge with access to the TNMoC Econet Cloud (see [playing Elite over Econet](https://elite.bbcelite.com/elite_over_econet_downloads.html) for details), or you'll need to install the game on your own Econet fileserver by choosing one of these options and following the instructions below (they both contain the same files, so choose the one that's easiest to install on your network):

- [Elite over Econet as a DSD disc image](https://elite.bbcelite.com/versions/elite_over_econet/elite-over-econet-flicker-free.dsd)for installing via a BBC Micro, BBC Master or Acorn Electron
- [Elite over Econet as a RISC OS zip file](https://elite.bbcelite.com/versions/elite_over_econet/elite-over-econet-flicker-free.zip)for installing via an Archimedes

If you want to be able to transmit scores from Archimedes Elite to scoreboards on your network, you should also download the following:

- The [EliteNet application](https://elite.bbcelite.com/versions/elite_over_econet/elitenet.zip)as a RISC OS zip file
- Version 1.14 of Archimedes Elite, which you can [download from archive.org](https://web.archive.org/web/20060130144818/http://phlamethrower.co.uk/riscos/elite.zip).

See [Elite over Econet on the Acorn Archimedes](https://elite.bbcelite.com/elite_over_econet_acorn_archimedes.html) for more details about playing Archimedes Elite over Econet; the rest of this page covers the 8-bit version.

While there isn't a version of Econet Elite for the Acorn Atom, Ian Stocks has written a version of the Elite scoreboard that runs on the Atom, which you can download [as a BASIC program](https://elite.bbcelite.com/versions/elite_over_econet/A42) or [as a text file](https://elite.bbcelite.com/versions/elite_over_econet/A42.txt). See [the Elite multiplayer scoreboard](https://elite.bbcelite.com/elite_over_econet_scoreboard.html) for details.

You can install Elite over Econet on any network that has a Level 2, Level 3, Level 4, MFDS or PiFS (PiEconetBridge) fileserver. You can install the game via a BBC Micro, a BBC Master, an Acorn Electron or an Archimedes, and you can either install the game for all users of the network, only for individual users, or into a dedicated user account.

Basic installation instructions are provided in a ReadMe file on the disc, but for much more detailed information, see below.

Note that the links above will download the flicker-free version of Elite over Econet. If you would prefer to install the original version, you can download this [as a DSD disc image](https://elite.bbcelite.com/versions/elite_over_econet/elite-over-econet.dsd) or a [RISC OS zip file](https://elite.bbcelite.com/versions/elite_over_econet/elite-over-econet.zip) instead. Note that the Acorn Electron version is always flicker-free when playing over Econet; only the BBC versions retain their flicker in this alternative download.

If you have any problems installing or running Elite over Econet, you can post to [this Stardot thread](https://www.stardot.org.uk/forums/viewtopic.php?t=28355) and I'll do my best to help.

## Installation options

													 --------------------

						Elite can be installed in two ways: for all users on your network, or for individual users. The installation instructions below cover both options.

You can also choose where to install the game binaries. By default they live in the $.EliteGame directory, but you can change this location by using an EliteConf file. This process is described below.

A common configuration is to create a dedicated user called ELITE, and to install Elite for just that user. You can then set up a !BOOT file like this to run the game on login:

*DIR *DIR EliteCmdrs *Elite

This means that users of your network can run Elite by simply typing:

*I AM ELITE

The only thing to be aware of is that because there is only one login, all saved games will go into the same directory (e.g. $.ELITE.EliteCmdrs). So, when saving commanders, it's a good idea to use the catalogue option first to make sure there isn't an existing commander file with the same name.

## Installation instructions via a BBC Micro, BBC Master or Acorn Electron

													 -----------------------------------------------------------------------

						To install Elite using a BBC Micro, BBC Master or Acorn Electron, download the DSD disc image and copy the files to your server as follows (files have been grouped into DFS directories to make this process easier). Note that the disc image is a double-sided disc, so it contains files on both drive 0 and drive 2. I use [TREECOPY](https://mdfs.net/Software/FileTools/) to copy files from the disc to the server, but other copying programs are available.

- Create a directory on the server called $.EliteGame, to use for the game binaries (see the section below if you want to install the game into a different location).
- Copy all the files from DFS directory G on drive 0 of the disc image into $.EliteGame.
- Copy all the files from DFS directory G on drive 2 of the disc image into $.EliteGame.
- Create a directory called D inside $.EliteGame (i.e. $.EliteGame.D) and copy all the files from DFS directory D on drive 2 of the disc image into there.
- Create a directory called EliteCmdrs in the top level of the main home directory for each user who wants to play Elite (e.g. $.Mark.EliteCmdrs for user Mark), and copy all the files from DFS directory C on drive 2 of the disc image to there. If you don't create the EliteCmdrs directory, then the game will not work for that user.
- Do one of the following, depending on who you want to be able to play the game:
								- If you want all users to be able to play Elite, then copy all the files from DFS directory L on drive 2 of the disc image into $.Library and $.Library1 and ensure all users have their library set accordingly.
- If you want to restrict the game to specific users, then copy all the files from DFS directory L on drive 2 of the disc image into the EliteCmdrs directory that you just created in each of the users' main home directories.
 

The game is now installed - see the section on [playing Elite over Econet](https://elite.bbcelite.com/elite_over_econet_downloads.html#playing) for details on how to run the game.

## Installation instructions via an Archimedes

													 -------------------------------------------

						To install Elite using an Archimedes, download the zip file and open it up using an application like SparkFS (you can download SparkFS for free from [David Pilling's site](https://www.davidpilling.com/wiki/index.php/SparkFS)). Then copy the directories from the zip file to your server as follows:

- Copy the EliteGame directory to your fileserver's root directory, to create a directory called $.EliteGame on the server (see the section below if you want to install the game into a different location).
- Copy the EliteCmdrs directory to the top level of the main home directory for each user who wants to play Elite (e.g. $.Mark.EliteCmdrs for user Mark)
- Do one of the following, depending on who you want to be able to play the game:
								- If you want all users to be able to play Elite, then copy the files from the Library and Library1 directories into $.Library and $.Library1 on your fileserver, and ensure all users have their library set accordingly.
- If you want to restrict the game to specific users, then copy all the files from the Library directory into the EliteCmdrs directory that you created in each of the users' main home directories.
 

The game is now installed - see the section on [playing Elite over Econet](https://elite.bbcelite.com/elite_over_econet_downloads.html#playing) for details on how to run the game.

## Installing to a different directory or library

													 ----------------------------------------------

						If you don't want to install the Elite binaries into the default directory of $.EliteGame, then that's no problem - you can install them anywhere you like. It is even possible to install Elite for just one user and have every single Elite-related file, including the loaders and binaries, within that user's directory and nowhere else.

If you do install the game binaries into a custom directory, then you need to tell the game where to look. To do this, you need to create a file called EliteConf that contains the full path of the directory where you've installed the binaries, followed by a carriage return (see below for instructions on creating this file).

- If you have installed Elite for all users then you should create the EliteConf file in $.Library (and $.Library1 if present).
- If you have installed Elite for individual users, then you should create EliteConf in the EliteCmdrs directory for each user (so EliteConf goes in the same directory as the loader programs Elite and EliteB).
- If your users have their own libraries, or you have your own custom library structure on your fileserver, then you just need to make sure that the loader programs Elite and EliteB are on the load path, with EliteConf in the same directory as the loaders. As long as the loader can be run with *Elite, then things should work.

If you are installing Elite via a BBC Micro, BBC Master or Acorn Electron, then the easiest way to create the EliteConf file is by typing:

*BUILD EliteConf

Type the full directory path containing the game binaries (e.g. $.Games.Elite if you have installed the binaries into $.Games.Elite), and then press RETURN and then ESCAPE.

Note that you must give public read access to this file, which you can do like this:

*ACCESS EliteConf WR/R

You can tailor this permission to your own needs, just as long as there is public read access (i.e. the "/R" part in the above). Make sure you set the correct permissions for all copies of EliteConf.

Once you have created the EliteConf file, Elite should run correctly from the newly configured directory. If you upgrade Elite over Econet to a later version, then the EliteConf file will be left untouched by the upgrade process, so you can simply deploy the new version's files into your custom directory structure, and the upgraded version should continue to work without needing to repeat the configuration process.

If you are installing Elite to a custom directory via an Archimedes, then you can either use the *BUILD approach above (in a task window or by pressing F12), or you can create the file using Edit.

If you choose to do the latter, then type the full directory path on the first line of the file, followed by RETURN, and then convert the line feed to a carriage return with the CR<->LF option in the Edit submenu. This will show as [0d], so if you are setting the directory to $.Games.Elite, for example, then it will appear as $.Games.Elite[0d] in the Edit window. Save this file as EliteConf into the correct locations on the server (i.e. $.Library, $.Library1 or EliteCmdrs), and make sure you give all copies public read access via the Access submenu in the Filer.

## Installed files

													 ---------------

						If you install Elite over Econet in the default location, then the complete list of installed files on your server should look like this if you are installing Elite for all users:

- $.EliteGame
								- ElDebug
- ElScore
- ELTAB
- ELTAD
- ELTAI
- ELTAT
- ELTBD
- ELTBI
- ELTBM
- ELTBR
- ELTBS
- ELTBT
- ELTEC
- ELTED
- ELTEE
- ELTEL
- ELTER
- ELTMC
- ELTMD
- ELTME
- ELTSA
- ELTSE
- ELTSI
- ELTSP
- ELTXA
- ELTXE
- ELTXI
- ELTXP
- FixPAGE
- Version
 
- $.Library
								- Elite
- EliteB
 
- $.Library1
								- Elite
- EliteB
 
- $.User1.EliteCmdrs
								- MAX
 
- $.User2.EliteCmdrs
								- MAX
 
- ...

Or like this if you are just installing Elite for one user:

- $.EliteGame
								- ElDebug
- ElScore
- ELTAB
- ELTAD
- ELTAI
- ELTAT
- ELTBD
- ELTBI
- ELTBM
- ELTBR
- ELTBS
- ELTBT
- ELTEC
- ELTED
- ELTEE
- ELTEL
- ELTER
- ELTMC
- ELTMD
- ELTME
- ELTSA
- ELTSE
- ELTSI
- ELTSP
- ELTXA
- ELTXE
- ELTXI
- ELTXP
- FixPAGE
- Version
 
- $.User.EliteCmdrs
								- MAX
- Elite
- EliteB
 

The 2024 version of Elite over Econet also contained EliteM, EliteSP and EliteX files, but these were rolled into the Elite binary in 2025, so if you are upgrading, these files can be removed from the library.

If you install the game binaries to a directory other than $.EliteGame, then you need to add the EliteConf file as described in the previous section. If you are installing Elite for all users then you need to add these files:

- $.Library
								- EliteConf
 
- $.Library1
								- EliteConf
 

If you are just installing Elite for one user, then this is the file to add:

- $.User.EliteCmdrs
								- EliteConf
 

If you can't get your installation working, let me know in [this Stardot thread](https://www.stardot.org.uk/forums/viewtopic.php?t=28355) and I'll try to help.


													 ---------------

						Elite over Econet has had the following releases:

- 2024-01-16 - Initial release
- 2024-04-15 - Added BBC Micro sideways RAM version
- 2024-04-16 - Fixed loading issues with BBC Micro version when multiple RAM banks are available
- 2024-04-20 - Fixed a bug in the BBC Micro version that would incorrectly dock the ship following death
- 2024-05-01 - Added standard BBC Micro version and multiplayer scoreboard
- 2024-05-03 - Updated BBC Micro sideways RAM version to work with IntegraB board
- 2024-05-11 - Fixed a bug in the scoreboard where changing port would break transmissions
- 2024-05-13 - Fixed a crash with NFS 3.34 on launching in the BBC Micro version
- 2024-05-14 - Added a warning to the BBC Micro loader if PAGE is too high, updated FixPAGE to disable ANFS where present
- 2024-05-15 - Fixed a minor alignment issue with numbers in the scoreboard
- 2024-05-16 - Reduced size of EliteB loader to allow for long custom install directory names
- 2024-05-18 - Fixed incorrect network number shown in the scoreboard when run on a BBC Micro
- 2024-05-23 - Forwarding now retains the correct network address of each player
- 2024-05-28 - Added EliteConf file for configuring installation directory, improved FixPAGE process for BBC Micro, added Executive version of 6502 Second Processor Elite
- 2025-03-24 - Major flicker-free update:
								- Flicker-free ships and planets added
- 6502 Second Processor versions now run at a playable speed
- New *Elite command-line options: [V]ersion, [S]coreboard, [D]ebugger and e[X]ecutive
- Fewer files in $.Library (from five down to just two)
- New scoreboard features: up to 100 players (was 20), scores can be deleted, faster screen refresh, better key handling, three-digit station numbers, ranking takes death count into consideration, save scoreboard to a TSV file
- New debugger features: log activity to a TSV file, forward scores to multiple stations, transmit test data, pause debugging
- Fixed a bug in the standard BBC Micro version that would hang the game when launching from the station
- EliteConf now works on all the main Econet servers (Level 2, Level 3, Level 4, MDFS and PiFS)
- The single-user BBC Micro version now runs without having to log in twice
 
- 2025-04-27 - TNMoC LAN party update:
								- Added scoreboard support to Archimedes Elite
- The kill count is now two bytes, so combat competitions can go on for as long as you like
- Saving a commander file will also save multiplayer scores, so you can take a break during a competition and pick it up later
- New scoreboard features: load and save score files, automated page-turning
- New debugger features: convert score files to TSV, merge score files
- Version information (*ELITE V) appears much more quickly on a BBC Micro
 
- 2025-05-08 - Fixed saving and loading of one-score scoreboards, added a *-command option to the scoreboard, fixed test data transmission in the debugger, fixed a bug in the BBC Micro version that accidentally disabled versions 3.40, 3.60 and 3.62 of NFS
- 2025-05-11 - Updated the BBC Micro version to support every known variant of NFS, improved stability of EliteNet
- 2025-05-13 - Further improvements to EliteNet stability
- 2025-05-17 - Added save/load of configuration and scores in EliteNet, fixed a deletion bug in the scoreboard, fixed an incorrect number of test users in the debugger, sanitise commander names sent from Archimedes Elite
- 2025-06-03 - Resetting scores no longer resets credits, broken beeps are fixed in BBC disc Elite, scoreboard page-turner supports screen-saving and alternates the sort order
- 2025-06-05 - Added Electron Elite sideways RAM version, improved error handling for scoreboard screen saving

You can check the release date for a given disc image by loading the disc and typing *TYPE README to display the credits. The build date is at the end.

You can check the release date for the installed version of Elite by typing *ELITE V, or by using *TYPE to look in the Versions file in the game binary folder (in the default installation, that's $.EliteGame.Version).


													 ------------

						The BBC Micro version of Elite over Econet has some known issues:

- If the scoreboard machine is a BBC Micro fitted with NFS 3.34, then the scoreboard won't show updates coming from the other side of a bridge (though it will show updates from machines on the local network). Upgrading to NFS 3.40+ fixes this.
- DFS 0.9 does not get disabled by the loader process, so you will have to find another way of disabling it (such as physically unplugging the ROM, or upgrading to DNFS or a later version of DFS). Upgrading to DFS 1.00+ or DNFS fixes this. This issue also applies to some MMFS ROMs (as they are based on DFS).
- The BBC Micro version of Elite over Econet will not work with ANFS (though ANFS is fine for the BBC Master and 6502 Second Processor versions). This is because ANFS 4.18 on the BBC Micro takes up too much memory to support Elite (the minimum value of PAGE is &1900 but Elite needs it to be &1200). You have to have NFS or DNFS installed for the BBC Micro version to work. The loader will disable ANFS, so if you have ANFS fitted as well as NFS or DNFS, then the game should run; if you only have ANFS fitted, then Elite will not load.
- If you have a teletext adapter with Acorn TFS, then turn off your teletext adapter but leave it plugged in, as otherwise TFS will steal enough memory to prevent Elite from loading. Alternatively, remove the TFS ROM from your machine.
- If you have the Superior Software Speech! ROM installed, then it will break Elite over Econet (for example, it will kill you randomly, particularly on hyperspacing). Unfortunately this ROM refuses to be disabled, so the only solution is to remove it from your machine.
- If Elite is being served from a PiFS server to a BBC Micro or BBC Master with a 6502 Second Processor enabled, then if you use the default PiEconetBridge clock speed, you may get a "No reply" error every now and then. Machines with second processors need a slightly slower clock speed to work reliably, and changing the clock speed from the default 5us period to 5.5us should help (while keeping the 1us mark). On more recent models of the bridge, you can do that using this command: econet-clock -p 5.5 -m 1 (and higher values of -p will also work, so setting it to 8 to cater for Electron Econet will also solve the co-pro issues).

The Acorn Electron version has some minor known issues:

- The catalogue option in the save and load menu can only show one screen of content, so if you have a lot of saved files, you might not see them all. (The BBC versions allow you to step through multiple screens by pressing RETURN, but this option is not yet available in the Electron version.)
- Elite over Econet is only compatible with the Electron-specific version of NFS 3.42, which supports the *BLANK and *NOBLANK commands. This is currently the only NFS available for the Electron, and it's the version that comes with the only available interface (from Roland on Stardot), so this shouldn't be a problem.

There are also some known issues with the EliteNet application for Archimedes Elite:

- When loading a new commander with a high score, go into the game, come back out and then reset the scores, as otherwise you might be awarded an extra kill (from when the score "jumps" on loading). You can see this in the Kills score in the application window.
- The current condition (red, yellow, green, docked) only updates if the Status screen is shown.
- The game will crash if the EliteOverEconet module is manually killed, so you should also quit the game if you kill the module.
- Some versions of ShareFS will double the interval between transmissions, so if the interval is set to 10 seconds then the game will transmit every 20 seconds. If this happens, the simplest solution is to halve the configured interval.

If you find any other issues, you can let me know in [this Stardot thread](https://www.stardot.org.uk/forums/viewtopic.php?t=28355).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*DIR
  *DIR EliteCmdrs
  *Elite
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*I AM ELITE
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*BUILD EliteConf
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*ACCESS EliteConf WR/R
```



---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_over_econet_installing.html](https://elite.bbcelite.com/hacks/elite_over_econet_installing.html)*
