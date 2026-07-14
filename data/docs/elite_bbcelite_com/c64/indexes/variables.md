---
title: List of all variables in the Commodore 64 version of Elite
source_url: https://elite.bbcelite.com/c64/indexes/variables.html
category: source-code
topics:
- sprite programming
- sound generation
- basic
- input handling
- raster interrupts
- assembly
- graphics
difficulty: advanced
language: mixed
hardware:
- BASIC ROM
- VIC-II
- CIA
- SID
- CPU
- KERNAL
related:
- cia-registers
- keyboard-handling
- sound-programming
- music-player
- raster-interrupts
- joystick-reading
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# List of all variables in the Commodore 64 version of Elite

This index contains every variable that appears in the source code for the Commodore 64 version of Elite, grouped by category. A variable is defined as a labelled memory location that is used for storing data, and this list includes both variables that are defined in workspaces, and variables that are declared within the body of the source code.

- [Drawing lines](https://elite.bbcelite.com#drawing-lines)
- [Drawing pixels](https://elite.bbcelite.com#drawing-pixels)
- [Drawing ships](https://elite.bbcelite.com#drawing-ships)
- [Drawing the screen](https://elite.bbcelite.com#drawing-the-screen)
- [Equipment](https://elite.bbcelite.com#equipment)
- [Keyboard](https://elite.bbcelite.com#keyboard)
- [Loader](https://elite.bbcelite.com#loader)
- [Market](https://elite.bbcelite.com#market)
- [Maths (Arithmetic)](https://elite.bbcelite.com#maths-arithmetic)
- [Maths (Geometry)](https://elite.bbcelite.com#maths-geometry)
- [Missions](https://elite.bbcelite.com#missions)
- [Save and load](https://elite.bbcelite.com#save-and-load)
- [Sound](https://elite.bbcelite.com#sound)
- [Sprites](https://elite.bbcelite.com#sprites)
- [Status](https://elite.bbcelite.com#status)
- [Text](https://elite.bbcelite.com#text)
- [Universe](https://elite.bbcelite.com#universe)
- [Utility routines](https://elite.bbcelite.com#utility-routines)
- [Workspace variables](https://elite.bbcelite.com#workspace-variables)

| ## Drawing lines | |
| [LIJT1](https://elite.bbcelite.com/c64/main/variable/lijt1.html) | Addresses for modifying the low byte of the JMP instruction at LI71 to support the unrolled algorithm in part 3 of LOIN | 
| [LIJT2](https://elite.bbcelite.com/c64/main/variable/lijt2.html) | Addresses for modifying the high byte of the JMP instruction at LI71 to support the unrolled algorithm in part 3 of LOIN | 
| [LIJT3](https://elite.bbcelite.com/c64/main/variable/lijt3.html) | Addresses for modifying the low byte of the JMP instruction at LI72 to support the unrolled algorithm in part 3 of LOIN | 
| [LIJT4](https://elite.bbcelite.com/c64/main/variable/lijt4.html) | Addresses for modifying the high byte of the JMP instruction at LI72 to support the unrolled algorithm in part 3 of LOIN | 
| [LIJT5](https://elite.bbcelite.com/c64/main/variable/lijt5.html) | Addresses for modifying the low byte of the JMP instruction at LI91 to support the unrolled algorithm in part 4 of LOIN | 
| [LIJT6](https://elite.bbcelite.com/c64/main/variable/lijt6.html) | Addresses for modifying the high byte of the JMP instruction at LI91 to support the unrolled algorithm in part 4 of LOIN | 
| [LIJT7](https://elite.bbcelite.com/c64/main/variable/lijt7.html) | Addresses for modifying the low byte of the JMP instruction at LI92 to support the unrolled algorithm in part 4 of LOIN | 
| [LIJT8](https://elite.bbcelite.com/c64/main/variable/lijt8.html) | Addresses for modifying the high byte of the JMP instruction at LI92 to support the unrolled algorithm in part 4 of LOIN | 
| [LSX2](https://elite.bbcelite.com/c64/main/variable/lsx2.html) | The ball line heap for storing x-coordinates | 
| [LSY2](https://elite.bbcelite.com/c64/main/variable/lsy2.html) | The ball line heap for storing y-coordinates | 
| [sightcol](https://elite.bbcelite.com/c64/main/variable/sightcol.html) | Colours for the crosshair sights on the different laser types | 
| [TWFL](https://elite.bbcelite.com/c64/main/variable/twfl.html) | Ready-made character rows for the left end of a horizontal line in the space view | 
| [TWFR](https://elite.bbcelite.com/c64/main/variable/twfr.html) | Ready-made character rows for the right end of a horizontal line in the space view | 
| ## Drawing pixels | |
| [celllookh](https://elite.bbcelite.com/c64/main/variable/celllookh.html) | Lookup table for converting a text y-coordinate to the high byte of the address of the start of the character row in screen RAM | 
| [celllookl](https://elite.bbcelite.com/c64/main/variable/celllookl.html) | Lookup table for converting a text y-coordinate to the low byte of the address of the start of the character row | 
| [CTWOS](https://elite.bbcelite.com/c64/main/variable/ctwos.html) | Ready-made double-pixel character row bytes for the dashboard | 
| [CTWOS2](https://elite.bbcelite.com/c64/main/variable/ctwos2.html) | Ready-made single-pixel character row bytes for multicolour bitmap mode | 
| [DTWOS](https://elite.bbcelite.com/c64/main/variable/dtwos.html) | An unused table of ready-made double-pixel character row bytes for the dashboard | 
| [TWOS](https://elite.bbcelite.com/c64/main/variable/twos.html) | Ready-made single-pixel character row bytes for the space view | 
| [TWOS2](https://elite.bbcelite.com/c64/main/variable/twos2.html) | Ready-made double-pixel character row bytes for the space view | 
| [ylookuph](https://elite.bbcelite.com/c64/main/variable/ylookuph.html) | Lookup table for converting a pixel y-coordinate to the high byte of a screen address (within the 256-pixel wide game screen) | 
| [ylookupl](https://elite.bbcelite.com/c64/main/variable/ylookupl.html) | Lookup table for converting a pixel y-coordinate to the low byte of a screen address (within the 256-pixel wide game screen) | 
| ## Drawing ships | |
| [E% (Game data)](https://elite.bbcelite.com/c64/game_data/variable/e_per_cent.html) | Ship blueprints default NEWB flags | 
| [exlook](https://elite.bbcelite.com/c64/main/variable/exlook.html) | A table to shift X left by one place when X is 0 or 1 | 
| [scacol](https://elite.bbcelite.com/c64/main/variable/scacol.html) | Ship colours on the scanner | 
| [SHIP_ADDER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_adder.html) | Ship blueprint for an Adder | 
| [SHIP_ANACONDA (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_anaconda.html) | Ship blueprint for an Anaconda | 
| [SHIP_ASP_MK_2 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_asp_mk_2.html) | Ship blueprint for an Asp Mk II | 
| [SHIP_ASTEROID (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_asteroid.html) | Ship blueprint for an asteroid | 
| [SHIP_BOA (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_boa.html) | Ship blueprint for a Boa | 
| [SHIP_BOULDER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_boulder.html) | Ship blueprint for a boulder | 
| [SHIP_CANISTER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_canister.html) | Ship blueprint for a cargo canister | 
| [SHIP_COBRA_MK_1 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_cobra_mk_1.html) | Ship blueprint for a Cobra Mk I | 
| [SHIP_COBRA_MK_3 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_cobra_mk_3.html) | Ship blueprint for a Cobra Mk III | 
| [SHIP_COBRA_MK_3_P (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_cobra_mk_3_p.html) | Ship blueprint for a Cobra Mk III (pirate) | 
| [SHIP_CONSTRICTOR (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_constrictor.html) | Ship blueprint for a Constrictor | 
| [SHIP_CORIOLIS (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_coriolis.html) | Ship blueprint for a Coriolis space station | 
| [SHIP_COUGAR (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_cougar.html) | Ship blueprint for a Cougar | 
| [SHIP_DODO (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_dodo.html) | Ship blueprint for a Dodecahedron ("Dodo") space station | 
| [SHIP_ESCAPE_POD (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_escape_pod.html) | Ship blueprint for an escape pod | 
| [SHIP_FER_DE_LANCE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_fer_de_lance.html) | Ship blueprint for a Fer-de-Lance | 
| [SHIP_GECKO (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_gecko.html) | Ship blueprint for a Gecko | 
| [SHIP_KRAIT (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_krait.html) | Ship blueprint for a Krait | 
| [SHIP_MAMBA (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_mamba.html) | Ship blueprint for a Mamba | 
| [SHIP_MISSILE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_missile.html) | Ship blueprint for a missile | 
| [SHIP_MORAY (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_moray.html) | Ship blueprint for a Moray | 
| [SHIP_PLATE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_plate.html) | Ship blueprint for an alloy plate | 
| [SHIP_PYTHON (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_python.html) | Ship blueprint for a Python | 
| [SHIP_PYTHON_P (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_python_p.html) | Ship blueprint for a Python (pirate) | 
| [SHIP_ROCK_HERMIT (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_rock_hermit.html) | Ship blueprint for a rock hermit (asteroid) | 
| [SHIP_SHUTTLE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_shuttle.html) | Ship blueprint for a Shuttle | 
| [SHIP_SIDEWINDER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_sidewinder.html) | Ship blueprint for a Sidewinder | 
| [SHIP_SPLINTER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_splinter.html) | Ship blueprint for a splinter | 
| [SHIP_THARGOID (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_thargoid.html) | Ship blueprint for a Thargoid mothership | 
| [SHIP_THARGON (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_thargon.html) | Ship blueprint for a Thargon | 
| [SHIP_TRANSPORTER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_transporter.html) | Ship blueprint for a Transporter | 
| [SHIP_VIPER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_viper.html) | Ship blueprint for a Viper | 
| [SHIP_WORM (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_worm.html) | Ship blueprint for a Worm | 
| [XX21 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/xx21.html) | Ship blueprints lookup table | 
| ## Drawing the screen | |
| [abraxas](https://elite.bbcelite.com/c64/main/variable/abraxas.html) | The value for VIC register $18 to set the screen RAM address for a raster count of 1 in the interrupt routine (i.e. the dashboard) | 
| [caravanserai](https://elite.bbcelite.com/c64/main/variable/caravanserai.html) | Controls whether multicolour or standard bitmap mode is used for the lower part of the screen (i.e. the dashboard) | 
| [cdump (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/cdump.html) | Colour RAM colour data for the dashboard | 
| [DIALS (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/dials.html) | The dashboard bitmap and colour data for screen RAM | 
| [innersec](https://elite.bbcelite.com/c64/main/variable/innersec.html) | A table for converting the value of X from 0 to 1 or from 1 to 0, for use when flipping RASCT between 0 and 1 on each interrupt | 
| [lotus](https://elite.bbcelite.com/c64/main/variable/lotus.html) | The colour of the explosion sprite in the upper and lower parts of the screen | 
| [moonflower](https://elite.bbcelite.com/c64/main/variable/moonflower.html) | Controls the energy bomb effect by switching between multicolour and standard mode | 
| [RASTCT](https://elite.bbcelite.com/c64/main/variable/rastct.html) | The current raster count, which flips between 0 and 1 on each call to the COMIRQ1 interrupt handler (0 = space view, 1 = dashboard) | 
| [santana](https://elite.bbcelite.com/c64/main/variable/santana.html) | Controls whether sprite 1 (the explosion sprite) is drawn in single colour or multicolour mode | 
| [sdump (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/sdump.html) | Screen RAM colour data for the dashboard | 
| [shango](https://elite.bbcelite.com/c64/main/variable/shango.html) | The raster lines that fire the raster interrupt, so it fires at the top of the screen (51) and the top of the dashboard (51 + 143) | 
| [spritp (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/spritp.html) | Sprite definitions | 
| [welcome](https://elite.bbcelite.com/c64/main/variable/welcome.html) | The background colour for the upper and lower parts of the screen, used by the energy bomb to flash the screen's background colour | 
| [zebop](https://elite.bbcelite.com/c64/main/variable/zebop.html) | The value for VIC register $18 to set the screen RAM address for a raster count of 0 in the interrupt routine (i.e. the space view) | 
| ## Equipment | |
| [PRXS](https://elite.bbcelite.com/c64/main/variable/prxs.html) | Equipment prices | 
| ## Keyboard | |
| [KTRAN](https://elite.bbcelite.com/c64/main/variable/ktran.html) | An unused key logger buffer that's left over from the 6502 Second Processor version of Elite | 
| [KYTB](https://elite.bbcelite.com/c64/main/variable/kytb.html) | Lookup table for in-flight keyboard controls | 
| [TGINT](https://elite.bbcelite.com/c64/main/variable/tgint.html) | The keys used to toggle configuration settings when the game is paused | 
| [TRANTABLE](https://elite.bbcelite.com/c64/main/variable/trantable.html) | Translation table from internal key number to ASCII | 
| ## Loader | |
| [basicBootstrap (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/variable/basicbootstrap.html) | Call the RelocateLoader routine even if the firebird file is loaded as a BASIC program | 
| [basicVectors (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/variable/basicvectors.html) | Addresses that override the BASIC vectors for when the loader file is loaded at the address in its PRG header, $02A7 | 
| [date (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/date.html) | A date image that is included into the source disk binaries (this is just random noise in the released game) | 
| [fastLoaderOffered (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/fastloaderoffered.html) | A flag to record whether we have already asked whether to use the fast loader, so we don't ask twice | 
| [fastTrackSector (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/fasttracksector.html) | A track and sector table for use by the fast loader | 
| [filename (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/filename.html) | The GMA filename used to load the game files, buried in a message from GMA, the author of the loader | 
| [FRIN (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/frin.html) | A temporary variable that's used for storing addresses | 
| [loaderScreens (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/loaderscreens.html) | PETSCII codes for clearing the screen and displaying the fast loader prompt and loading screens | 
| [RDLI](https://elite.bbcelite.com/c64/main/variable/rdli.html) | The OS command string for running the flight code in file D.CODE in the disc version of Elite | 
| [trackSector (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/tracksector.html) | Track and sector numbers for all the files on the disk, for use in the fast loader | 
| ## Market | |
| [QQ23](https://elite.bbcelite.com/c64/main/variable/qq23.html) | Market prices table | 
| ## Maths (Arithmetic) | |
| [antilog](https://elite.bbcelite.com/c64/main/variable/antilog.html) | Binary antilogarithm table | 
| [antilogODD](https://elite.bbcelite.com/c64/main/variable/antilogodd.html) | Binary antilogarithm table | 
| [log](https://elite.bbcelite.com/c64/main/variable/log.html) | Binary logarithm table (high byte) | 
| [logL](https://elite.bbcelite.com/c64/main/variable/logl.html) | Binary logarithm table (low byte) | 
| ## Maths (Geometry) | |
| [ACT (Game data)](https://elite.bbcelite.com/c64/game_data/variable/act.html) | Arctan table | 
| [SNE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/sne.html) | Sine/cosine table | 
| ## Missions | |
| [SPMASK](https://elite.bbcelite.com/c64/main/variable/spmask.html) | Masks for updating sprite bits in VIC+$10 for the top bit of the 9-bit x-coordinates of the Trumble sprites | 
| [TRIBDIR](https://elite.bbcelite.com/c64/main/variable/tribdir.html) | The low byte of the four 16-bit directions in which Trumble sprites can move | 
| [TRIBDIRH](https://elite.bbcelite.com/c64/main/variable/tribdirh.html) | The high byte of the four 16-bit directions in which Trumble sprites can move | 
| [TRIBMA](https://elite.bbcelite.com/c64/main/variable/tribma.html) | A table for converting the number of Trumbles in the hold into a sprite-enable flag to use with VIC register $15 | 
| [TRIBTA](https://elite.bbcelite.com/c64/main/variable/tribta.html) | A table for converting the number of Trumbles in the hold into a number of sprites in the range 0 to 6 | 
| ## Save and load | |
| [CHK](https://elite.bbcelite.com/c64/main/variable/chk.html) | First checksum byte for the saved commander data file | 
| [CHK2](https://elite.bbcelite.com/c64/main/variable/chk2.html) | Second checksum byte for the saved commander data file | 
| [CHK3](https://elite.bbcelite.com/c64/main/variable/chk3.html) | Third checksum byte for the saved commander data file | 
| [filesys](https://elite.bbcelite.com/c64/main/variable/filesys.html) | A lookup table containing the device numbers for tape and disk | 
| [NA%](https://elite.bbcelite.com/c64/main/variable/na_per_cent.html) | The data block for the last saved commander | 
| [NA2%](https://elite.bbcelite.com/c64/main/variable/na2_per_cent.html) | The data block for the default commander | 
| [oldlong](https://elite.bbcelite.com/c64/main/variable/oldlong.html) | Contains the length of the last saved commander name | 
| [S1%](https://elite.bbcelite.com/c64/main/variable/s1_per_cent.html) | The drive and directory number used when saving or loading a commander file | 
| [thislong](https://elite.bbcelite.com/c64/main/variable/thislong.html) | Contains the length of the most recently entered commander name | 
| ## Sound | |
| [BDJMPTBH](https://elite.bbcelite.com/c64/main/variable/bdjmptbh.html) | A jump table containing addresses for processing music commands 1 through 15 (high bytes) | 
| [BDJMPTBL](https://elite.bbcelite.com/c64/main/variable/bdjmptbl.html) | A jump table containing addresses for processing music commands 1 through 15 (low bytes) | 
| [COMUDAT](https://elite.bbcelite.com/c64/main/variable/comudat.html) | Music data from the C.COMUDAT file | 
| [SEVENS](https://elite.bbcelite.com/c64/main/variable/sevens.html) | A table for converting the value of Y to 7 * Y | 
| [SFXATK](https://elite.bbcelite.com/c64/main/variable/sfxatk.html) | The attack and decay length (SID+$5) for each sound effect | 
| [SFXCNT](https://elite.bbcelite.com/c64/main/variable/sfxcnt.html) | The counter for each sound effect, which defines the duration of the effect in frames | 
| [SFXCR](https://elite.bbcelite.com/c64/main/variable/sfxcr.html) | The voice control register (SID+$4) for each sound effect | 
| [SFXFQ](https://elite.bbcelite.com/c64/main/variable/sfxfq.html) | The frequency (SID+$5) for each sound effect | 
| [SFXFRCH](https://elite.bbcelite.com/c64/main/variable/sfxfrch.html) | The frequency change to be applied to each sound effect in each frame (as a signed number) | 
| [SFXPR](https://elite.bbcelite.com/c64/main/variable/sfxpr.html) | The priority level for each sound effect | 
| [SFXSUS](https://elite.bbcelite.com/c64/main/variable/sfxsus.html) | The release length and sustain volume (SID+$6) for each sound effect | 
| [SFXVCH](https://elite.bbcelite.com/c64/main/variable/sfxvch.html) | The volume change rate for each sound effect, i.e. how many frames need to pass before the sound effect's volume is reduced by one | 
| ## Sprites | |
| [spritp (Sprites)](https://elite.bbcelite.com/c64/sprites/variable/spritp.html) | Sprite definitions for four laser sights, the explosion sprite and two Trumbles | 
| ## Status | |
| [KWH% (Game data)](https://elite.bbcelite.com/c64/game_data/variable/kwh_per_cent.html) | Integer number of kills awarded for destroying each type of ship | 
| [KWL% (Game data)](https://elite.bbcelite.com/c64/game_data/variable/kwl_per_cent.html) | Fractional number of kills awarded for destroying each type of ship | 
| ## Text | |
| [DTW1](https://elite.bbcelite.com/c64/main/variable/dtw1.html) | A mask for applying the lower case part of Sentence Case to extended text tokens | 
| [DTW2](https://elite.bbcelite.com/c64/main/variable/dtw2.html) | A flag that indicates whether we are currently printing a word | 
| [DTW3](https://elite.bbcelite.com/c64/main/variable/dtw3.html) | A flag for switching between standard and extended text tokens | 
| [DTW4](https://elite.bbcelite.com/c64/main/variable/dtw4.html) | Flags that govern how justified extended text tokens are printed | 
| [DTW5](https://elite.bbcelite.com/c64/main/variable/dtw5.html) | The size of the justified text buffer at BUF | 
| [DTW6](https://elite.bbcelite.com/c64/main/variable/dtw6.html) | A flag to denote whether printing in lower case is enabled for extended text tokens | 
| [DTW8](https://elite.bbcelite.com/c64/main/variable/dtw8.html) | A mask for capitalising the next letter in an extended text token | 
| [JMTB](https://elite.bbcelite.com/c64/main/variable/jmtb.html) | The extended token table for jump tokens 1-32 (DETOK) | 
| [MTIN](https://elite.bbcelite.com/c64/main/variable/mtin.html) | Lookup table for random tokens in the extended token table (0-37) | 
| [QQ16](https://elite.bbcelite.com/c64/main/variable/qq16.html) | The two-letter token lookup table | 
| [QQ18 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/qq18.html) | The recursive token table for tokens 0-148 | 
| [RLINE](https://elite.bbcelite.com/c64/main/variable/rline.html) | The OSWORD configuration block used to fetch a line of text from the keyboard | 
| [RUGAL (Game data)](https://elite.bbcelite.com/c64/game_data/variable/rugal.html) | The criteria for systems with extended description overrides | 
| [RUPLA (Game data)](https://elite.bbcelite.com/c64/game_data/variable/rupla.html) | System numbers that have extended description overrides | 
| [RUTOK (Game data)](https://elite.bbcelite.com/c64/game_data/variable/rutok.html) | The second extended token table for recursive tokens 0-26 (DETOK3) | 
| [TENS](https://elite.bbcelite.com/c64/main/variable/tens.html) | A constant used when printing large numbers in BPRNT | 
| [TKN1 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/tkn1.html) | The first extended token table for recursive tokens 0-255 (DETOK) | 
| [TKN2](https://elite.bbcelite.com/c64/main/variable/tkn2.html) | The extended two-letter token lookup table | 
| ## Universe | |
| [spasto](https://elite.bbcelite.com/c64/main/variable/spasto.html) | Contains the address of the Coriolis space station's ship blueprint | 
| [UNIV](https://elite.bbcelite.com/c64/main/variable/univ.html) | Table of pointers to the local universe's ship data blocks | 
| ## Utility routines | |
| [brkd](https://elite.bbcelite.com/c64/main/variable/brkd.html) | A flag that indicates whether a system error has occurred | 
| [F%](https://elite.bbcelite.com/c64/main/variable/f_per_cent.html) | Denotes the end of the main game code, from ELITE A to ELITE K | 
| [G%](https://elite.bbcelite.com/c64/main/variable/g_per_cent.html) | Denotes the start of the main game code, from ELITE A to ELITE K | 
| [L1M](https://elite.bbcelite.com/c64/main/variable/l1m.html) | Temporary storage for the new value of the 6510 input/output port register | 
| [R%](https://elite.bbcelite.com/c64/main/variable/r_per_cent.html) | Denotes the end of the first part of the main game code (CODE1), from ELITE A to ELITE C | 
| [V% (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/v_per_cent.html) | Denotes the end of the second block of loader code, as used in the encryption/decryption process | 
| [W% (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/w_per_cent.html) | Denotes the start of the first block of loader code, as used in the encryption/decryption process | 
| [X% (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/x_per_cent.html) | Denotes the end of the first block of loader code, as used in the encryption/decryption process | 
| ## Workspace variables | |
| [ALP1](https://elite.bbcelite.com/c64/main/workspace/zp.html#alp1) | Magnitude of the roll angle alpha, i.e. |alpha|, which is a positive value between 0 and 31 | 
| [ALP2](https://elite.bbcelite.com/c64/main/workspace/zp.html#alp2) | Bit 7 of ALP2 = sign of the roll angle in ALPHA | 
| [ALPHA](https://elite.bbcelite.com/c64/main/workspace/zp.html#alpha) | The current roll angle alpha, which is reduced from JSTX to a sign-magnitude value between -31 and +31 | 
| [ALTIT](https://elite.bbcelite.com/c64/main/workspace/wp.html#altit) | Our altitude above the surface of the planet or sun | 
| [ASH](https://elite.bbcelite.com/c64/main/workspace/up.html#ash) | Aft shield status | 
| [auto](https://elite.bbcelite.com/c64/main/workspace/up.html#auto) | Docking computer activation status | 
| [AVL](https://elite.bbcelite.com/c64/main/workspace/up.html#avl) | Market availability in the current system | 
| [BALI](https://elite.bbcelite.com/c64/main/workspace/wp.html#bali) | This byte appears to be unused | 
| [BDBUFF](https://elite.bbcelite.com/c64/main/workspace/zp.html#bdbuff) | The music data byte that is currently being processed, with the low nibble being processed first, and then the high nibble | 
| [BDdataptr1](https://elite.bbcelite.com/c64/main/workspace/zp.html#bddataptr1) | The low byte of the address of the music data pointer in BDdataptr1(1 0), which points to the end of the music data currently being processed | 
| [BDdataptr2](https://elite.bbcelite.com/c64/main/workspace/zp.html#bddataptr2) | The high byte of the address of the music data pointer in BDdataptr1(1 0), which points to the end of the music data currently being processed | 
| [BDdataptr3](https://elite.bbcelite.com/c64/main/workspace/zp.html#bddataptr3) | The low byte of the address of the music data pointer in BDdataptr3(1 0), which is a backup of the initial value of the BDdataptr1(1 0) pointer, so music can be repeated | 
| [BDdataptr4](https://elite.bbcelite.com/c64/main/workspace/zp.html#bddataptr4) | The high byte of the address of the music data pointer in BDdataptr3(1 0), which is a backup of the initial value of the BDdataptr1(1 0) pointer, so music can be repeated | 
| [BET1](https://elite.bbcelite.com/c64/main/workspace/zp.html#bet1) | The magnitude of the pitch angle beta, i.e. |beta|, which is a positive value between 0 and 8 | 
| [BET2](https://elite.bbcelite.com/c64/main/workspace/zp.html#bet2) | Bit 7 of BET2 = sign of the pitch angle in BETA | 
| [BETA](https://elite.bbcelite.com/c64/main/workspace/zp.html#beta) | The current pitch angle beta, which is reduced from JSTY to a sign-magnitude value between -8 and +8 | 
| [BOMB](https://elite.bbcelite.com/c64/main/workspace/up.html#bomb) | Energy bomb | 
| [boxsize](https://elite.bbcelite.com/c64/main/workspace/wp.html#boxsize) | This byte appears to be unused | 
| [BST](https://elite.bbcelite.com/c64/main/workspace/up.html#bst) | Fuel scoops (BST stands for "barrel status") | 
| [BUF](https://elite.bbcelite.com/c64/main/workspace/wp.html#buf) | The line buffer used by DASC to print justified text | 
| [CABTMP](https://elite.bbcelite.com/c64/main/workspace/up.html#cabtmp) | Cabin temperature | 
| [CASH](https://elite.bbcelite.com/c64/main/workspace/up.html#cash) | Our current cash pot | 
| [CNT](https://elite.bbcelite.com/c64/main/workspace/zp.html#cnt) | Temporary storage, typically used for storing the number of iterations required when looping | 
| [CNT2](https://elite.bbcelite.com/c64/main/workspace/zp.html#cnt2) | Temporary storage, used in the planet-drawing routine to store the segment number where the arc of a partial circle should start | 
| [COK](https://elite.bbcelite.com/c64/main/workspace/up.html#cok) | Flags used to generate the competition code | 
| [COL](https://elite.bbcelite.com/c64/main/workspace/zp.html#col) | Temporary storage, used to store colour information when drawing pixels in the dashboard | 
| [COL2](https://elite.bbcelite.com/c64/main/workspace/up.html#col2) | The text colour of the next character to draw in CHPR | 
| [COMC](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#comc) | The colour of the dot on the compass | 
| [COMX](https://elite.bbcelite.com/c64/main/workspace/up.html#comx) | The x-coordinate of the compass dot | 
| [COMY](https://elite.bbcelite.com/c64/main/workspace/up.html#comy) | The y-coordinate of the compass dot | 
| [counter](https://elite.bbcelite.com/c64/main/workspace/zp.html#counter) | The rest counter when playing music, for implementing music commands #8 and #15 | 
| [CRGO](https://elite.bbcelite.com/c64/main/workspace/up.html#crgo) | Our ship's cargo capacity | 
| [DAMP](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#damp) | Keyboard damping configuration setting | 
| [de](https://elite.bbcelite.com/c64/main/workspace/up.html#de) | Equipment destruction flag | 
| [DELT4](https://elite.bbcelite.com/c64/main/workspace/zp.html#delt4) | Our current speed * 64 as a 16-bit value | 
| [DELTA](https://elite.bbcelite.com/c64/main/workspace/zp.html#delta) | Our current speed, in the range 1-40 | 
| [DFLAG](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#dflag) | A flag that indicates whether the dashboard is currently being shown on-screen | 
| [DISK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#disk) | Current media configuration setting | 
| [distaway](https://elite.bbcelite.com/c64/main/workspace/wp.html#distaway) | Used to store the nearest distance of the rotating ship on the title screen | 
| [DJD](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#djd) | Keyboard auto-recentre configuration setting | 
| [DKCMP](https://elite.bbcelite.com/c64/main/workspace/up.html#dkcmp) | Docking computer | 
| [DL](https://elite.bbcelite.com/c64/main/workspace/zp.html#dl) | This byte is unused in this version of Elite (it is used to store the vertical sync flag in the BBC Micro versions) | 
| [DLY](https://elite.bbcelite.com/c64/main/workspace/up.html#dly) | In-flight message delay | 
| [DNOIZ](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#dnoiz) | Sound on/off configuration setting | 
| [dontclip](https://elite.bbcelite.com/c64/main/workspace/zp.html#dontclip) | A flag that controls whether the LL145 routine clips lines to the dimensions of the space view (which we want to disable in the Short-range Chart, as there is no dashboard and the chart needs to use the whole screen) | 
| [ECM](https://elite.bbcelite.com/c64/main/workspace/up.html#ecm) | E.C.M. system | 
| [ECMA](https://elite.bbcelite.com/c64/main/workspace/zp.html#ecma) | The E.C.M. countdown timer, which determines whether an E.C.M. system is currently operating | 
| [ECMP](https://elite.bbcelite.com/c64/main/workspace/up.html#ecmp) | Our E.C.M. status | 
| [ENERGY](https://elite.bbcelite.com/c64/main/workspace/up.html#energy) | Energy bank status | 
| [ENGY](https://elite.bbcelite.com/c64/main/workspace/up.html#engy) | Energy unit | 
| [ESCP](https://elite.bbcelite.com/c64/main/workspace/up.html#escp) | Escape pod | 
| [EV](https://elite.bbcelite.com/c64/main/workspace/up.html#ev) | The "extra vessels" spawning counter | 
| [FIST](https://elite.bbcelite.com/c64/main/workspace/up.html#fist) | Our legal status (FIST stands for "fugitive/innocent status") | 
| [FLAG](https://elite.bbcelite.com/c64/main/workspace/zp.html#flag) | A flag that's used to define whether this is the first call to the ball line routine in BLINE, so it knows whether to wait for the second call before storing segment data in the ball line heap | 
| [FLH](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#flh) | Flashing console bars configuration setting | 
| [FRIN](https://elite.bbcelite.com/c64/main/workspace/up.html#frin) | Slots for the ships in the local bubble of universe | 
| [frump](https://elite.bbcelite.com/c64/main/workspace/up.html#frump) | Used to store the number of particles in the explosion cloud | 
| [FSH](https://elite.bbcelite.com/c64/main/workspace/up.html#fsh) | Forward shield status | 
| [GCNT](https://elite.bbcelite.com/c64/main/workspace/up.html#gcnt) | The number of the current galaxy (0-7) | 
| [GHYP](https://elite.bbcelite.com/c64/main/workspace/up.html#ghyp) | Galactic hyperdrive | 
| [GNTMP](https://elite.bbcelite.com/c64/main/workspace/up.html#gntmp) | Laser temperature (or "gun temperature") | 
| [gov](https://elite.bbcelite.com/c64/main/workspace/up.html#gov) | The current system's government type (0-7) | 
| [HFX](https://elite.bbcelite.com/c64/main/workspace/up.html#hfx) | This flag is unused in this version of Elite. In the other versions, setting HFX to a non-zero value makes the hyperspace rings multi-coloured, but that effect is not used in this version | 
| [INF](https://elite.bbcelite.com/c64/main/workspace/zp.html#inf) | Temporary storage, typically used for storing the address of a ship's data block, so it can be copied to and from the internal workspace at INWK | 
| [INWK](https://elite.bbcelite.com/c64/main/workspace/zp.html#inwk) | The zero-page internal workspace for the current ship data block | 
| [JSTE](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#jste) | Reverse both joystick channels configuration setting | 
| [JSTGY](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#jstgy) | Reverse joystick Y-channel configuration setting | 
| [JSTK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#jstk) | Keyboard or joystick configuration setting | 
| [JSTX](https://elite.bbcelite.com/c64/main/workspace/up.html#jstx) | Our current roll rate | 
| [JSTY](https://elite.bbcelite.com/c64/main/workspace/up.html#jsty) | Our current pitch rate | 
| [JUNK](https://elite.bbcelite.com/c64/main/workspace/up.html#junk) | The amount of junk in the local bubble | 
| [K](https://elite.bbcelite.com/c64/main/workspace/zp.html#k) | Temporary storage, used in a number of places | 
| [K2](https://elite.bbcelite.com/c64/main/workspace/zp.html#k2) | Temporary storage, used in a number of places | 
| [K3](https://elite.bbcelite.com/c64/main/workspace/zp.html#k3) | Temporary storage, used in a number of places | 
| [K4](https://elite.bbcelite.com/c64/main/workspace/zp.html#k4) | Temporary storage, used in a number of places | 
| [K5](https://elite.bbcelite.com/c64/main/workspace/zp.html#k5) | Temporary storage used to store segment coordinates across successive calls to BLINE, the ball line routine | 
| [K6](https://elite.bbcelite.com/c64/main/workspace/zp.html#k6) | Temporary storage, typically used for storing coordinates during vector calculations | 
| [KL](https://elite.bbcelite.com/c64/main/workspace/up.html#kl) | If a key is being pressed that is not in the keyboard table at KYTB, it can be stored here (as seen in routine DK4, for example) | 
| [KLO](https://elite.bbcelite.com/c64/main/workspace/keylook.html#klo) | The key logger in the BBC Micro version has a spare byte at the start for storing the last key press, so we also include a spare byte here so the KLO logger in the Commodore 64 version behaves in a similar way to the KL key logger in the BBC Micro | 
| [KY1](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky1) | "?" is being pressed (slow down, KLO+$9) | 
| [KY12](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky12) | "C=" is being pressed (energy bomb, KLO+$3) | 
| [KY13](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky13) | Left arrow is being pressed (launch escape pod, KLO+$7) | 
| [KY14](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky14) | "T" is being pressed (target missile, KLO+$2A) | 
| [KY15](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky15) | "U" is being pressed (unarm missile, KLO+$22) | 
| [KY16](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky16) | "M" is being pressed (fire missile, KLO+$1C) | 
| [KY17](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky17) | "E" is being pressed (activate E.C.M., KLO+$32) | 
| [KY18](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky18) | "J" is being pressed (in-system jump, KLO+$1E) | 
| [KY19](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky19) | "C" is being pressed (activate docking computer, KLO+$2C) | 
| [KY2](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky2) | Space is being pressed (speed up, KLO+$4) | 
| [KY20](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky20) | "P" is being pressed (deactivate docking computer, KLO+$17) | 
| [KY3](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky3) | "<" is being pressed (roll left, KYO+$11) | 
| [KY4](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky4) | ">" is being pressed (roll right, KLO+$14) | 
| [KY5](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky5) | "X" is being pressed (pull up, KLO+$29) | 
| [KY6](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky6) | "S" is being pressed (pitch down, KLO+$33) | 
| [KY7](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky7) | "A" is being pressed (fire lasers, KLO+$36) | 
| [LAS](https://elite.bbcelite.com/c64/main/workspace/zp.html#las) | Contains the laser power of the laser fitted to the current space view (or 0 if there is no laser fitted to the current view) | 
| [LAS2](https://elite.bbcelite.com/c64/main/workspace/up.html#las2) | Laser power for the current laser | 
| [LASCT](https://elite.bbcelite.com/c64/main/workspace/up.html#lasct) | The laser pulse count for the current laser | 
| [LASER](https://elite.bbcelite.com/c64/main/workspace/up.html#laser) | The specifications of the lasers fitted to each of the four space views | 
| [LASX](https://elite.bbcelite.com/c64/main/workspace/wp.html#lasx) | The x-coordinate of the tip of the laser line | 
| [LASY](https://elite.bbcelite.com/c64/main/workspace/wp.html#lasy) | The y-coordinate of the tip of the laser line | 
| [LSO](https://elite.bbcelite.com/c64/main/workspace/wp.html#lso) | The ship line heap for the space station (see NWSPS) and the sun line heap (see SUN) | 
| [LSP](https://elite.bbcelite.com/c64/main/workspace/zp.html#lsp) | The ball line heap pointer, which contains the number of the first free byte after the end of the LSX2 and LSY2 heaps | 
| [LSX](https://elite.bbcelite.com/c64/main/workspace/wp.html#lsx) | LSX is an alias that points to the first byte of the sun line heap at LSO | 
| [MANY](https://elite.bbcelite.com/c64/main/workspace/up.html#many) | The number of ships of each type in the local bubble of universe | 
| [MCH](https://elite.bbcelite.com/c64/main/workspace/up.html#mch) | The text token number of the in-flight message that is currently being shown, and which will be removed by the me2 routine when the counter in DLY reaches zero | 
| [MCNT](https://elite.bbcelite.com/c64/main/workspace/zp.html#mcnt) | The main loop counter | 
| [messXC](https://elite.bbcelite.com/c64/main/workspace/zp.html#messxc) | Temporary storage, used to store the text column of the in-flight message in MESS, so it can be erased from the screen at the correct time | 
| [MJ](https://elite.bbcelite.com/c64/main/workspace/up.html#mj) | Are we in witchspace (i.e. have we mis-jumped)? | 
| [MOS](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mos) | This variable appears to be unused | 
| [MSAR](https://elite.bbcelite.com/c64/main/workspace/up.html#msar) | The targeting state of our leftmost missile | 
| [MSTG](https://elite.bbcelite.com/c64/main/workspace/zp.html#mstg) | The current missile lock target | 
| [MUDOCK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mudock) | Docking music tune configuration setting | 
| [MUFOR](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mufor) | Configuration setting that controls whether the docking music can be enabled or disabled | 
| [MULIE](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mulie) | A flag to record whether the RESET routine is being being called from within the TITLE routine, when the title screen is being displayed, as we don't want to stop the title music from playing when this is the case | 
| [MUPLA](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mupla) | A flag to record whether any music is currently playing | 
| [MUSILLY](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#musilly) | Sounds during music configuration setting | 
| [MUTOK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mutok) | Docking music configuration setting | 
| [MUTOKOLD](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mutokold) | Used to store the previous value of MUTOK, so we can track whether the docking music configuration changes | 
| [NAME](https://elite.bbcelite.com/c64/main/workspace/up.html#name) | The current commander name | 
| [NEWB](https://elite.bbcelite.com/c64/main/workspace/zp.html#newb) | The ship's "new byte flags" (or NEWB flags) | 
| [newzp](https://elite.bbcelite.com/c64/main/workspace/zp.html#newzp) | This is used by the STARS2 routine for storing the stardust particle's delta_x value | 
| [NOMSL](https://elite.bbcelite.com/c64/main/workspace/up.html#nomsl) | The number of missiles we have fitted (0-4) | 
| [NOSTM](https://elite.bbcelite.com/c64/main/workspace/up.html#nostm) | The number of stardust particles shown on screen, which is 12 (#NOST) for normal space, and 3 for witchspace | 
| [P](https://elite.bbcelite.com/c64/main/workspace/zp.html#p) | Temporary storage, used in a number of places | 
| [P2](https://elite.bbcelite.com/c64/main/workspace/zp.html#p2) | Temporary storage, used in place of variable P in the line-drawing routines | 
| [PATG](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#patg) | Configuration setting to show the author names on the start-up screen and enable manual hyperspace mis-jumps | 
| [PLTOG](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#pltog) | Planetary details configuration setting | 
| [PULSEW](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#pulsew) | The current pulse width for sound effects | 
| [Q](https://elite.bbcelite.com/c64/main/workspace/zp.html#q) | Temporary storage, used in a number of places | 
| [Q2](https://elite.bbcelite.com/c64/main/workspace/zp.html#q2) | Temporary storage, used in place of variable Q in the line-drawing routines | 
| [QQ0](https://elite.bbcelite.com/c64/main/workspace/up.html#qq0) | The current system's galactic x-coordinate (0-256) | 
| [QQ1](https://elite.bbcelite.com/c64/main/workspace/up.html#qq1) | The current system's galactic y-coordinate (0-256) | 
| [QQ10](https://elite.bbcelite.com/c64/main/workspace/up.html#qq10) | The galactic y-coordinate of the crosshairs in the galaxy chart (and, most of the time, the selected system's galactic y-coordinate) | 
| [QQ11](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq11) | The type of the current view: | 
| [QQ12](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq12) | Our "docked" status | 
| [QQ14](https://elite.bbcelite.com/c64/main/workspace/up.html#qq14) | Our current fuel level (0-70) | 
| [QQ15](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq15) | The three 16-bit seeds for the selected system, i.e. the one in the crosshairs in the Short-range Chart | 
| [QQ17](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq17) | Contains a number of flags that affect how text tokens are printed, particularly capitalisation | 
| [QQ19](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq19) | Temporary storage, used in a number of places | 
| [QQ2](https://elite.bbcelite.com/c64/main/workspace/up.html#qq2) | The three 16-bit seeds for the current system, i.e. the one we are currently in | 
| [QQ20](https://elite.bbcelite.com/c64/main/workspace/up.html#qq20) | The contents of our cargo hold | 
| [QQ21](https://elite.bbcelite.com/c64/main/workspace/up.html#qq21) | The three 16-bit seeds for the current galaxy | 
| [QQ22](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq22) | The two hyperspace countdown counters | 
| [QQ24](https://elite.bbcelite.com/c64/main/workspace/up.html#qq24) | Temporary storage, used to store the current market item's price in routine TT151 | 
| [QQ25](https://elite.bbcelite.com/c64/main/workspace/up.html#qq25) | Temporary storage, used to store the current market item's availability in routine TT151 | 
| [QQ26](https://elite.bbcelite.com/c64/main/workspace/up.html#qq26) | A random value used to randomise market data | 
| [QQ28](https://elite.bbcelite.com/c64/main/workspace/up.html#qq28) | The current system's economy (0-7) | 
| [QQ29](https://elite.bbcelite.com/c64/main/workspace/up.html#qq29) | Temporary storage, used in a number of places | 
| [QQ3](https://elite.bbcelite.com/c64/main/workspace/up.html#qq3) | The selected system's economy (0-7) | 
| [QQ4](https://elite.bbcelite.com/c64/main/workspace/up.html#qq4) | The selected system's government (0-7) | 
| [QQ5](https://elite.bbcelite.com/c64/main/workspace/up.html#qq5) | The selected system's tech level (0-14) | 
| [QQ6](https://elite.bbcelite.com/c64/main/workspace/up.html#qq6) | The selected system's population in billions * 10 (1-71), so the maximum population is 7.1 billion | 
| [QQ7](https://elite.bbcelite.com/c64/main/workspace/up.html#qq7) | The selected system's productivity in M CR (96-62480) | 
| [QQ8](https://elite.bbcelite.com/c64/main/workspace/up.html#qq8) | The distance from the current system to the selected system in light years * 10, stored as a 16-bit number | 
| [QQ9](https://elite.bbcelite.com/c64/main/workspace/up.html#qq9) | The galactic x-coordinate of the crosshairs in the galaxy chart (and, most of the time, the selected system's galactic x-coordinate) | 
| [R](https://elite.bbcelite.com/c64/main/workspace/zp.html#r) | Temporary storage, used in a number of places | 
| [R2](https://elite.bbcelite.com/c64/main/workspace/zp.html#r2) | Temporary storage, used in place of variable R in the line-drawing routines | 
| [RAND](https://elite.bbcelite.com/c64/main/workspace/zp.html#rand) | Four 8-bit seeds for the random number generation system implemented in the DORND routine | 
| [RAT](https://elite.bbcelite.com/c64/main/workspace/zp.html#rat) | Used to store different signs depending on the current space view, for use in calculating stardust movement | 
| [RAT2](https://elite.bbcelite.com/c64/main/workspace/zp.html#rat2) | Temporary storage, used to store the pitch and roll signs when moving objects and stardust | 
| [S](https://elite.bbcelite.com/c64/main/workspace/zp.html#s) | Temporary storage, used in a number of places | 
| [S2](https://elite.bbcelite.com/c64/main/workspace/zp.html#s2) | Temporary storage, used in place of variable S in the line-drawing routines | 
| [safehouse](https://elite.bbcelite.com/c64/main/workspace/up.html#safehouse) | Backup storage for the seeds for the selected system | 
| [SC](https://elite.bbcelite.com/c64/main/workspace/zp.html#sc) | Screen address (low byte) | 
| [SCH](https://elite.bbcelite.com/c64/main/workspace/zp.html#sch) | Screen address (high byte) | 
| [SLSP](https://elite.bbcelite.com/c64/main/workspace/up.html#slsp) | The address of the bottom of the ship line heap | 
| [SOATK](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#soatk) | Sound buffer for attack and decay lengths | 
| [SOCNT](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#socnt) | Sound buffer for sound effect counters | 
| [SOCR](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#socr) | Sound buffer for voice control register values | 
| [SOFLG](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#soflg) | Sound buffer for sound effect flags | 
| [SOFRCH](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sofrch) | Sound buffer for frequency change values | 
| [SOFRQ](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sofrq) | Sound buffer for sound effect frequencies | 
| [SOPR](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sopr) | Sound buffer for sound effect priorities | 
| [SOSUS](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sosus) | Sound buffer for release length and sustain volume | 
| [SOVCH](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sovch) | Sound buffer for the volume change rate | 
| [sprx](https://elite.bbcelite.com/c64/main/workspace/up.html#sprx) | Contains the x-coordinate offset for the explosion sprite, i.e. the relative position of the sprite compared to the centre of the explosion, which needs to be set according to the size of the sprite | 
| [spry](https://elite.bbcelite.com/c64/main/workspace/up.html#spry) | Contains the y-coordinate offset for the explosion sprite, i.e. the relative position of the sprite compared to the centre of the explosion, which needs to be set according to the size of the sprite | 
| [SSPR](https://elite.bbcelite.com/c64/main/workspace/up.html#sspr) | "Space station present" flag | 
| [STP](https://elite.bbcelite.com/c64/main/workspace/zp.html#stp) | The step size for drawing circles | 
| [SUNX](https://elite.bbcelite.com/c64/main/workspace/zp.html#sunx) | The 16-bit x-coordinate of the vertical centre axis of the sun (which might be off-screen) | 
| [SVC](https://elite.bbcelite.com/c64/main/workspace/up.html#svc) | The save count | 
| [SWAP](https://elite.bbcelite.com/c64/main/workspace/wp.html#swap) | Temporary storage, used to store a flag that records whether or not we had to swap a line's start and end coordinates around when clipping the line in routine LL145 (the flag is used in places like BLINE to swap them back) | 
| [SX](https://elite.bbcelite.com/c64/main/workspace/wp.html#sx) | This is where we store the x_hi coordinates for all the stardust particles | 
| [SXL](https://elite.bbcelite.com/c64/main/workspace/wp.html#sxl) | This is where we store the x_lo coordinates for all the stardust particles | 
| [SY](https://elite.bbcelite.com/c64/main/workspace/wp.html#sy) | This is where we store the y_hi coordinates for all the stardust particles | 
| [SYL](https://elite.bbcelite.com/c64/main/workspace/wp.html#syl) | This is where we store the y_lo coordinates for all the stardust particles | 
| [SZ](https://elite.bbcelite.com/c64/main/workspace/wp.html#sz) | This is where we store the z_hi coordinates for all the stardust particles | 
| [SZL](https://elite.bbcelite.com/c64/main/workspace/wp.html#szl) | This is where we store the z_lo coordinates for all the stardust particles | 
| [T](https://elite.bbcelite.com/c64/main/workspace/zp.html#t) | Temporary storage, used in a number of places | 
| [T1](https://elite.bbcelite.com/c64/main/workspace/zp.html#t1) | Temporary storage, used in a number of places | 
| [T2](https://elite.bbcelite.com/c64/main/workspace/zp.html#t2) | Temporary storage, used in place of variable T in the line-drawing routines | 
| [TALLY](https://elite.bbcelite.com/c64/main/workspace/up.html#tally) | Our combat rank | 
| [TALLYL](https://elite.bbcelite.com/c64/main/workspace/up.html#tallyl) | Combat rank fraction | 
| [tek](https://elite.bbcelite.com/c64/main/workspace/up.html#tek) | The current system's tech level (0-14) | 
| [TGT](https://elite.bbcelite.com/c64/main/workspace/zp.html#tgt) | Temporary storage, typically used as a target value for counters when drawing explosion clouds and partial circles | 
| [thiskey](https://elite.bbcelite.com/c64/main/workspace/zp.html#thiskey) | If a key is being pressed that is not in the keyboard table at KYTB, it can be stored in KL and thiskey (as seen in routine DK4, for example) | 
| [TP](https://elite.bbcelite.com/c64/main/workspace/up.html#tp) | The current mission status | 
| [TRIBBLE](https://elite.bbcelite.com/c64/main/workspace/up.html#tribble) | The number of Trumbles in the cargo hold | 
| [TRIBCT](https://elite.bbcelite.com/c64/main/workspace/up.html#tribct) | Contains the number of Trumble sprites that we are showing on-screen, in the range 0 to 6 | 
| [TRIBVX](https://elite.bbcelite.com/c64/main/workspace/up.html#tribvx) | Contains the low byte of the 16-bit x-axis velocity of each of the Trumbles | 
| [TRIBVXH](https://elite.bbcelite.com/c64/main/workspace/up.html#tribvxh) | Contains the high byte of the 16-bit x-axis velocity of each of the Trumbles | 
| [TRIBXH](https://elite.bbcelite.com/c64/main/workspace/up.html#tribxh) | Contains bit 8 of the x-coordinate for each of the Trumble sprites (as x-coordinates are 9-bit values) | 
| [TYPE](https://elite.bbcelite.com/c64/main/workspace/zp.html#type) | The current ship type | 
| [U](https://elite.bbcelite.com/c64/main/workspace/zp.html#u) | Temporary storage, used in a number of places | 
| [UPO](https://elite.bbcelite.com/c64/main/workspace/wp.html#upo) | This byte appears to be unused | 
| [V](https://elite.bbcelite.com/c64/main/workspace/zp.html#v) | Temporary storage, typically used for storing an address pointer | 
| [value0](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value0) | An unused counter that increments every time we process music command <#6> | 
| [value1](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value1) | Stores the voice control register for voice 1 | 
| [value2](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value2) | Stores the voice control register for voice 2 | 
| [value3](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value3) | Stores the voice control register for voice 3 | 
| [value4](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value4) | Stores the rest length for commands #8 and #15 | 
| [value5](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value5) | The address before the start of the music data for the tune that is configured to play for docking, so this can be changed to alter the docking music | 
| [vibrato2](https://elite.bbcelite.com/c64/main/workspace/zp.html#vibrato2) | The vibrato counter for voice 2 | 
| [vibrato3](https://elite.bbcelite.com/c64/main/workspace/zp.html#vibrato3) | The vibrato counter for voice 3 | 
| [VIEW](https://elite.bbcelite.com/c64/main/workspace/up.html#view) | The number of the current space view | 
| [voice2hi1](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice2hi1) | The low byte of the first vibrato frequency for voice 2, which contains the lower frequency | 
| [voice2hi2](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice2hi2) | The low byte of the second vibrato frequency for voice 2, which contains the higher frequency | 
| [voice2lo1](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice2lo1) | The high byte of the first vibrato frequency for voice 2, which contains the lower frequency | 
| [voice2lo2](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice2lo2) | The high byte of the second vibrato frequency for voice 2, which contains the higher frequency | 
| [voice3hi1](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice3hi1) | The low byte of the first vibrato frequency for voice 3, which contains the lower frequency | 
| [voice3hi2](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice3hi2) | The low byte of the second vibrato frequency for voice 3, which contains the higher frequency | 
| [voice3lo1](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice3lo1) | The high byte of the first vibrato frequency for voice 3, which contains the lower frequency | 
| [voice3lo2](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice3lo2) | The high byte of the second vibrato frequency for voice 3, which contains the higher frequency | 
| [widget](https://elite.bbcelite.com/c64/main/workspace/zp.html#widget) | Temporary storage, used to store the original argument in A in the logarithmic FMLTU and LL28 routines | 
| [X1](https://elite.bbcelite.com/c64/main/workspace/zp.html#x1) | Temporary storage, typically used for x-coordinates in the line-drawing routines | 
| [X2](https://elite.bbcelite.com/c64/main/workspace/zp.html#x2) | Temporary storage, typically used for x-coordinates in the line-drawing routines | 
| [XC](https://elite.bbcelite.com/c64/main/workspace/zp.html#xc) | The x-coordinate of the text cursor (i.e. the text column), which can be from 0 to 32 | 
| [XP](https://elite.bbcelite.com/c64/main/workspace/wp.html#xp) | This byte appears to be unused | 
| [XSAV](https://elite.bbcelite.com/c64/main/workspace/zp.html#xsav) | Temporary storage for saving the value of the X register, used in a number of places | 
| [XSAV2](https://elite.bbcelite.com/c64/main/workspace/up.html#xsav2) | Temporary storage, used for storing the value of the X register in the CHPR routine | 
| [XX](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx) | Temporary storage, typically used for storing a 16-bit x-coordinate | 
| [XX0](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx0) | Temporary storage, used to store the address of a ship blueprint. For example, it is used when we add a new ship to the local bubble in routine NWSHP, and it contains the address of the current ship's blueprint as we loop through all the nearby ships in the main flight loop | 
| [XX1](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx1) | This is an alias for INWK that is used in the main ship-drawing routine at LL9 | 
| [XX12](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx12) | Temporary storage for a block of values, used in a number of places | 
| [XX13](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx13) | Temporary storage, typically used in the line-drawing routines | 
| [XX14](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx14) | This byte appears to be unused | 
| [XX15](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx15) | Temporary storage, typically used for storing screen coordinates in line-drawing routines | 
| [XX16](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx16) | Temporary storage for a block of values, used in a number of places | 
| [XX17](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx17) | Temporary storage, used in BPRNT to store the number of characters to print, and as the edge counter in the main ship-drawing routine | 
| [XX18](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx18) | Temporary storage used to store coordinates in the LL9 ship-drawing routine | 
| [XX19](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx19) | XX19(1 0) shares its location with INWK(34 33), which contains the address of the ship line heap | 
| [XX2](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx2) | Temporary storage, used to store the visibility of the ship's faces during the ship-drawing routine at LL9 | 
| [XX20](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx20) | Temporary storage, used in a number of places | 
| [XX24](https://elite.bbcelite.com/c64/main/workspace/wp.html#xx24) | This byte appears to be unused | 
| [XX4](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx4) | Temporary storage, used in a number of places | 
| [Y1](https://elite.bbcelite.com/c64/main/workspace/zp.html#y1) | Temporary storage, typically used for y-coordinates in line-drawing routines | 
| [Y2](https://elite.bbcelite.com/c64/main/workspace/zp.html#y2) | Temporary storage, typically used for y-coordinates in line-drawing routines | 
| [YC](https://elite.bbcelite.com/c64/main/workspace/zp.html#yc) | The y-coordinate of the text cursor (i.e. the text row), which can be from 0 to 23 | 
| [YP](https://elite.bbcelite.com/c64/main/workspace/wp.html#yp) | This byte appears to be unused | 
| [YS](https://elite.bbcelite.com/c64/main/workspace/wp.html#ys) | This byte appears to be unused | 
| [YSAV](https://elite.bbcelite.com/c64/main/workspace/zp.html#ysav) | Temporary storage for saving the value of the Y register, used in a number of places | 
| [YSAV2](https://elite.bbcelite.com/c64/main/workspace/up.html#ysav2) | Temporary storage, used for storing the value of the Y register in the CHPR routine | 
| [Yx2M1](https://elite.bbcelite.com/c64/main/workspace/zp.html#yx2m1) | This is used to store the number of pixel rows in the space view minus 1, which is also the y-coordinate of the bottom pixel row of the space view (it is set to 191 in the RES2 routine) | 
| [YY](https://elite.bbcelite.com/c64/main/workspace/zp.html#yy) | Temporary storage, typically used for storing a 16-bit y-coordinate | 
| [ZP2 (Game Loader)](https://elite.bbcelite.com/c64/game_loader/workspace/zp.html#zp2) | Stores addresses used for moving content around | 
| [ZZ](https://elite.bbcelite.com/c64/main/workspace/zp.html#zz) | Temporary storage, typically used for distance values |

---
*Fonte originale: [https://elite.bbcelite.com/c64/indexes/variables.html](https://elite.bbcelite.com/c64/indexes/variables.html)*
