---
title: A-Z index of the source code in the Commodore 64 version of Elite
source_url: https://elite.bbcelite.com/c64/indexes/a-z.html
category: source-code
topics:
- raster interrupts
- memory management
- basic
- graphics
- sprite programming
- assembly
- input handling
- sound generation
difficulty: advanced
language: mixed
hardware:
- CIA
- SID
- CPU
- VIC-II
- KERNAL
- BASIC ROM
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

# A-Z index of the source code in the Commodore 64 version of Elite

This index contains every subroutine, entry point, variable, workspace and macro that appears in the source code for the Commodore 64 version of Elite, sorted alphabetically.

| Name | Category | Description | 
|---|---|---|
| [ABORT](https://elite.bbcelite.com/c64/main/subroutine/abort.html) | Dashboard | Unarm missiles and update the dashboard indicators | 
| [ABORT2](https://elite.bbcelite.com/c64/main/subroutine/abort2.html) | Dashboard | Set/unset the lock target for a missile and update the dashboard | 
| [abraxas](https://elite.bbcelite.com/c64/main/variable/abraxas.html) | Drawing the screen | The value for VIC register $18 to set the screen RAM address for a raster count of 1 in the interrupt routine (i.e. the dashboard) | 
| [ACT (Game data)](https://elite.bbcelite.com/c64/game_data/variable/act.html) | Maths (Geometry) | Arctan table | 
| [ADD](https://elite.bbcelite.com/c64/main/subroutine/add.html) | Maths (Arithmetic) | Calculate (A X) = (A P) + (S R) | 
| [ALP1](https://elite.bbcelite.com/c64/main/workspace/zp.html#alp1) | Workspace variable | Magnitude of the roll angle alpha, i.e. |alpha|, which is a positive value between 0 and 31 | 
| [ALP2](https://elite.bbcelite.com/c64/main/workspace/zp.html#alp2) | Workspace variable | Bit 7 of ALP2 = sign of the roll angle in ALPHA | 
| [ALPHA](https://elite.bbcelite.com/c64/main/workspace/zp.html#alpha) | Workspace variable | The current roll angle alpha, which is reduced from JSTX to a sign-magnitude value between -31 and +31 | 
| [ALTIT](https://elite.bbcelite.com/c64/main/workspace/wp.html#altit) | Workspace variable | Our altitude above the surface of the planet or sun | 
| [ANGRY](https://elite.bbcelite.com/c64/main/subroutine/angry.html) | Tactics | Make a ship or station hostile, and if this is a ship then enable the ship's AI and give it a kick of speed | 
| [antilog](https://elite.bbcelite.com/c64/main/variable/antilog.html) | Maths (Arithmetic) | Binary antilogarithm table | 
| [antilogODD](https://elite.bbcelite.com/c64/main/variable/antilogodd.html) | Maths (Arithmetic) | Binary antilogarithm table | 
| [april16](https://elite.bbcelite.com/c64/main/subroutine/startbd.html) | Sound | Start playing the docking music, irrespective of the current configuration settings | 
| [ARCTAN](https://elite.bbcelite.com/c64/main/subroutine/arctan.html) | Maths (Geometry) | Calculate A = arctan(P / Q) | 
| [ASH](https://elite.bbcelite.com/c64/main/workspace/up.html#ash) | Workspace variable | Aft shield status | 
| [auto](https://elite.bbcelite.com/c64/main/workspace/up.html#auto) | Workspace variable | Docking computer activation status | 
| [AVL](https://elite.bbcelite.com/c64/main/workspace/up.html#avl) | Workspace variable | Market availability in the current system | 
| [backtonormal](https://elite.bbcelite.com/c64/main/subroutine/backtonormal.html) | Utility routines | Disable the keyboard, set the SVN flag to 0, and return with A = 0 | 
| [BAD](https://elite.bbcelite.com/c64/main/subroutine/bad.html) | Status | Calculate how bad we have been | 
| [BALI](https://elite.bbcelite.com/c64/main/workspace/wp.html#bali) | Workspace variable | This byte appears to be unused | 
| [basicBootstrap (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/variable/basicbootstrap.html) | Loader | Call the RelocateLoader routine even if the firebird file is loaded as a BASIC program | 
| [basicVectors (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/variable/basicvectors.html) | Loader | Addresses that override the BASIC vectors for when the loader file is loaded at the address in its PRG header, $02A7 | 
| [BAY](https://elite.bbcelite.com/c64/main/subroutine/bay.html) | Status | Go to the docking bay (i.e. show the Status Mode screen) | 
| [BAY2](https://elite.bbcelite.com/c64/main/subroutine/tt219.html) | Market | Jump into the main loop at FRCE, setting the key "pressed" to the Inventory key | 
| [BAYSTEP](https://elite.bbcelite.com/c64/main/subroutine/brp.html) | Missions | Go to the docking bay (i.e. show the Status Mode screen) | 
| [BDBUFF](https://elite.bbcelite.com/c64/main/workspace/zp.html#bdbuff) | Workspace variable | The music data byte that is currently being processed, with the low nibble being processed first, and then the high nibble | 
| [BDdataptr1](https://elite.bbcelite.com/c64/main/workspace/zp.html#bddataptr1) | Workspace variable | The low byte of the address of the music data pointer in BDdataptr1(1 0), which points to the end of the music data currently being processed | 
| [BDdataptr2](https://elite.bbcelite.com/c64/main/workspace/zp.html#bddataptr2) | Workspace variable | The high byte of the address of the music data pointer in BDdataptr1(1 0), which points to the end of the music data currently being processed | 
| [BDdataptr3](https://elite.bbcelite.com/c64/main/workspace/zp.html#bddataptr3) | Workspace variable | The low byte of the address of the music data pointer in BDdataptr3(1 0), which is a backup of the initial value of the BDdataptr1(1 0) pointer, so music can be repeated | 
| [BDdataptr4](https://elite.bbcelite.com/c64/main/workspace/zp.html#bddataptr4) | Workspace variable | The high byte of the address of the music data pointer in BDdataptr3(1 0), which is a backup of the initial value of the BDdataptr1(1 0) pointer, so music can be repeated | 
| [BDENTRY](https://elite.bbcelite.com/c64/main/subroutine/bdentry.html) | Sound | Start playing a new tune as background music | 
| [BDirqhere](https://elite.bbcelite.com/c64/main/subroutine/bdirqhere.html) | Sound | The interrupt routine for playing background music | 
| [BDJMPTBH](https://elite.bbcelite.com/c64/main/variable/bdjmptbh.html) | Sound | A jump table containing addresses for processing music commands 1 through 15 (high bytes) | 
| [BDJMPTBL](https://elite.bbcelite.com/c64/main/variable/bdjmptbl.html) | Sound | A jump table containing addresses for processing music commands 1 through 15 (low bytes) | 
| [BDlab1](https://elite.bbcelite.com/c64/main/subroutine/bdlab1.html) | Sound | Apply vibrato before cleaning up and returning from the interrupt routine | 
| [BDlab19](https://elite.bbcelite.com/c64/main/subroutine/bdlab19.html) | Sound | Increment the music data pointer in BDdataptr1(1 0) and fetch the next data byte into A | 
| [BDlab21](https://elite.bbcelite.com/c64/main/subroutine/bdlab21.html) | Sound | Clean up and return from the interrupt routine | 
| [BDlab23](https://elite.bbcelite.com/c64/main/subroutine/bdlab23.html) | Sound | Apply a vibrato frequency change to voice 3 | 
| [BDlab24](https://elite.bbcelite.com/c64/main/subroutine/bdlab24.html) | Sound | Apply a vibrato frequency change to voice 2 | 
| [BDlab3](https://elite.bbcelite.com/c64/main/subroutine/bdlab3.html) | Sound | Fetch the next two music data bytes and set the frequency of voice 1 (high byte then low byte) | 
| [BDlab4](https://elite.bbcelite.com/c64/main/subroutine/bdlab4.html) | Sound | Set the voice control register for voice 1 to value1 | 
| [BDlab5](https://elite.bbcelite.com/c64/main/subroutine/bdlab5.html) | Sound | Fetch the next two music data bytes and set the frequency of voice 2 (high byte then low byte) and the vibrato variables | 
| [BDlab6](https://elite.bbcelite.com/c64/main/subroutine/bdlab6.html) | Sound | Set the voice control register for voice 2 to value2 | 
| [BDlab7](https://elite.bbcelite.com/c64/main/subroutine/bdlab7.html) | Sound | Fetch the next two music data bytes and set the frequency of voice 3 (high byte then low byte) and the vibrato variables | 
| [BDlab8](https://elite.bbcelite.com/c64/main/subroutine/bdlab8.html) | Sound | Set the voice control register for voice 3 to value3 | 
| [BDRO1](https://elite.bbcelite.com/c64/main/subroutine/bdro1.html) | Sound | Process music command <#1 fh1 fl1> to set the frequency for voice 1 to (fh1 fl1) and the control register for voice 1 to value1 | 
| [BDRO10](https://elite.bbcelite.com/c64/main/subroutine/bdro10.html) | Sound | Process music command <#10 h1 l1 h2 l2 h3 l3> to set the pulse width to all three voices | 
| [BDRO11](https://elite.bbcelite.com/c64/main/subroutine/bdro11.html) | Sound | Process music command <#11>, which does the same as command <#9> and restarts the current tune | 
| [BDRO12](https://elite.bbcelite.com/c64/main/subroutine/bdro12.html) | Sound | Process music command <#12 n> to set value4 = n, which sets the rest length for commands #8 and #15 | 
| [BDRO13](https://elite.bbcelite.com/c64/main/subroutine/bdro13.html) | Sound | Process music command <#13 v1 v2 v3> to set value1, value2, value3 to the voice control register values for commands <#1> to <#3> | 
| [BDRO14](https://elite.bbcelite.com/c64/main/subroutine/bdro14.html) | Sound | Process music command <#14 vf fc cf> to set the volume and filter modes, filter control and filter cut-off frequency | 
| [BDRO15](https://elite.bbcelite.com/c64/main/subroutine/bdro15.html) | Sound | Process music command <#15> to rest for 2 * value4 interrupts | 
| [BDRO2](https://elite.bbcelite.com/c64/main/subroutine/bdro2.html) | Sound | Process music command <#2 fh1 fl1> to set the frequency for voice 2 to (fh2 fl2) and the control register for voice 2 to value2 | 
| [BDRO3](https://elite.bbcelite.com/c64/main/subroutine/bdro3.html) | Sound | Process music command <#3 fh1 fl1> to set the frequency for voice 3 to (fh3 fl3) and the control register for voice 3 to value3 | 
| [BDRO4](https://elite.bbcelite.com/c64/main/subroutine/bdro4.html) | Sound | Process music command <#4 fh1 fl1 fh2 fl2> to set the frequencies and voice control registers for voices 1 and 2 | 
| [BDRO5](https://elite.bbcelite.com/c64/main/subroutine/bdro5.html) | Sound | Process music command <#5 fh1 fl1 fh2 fl2 fh3 fl3> to set the frequencies and voice control registers for voices 1, 2 and 3 | 
| [BDRO6](https://elite.bbcelite.com/c64/main/subroutine/bdro6.html) | Sound | Process music command <#6> to increment value0 and move on to the next nibble of music data | 
| [BDRO7](https://elite.bbcelite.com/c64/main/subroutine/bdro7.html) | Sound | Process music command <#7 ad1 ad2 ad3 sr1 sr2 sr3> to set three voices' attack and decay length, sustain volume and release length | 
| [BDRO8](https://elite.bbcelite.com/c64/main/subroutine/bdro8.html) | Sound | Process music command <#8> to rest for value4 interrupts | 
| [BDRO9](https://elite.bbcelite.com/c64/main/subroutine/bdro9.html) | Sound | Process music command <#9> to restart the current tune | 
| [BDskip1](https://elite.bbcelite.com/c64/main/subroutine/bdirqhere.html) | Sound | Process the next nibble of music data in BDBUFF | 
| [BEEP](https://elite.bbcelite.com/c64/main/subroutine/beep.html) | Sound | Make a short, high beep | 
| [BEGIN](https://elite.bbcelite.com/c64/main/subroutine/begin.html) | Loader | Initialise the configuration variables and start the game | 
| [BELL](https://elite.bbcelite.com/c64/main/subroutine/bell.html) | Sound | Make a standard system beep | 
| [BET1](https://elite.bbcelite.com/c64/main/workspace/zp.html#bet1) | Workspace variable | The magnitude of the pitch angle beta, i.e. |beta|, which is a positive value between 0 and 8 | 
| [BET2](https://elite.bbcelite.com/c64/main/workspace/zp.html#bet2) | Workspace variable | Bit 7 of BET2 = sign of the pitch angle in BETA | 
| [BETA](https://elite.bbcelite.com/c64/main/workspace/zp.html#beta) | Workspace variable | The current pitch angle beta, which is reduced from JSTY to a sign-magnitude value between -8 and +8 | 
| [BLINE](https://elite.bbcelite.com/c64/main/subroutine/bline.html) | Drawing circles | Draw a circle segment and add it to the ball line heap | 
| [BLUEBAND](https://elite.bbcelite.com/c64/main/subroutine/blueband.html) | Drawing the screen | Clear two four-character borders along each side of the space view | 
| [BLUEBANDS](https://elite.bbcelite.com/c64/main/subroutine/bluebands.html) | Drawing the screen | Clear a four-character border along one side of the space view | 
| [BOMB](https://elite.bbcelite.com/c64/main/workspace/up.html#bomb) | Workspace variable | Energy bomb | 
| [BOMBOFF](https://elite.bbcelite.com/c64/main/subroutine/bomboff.html) | Drawing the screen | Switch off the energy bomb effect | 
| [BOX](https://elite.bbcelite.com/c64/main/subroutine/ttx66k.html) | Drawing the screen | Just draw the border box along the top and sides | 
| [BOX2](https://elite.bbcelite.com/c64/main/subroutine/box2.html) | Drawing the screen | Draw the left and right edges of the border box for the space view | 
| [BOXS](https://elite.bbcelite.com/c64/main/subroutine/boxs.html) | Drawing the screen | Draw a horizontal line across the screen at pixel y-coordinate X | 
| [BOXS2](https://elite.bbcelite.com/c64/main/subroutine/boxs2.html) | Drawing the screen | Draw a vertical line for the left or right border box edge | 
| [boxsize](https://elite.bbcelite.com/c64/main/workspace/wp.html#boxsize) | Workspace variable | This byte appears to be unused | 
| [BPRNT](https://elite.bbcelite.com/c64/main/subroutine/bprnt.html) | Text | Print a 32-bit number, left-padded to a specific number of digits, with an optional decimal point | 
| [BR1 (Part 1 of 2)](https://elite.bbcelite.com/c64/main/subroutine/br1_part_1_of_2.html) | Start and end | Show the "Load New Commander (Y/N)?" screen and start the game | 
| [BR1 (Part 2 of 2)](https://elite.bbcelite.com/c64/main/subroutine/br1_part_2_of_2.html) | Start and end | Show the "Press Fire or Space, Commander" screen and start the game | 
| [BRBR](https://elite.bbcelite.com/c64/main/subroutine/brbr.html) | Utility routines | The standard BRKV handler for the game | 
| [BRIEF](https://elite.bbcelite.com/c64/main/subroutine/brief.html) | Missions | Start mission 1 and show the mission briefing | 
| [BRIEF2](https://elite.bbcelite.com/c64/main/subroutine/brief2.html) | Missions | Start mission 2 | 
| [BRIEF3](https://elite.bbcelite.com/c64/main/subroutine/brief3.html) | Missions | Receive the briefing and plans for mission 2 | 
| [BRIS](https://elite.bbcelite.com/c64/main/subroutine/bris.html) | Missions | Clear the screen, display "INCOMING MESSAGE" and wait for 2 seconds | 
| [BRKBK](https://elite.bbcelite.com/c64/main/subroutine/brkbk.html) | Save and load | Set the standard BRKV handler for the game | 
| [brkd](https://elite.bbcelite.com/c64/main/variable/brkd.html) | Utility routines | A flag that indicates whether a system error has occurred | 
| [BRP](https://elite.bbcelite.com/c64/main/subroutine/brp.html) | Missions | Print an extended token and show the Status Mode screen | 
| [BRPS](https://elite.bbcelite.com/c64/main/subroutine/debrief.html) | Missions | Print the extended token in A, show the Status Mode screen and return from the subroutine | 
| [BST](https://elite.bbcelite.com/c64/main/workspace/up.html#bst) | Workspace variable | Fuel scoops (BST stands for "barrel status") | 
| [BUF](https://elite.bbcelite.com/c64/main/workspace/wp.html#buf) | Workspace variable | The line buffer used by DASC to print justified text | 
| [BUMP2](https://elite.bbcelite.com/c64/main/subroutine/bump2.html) | Dashboard | Bump up the value of the pitch or roll dashboard indicator | 
| [c](https://elite.bbcelite.com/c64/main/subroutine/prx.html) | Equipment | Contains an RTS | 
| [CABTMP](https://elite.bbcelite.com/c64/main/workspace/up.html#cabtmp) | Workspace variable | Cabin temperature | 
| [caravanserai](https://elite.bbcelite.com/c64/main/variable/caravanserai.html) | Drawing the screen | Controls whether multicolour or standard bitmap mode is used for the lower part of the screen (i.e. the dashboard) | 
| [CASH](https://elite.bbcelite.com/c64/main/workspace/up.html#cash) | Workspace variable | Our current cash pot | 
| [cdump (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/cdump.html) | Drawing the screen | Colour RAM colour data for the dashboard | 
| [celllookh](https://elite.bbcelite.com/c64/main/variable/celllookh.html) | Drawing pixels | Lookup table for converting a text y-coordinate to the high byte of the address of the start of the character row in screen RAM | 
| [celllookl](https://elite.bbcelite.com/c64/main/variable/celllookl.html) | Drawing pixels | Lookup table for converting a text y-coordinate to the low byte of the address of the start of the character row | 
| [CHAR (Game data)](https://elite.bbcelite.com/c64/game_data/macro/char.html) | Text | Macro definition for characters in the recursive token table | 
| [CHECK](https://elite.bbcelite.com/c64/main/subroutine/check.html) | Save and load | Calculate the checksum for the last saved commander data block | 
| [CHECK2](https://elite.bbcelite.com/c64/main/subroutine/check2.html) | Save and load | Calculate the third checksum for the last saved commander data block (Commodore 64 and Apple II versions only) | 
| [Checksum](https://elite.bbcelite.com/c64/main/subroutine/checksum.html) | Copy protection | Checksum the code from $1000 to $9FFF and check against S%-1 | 
| [CHK](https://elite.bbcelite.com/c64/main/variable/chk.html) | Save and load | First checksum byte for the saved commander data file | 
| [CHK2](https://elite.bbcelite.com/c64/main/variable/chk2.html) | Save and load | Second checksum byte for the saved commander data file | 
| [CHK3](https://elite.bbcelite.com/c64/main/variable/chk3.html) | Save and load | Third checksum byte for the saved commander data file | 
| [CHKON](https://elite.bbcelite.com/c64/main/subroutine/chkon.html) | Drawing circles | Check whether any part of a circle appears on the extended screen | 
| [CHPR](https://elite.bbcelite.com/c64/main/subroutine/chpr.html) | Text | Print a character at the text cursor by poking into screen memory | 
| [CHPR2](https://elite.bbcelite.com/c64/main/subroutine/chpr2.html) | Text | Character print vector handler | 
| [CIRCLE](https://elite.bbcelite.com/c64/main/subroutine/circle.html) | Drawing circles | Draw a circle for the planet | 
| [CIRCLE2](https://elite.bbcelite.com/c64/main/subroutine/circle2.html) | Drawing circles | Draw a circle (for the planet or chart) | 
| [CLDELAY](https://elite.bbcelite.com/c64/main/subroutine/cldelay.html) | Utility routines | Delay by iterating through 5 * 256 (1280) empty loops | 
| [clss](https://elite.bbcelite.com/c64/main/subroutine/clss.html) | Drawing the screen | Clear the screen, move the text cursor to the top-left corner and jump back into the CHPR routine to print the next character | 
| [CLYNS](https://elite.bbcelite.com/c64/main/subroutine/clyns.html) | Drawing the screen | Clear the bottom three text rows of the space view | 
| [cmn](https://elite.bbcelite.com/c64/main/subroutine/cmn.html) | Status | Print the commander's name | 
| [cmn-1](https://elite.bbcelite.com/c64/main/subroutine/cmn.html) | Status | Contains an RTS | 
| [CNT](https://elite.bbcelite.com/c64/main/workspace/zp.html#cnt) | Workspace variable | Temporary storage, typically used for storing the number of iterations required when looping | 
| [CNT2](https://elite.bbcelite.com/c64/main/workspace/zp.html#cnt2) | Workspace variable | Temporary storage, used in the planet-drawing routine to store the segment number where the arc of a partial circle should start | 
| [cntr](https://elite.bbcelite.com/c64/main/subroutine/cntr.html) | Dashboard | Apply damping to the pitch or roll dashboard indicator | 
| [coffee](https://elite.bbcelite.com/c64/main/subroutine/coffee.html) | Sound | Return from the interrupt routine, for when we are making sound effects | 
| [coffeeex](https://elite.bbcelite.com/c64/main/subroutine/stopbd.html) | Sound | Restore the memory configuration and return from the subroutine | 
| [COK](https://elite.bbcelite.com/c64/main/workspace/up.html#cok) | Workspace variable | Flags used to generate the competition code | 
| [COL](https://elite.bbcelite.com/c64/main/workspace/zp.html#col) | Workspace variable | Temporary storage, used to store colour information when drawing pixels in the dashboard | 
| [COL2](https://elite.bbcelite.com/c64/main/workspace/up.html#col2) | Workspace variable | The text colour of the next character to draw in CHPR | 
| [COLD](https://elite.bbcelite.com/c64/main/subroutine/cold.html) | Loader | Configure memory, set up interrupt handlers and configure the VIC-II, SID and CIA chips | 
| [COMC](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#comc) | Workspace variable | The colour of the dot on the compass | 
| [COMIRQ1](https://elite.bbcelite.com/c64/main/subroutine/comirq1.html) | Drawing the screen | The split screen and sound interrupt handler (the IRQ interrupt service hardware vector at $FFFE points here) | 
| [COMPAS](https://elite.bbcelite.com/c64/main/subroutine/compas.html) | Dashboard | Update the compass | 
| [COMUDAT](https://elite.bbcelite.com/c64/main/variable/comudat.html) | Sound | Music data from the C.COMUDAT file | 
| [COMX](https://elite.bbcelite.com/c64/main/workspace/up.html#comx) | Workspace variable | The x-coordinate of the compass dot | 
| [COMY](https://elite.bbcelite.com/c64/main/workspace/up.html#comy) | Workspace variable | The y-coordinate of the compass dot | 
| [CONT (Game data)](https://elite.bbcelite.com/c64/game_data/macro/cont.html) | Text | Macro definition for control codes in the recursive token table | 
| [CopyZeroPage (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/copyzeropage.html) | Loader | Copy a page of data in a specified direction between zero page and the page at $CE00, omitting the first two bytes | 
| [counter](https://elite.bbcelite.com/c64/main/workspace/zp.html#counter) | Workspace variable | The rest counter when playing music, for implementing music commands #8 and #15 | 
| [CPIX2](https://elite.bbcelite.com/c64/main/subroutine/cpix2.html) | Drawing pixels | Draw a single-height dash on the dashboard | 
| [CPIX4](https://elite.bbcelite.com/c64/main/subroutine/cpix4.html) | Drawing pixels | Draw a double-height dot on the dashboard | 
| [cpl](https://elite.bbcelite.com/c64/main/subroutine/cpl.html) | Universe | Print the selected system name | 
| [CRGO](https://elite.bbcelite.com/c64/main/workspace/up.html#crgo) | Workspace variable | Our ship's cargo capacity | 
| [crlf](https://elite.bbcelite.com/c64/main/subroutine/crlf.html) | Text | Tab to column 21 and print a colon | 
| [csh](https://elite.bbcelite.com/c64/main/subroutine/csh.html) | Status | Print the current amount of cash | 
| [CTRL](https://elite.bbcelite.com/c64/main/subroutine/ctrl.html) | Keyboard | Scan the keyboard to see if CTRL is currently pressed | 
| [CTWOS](https://elite.bbcelite.com/c64/main/variable/ctwos.html) | Drawing pixels | Ready-made double-pixel character row bytes for the dashboard | 
| [CTWOS2](https://elite.bbcelite.com/c64/main/variable/ctwos2.html) | Drawing pixels | Ready-made single-pixel character row bytes for multicolour bitmap mode | 
| [DAMP](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#damp) | Workspace variable | Keyboard damping configuration setting | 
| [DASC](https://elite.bbcelite.com/c64/main/subroutine/tt26.html) | Text | DASC does exactly the same as TT26 and prints a character at the text cursor, with support for verified text in extended tokens | 
| [date (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/date.html) | Loader | A date image that is included into the source disk binaries (this is just random noise in the released game) | 
| [DCS1](https://elite.bbcelite.com/c64/main/subroutine/dcs1.html) | Flight | Calculate the vector from the ideal docking position to the ship | 
| [de](https://elite.bbcelite.com/c64/main/workspace/up.html#de) | Workspace variable | Equipment destruction flag | 
| [DEATH](https://elite.bbcelite.com/c64/main/subroutine/death.html) | Start and end | Display the death screen | 
| [DEATH2](https://elite.bbcelite.com/c64/main/subroutine/death2.html) | Start and end | Reset most of the game and restart from the title screen | 
| [DEBRIEF](https://elite.bbcelite.com/c64/main/subroutine/debrief.html) | Missions | Finish mission 1 | 
| [DEBRIEF2](https://elite.bbcelite.com/c64/main/subroutine/debrief2.html) | Missions | Finish mission 2 | 
| [dec27](https://elite.bbcelite.com/c64/main/subroutine/tt26.html) | Text | Contains an RTS | 
| [DEEOR](https://elite.bbcelite.com/c64/main/subroutine/deeor.html) | Utility routines | Unscramble the main code | 
| [DEEORS](https://elite.bbcelite.com/c64/main/subroutine/deeors.html) | Utility routines | Decrypt a multi-page block of memory | 
| [DEEORS (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/deeors.html) | Loader | Decrypt a multi-page block of memory | 
| [DELAY](https://elite.bbcelite.com/c64/main/subroutine/delay.html) | Utility routines | Wait for a specified time, in either 1/50s of a second (on PAL systems) or 1/60s of a second (on NTSC systems) | 
| [DELT4](https://elite.bbcelite.com/c64/main/workspace/zp.html#delt4) | Workspace variable | Our current speed * 64 as a 16-bit value | 
| [DELTA](https://elite.bbcelite.com/c64/main/workspace/zp.html#delta) | Workspace variable | Our current speed, in the range 1-40 | 
| [DENGY](https://elite.bbcelite.com/c64/main/subroutine/dengy.html) | Flight | Drain some energy from the energy banks | 
| [DET1](https://elite.bbcelite.com/c64/main/subroutine/det1.html) | Drawing the screen | Show or hide the dashboard (for when we die) | 
| [DETOK](https://elite.bbcelite.com/c64/main/subroutine/detok.html) | Text | Print an extended recursive token from the TKN1 token table | 
| [DETOK2](https://elite.bbcelite.com/c64/main/subroutine/detok2.html) | Text | Print an extended text token (1-255) | 
| [DETOK3](https://elite.bbcelite.com/c64/main/subroutine/detok3.html) | Text | Print an extended recursive token from the RUTOK token table | 
| [DFAULT](https://elite.bbcelite.com/c64/main/subroutine/dfault.html) | Start and end | Reset the current commander data block to the last saved commander | 
| [DFLAG](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#dflag) | Workspace variable | A flag that indicates whether the dashboard is currently being shown on-screen | 
| [DIALS (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/dials.html) | Drawing the screen | The dashboard bitmap and colour data for screen RAM | 
| [DIALS (Part 1 of 4)](https://elite.bbcelite.com/c64/main/subroutine/dials_part_1_of_4.html) | Dashboard | Update the dashboard: speed indicator | 
| [DIALS (Part 2 of 4)](https://elite.bbcelite.com/c64/main/subroutine/dials_part_2_of_4.html) | Dashboard | Update the dashboard: pitch and roll indicators | 
| [DIALS (Part 3 of 4)](https://elite.bbcelite.com/c64/main/subroutine/dials_part_3_of_4.html) | Dashboard | Update the dashboard: four energy banks | 
| [DIALS (Part 4 of 4)](https://elite.bbcelite.com/c64/main/subroutine/dials_part_4_of_4.html) | Dashboard | Update the dashboard: shields, fuel, laser & cabin temp, altitude | 
| [DIL](https://elite.bbcelite.com/c64/main/subroutine/dilx.html) | Dashboard | The range of the indicator is 0-16 (for the energy banks) | 
| [DIL-1](https://elite.bbcelite.com/c64/main/subroutine/dilx.html) | Dashboard | The range of the indicator is 0-32 (for the speed indicator) | 
| [DIL2](https://elite.bbcelite.com/c64/main/subroutine/dil2.html) | Dashboard | Update the roll or pitch indicator on the dashboard | 
| [DILX](https://elite.bbcelite.com/c64/main/subroutine/dilx.html) | Dashboard | Update a bar-based indicator on the dashboard | 
| [DILX+2](https://elite.bbcelite.com/c64/main/subroutine/dilx.html) | Dashboard | The range of the indicator is 0-64 (for the fuel indicator) | 
| [DISK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#disk) | Workspace variable | Current media configuration setting | 
| [distaway](https://elite.bbcelite.com/c64/main/workspace/wp.html#distaway) | Workspace variable | Used to store the nearest distance of the rotating ship on the title screen | 
| [DJD](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#djd) | Workspace variable | Keyboard auto-recentre configuration setting | 
| [djd1](https://elite.bbcelite.com/c64/main/subroutine/redu2.html) | Dashboard | Auto-recentre the value in X, if keyboard auto-recentre is configured | 
| [DK4](https://elite.bbcelite.com/c64/main/subroutine/dk4.html) | Keyboard | Scan for pause, configuration and secondary flight keys | 
| [DKCMP](https://elite.bbcelite.com/c64/main/workspace/up.html#dkcmp) | Workspace variable | Docking computer | 
| [DKJ1](https://elite.bbcelite.com/c64/main/subroutine/dkj1.html) | Keyboard | Read joystick and flight controls | 
| [DKS2](https://elite.bbcelite.com/c64/main/subroutine/dks2.html) | Keyboard | Read the joystick position | 
| [DKS3](https://elite.bbcelite.com/c64/main/subroutine/dks3.html) | Keyboard | Toggle a configuration setting and emit a beep | 
| [DKS4](https://elite.bbcelite.com/c64/main/subroutine/dks4.html) | Keyboard | Scan the keyboard to see if a specific key is being pressed | 
| [DKSANYKEY](https://elite.bbcelite.com/c64/main/subroutine/dksanykey.html) | Keyboard | An unused routine that scans a specific column in the keyboard matrix for a key press | 
| [DL](https://elite.bbcelite.com/c64/main/workspace/zp.html#dl) | Workspace variable | This byte is unused in this version of Elite (it is used to store the vertical sync flag in the BBC Micro versions) | 
| [DLY](https://elite.bbcelite.com/c64/main/workspace/up.html#dly) | Workspace variable | In-flight message delay | 
| [dn](https://elite.bbcelite.com/c64/main/subroutine/dn.html) | Market | Print the amount of money we have left in the cash pot, then make a short, high beep and delay for 1 second | 
| [dn2](https://elite.bbcelite.com/c64/main/subroutine/dn2.html) | Text | Make a short, high beep and delay for 1 second | 
| [DNOIZ](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#dnoiz) | Workspace variable | Sound on/off configuration setting | 
| [dockEd](https://elite.bbcelite.com/c64/main/subroutine/docked.html) | Flight | Print a message to say there is no hyperspacing allowed inside the station | 
| [DOCKIT](https://elite.bbcelite.com/c64/main/subroutine/dockit.html) | Flight | Apply docking manoeuvres to the ship in INWK | 
| [DOCOL](https://elite.bbcelite.com/c64/main/subroutine/docol.html) | Text | Implement the #SETCOL <colour> command (set the current colour) | 
| [DOENTRY](https://elite.bbcelite.com/c64/main/subroutine/doentry.html) | Flight | Dock at the space station and work out any mission progression | 
| [DOEXP](https://elite.bbcelite.com/c64/main/subroutine/doexp.html) | Drawing ships | Draw an exploding ship | 
| [DOHFX](https://elite.bbcelite.com/c64/main/subroutine/dohfx.html) | Drawing circles | Implement the #DOHFX <flag> command (update the hyperspace effect flag) | 
| [DOKEY](https://elite.bbcelite.com/c64/main/subroutine/dokey.html) | Keyboard | Scan for the seven primary flight controls and apply the docking computer manoeuvring code | 
| [dontclip](https://elite.bbcelite.com/c64/main/workspace/zp.html#dontclip) | Workspace variable | A flag that controls whether the LL145 routine clips lines to the dimensions of the space view (which we want to disable in the Short-range Chart, as there is no dashboard and the chart needs to use the whole screen) | 
| [DORND](https://elite.bbcelite.com/c64/main/subroutine/dornd.html) | Maths (Arithmetic) | Generate random numbers | 
| [DORND2](https://elite.bbcelite.com/c64/main/subroutine/dornd.html) | Maths (Arithmetic) | Make sure the C flag doesn't affect the outcome | 
| [DOSVN](https://elite.bbcelite.com/c64/main/subroutine/dosvn.html) | Save and load | Implement the #DOSVN <flag> command (update the "save in progress" flag) | 
| [DOT](https://elite.bbcelite.com/c64/main/subroutine/dot.html) | Dashboard | Draw a dash on the compass | 
| [DOVDU19](https://elite.bbcelite.com/c64/main/subroutine/dovdu19.html) | Drawing the screen | Implement the #SETVDU19 <offset> command (change mode 1 palette) | 
| [DOXC](https://elite.bbcelite.com/c64/main/subroutine/doxc.html) | Text | Move the text cursor to a specific column | 
| [DOYC](https://elite.bbcelite.com/c64/main/subroutine/doyc.html) | Text | Move the text cursor to a specific row | 
| [DTEN](https://elite.bbcelite.com/c64/main/subroutine/detok.html) | Text | Print recursive token number X from the token table pointed to by (A V), used to print tokens from the RUTOK table via calls to DETOK3 | 
| [DTS](https://elite.bbcelite.com/c64/main/subroutine/detok2.html) | Text | Print a single letter in the correct case | 
| [DTW1](https://elite.bbcelite.com/c64/main/variable/dtw1.html) | Text | A mask for applying the lower case part of Sentence Case to extended text tokens | 
| [DTW2](https://elite.bbcelite.com/c64/main/variable/dtw2.html) | Text | A flag that indicates whether we are currently printing a word | 
| [DTW3](https://elite.bbcelite.com/c64/main/variable/dtw3.html) | Text | A flag for switching between standard and extended text tokens | 
| [DTW4](https://elite.bbcelite.com/c64/main/variable/dtw4.html) | Text | Flags that govern how justified extended text tokens are printed | 
| [DTW5](https://elite.bbcelite.com/c64/main/variable/dtw5.html) | Text | The size of the justified text buffer at BUF | 
| [DTW6](https://elite.bbcelite.com/c64/main/variable/dtw6.html) | Text | A flag to denote whether printing in lower case is enabled for extended text tokens | 
| [DTW8](https://elite.bbcelite.com/c64/main/variable/dtw8.html) | Text | A mask for capitalising the next letter in an extended text token | 
| [DTWOS](https://elite.bbcelite.com/c64/main/variable/dtwos.html) | Drawing pixels | An unused table of ready-made double-pixel character row bytes for the dashboard | 
| [DV41](https://elite.bbcelite.com/c64/main/subroutine/dv41.html) | Maths (Arithmetic) | Calculate (P R) = 256 * DELTA / A | 
| [DV42](https://elite.bbcelite.com/c64/main/subroutine/dv42.html) | Maths (Arithmetic) | Calculate (P R) = 256 * DELTA / z_hi | 
| [DVID3B2](https://elite.bbcelite.com/c64/main/subroutine/dvid3b2.html) | Maths (Arithmetic) | Calculate K(3 2 1 0) = (A P+1 P) / (z_sign z_hi z_lo) | 
| [DVID4](https://elite.bbcelite.com/c64/main/subroutine/dvid4.html) | Maths (Arithmetic) | Calculate (P R) = 256 * A / Q | 
| [DVIDT](https://elite.bbcelite.com/c64/main/subroutine/dvidt.html) | Maths (Arithmetic) | Calculate (P+1 A) = (A P) / Q | 
| [E% (Game data)](https://elite.bbcelite.com/c64/game_data/variable/e_per_cent.html) | Drawing ships | Ship blueprints default NEWB flags | 
| [ECBLB](https://elite.bbcelite.com/c64/main/subroutine/ecblb.html) | Dashboard | Light up the E.C.M. indicator bulb ("E") on the dashboard | 
| [ECBLB2](https://elite.bbcelite.com/c64/main/subroutine/ecblb2.html) | Dashboard | Start up the E.C.M. (light up the indicator, start the countdown and make the E.C.M. sound) | 
| [ECHR (Game data)](https://elite.bbcelite.com/c64/game_data/macro/echr.html) | Text | Macro definition for characters in the extended token table | 
| [ECM](https://elite.bbcelite.com/c64/main/workspace/up.html#ecm) | Workspace variable | E.C.M. system | 
| [ECMA](https://elite.bbcelite.com/c64/main/workspace/zp.html#ecma) | Workspace variable | The E.C.M. countdown timer, which determines whether an E.C.M. system is currently operating | 
| [ECMOF](https://elite.bbcelite.com/c64/main/subroutine/ecmof.html) | Dashboard | Switch off the E.C.M. and turn off the dashboard bulb | 
| [ECMP](https://elite.bbcelite.com/c64/main/workspace/up.html#ecmp) | Workspace variable | Our E.C.M. status | 
| [EDGE (Game data)](https://elite.bbcelite.com/c64/game_data/macro/edge.html) | Drawing ships | Macro definition for adding edges to ship blueprints | 
| [EDGES](https://elite.bbcelite.com/c64/main/subroutine/edges.html) | Drawing lines | Draw a horizontal line given a centre and a half-width | 
| [ee3](https://elite.bbcelite.com/c64/main/subroutine/ee3.html) | Flight | Print the hyperspace countdown in the top-left of the screen | 
| [EE51](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_1_of_12.html) | Drawing ships | Remove the current ship from the screen, called from SHPPT before drawing the ship as a point | 
| [EJMP (Game data)](https://elite.bbcelite.com/c64/game_data/macro/ejmp.html) | Text | Macro definition for jump tokens in the extended token table | 
| [Elite GMA loader (Part 1 of 4) (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_1_of_4.html) | Loader | Skip past the table of track and sector numbers if present | 
| [Elite GMA loader (Part 2 of 4) (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_2_of_4.html) | Loader | Offer the option of a fast loader and run the disk protection code in the GMA3 file | 
| [Elite GMA loader (Part 3 of 4) (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_3_of_4.html) | Loader | Run the Elite loader in the GMA4 file | 
| [Elite GMA loader (Part 4 of 4) (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_4_of_4.html) | Loader | Load the GMA5 and GMA6 binaries and start the game | 
| [Elite loader (Part 1 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_1_of_7.html) | Loader | Unscramble the loader code and game data | 
| [Elite loader (Part 2 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_2_of_7.html) | Loader | Copy the game data to their correct locations | 
| [Elite loader (Part 3 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_3_of_7.html) | Loader | Configure the memory layout and the CIA chips | 
| [Elite loader (Part 4 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_4_of_7.html) | Loader | Configure the VIC-II for screen memory and sprites | 
| [Elite loader (Part 5 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_5_of_7.html) | Loader | Configure the screen bitmap and copy colour data into screen RAM | 
| [Elite loader (Part 6 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_6_of_7.html) | Loader | Copy colour data into colour RAM and configure more screen RAM | 
| [Elite loader (Part 7 of 7) (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/elite_loader_part_7_of_7.html) | Loader | Set up the sprite pointers, make a copy of the dashboard bitmap in DSTORE% and copy the sprite definitions to SPRITELOC% | 
| [ENERGY](https://elite.bbcelite.com/c64/main/workspace/up.html#energy) | Workspace variable | Energy bank status | 
| [ENGY](https://elite.bbcelite.com/c64/main/workspace/up.html#engy) | Workspace variable | Energy unit | 
| [eq](https://elite.bbcelite.com/c64/main/subroutine/eq.html) | Equipment | Subtract the price of equipment from the cash pot | 
| [EQSHP](https://elite.bbcelite.com/c64/main/subroutine/eqshp.html) | Equipment | Show the Equip Ship screen | 
| [ERND (Game data)](https://elite.bbcelite.com/c64/game_data/macro/ernd.html) | Text | Macro definition for random tokens in the extended token table | 
| [err](https://elite.bbcelite.com/c64/main/subroutine/eqshp.html) | Equipment | Beep, pause and go to the docking bay (i.e. show the Status Mode screen) | 
| [ESCAPE](https://elite.bbcelite.com/c64/main/subroutine/escape.html) | Flight | Launch our escape pod | 
| [ESCP](https://elite.bbcelite.com/c64/main/workspace/up.html#escp) | Workspace variable | Escape pod | 
| [ETOK (Game data)](https://elite.bbcelite.com/c64/game_data/macro/etok.html) | Text | Macro definition for recursive tokens in the extended token table | 
| [ETWO (Game data)](https://elite.bbcelite.com/c64/game_data/macro/etwo.html) | Text | Macro definition for two-letter tokens in the extended token table | 
| [EV](https://elite.bbcelite.com/c64/main/workspace/up.html#ev) | Workspace variable | The "extra vessels" spawning counter | 
| [ex](https://elite.bbcelite.com/c64/main/subroutine/ex.html) | Text | Print a recursive token | 
| [exlook](https://elite.bbcelite.com/c64/main/variable/exlook.html) | Drawing ships | A table to shift X left by one place when X is 0 or 1 | 
| [EXNO](https://elite.bbcelite.com/c64/main/subroutine/exno.html) | Sound | Make the sound of a laser strike on another ship | 
| [EXNO2](https://elite.bbcelite.com/c64/main/subroutine/exno2.html) | Status | Process us making a kill | 
| [EXNO3](https://elite.bbcelite.com/c64/main/subroutine/exno3.html) | Sound | Make an explosion sound | 
| [EXS1](https://elite.bbcelite.com/c64/main/subroutine/doexp.html) | Drawing ships | Set (A X) = (A R) +/- random * cloud size | 
| [F%](https://elite.bbcelite.com/c64/main/variable/f_per_cent.html) | Utility routines | Denotes the end of the main game code, from ELITE A to ELITE K | 
| [FACE (Game data)](https://elite.bbcelite.com/c64/game_data/macro/face.html) | Drawing ships | Macro definition for adding faces to ship blueprints | 
| [FAROF](https://elite.bbcelite.com/c64/main/subroutine/farof.html) | Maths (Geometry) | Compare x_hi, y_hi and z_hi with 224 | 
| [FAROF2](https://elite.bbcelite.com/c64/main/subroutine/farof2.html) | Maths (Geometry) | Compare x_hi, y_hi and z_hi with A | 
| [fastLoaderOffered (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/fastloaderoffered.html) | Loader | A flag to record whether we have already asked whether to use the fast loader, so we don't ask twice | 
| [fastTrackSector (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/fasttracksector.html) | Loader | A track and sector table for use by the fast loader | 
| [FEED](https://elite.bbcelite.com/c64/main/subroutine/feed.html) | Text | Print a newline | 
| [filename (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/subroutine/filename.html) | Loader | A wildcarded filename that matches the first GMA file on disk | 
| [filename (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/filename.html) | Loader | The GMA filename used to load the game files, buried in a message from GMA, the author of the loader | 
| [FILEPR](https://elite.bbcelite.com/c64/main/subroutine/filepr.html) | Save and load | Display the currently selected media (disk or tape) | 
| [filesys](https://elite.bbcelite.com/c64/main/variable/filesys.html) | Save and load | A lookup table containing the device numbers for tape and disk | 
| [FIST](https://elite.bbcelite.com/c64/main/workspace/up.html#fist) | Workspace variable | Our legal status (FIST stands for "fugitive/innocent status") | 
| [FLAG](https://elite.bbcelite.com/c64/main/workspace/zp.html#flag) | Workspace variable | A flag that's used to define whether this is the first call to the ball line routine in BLINE, so it knows whether to wait for the second call before storing segment data in the ball line heap | 
| [FLFLLS](https://elite.bbcelite.com/c64/main/subroutine/flflls.html) | Drawing suns | Reset the sun line heap | 
| [FLH](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#flh) | Workspace variable | Flashing console bars configuration setting | 
| [FLIP](https://elite.bbcelite.com/c64/main/subroutine/flip.html) | Stardust | Reflect the stardust particles in the screen diagonal and redraw the stardust field | 
| [FLKB](https://elite.bbcelite.com/c64/main/subroutine/flkb.html) | Keyboard | Flush the keyboard buffer | 
| [FMLTU](https://elite.bbcelite.com/c64/main/subroutine/fmltu.html) | Maths (Arithmetic) | Calculate A = A * Q / 256 | 
| [FMLTU2](https://elite.bbcelite.com/c64/main/subroutine/fmltu2.html) | Maths (Arithmetic) | Calculate A = K * sin(A) | 
| [fq1](https://elite.bbcelite.com/c64/main/subroutine/frs1.html) | Tactics | Used to add a cargo canister to the universe | 
| [FR1](https://elite.bbcelite.com/c64/main/subroutine/fr1.html) | Tactics | Display the "missile jammed" message | 
| [FR1-2](https://elite.bbcelite.com/c64/main/subroutine/fr1.html) | Tactics | Clear the C flag and return from the subroutine | 
| [FRCE](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_6_of_6.html) | Main loop | The entry point for the main game loop if we want to jump straight to a specific screen, by pretending to "press" a key, in which case A contains the internal key number of the key we want to "press" | 
| [FREEZE](https://elite.bbcelite.com/c64/main/subroutine/dk4.html) | Keyboard | Rejoin the pause routine after processing a screen save | 
| [FRIN](https://elite.bbcelite.com/c64/main/workspace/up.html#frin) | Workspace variable | Slots for the ships in the local bubble of universe | 
| [FRIN (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/frin.html) | Loader | A temporary variable that's used for storing addresses | 
| [FRMIS](https://elite.bbcelite.com/c64/main/subroutine/frmis.html) | Tactics | Fire a missile from our ship | 
| [FRS1](https://elite.bbcelite.com/c64/main/subroutine/frs1.html) | Tactics | Launch a ship straight ahead of us, below the laser sights | 
| [frump](https://elite.bbcelite.com/c64/main/workspace/up.html#frump) | Workspace variable | Used to store the number of particles in the explosion cloud | 
| [FSH](https://elite.bbcelite.com/c64/main/workspace/up.html#fsh) | Workspace variable | Forward shield status | 
| [fwl](https://elite.bbcelite.com/c64/main/subroutine/fwl.html) | Status | Print fuel and cash levels | 
| [G%](https://elite.bbcelite.com/c64/main/variable/g_per_cent.html) | Utility routines | Denotes the start of the main game code, from ELITE A to ELITE K | 
| [GC2](https://elite.bbcelite.com/c64/main/subroutine/gc2.html) | Maths (Arithmetic) | Calculate (Y X) = (A P) * 4 | 
| [GCASH](https://elite.bbcelite.com/c64/main/subroutine/gcash.html) | Maths (Arithmetic) | Calculate (Y X) = P * Q * 4 | 
| [GCNT](https://elite.bbcelite.com/c64/main/workspace/up.html#gcnt) | Workspace variable | The number of the current galaxy (0-7) | 
| [Ghy](https://elite.bbcelite.com/c64/main/subroutine/ghy.html) | Flight | Perform a galactic hyperspace jump | 
| [GHYP](https://elite.bbcelite.com/c64/main/workspace/up.html#ghyp) | Workspace variable | Galactic hyperdrive | 
| [GINF](https://elite.bbcelite.com/c64/main/subroutine/ginf.html) | Universe | Fetch the address of a ship's data block into INF | 
| [GNTMP](https://elite.bbcelite.com/c64/main/workspace/up.html#gntmp) | Workspace variable | Laser temperature (or "gun temperature") | 
| [gnum](https://elite.bbcelite.com/c64/main/subroutine/gnum.html) | Market | Get a number from the keyboard | 
| [GOIN](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_9_of_16.html) | Main loop | We jump here from part 3 of the main flight loop if the docking computer is activated by pressing "C" | 
| [GOPL](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_3_of_7.html) | Tactics | Make the ship head towards the planet | 
| [gov](https://elite.bbcelite.com/c64/main/workspace/up.html#gov) | Workspace variable | The current system's government type (0-7) | 
| [GTDRV](https://elite.bbcelite.com/c64/main/subroutine/gtdrv.html) | Save and load | Get an ASCII disk drive number from the keyboard | 
| [GTHG](https://elite.bbcelite.com/c64/main/subroutine/gthg.html) | Universe | Spawn a Thargoid ship and a Thargon companion | 
| [GTNMEW](https://elite.bbcelite.com/c64/main/subroutine/gtnmew.html) | Save and load | Fetch the name of a commander file to save or load | 
| [GVL](https://elite.bbcelite.com/c64/main/subroutine/gvl.html) | Universe | Calculate the availability of market items | 
| [HFS1](https://elite.bbcelite.com/c64/main/subroutine/hfs2.html) | Drawing circles | Don't clear the screen, and draw 8 concentric rings with the step size in STP | 
| [HFS2](https://elite.bbcelite.com/c64/main/subroutine/hfs2.html) | Drawing circles | Draw the launch or hyperspace tunnel | 
| [HFX](https://elite.bbcelite.com/c64/main/workspace/up.html#hfx) | Workspace variable | This flag is unused in this version of Elite. In the other versions, setting HFX to a non-zero value makes the hyperspace rings multi-coloured, but that effect is not used in this version | 
| [HI1](https://elite.bbcelite.com/c64/main/subroutine/hitch.html) | Tactics | Contains an RTS | 
| [HITCH](https://elite.bbcelite.com/c64/main/subroutine/hitch.html) | Tactics | Work out if the ship in INWK is in our crosshairs | 
| [HL6](https://elite.bbcelite.com/c64/main/subroutine/loin_part_7_of_7.html) | Drawing lines | Contains an RTS | 
| [HLOIN](https://elite.bbcelite.com/c64/main/subroutine/hloin.html) | Drawing lines | Draw a horizontal line from (X1, Y1) to (X2, Y1) | 
| [HLOIN2](https://elite.bbcelite.com/c64/main/subroutine/hloin2.html) | Drawing lines | Remove a line from the sun line heap and draw it on-screen | 
| [hm](https://elite.bbcelite.com/c64/main/subroutine/hm.html) | Charts | Select the closest system and redraw the chart crosshairs | 
| [HME2](https://elite.bbcelite.com/c64/main/subroutine/hme2.html) | Charts | Search the galaxy for a system | 
| [hy5](https://elite.bbcelite.com/c64/main/subroutine/jmp.html) | Universe | Contains an RTS | 
| [hyp](https://elite.bbcelite.com/c64/main/subroutine/hyp.html) | Flight | Start the hyperspace process | 
| [hyp1](https://elite.bbcelite.com/c64/main/subroutine/hyp1.html) | Universe | Process a jump to the system closest to (QQ9, QQ10) | 
| [hyp1+3](https://elite.bbcelite.com/c64/main/subroutine/hyp1.html) | Universe | Jump straight to the system at (QQ9, QQ10) without first calculating which system is closest. We do this if we already know that (QQ9, QQ10) points to a system | 
| [HYPNOISE](https://elite.bbcelite.com/c64/main/subroutine/hypnoise.html) | Sound | Make the sound of the hyperspace drive being engaged | 
| [hyR](https://elite.bbcelite.com/c64/main/subroutine/gvl.html) | Universe | Contains an RTS | 
| [INCYC](https://elite.bbcelite.com/c64/main/subroutine/incyc.html) | Text | Move the text cursor to the next row | 
| [INF](https://elite.bbcelite.com/c64/main/workspace/zp.html#inf) | Workspace variable | Temporary storage, typically used for storing the address of a ship's data block, so it can be copied to and from the internal workspace at INWK | 
| [innersec](https://elite.bbcelite.com/c64/main/variable/innersec.html) | Drawing the screen | A table for converting the value of X from 0 to 1 or from 1 to 0, for use when flipping RASCT between 0 and 1 on each interrupt | 
| [INWK](https://elite.bbcelite.com/c64/main/workspace/zp.html#inwk) | Workspace variable | The zero-page internal workspace for the current ship data block | 
| [ITEM](https://elite.bbcelite.com/c64/main/macro/item.html) | Market | Macro definition for the market prices table | 
| [itsoff](https://elite.bbcelite.com/c64/main/subroutine/dvidt.html) | Maths (Arithmetic) | Contains an RTS | 
| [JAMESON](https://elite.bbcelite.com/c64/main/subroutine/jameson.html) | Save and load | Restore the default JAMESON commander | 
| [jmp](https://elite.bbcelite.com/c64/main/subroutine/jmp.html) | Universe | Set the current system to the selected system | 
| [JMTB](https://elite.bbcelite.com/c64/main/variable/jmtb.html) | Text | The extended token table for jump tokens 1-32 (DETOK) | 
| [JSTE](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#jste) | Workspace variable | Reverse both joystick channels configuration setting | 
| [JSTGY](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#jstgy) | Workspace variable | Reverse joystick Y-channel configuration setting | 
| [JSTK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#jstk) | Workspace variable | Keyboard or joystick configuration setting | 
| [JSTX](https://elite.bbcelite.com/c64/main/workspace/up.html#jstx) | Workspace variable | Our current roll rate | 
| [JSTY](https://elite.bbcelite.com/c64/main/workspace/up.html#jsty) | Workspace variable | Our current pitch rate | 
| [JUNK](https://elite.bbcelite.com/c64/main/workspace/up.html#junk) | Workspace variable | The amount of junk in the local bubble | 
| [K](https://elite.bbcelite.com/c64/main/workspace/zp.html#k) | Workspace variable | Temporary storage, used in a number of places | 
| [K%](https://elite.bbcelite.com/c64/main/workspace/k_per_cent.html) | Workspaces | Ship data blocks and ship line heaps | 
| [K2](https://elite.bbcelite.com/c64/main/workspace/zp.html#k2) | Workspace variable | Temporary storage, used in a number of places | 
| [K3](https://elite.bbcelite.com/c64/main/workspace/zp.html#k3) | Workspace variable | Temporary storage, used in a number of places | 
| [K4](https://elite.bbcelite.com/c64/main/workspace/zp.html#k4) | Workspace variable | Temporary storage, used in a number of places | 
| [K5](https://elite.bbcelite.com/c64/main/workspace/zp.html#k5) | Workspace variable | Temporary storage used to store segment coordinates across successive calls to BLINE, the ball line routine | 
| [K6](https://elite.bbcelite.com/c64/main/workspace/zp.html#k6) | Workspace variable | Temporary storage, typically used for storing coordinates during vector calculations | 
| [KERNALSETUP](https://elite.bbcelite.com/c64/main/subroutine/kernalsetup.html) | Save and load | Set up memory and interrupts so we can use the Kernal functions and configure the file system device number and filename | 
| [KEYLOOK](https://elite.bbcelite.com/c64/main/workspace/keylook.html) | Keyboard | The key logger | 
| [KILLSHP](https://elite.bbcelite.com/c64/main/subroutine/killshp.html) | Universe | Remove a ship from our local bubble of universe | 
| [KL](https://elite.bbcelite.com/c64/main/workspace/up.html#kl) | Workspace variable | If a key is being pressed that is not in the keyboard table at KYTB, it can be stored here (as seen in routine DK4, for example) | 
| [KLO](https://elite.bbcelite.com/c64/main/workspace/keylook.html#klo) | Workspace variable | The key logger in the BBC Micro version has a spare byte at the start for storing the last key press, so we also include a spare byte here so the KLO logger in the Commodore 64 version behaves in a similar way to the KL key logger in the BBC Micro | 
| [KS1](https://elite.bbcelite.com/c64/main/subroutine/ks1.html) | Universe | Remove the current ship from our local bubble of universe | 
| [KS2](https://elite.bbcelite.com/c64/main/subroutine/ks2.html) | Universe | Check the local bubble for missiles with target lock | 
| [KS3](https://elite.bbcelite.com/c64/main/subroutine/ks3.html) | Universe | Set the SLSP ship line heap pointer after shuffling ship slots | 
| [KS4](https://elite.bbcelite.com/c64/main/subroutine/ks4.html) | Universe | Remove the space station and replace it with the sun | 
| [KTRAN](https://elite.bbcelite.com/c64/main/variable/ktran.html) | Keyboard | An unused key logger buffer that's left over from the 6502 Second Processor version of Elite | 
| [KWH% (Game data)](https://elite.bbcelite.com/c64/game_data/variable/kwh_per_cent.html) | Status | Integer number of kills awarded for destroying each type of ship | 
| [KWL% (Game data)](https://elite.bbcelite.com/c64/game_data/variable/kwl_per_cent.html) | Status | Fractional number of kills awarded for destroying each type of ship | 
| [KY1](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky1) | Workspace variable | "?" is being pressed (slow down, KLO+$9) | 
| [KY12](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky12) | Workspace variable | "C=" is being pressed (energy bomb, KLO+$3) | 
| [KY13](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky13) | Workspace variable | Left arrow is being pressed (launch escape pod, KLO+$7) | 
| [KY14](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky14) | Workspace variable | "T" is being pressed (target missile, KLO+$2A) | 
| [KY15](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky15) | Workspace variable | "U" is being pressed (unarm missile, KLO+$22) | 
| [KY16](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky16) | Workspace variable | "M" is being pressed (fire missile, KLO+$1C) | 
| [KY17](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky17) | Workspace variable | "E" is being pressed (activate E.C.M., KLO+$32) | 
| [KY18](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky18) | Workspace variable | "J" is being pressed (in-system jump, KLO+$1E) | 
| [KY19](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky19) | Workspace variable | "C" is being pressed (activate docking computer, KLO+$2C) | 
| [KY2](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky2) | Workspace variable | Space is being pressed (speed up, KLO+$4) | 
| [KY20](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky20) | Workspace variable | "P" is being pressed (deactivate docking computer, KLO+$17) | 
| [KY3](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky3) | Workspace variable | "<" is being pressed (roll left, KYO+$11) | 
| [KY4](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky4) | Workspace variable | ">" is being pressed (roll right, KLO+$14) | 
| [KY5](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky5) | Workspace variable | "X" is being pressed (pull up, KLO+$29) | 
| [KY6](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky6) | Workspace variable | "S" is being pressed (pitch down, KLO+$33) | 
| [KY7](https://elite.bbcelite.com/c64/main/workspace/keylook.html#ky7) | Workspace variable | "A" is being pressed (fire lasers, KLO+$36) | 
| [KYTB](https://elite.bbcelite.com/c64/main/variable/kytb.html) | Keyboard | Lookup table for in-flight keyboard controls | 
| [L1M](https://elite.bbcelite.com/c64/main/variable/l1m.html) | Utility routines | Temporary storage for the new value of the 6510 input/output port register | 
| [LAS](https://elite.bbcelite.com/c64/main/workspace/zp.html#las) | Workspace variable | Contains the laser power of the laser fitted to the current space view (or 0 if there is no laser fitted to the current view) | 
| [LAS2](https://elite.bbcelite.com/c64/main/workspace/up.html#las2) | Workspace variable | Laser power for the current laser | 
| [LASCT](https://elite.bbcelite.com/c64/main/workspace/up.html#lasct) | Workspace variable | The laser pulse count for the current laser | 
| [LASER](https://elite.bbcelite.com/c64/main/workspace/up.html#laser) | Workspace variable | The specifications of the lasers fitted to each of the four space views | 
| [LASLI](https://elite.bbcelite.com/c64/main/subroutine/lasli.html) | Drawing lines | Draw the laser lines for when we fire our lasers | 
| [LASLI-1](https://elite.bbcelite.com/c64/main/subroutine/lasli.html) | Drawing lines | Contains an RTS | 
| [LASLI2](https://elite.bbcelite.com/c64/main/subroutine/lasli.html) | Drawing lines | Just draw the current laser lines without moving the centre point, draining energy or heating up. This has the effect of removing the lines from the screen | 
| [LASX](https://elite.bbcelite.com/c64/main/workspace/wp.html#lasx) | Workspace variable | The x-coordinate of the tip of the laser line | 
| [LASY](https://elite.bbcelite.com/c64/main/workspace/wp.html#lasy) | Workspace variable | The y-coordinate of the tip of the laser line | 
| [LAUN](https://elite.bbcelite.com/c64/main/subroutine/laun.html) | Drawing circles | Make the launch sound and draw the launch tunnel | 
| [LCASH](https://elite.bbcelite.com/c64/main/subroutine/lcash.html) | Maths (Arithmetic) | Subtract an amount of cash from the cash pot | 
| [LIJT1](https://elite.bbcelite.com/c64/main/variable/lijt1.html) | Drawing lines | Addresses for modifying the low byte of the JMP instruction at LI71 to support the unrolled algorithm in part 3 of LOIN | 
| [LIJT2](https://elite.bbcelite.com/c64/main/variable/lijt2.html) | Drawing lines | Addresses for modifying the high byte of the JMP instruction at LI71 to support the unrolled algorithm in part 3 of LOIN | 
| [LIJT3](https://elite.bbcelite.com/c64/main/variable/lijt3.html) | Drawing lines | Addresses for modifying the low byte of the JMP instruction at LI72 to support the unrolled algorithm in part 3 of LOIN | 
| [LIJT4](https://elite.bbcelite.com/c64/main/variable/lijt4.html) | Drawing lines | Addresses for modifying the high byte of the JMP instruction at LI72 to support the unrolled algorithm in part 3 of LOIN | 
| [LIJT5](https://elite.bbcelite.com/c64/main/variable/lijt5.html) | Drawing lines | Addresses for modifying the low byte of the JMP instruction at LI91 to support the unrolled algorithm in part 4 of LOIN | 
| [LIJT6](https://elite.bbcelite.com/c64/main/variable/lijt6.html) | Drawing lines | Addresses for modifying the high byte of the JMP instruction at LI91 to support the unrolled algorithm in part 4 of LOIN | 
| [LIJT7](https://elite.bbcelite.com/c64/main/variable/lijt7.html) | Drawing lines | Addresses for modifying the low byte of the JMP instruction at LI92 to support the unrolled algorithm in part 4 of LOIN | 
| [LIJT8](https://elite.bbcelite.com/c64/main/variable/lijt8.html) | Drawing lines | Addresses for modifying the high byte of the JMP instruction at LI92 to support the unrolled algorithm in part 4 of LOIN | 
| [LL10-1](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_2_of_12.html) | Drawing ships | Contains an RTS | 
| [LL118](https://elite.bbcelite.com/c64/main/subroutine/ll118.html) | Drawing lines | Move a point along a line until it is on-screen | 
| [LL118-1](https://elite.bbcelite.com/c64/main/subroutine/ll118.html) | Drawing lines | Contains an RTS | 
| [LL120](https://elite.bbcelite.com/c64/main/subroutine/ll120.html) | Maths (Arithmetic) | Calculate (Y X) = (S x1_lo) * XX12+2 or (S x1_lo) / XX12+2 | 
| [LL121](https://elite.bbcelite.com/c64/main/subroutine/ll123.html) | Maths (Arithmetic) | Calculate (Y X) = (S R) / Q and set the sign to the opposite of the top byte on the stack | 
| [LL122](https://elite.bbcelite.com/c64/main/subroutine/ll120.html) | Maths (Arithmetic) | Calculate (Y X) = (S R) * Q and set the sign to the opposite of the top byte on the stack | 
| [LL123](https://elite.bbcelite.com/c64/main/subroutine/ll123.html) | Maths (Arithmetic) | Calculate (Y X) = (S R) / XX12+2 or (S R) * XX12+2 | 
| [LL128](https://elite.bbcelite.com/c64/main/subroutine/ll123.html) | Maths (Arithmetic) | Contains an RTS | 
| [LL129](https://elite.bbcelite.com/c64/main/subroutine/ll129.html) | Maths (Arithmetic) | Calculate Q = XX12+2, A = S EOR XX12+3 and (S R) = |S R| | 
| [LL133](https://elite.bbcelite.com/c64/main/subroutine/ll123.html) | Maths (Arithmetic) | Negate (Y X) and return from the subroutine | 
| [LL145 (Part 1 of 4)](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_1_of_4.html) | Drawing lines | Clip line: Work out which end-points are on-screen, if any | 
| [LL145 (Part 2 of 4)](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_2_of_4.html) | Drawing lines | Clip line: Work out if any part of the line is on-screen | 
| [LL145 (Part 3 of 4)](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_3_of_4.html) | Drawing lines | Clip line: Calculate the line's gradient | 
| [LL145 (Part 4 of 4)](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_4_of_4.html) | Drawing lines | Clip line: Call the routine in LL188 to do the actual clipping | 
| [LL147](https://elite.bbcelite.com/c64/main/subroutine/ll145_part_1_of_4.html) | Drawing lines | Don't initialise the values in SWAP or A | 
| [LL164](https://elite.bbcelite.com/c64/main/subroutine/ll164.html) | Drawing circles | Make the hyperspace sound and draw the hyperspace tunnel | 
| [LL28](https://elite.bbcelite.com/c64/main/subroutine/ll28.html) | Maths (Arithmetic) | Calculate R = 256 * A / Q | 
| [LL28+4](https://elite.bbcelite.com/c64/main/subroutine/ll28.html) | Maths (Arithmetic) | Skips the A >= Q check and always returns with C flag cleared, so this can be called if we know the division will work | 
| [LL30](https://elite.bbcelite.com/c64/main/subroutine/loin_part_1_of_7.html) | Drawing lines | LL30 is a synonym for LOIN and draws a line from (X1, Y1) to (X2, Y2) | 
| [LL31](https://elite.bbcelite.com/c64/main/subroutine/ll28.html) | Maths (Arithmetic) | Skips the A >= Q check and does not set the R counter, so this can be used for jumping straight into the division loop if R is already set to 254 and we know the division will work | 
| [LL38](https://elite.bbcelite.com/c64/main/subroutine/ll38.html) | Maths (Arithmetic) | Calculate (S A) = (S R) + (A Q) | 
| [LL5](https://elite.bbcelite.com/c64/main/subroutine/ll5.html) | Maths (Arithmetic) | Calculate Q = SQRT(R Q) | 
| [LL51](https://elite.bbcelite.com/c64/main/subroutine/ll51.html) | Maths (Geometry) | Calculate the dot product of XX15 and XX16 | 
| [LL61](https://elite.bbcelite.com/c64/main/subroutine/ll61.html) | Maths (Arithmetic) | Calculate (U R) = 256 * A / Q | 
| [LL62](https://elite.bbcelite.com/c64/main/subroutine/ll62.html) | Maths (Arithmetic) | Calculate 128 - (U R) | 
| [LL66](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_8_of_12.html) | Drawing ships | A re-entry point into the ship-drawing routine, used by the LL62 routine to store 128 - (U R) on the XX3 heap | 
| [LL70+1](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_8_of_12.html) | Drawing ships | Contains an RTS (as the first byte of an LDA instruction) | 
| [LL81+2](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_11_of_12.html) | Drawing ships | Draw the contents of the ship line heap, used to draw the ship as a dot from SHPPT | 
| [LL9 (Part 1 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_1_of_12.html) | Drawing ships | Draw ship: Check if ship is exploding, check if ship is in front | 
| [LL9 (Part 2 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_2_of_12.html) | Drawing ships | Draw ship: Check if ship is in field of view, close enough to draw | 
| [LL9 (Part 3 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_3_of_12.html) | Drawing ships | Draw ship: Set up orientation vector, ship coordinate variables | 
| [LL9 (Part 4 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_4_of_12.html) | Drawing ships | Draw ship: Set visibility for exploding ship (all faces visible) | 
| [LL9 (Part 5 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_5_of_12.html) | Drawing ships | Draw ship: Calculate the visibility of each of the ship's faces | 
| [LL9 (Part 6 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_6_of_12.html) | Drawing ships | Draw ship: Calculate the visibility of each of the ship's vertices | 
| [LL9 (Part 7 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_7_of_12.html) | Drawing ships | Draw ship: Calculate the visibility of each of the ship's vertices | 
| [LL9 (Part 8 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_8_of_12.html) | Drawing ships | Draw ship: Calculate the screen coordinates of visible vertices | 
| [LL9 (Part 9 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_9_of_12.html) | Drawing ships | Draw ship: Draw laser beams if the ship is firing its laser at us | 
| [LL9 (Part 10 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_10_of_12.html) | Drawing ships | Draw ship: Calculate the visibility of each of the ship's edges | 
| [LL9 (Part 11 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_11_of_12.html) | Drawing ships | Draw ship: Add all visible edges to the ship line heap | 
| [LL9 (Part 12 of 12)](https://elite.bbcelite.com/c64/main/subroutine/ll9_part_12_of_12.html) | Drawing ships | Draw ship: Draw all the visible edges from the ship line heap | 
| [LO2](https://elite.bbcelite.com/c64/main/subroutine/look1.html) | Flight | Contains an RTS | 
| [load3 (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/elite_gma_loader_part_3_of_4.html) | Loader | Jump to the entry point in elite-loader | 
| [loaderScreens (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/loaderscreens.html) | Loader | PETSCII codes for clearing the screen and displaying the fast loader prompt and loading screens | 
| [LoadGMAFile (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/loadgmafile.html) | Loader | Load a specific GMA file | 
| [LOD](https://elite.bbcelite.com/c64/main/subroutine/lod.html) | Save and load | Load a commander file | 
| [LODATA (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/lodata.html) | Loader | The binaries for recursive tokens and the game font | 
| [log](https://elite.bbcelite.com/c64/main/variable/log.html) | Maths (Arithmetic) | Binary logarithm table (high byte) | 
| [logL](https://elite.bbcelite.com/c64/main/variable/logl.html) | Maths (Arithmetic) | Binary logarithm table (low byte) | 
| [LOIN (Part 1 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_1_of_7.html) | Drawing lines | Draw a line: Calculate the line gradient in the form of deltas | 
| [LOIN (Part 2 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_2_of_7.html) | Drawing lines | Draw a line: Line has a shallow gradient, step right along x-axis | 
| [LOIN (Part 3 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_3_of_7.html) | Drawing lines | Draw a shallow line going right and up or left and down | 
| [LOIN (Part 4 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_4_of_7.html) | Drawing lines | Draw a shallow line going right and down or left and up | 
| [LOIN (Part 5 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_5_of_7.html) | Drawing lines | Draw a line: Line has a steep gradient, step up along y-axis | 
| [LOIN (Part 6 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_6_of_7.html) | Drawing lines | Draw a steep line going up and left or down and right | 
| [LOIN (Part 7 of 7)](https://elite.bbcelite.com/c64/main/subroutine/loin_part_7_of_7.html) | Drawing lines | Draw a steep line going up and right or down and left | 
| [LOOK1](https://elite.bbcelite.com/c64/main/subroutine/look1.html) | Flight | Initialise the space view | 
| [LOR](https://elite.bbcelite.com/c64/main/subroutine/lod.html) | Save and load | Set the C flag and return from the subroutine | 
| [lotus](https://elite.bbcelite.com/c64/main/variable/lotus.html) | Drawing the screen | The colour of the explosion sprite in the upper and lower parts of the screen | 
| [LSO](https://elite.bbcelite.com/c64/main/workspace/wp.html#lso) | Workspace variable | The ship line heap for the space station (see NWSPS) and the sun line heap (see SUN) | 
| [LSP](https://elite.bbcelite.com/c64/main/workspace/zp.html#lsp) | Workspace variable | The ball line heap pointer, which contains the number of the first free byte after the end of the LSX2 and LSY2 heaps | 
| [LSX](https://elite.bbcelite.com/c64/main/workspace/wp.html#lsx) | Workspace variable | LSX is an alias that points to the first byte of the sun line heap at LSO | 
| [LSX2](https://elite.bbcelite.com/c64/main/variable/lsx2.html) | Drawing lines | The ball line heap for storing x-coordinates | 
| [LSY2](https://elite.bbcelite.com/c64/main/variable/lsy2.html) | Drawing lines | The ball line heap for storing y-coordinates | 
| [m](https://elite.bbcelite.com/c64/main/subroutine/mas2.html) | Maths (Geometry) | Do not include A in the calculation | 
| [M%](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_1_of_16.html) | Main loop | The entry point for the main flight loop | 
| [MA9](https://elite.bbcelite.com/c64/main/subroutine/mas1.html) | Maths (Geometry) | Contains an RTS | 
| [MAD](https://elite.bbcelite.com/c64/main/subroutine/mad.html) | Maths (Arithmetic) | Calculate (A X) = Q * A + (S R) | 
| [Main flight loop (Part 1 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_1_of_16.html) | Main loop | Seed the random number generator | 
| [Main flight loop (Part 2 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_2_of_16.html) | Main loop | Calculate the alpha and beta angles from the current pitch and roll of our ship | 
| [Main flight loop (Part 3 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_3_of_16.html) | Main loop | Scan for flight keys and process the results | 
| [Main flight loop (Part 4 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_4_of_16.html) | Main loop | For each nearby ship: Copy the ship's data block from K% to the zero-page workspace at INWK | 
| [Main flight loop (Part 5 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_5_of_16.html) | Main loop | For each nearby ship: If an energy bomb has been set off, potentially kill this ship | 
| [Main flight loop (Part 6 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_6_of_16.html) | Main loop | For each nearby ship: Move the ship in space and copy the updated INWK data block back to K% | 
| [Main flight loop (Part 7 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_7_of_16.html) | Main loop | For each nearby ship: Check whether we are docking, scooping or colliding with it | 
| [Main flight loop (Part 8 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_8_of_16.html) | Main loop | For each nearby ship: Process us potentially scooping this item | 
| [Main flight loop (Part 9 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_9_of_16.html) | Main loop | For each nearby ship: If it is a space station, check whether we are successfully docking with it | 
| [Main flight loop (Part 10 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_10_of_16.html) | Main loop | For each nearby ship: Remove if scooped, or process collisions | 
| [Main flight loop (Part 11 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_11_of_16.html) | Main loop | For each nearby ship: Process missile lock and firing our laser | 
| [Main flight loop (Part 12 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_12_of_16.html) | Main loop | For each nearby ship: Draw the ship, remove if killed, loop back | 
| [Main flight loop (Part 13 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_13_of_16.html) | Main loop | Show energy bomb effect, charge shields and energy banks | 
| [Main flight loop (Part 14 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_14_of_16.html) | Main loop | Spawn a space station if we are close enough to the planet | 
| [Main flight loop (Part 15 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_15_of_16.html) | Main loop | Perform altitude checks with the planet and sun and process fuel scooping if appropriate | 
| [Main flight loop (Part 16 of 16)](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_16_of_16.html) | Main loop | Process laser pulsing, E.C.M. energy drain, call stardust routine | 
| [Main game loop (Part 1 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_1_of_6.html) | Main loop | Spawn a trader (a Cobra Mk III, Python, Boa or Anaconda) | 
| [Main game loop (Part 2 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_2_of_6.html) | Main loop | Call the main flight loop, and potentially spawn a trader, an asteroid, or a cargo canister | 
| [Main game loop (Part 3 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_3_of_6.html) | Main loop | Potentially spawn a cop, particularly if we've been bad | 
| [Main game loop (Part 4 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_4_of_6.html) | Main loop | Potentially spawn a lone bounty hunter, a Thargoid, or up to four pirates | 
| [Main game loop (Part 5 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_5_of_6.html) | Main loop | Cool down lasers, make calls to update the dashboard | 
| [Main game loop (Part 6 of 6)](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_6_of_6.html) | Main loop | Process non-flight key presses (docked keys) | 
| [MAL1](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_4_of_16.html) | Main loop | Marks the beginning of the ship analysis loop, so we can jump back here from part 12 of the main flight loop to work our way through each ship in the local bubble. We also jump back here when a ship is removed from the bubble, so we can continue processing from the next ship | 
| [MANY](https://elite.bbcelite.com/c64/main/workspace/up.html#many) | Workspace variable | The number of ships of each type in the local bubble of universe | 
| [MAS1](https://elite.bbcelite.com/c64/main/subroutine/mas1.html) | Maths (Geometry) | Add an orientation vector coordinate to an INWK coordinate | 
| [MAS2](https://elite.bbcelite.com/c64/main/subroutine/mas2.html) | Maths (Geometry) | Calculate a cap on the maximum distance to the planet or sun | 
| [MAS3](https://elite.bbcelite.com/c64/main/subroutine/mas3.html) | Maths (Arithmetic) | Calculate A = x_hi^2 + y_hi^2 + z_hi^2 in the K% block | 
| [MAS4](https://elite.bbcelite.com/c64/main/subroutine/mas4.html) | Maths (Geometry) | Calculate a cap on the maximum distance to a ship | 
| [MCASH](https://elite.bbcelite.com/c64/main/subroutine/mcash.html) | Maths (Arithmetic) | Add an amount of cash to the cash pot | 
| [MCH](https://elite.bbcelite.com/c64/main/workspace/up.html#mch) | Workspace variable | The text token number of the in-flight message that is currently being shown, and which will be removed by the me2 routine when the counter in DLY reaches zero | 
| [MCNT](https://elite.bbcelite.com/c64/main/workspace/zp.html#mcnt) | Workspace variable | The main loop counter | 
| [me1](https://elite.bbcelite.com/c64/main/subroutine/me1.html) | Flight | Erase an old in-flight message and display a new one | 
| [me2](https://elite.bbcelite.com/c64/main/subroutine/me2.html) | Flight | Remove an in-flight message from the space view | 
| [me3](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_2_of_6.html) | Main loop | Used by me2 to jump back into the main game loop after printing an in-flight message | 
| [mes9](https://elite.bbcelite.com/c64/main/subroutine/mes9.html) | Flight | Print a text token, possibly followed by " DESTROYED" | 
| [MESS](https://elite.bbcelite.com/c64/main/subroutine/mess.html) | Flight | Display an in-flight message | 
| [messXC](https://elite.bbcelite.com/c64/main/workspace/zp.html#messxc) | Workspace variable | Temporary storage, used to store the text column of the in-flight message in MESS, so it can be erased from the screen at the correct time | 
| [MJ](https://elite.bbcelite.com/c64/main/workspace/up.html#mj) | Workspace variable | Are we in witchspace (i.e. have we mis-jumped)? | 
| [MJP](https://elite.bbcelite.com/c64/main/subroutine/mjp.html) | Flight | Process a mis-jump into witchspace | 
| [MLOOP](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_5_of_6.html) | Main loop | The entry point for the main game loop. This entry point comes after the call to the main flight loop and spawning routines, so it marks the start of the main game loop for when we are docked (as we don't need to call the main flight loop or spawning routines if we aren't in space) | 
| [MLS1](https://elite.bbcelite.com/c64/main/subroutine/mls1.html) | Maths (Arithmetic) | Calculate (A P) = ALP1 * A | 
| [MLS2](https://elite.bbcelite.com/c64/main/subroutine/mls2.html) | Maths (Arithmetic) | Calculate (S R) = XX(1 0) and (A P) = A * ALP1 | 
| [MLTU2](https://elite.bbcelite.com/c64/main/subroutine/mltu2.html) | Maths (Arithmetic) | Calculate (A P+1 P) = (A ~P) * Q | 
| [MLTU2-2](https://elite.bbcelite.com/c64/main/subroutine/mltu2.html) | Maths (Arithmetic) | Set Q to X, so this calculates (A P+1 P) = (A ~P) * X | 
| [MLU1](https://elite.bbcelite.com/c64/main/subroutine/mlu1.html) | Maths (Arithmetic) | Calculate Y1 = y_hi and (A P) = |y_hi| * Q for Y-th stardust | 
| [MLU2](https://elite.bbcelite.com/c64/main/subroutine/mlu2.html) | Maths (Arithmetic) | Calculate (A P) = |A| * Q | 
| [moonflower](https://elite.bbcelite.com/c64/main/variable/moonflower.html) | Drawing the screen | Controls the energy bomb effect by switching between multicolour and standard mode | 
| [MOS](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mos) | Workspace variable | This variable appears to be unused | 
| [MSAR](https://elite.bbcelite.com/c64/main/workspace/up.html#msar) | Workspace variable | The targeting state of our leftmost missile | 
| [MSBAR](https://elite.bbcelite.com/c64/main/subroutine/msbar.html) | Dashboard | Draw a specific indicator in the dashboard's missile bar | 
| [msblob](https://elite.bbcelite.com/c64/main/subroutine/msblob.html) | Dashboard | Display the dashboard's missile indicators in green | 
| [MSTG](https://elite.bbcelite.com/c64/main/workspace/zp.html#mstg) | Workspace variable | The current missile lock target | 
| [MT1](https://elite.bbcelite.com/c64/main/subroutine/mt1.html) | Text | Switch to ALL CAPS when printing extended tokens | 
| [MT13](https://elite.bbcelite.com/c64/main/subroutine/mt13.html) | Text | Switch to lower case when printing extended tokens | 
| [MT14](https://elite.bbcelite.com/c64/main/subroutine/mt14.html) | Text | Switch to justified text when printing extended tokens | 
| [MT15](https://elite.bbcelite.com/c64/main/subroutine/mt15.html) | Text | Switch to left-aligned text when printing extended tokens | 
| [MT16](https://elite.bbcelite.com/c64/main/subroutine/mt16.html) | Text | Print the character in variable DTW7 | 
| [MT17](https://elite.bbcelite.com/c64/main/subroutine/mt17.html) | Text | Print the selected system's adjective, e.g. Lavian for Lave | 
| [MT18](https://elite.bbcelite.com/c64/main/subroutine/mt18.html) | Text | Print a random 1-8 letter word in Sentence Case | 
| [MT19](https://elite.bbcelite.com/c64/main/subroutine/mt19.html) | Text | Capitalise the next letter | 
| [MT2](https://elite.bbcelite.com/c64/main/subroutine/mt2.html) | Text | Switch to Sentence Case when printing extended tokens | 
| [MT23](https://elite.bbcelite.com/c64/main/subroutine/mt23.html) | Text | Move to row 10, switch to white text, and switch to lower case when printing extended tokens | 
| [MT26](https://elite.bbcelite.com/c64/main/subroutine/mt26.html) | Text | Fetch a line of text from the keyboard | 
| [MT27](https://elite.bbcelite.com/c64/main/subroutine/mt27.html) | Text | Print the captain's name during mission briefings | 
| [MT28](https://elite.bbcelite.com/c64/main/subroutine/mt28.html) | Text | Print the location hint during the mission 1 briefing | 
| [MT29](https://elite.bbcelite.com/c64/main/subroutine/mt29.html) | Text | Move to row 6 and switch to lower case when printing extended tokens | 
| [MT5](https://elite.bbcelite.com/c64/main/subroutine/mt5.html) | Text | Switch to extended tokens | 
| [MT6](https://elite.bbcelite.com/c64/main/subroutine/mt6.html) | Text | Switch to standard tokens in Sentence Case | 
| [MT8](https://elite.bbcelite.com/c64/main/subroutine/mt8.html) | Text | Tab to column 6 and start a new word when printing extended tokens | 
| [MT9](https://elite.bbcelite.com/c64/main/subroutine/mt9.html) | Text | Clear the screen and set the current view type to 1 | 
| [MTIN](https://elite.bbcelite.com/c64/main/variable/mtin.html) | Text | Lookup table for random tokens in the extended token table (0-37) | 
| [MU1](https://elite.bbcelite.com/c64/main/subroutine/mu1.html) | Maths (Arithmetic) | Copy X into P and A, and clear the C flag | 
| [MU11](https://elite.bbcelite.com/c64/main/subroutine/mu11.html) | Maths (Arithmetic) | Calculate (A P) = P * X | 
| [MU5](https://elite.bbcelite.com/c64/main/subroutine/mu5.html) | Maths (Arithmetic) | Set K(3 2 1 0) = (A A A A) and clear the C flag | 
| [MU6](https://elite.bbcelite.com/c64/main/subroutine/mu6.html) | Maths (Arithmetic) | Set P(1 0) = (A A) | 
| [MUDOCK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mudock) | Workspace variable | Docking music tune configuration setting | 
| [MUFOR](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mufor) | Workspace variable | Configuration setting that controls whether the docking music can be enabled or disabled | 
| [MULIE](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mulie) | Workspace variable | A flag to record whether the RESET routine is being being called from within the TITLE routine, when the title screen is being displayed, as we don't want to stop the title music from playing when this is the case | 
| [MULT1](https://elite.bbcelite.com/c64/main/subroutine/mult1.html) | Maths (Arithmetic) | Calculate (A P) = Q * A | 
| [MULT12](https://elite.bbcelite.com/c64/main/subroutine/mult12.html) | Maths (Arithmetic) | Calculate (S R) = Q * A | 
| [MULT3](https://elite.bbcelite.com/c64/main/subroutine/mult3.html) | Maths (Arithmetic) | Calculate K(3 2 1 0) = (A P+1 P) * Q | 
| [MULTS-2](https://elite.bbcelite.com/c64/main/subroutine/mls1.html) | Maths (Arithmetic) | Calculate (A P) = X * A | 
| [MULTU](https://elite.bbcelite.com/c64/main/subroutine/multu.html) | Maths (Arithmetic) | Calculate (A P) = P * Q | 
| [MUPLA](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mupla) | Workspace variable | A flag to record whether any music is currently playing | 
| [Music variables](https://elite.bbcelite.com/c64/main/workspace/music_variables.html) | Sound | Variables that are used by the music player | 
| [MUSILLY](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#musilly) | Workspace variable | Sounds during music configuration setting | 
| [MUT1](https://elite.bbcelite.com/c64/main/subroutine/mut1.html) | Maths (Arithmetic) | Calculate R = XX and (A P) = Q * A | 
| [MUT2](https://elite.bbcelite.com/c64/main/subroutine/mut2.html) | Maths (Arithmetic) | Calculate (S R) = XX(1 0) and (A P) = Q * A | 
| [MUT3](https://elite.bbcelite.com/c64/main/subroutine/mut3.html) | Maths (Arithmetic) | An unused routine that does the same as MUT2 | 
| [MUTOK](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mutok) | Workspace variable | Docking music configuration setting | 
| [MUTOKCH](https://elite.bbcelite.com/c64/main/subroutine/mutokch.html) | Sound | Process a change in the docking music configuration setting | 
| [MUTOKOLD](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#mutokold) | Workspace variable | Used to store the previous value of MUTOK, so we can track whether the docking music configuration changes | 
| [MV40](https://elite.bbcelite.com/c64/main/subroutine/mv40.html) | Moving | Rotate the planet or sun's location in space by the amount of pitch and roll of our ship | 
| [MV45](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_6_of_9.html) | Moving | Rejoin the MVEIT routine after the rotation, tactics and scanner code | 
| [mvbllop](https://elite.bbcelite.com/c64/main/subroutine/mvblockk.html) | Utility routines | Only copy Y bytes, rather than a whole page | 
| [mvblock (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/mvblock.html) | Loader | Copy a number of pages in memory | 
| [mvblockK](https://elite.bbcelite.com/c64/main/subroutine/mvblockk.html) | Utility routines | Copy a specific number of pages in memory | 
| [MVEIT (Part 1 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_1_of_9.html) | Moving | Move current ship: Tidy the orientation vectors | 
| [MVEIT (Part 2 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_2_of_9.html) | Moving | Move current ship: Call tactics routine, remove ship from scanner | 
| [MVEIT (Part 3 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_3_of_9.html) | Moving | Move current ship: Move ship forward according to its speed | 
| [MVEIT (Part 4 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_4_of_9.html) | Moving | Move current ship: Apply acceleration to ship's speed as a one-off | 
| [MVEIT (Part 5 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_5_of_9.html) | Moving | Move current ship: Rotate ship's location by our pitch and roll | 
| [MVEIT (Part 6 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_6_of_9.html) | Moving | Move current ship: Move the ship in space according to our speed | 
| [MVEIT (Part 7 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_7_of_9.html) | Moving | Move current ship: Rotate ship's orientation vectors by pitch/roll | 
| [MVEIT (Part 8 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_8_of_9.html) | Moving | Move current ship: Rotate ship about itself by its own pitch/roll | 
| [MVEIT (Part 9 of 9)](https://elite.bbcelite.com/c64/main/subroutine/mveit_part_9_of_9.html) | Moving | Move current ship: Redraw on scanner, if it hasn't been destroyed | 
| [MVS4](https://elite.bbcelite.com/c64/main/subroutine/mvs4.html) | Moving | Apply pitch and roll to an orientation vector | 
| [MVS5](https://elite.bbcelite.com/c64/main/subroutine/mvs5.html) | Moving | Apply a 3.6 degree pitch or roll to an orientation vector | 
| [mvsm (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/mvsm.html) | Loader | Copy 280 bytes in memory | 
| [MVT1](https://elite.bbcelite.com/c64/main/subroutine/mvt1.html) | Moving | Calculate (x_sign x_hi x_lo) = (x_sign x_hi x_lo) + (A R) | 
| [MVT1-2](https://elite.bbcelite.com/c64/main/subroutine/mvt1.html) | Moving | Clear bits 0-6 of A before entering MVT1 | 
| [MVT3](https://elite.bbcelite.com/c64/main/subroutine/mvt3.html) | Moving | Calculate K(3 2 1) = (x_sign x_hi x_lo) + K(3 2 1) | 
| [MVT6](https://elite.bbcelite.com/c64/main/subroutine/mvt6.html) | Moving | Calculate (A P+2 P+1) = (x_sign x_hi x_lo) + (A P+2 P+1) | 
| [MVTRIBS](https://elite.bbcelite.com/c64/main/subroutine/mvtribs.html) | Missions | Move the Trumble sprites around on-screen | 
| [NA%](https://elite.bbcelite.com/c64/main/variable/na_per_cent.html) | Save and load | The data block for the last saved commander | 
| [NA2%](https://elite.bbcelite.com/c64/main/variable/na2_per_cent.html) | Save and load | The data block for the default commander | 
| [NAME](https://elite.bbcelite.com/c64/main/workspace/up.html#name) | Workspace variable | The current commander name | 
| [NEWB](https://elite.bbcelite.com/c64/main/workspace/zp.html#newb) | Workspace variable | The ship's "new byte flags" (or NEWB flags) | 
| [newosrdch](https://elite.bbcelite.com/c64/main/subroutine/newosrdch.html) | Tube | The custom OSRDCH routine for reading characters | 
| [newzp](https://elite.bbcelite.com/c64/main/workspace/zp.html#newzp) | Workspace variable | This is used by the STARS2 routine for storing the stardust particle's delta_x value | 
| [NLIN](https://elite.bbcelite.com/c64/main/subroutine/nlin.html) | Drawing lines | Draw a horizontal line at pixel row 23 to box in a title | 
| [NLIN2](https://elite.bbcelite.com/c64/main/subroutine/nlin2.html) | Drawing lines | Draw a screen-wide horizontal line at the pixel row in A | 
| [NLIN3](https://elite.bbcelite.com/c64/main/subroutine/nlin3.html) | Drawing lines | Print a title and draw a horizontal line at row 19 to box it in | 
| [NLIN4](https://elite.bbcelite.com/c64/main/subroutine/nlin4.html) | Drawing lines | Draw a horizontal line at pixel row 19 to box in a title | 
| [NMIpissoff](https://elite.bbcelite.com/c64/main/subroutine/nmipissoff.html) | Loader | Acknowledge NMI interrupts and ignore them | 
| [NO1](https://elite.bbcelite.com/c64/main/subroutine/norm.html) | Maths (Geometry) | Contains an RTS | 
| [NOISE](https://elite.bbcelite.com/c64/main/subroutine/noise.html) | Sound | Make the sound whose number is in Y | 
| [NOISE2](https://elite.bbcelite.com/c64/main/subroutine/noise2.html) | Sound | Make a sound effect with a specific volume and release length | 
| [NOISEOFF](https://elite.bbcelite.com/c64/main/subroutine/noiseoff.html) | Sound | Turn off a specific sound effect in whichever voice it is currently playing in | 
| [NOMSL](https://elite.bbcelite.com/c64/main/workspace/up.html#nomsl) | Workspace variable | The number of missiles we have fitted (0-4) | 
| [NOMVETR](https://elite.bbcelite.com/c64/main/subroutine/main_flight_loop_part_1_of_16.html) | Main loop | The re-entry point in the main game loop for when there are no sprites to move | 
| [NORM](https://elite.bbcelite.com/c64/main/subroutine/norm.html) | Maths (Geometry) | Normalise the three-coordinate vector in XX15 | 
| [NOSPRITES](https://elite.bbcelite.com/c64/main/subroutine/nosprites.html) | Missions | Disable all sprites and remove them from the screen | 
| [NOSTM](https://elite.bbcelite.com/c64/main/workspace/up.html#nostm) | Workspace variable | The number of stardust particles shown on screen, which is 12 (#NOST) for normal space, and 3 for witchspace | 
| [NWDAV4](https://elite.bbcelite.com/c64/main/subroutine/nwdav4.html) | Market | Print an "ITEM?" error, make a beep and rejoin the TT210 routine | 
| [NWDAVxx](https://elite.bbcelite.com/c64/main/subroutine/tt210.html) | Market | Used to rejoin this routine from the call to NWDAV4 | 
| [nWq](https://elite.bbcelite.com/c64/main/subroutine/nwq.html) | Stardust | Create a random cloud of stardust | 
| [NwS1](https://elite.bbcelite.com/c64/main/subroutine/nws1.html) | Universe | Flip the sign and double an INWK byte | 
| [NWSHP](https://elite.bbcelite.com/c64/main/subroutine/nwshp.html) | Universe | Add a new ship to our local bubble of universe | 
| [NWSPS](https://elite.bbcelite.com/c64/main/subroutine/nwsps.html) | Universe | Add a new space station to our local bubble of universe | 
| [NWSTARS](https://elite.bbcelite.com/c64/main/subroutine/nwstars.html) | Stardust | Initialise the stardust field | 
| [OfferFastLoader (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/offerfastloader.html) | Loader | Offer the option of using the fast loader, if we haven't already, and set up the fast loader if it is chosen | 
| [oh](https://elite.bbcelite.com/c64/main/subroutine/spin.html) | Universe | Contains an RTS | 
| [oldlong](https://elite.bbcelite.com/c64/main/variable/oldlong.html) | Save and load | Contains the length of the last saved commander name | 
| [OOPS](https://elite.bbcelite.com/c64/main/subroutine/oops.html) | Flight | Take some damage | 
| [Option variables](https://elite.bbcelite.com/c64/main/workspace/option_variables.html) | Workspaces | Variables that are predominantly used to store the game options | 
| [OTHERFILEPR](https://elite.bbcelite.com/c64/main/subroutine/otherfilepr.html) | Save and load | Display the non-selected media (disk or tape) | 
| [ou2](https://elite.bbcelite.com/c64/main/subroutine/ou2.html) | Flight | Display "E.C.M.SYSTEM DESTROYED" as an in-flight message | 
| [ou3](https://elite.bbcelite.com/c64/main/subroutine/ou3.html) | Flight | Display "FUEL SCOOPS DESTROYED" as an in-flight message | 
| [OUCH](https://elite.bbcelite.com/c64/main/subroutine/ouch.html) | Flight | Potentially lose cargo or equipment following damage | 
| [out](https://elite.bbcelite.com/c64/main/subroutine/tt217.html) | Keyboard | Contains an RTS | 
| [P](https://elite.bbcelite.com/c64/main/workspace/zp.html#p) | Workspace variable | Temporary storage, used in a number of places | 
| [P2](https://elite.bbcelite.com/c64/main/workspace/zp.html#p2) | Workspace variable | Temporary storage, used in place of variable P in the line-drawing routines | 
| [PAS1](https://elite.bbcelite.com/c64/main/subroutine/pas1.html) | Missions | Display a rotating ship at space coordinates (0, conhieght, 256) and scan the keyboard | 
| [PATG](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#patg) | Workspace variable | Configuration setting to show the author names on the start-up screen and enable manual hyperspace mis-jumps | 
| [PAUSE](https://elite.bbcelite.com/c64/main/subroutine/pause.html) | Missions | Display a rotating ship, waiting until a key is pressed, then remove the ship from the screen | 
| [PAUSE2](https://elite.bbcelite.com/c64/main/subroutine/pause2.html) | Keyboard | Wait until a key is pressed, ignoring any existing key press | 
| [PDESC](https://elite.bbcelite.com/c64/main/subroutine/pdesc.html) | Universe | Print the system's extended description or a mission 1 directive | 
| [ping](https://elite.bbcelite.com/c64/main/subroutine/ping.html) | Universe | Set the selected system to the current system | 
| [PIX1](https://elite.bbcelite.com/c64/main/subroutine/pix1.html) | Maths (Arithmetic) | Calculate (YY+1 SYL+Y) = (A P) + (S R) and draw stardust particle | 
| [PIXEL](https://elite.bbcelite.com/c64/main/subroutine/pixel.html) | Drawing pixels | Draw a one-pixel dot, two-pixel dash or four-pixel square | 
| [PIXEL2](https://elite.bbcelite.com/c64/main/subroutine/pixel2.html) | Drawing pixels | Draw a stardust particle relative to the screen centre | 
| [PL2](https://elite.bbcelite.com/c64/main/subroutine/pl2.html) | Drawing planets | Remove the planet or sun from the screen | 
| [PL2-1](https://elite.bbcelite.com/c64/main/subroutine/pl2.html) | Drawing planets | Contains an RTS | 
| [PL21](https://elite.bbcelite.com/c64/main/subroutine/pl21.html) | Drawing planets | Return from a planet/sun-drawing routine with a failure flag | 
| [PL44](https://elite.bbcelite.com/c64/main/subroutine/pls6.html) | Drawing planets | Clear the C flag and return from the subroutine | 
| [PL6](https://elite.bbcelite.com/c64/main/subroutine/pls6.html) | Drawing planets | Contains an RTS | 
| [PL9 (Part 1 of 3)](https://elite.bbcelite.com/c64/main/subroutine/pl9_part_1_of_3.html) | Drawing planets | Draw the planet, with either an equator and meridian, or a crater | 
| [PL9 (Part 2 of 3)](https://elite.bbcelite.com/c64/main/subroutine/pl9_part_2_of_3.html) | Drawing planets | Draw the planet's equator and meridian | 
| [PL9 (Part 3 of 3)](https://elite.bbcelite.com/c64/main/subroutine/pl9_part_3_of_3.html) | Drawing planets | Draw the planet's crater | 
| [PLANET](https://elite.bbcelite.com/c64/main/subroutine/planet.html) | Drawing planets | Draw the planet or sun | 
| [plf](https://elite.bbcelite.com/c64/main/subroutine/plf.html) | Text | Print a text token followed by a newline | 
| [plf2](https://elite.bbcelite.com/c64/main/subroutine/plf2.html) | Text | Print text followed by a newline and indent of 6 characters | 
| [PLS1](https://elite.bbcelite.com/c64/main/subroutine/pls1.html) | Drawing planets | Calculate (Y A) = nosev_x / z | 
| [PLS2](https://elite.bbcelite.com/c64/main/subroutine/pls2.html) | Drawing planets | Draw a half-ellipse | 
| [PLS22](https://elite.bbcelite.com/c64/main/subroutine/pls22.html) | Drawing planets | Draw an ellipse or half-ellipse | 
| [PLS3](https://elite.bbcelite.com/c64/main/subroutine/pls3.html) | Drawing planets | Calculate (Y A P) = 222 * roofv_x / z | 
| [PLS4](https://elite.bbcelite.com/c64/main/subroutine/pls4.html) | Drawing planets | Calculate CNT2 = arctan(P / A) / 4 | 
| [PLS5](https://elite.bbcelite.com/c64/main/subroutine/pls5.html) | Drawing planets | Calculate roofv_x / z and roofv_y / z | 
| [PLS6](https://elite.bbcelite.com/c64/main/subroutine/pls6.html) | Drawing planets | Calculate (X K) = (A P+1 P) / (z_sign z_hi z_lo) | 
| [PLTOG](https://elite.bbcelite.com/c64/main/workspace/option_variables.html#pltog) | Workspace variable | Planetary details configuration setting | 
| [PLUT](https://elite.bbcelite.com/c64/main/subroutine/plut.html) | Flight | Flip the coordinate axes for the four different views | 
| [pr2](https://elite.bbcelite.com/c64/main/subroutine/pr2.html) | Text | Print an 8-bit number, left-padded to 3 digits, and optional point | 
| [pr2+2](https://elite.bbcelite.com/c64/main/subroutine/pr2.html) | Text | Print the 8-bit number in X to the number of digits in A | 
| [pr5](https://elite.bbcelite.com/c64/main/subroutine/pr5.html) | Text | Print a 16-bit number, left-padded to 5 digits, and optional point | 
| [pr6](https://elite.bbcelite.com/c64/main/subroutine/pr6.html) | Text | Print 16-bit number, left-padded to 5 digits, no point | 
| [pres](https://elite.bbcelite.com/c64/main/subroutine/eqshp.html) | Equipment | Given an item number A with the item name in recursive token Y, show an error to say that the item is already present, refund the cost of the item, and then beep and exit to the docking bay (i.e. show the Status Mode screen) | 
| [PrintString (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/printstring.html) | Loader | Print the null-terminated string at offset X in loaderScreens | 
| [PROJ](https://elite.bbcelite.com/c64/main/subroutine/proj.html) | Maths (Geometry) | Project the current ship or planet onto the screen | 
| [prq](https://elite.bbcelite.com/c64/main/subroutine/prq.html) | Text | Print a text token followed by a question mark | 
| [prq+3](https://elite.bbcelite.com/c64/main/subroutine/prq.html) | Text | Print a question mark | 
| [prx](https://elite.bbcelite.com/c64/main/subroutine/prx.html) | Equipment | Return the price of a piece of equipment | 
| [prx-3](https://elite.bbcelite.com/c64/main/subroutine/prx.html) | Equipment | Return the price of the item with number A - 1 | 
| [PRXS](https://elite.bbcelite.com/c64/main/variable/prxs.html) | Equipment | Equipment prices | 
| [PTCLS2](https://elite.bbcelite.com/c64/main/subroutine/ptcls2.html) | Drawing ships | Draw the explosion along with an explosion sprite | 
| [ptg](https://elite.bbcelite.com/c64/main/subroutine/mjp.html) | Flight | Called when the user manually forces a mis-jump | 
| [PULSEW](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#pulsew) | Workspace variable | The current pulse width for sound effects | 
| [PUTBACK](https://elite.bbcelite.com/c64/main/subroutine/putback.html) | Tube | Reset the OSWRCH vector in WRCHV to point to USOSWRCH | 
| [PX4](https://elite.bbcelite.com/c64/main/subroutine/pixel.html) | Drawing pixels | Contains an RTS | 
| [PZW](https://elite.bbcelite.com/c64/main/subroutine/pzw.html) | Dashboard | Fetch the current dashboard colours, to support flashing | 
| [Q](https://elite.bbcelite.com/c64/main/workspace/zp.html#q) | Workspace variable | Temporary storage, used in a number of places | 
| [Q2](https://elite.bbcelite.com/c64/main/workspace/zp.html#q2) | Workspace variable | Temporary storage, used in place of variable Q in the line-drawing routines | 
| [QQ0](https://elite.bbcelite.com/c64/main/workspace/up.html#qq0) | Workspace variable | The current system's galactic x-coordinate (0-256) | 
| [QQ1](https://elite.bbcelite.com/c64/main/workspace/up.html#qq1) | Workspace variable | The current system's galactic y-coordinate (0-256) | 
| [QQ10](https://elite.bbcelite.com/c64/main/workspace/up.html#qq10) | Workspace variable | The galactic y-coordinate of the crosshairs in the galaxy chart (and, most of the time, the selected system's galactic y-coordinate) | 
| [QQ11](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq11) | Workspace variable | The type of the current view: | 
| [QQ12](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq12) | Workspace variable | Our "docked" status | 
| [QQ14](https://elite.bbcelite.com/c64/main/workspace/up.html#qq14) | Workspace variable | Our current fuel level (0-70) | 
| [QQ15](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq15) | Workspace variable | The three 16-bit seeds for the selected system, i.e. the one in the crosshairs in the Short-range Chart | 
| [QQ16](https://elite.bbcelite.com/c64/main/variable/qq16.html) | Text | The two-letter token lookup table | 
| [QQ17](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq17) | Workspace variable | Contains a number of flags that affect how text tokens are printed, particularly capitalisation | 
| [QQ18 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/qq18.html) | Text | The recursive token table for tokens 0-148 | 
| [QQ19](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq19) | Workspace variable | Temporary storage, used in a number of places | 
| [QQ2](https://elite.bbcelite.com/c64/main/workspace/up.html#qq2) | Workspace variable | The three 16-bit seeds for the current system, i.e. the one we are currently in | 
| [QQ20](https://elite.bbcelite.com/c64/main/workspace/up.html#qq20) | Workspace variable | The contents of our cargo hold | 
| [QQ21](https://elite.bbcelite.com/c64/main/workspace/up.html#qq21) | Workspace variable | The three 16-bit seeds for the current galaxy | 
| [QQ22](https://elite.bbcelite.com/c64/main/workspace/zp.html#qq22) | Workspace variable | The two hyperspace countdown counters | 
| [QQ23](https://elite.bbcelite.com/c64/main/variable/qq23.html) | Market | Market prices table | 
| [QQ24](https://elite.bbcelite.com/c64/main/workspace/up.html#qq24) | Workspace variable | Temporary storage, used to store the current market item's price in routine TT151 | 
| [QQ25](https://elite.bbcelite.com/c64/main/workspace/up.html#qq25) | Workspace variable | Temporary storage, used to store the current market item's availability in routine TT151 | 
| [QQ26](https://elite.bbcelite.com/c64/main/workspace/up.html#qq26) | Workspace variable | A random value used to randomise market data | 
| [QQ28](https://elite.bbcelite.com/c64/main/workspace/up.html#qq28) | Workspace variable | The current system's economy (0-7) | 
| [QQ29](https://elite.bbcelite.com/c64/main/workspace/up.html#qq29) | Workspace variable | Temporary storage, used in a number of places | 
| [QQ3](https://elite.bbcelite.com/c64/main/workspace/up.html#qq3) | Workspace variable | The selected system's economy (0-7) | 
| [QQ4](https://elite.bbcelite.com/c64/main/workspace/up.html#qq4) | Workspace variable | The selected system's government (0-7) | 
| [QQ5](https://elite.bbcelite.com/c64/main/workspace/up.html#qq5) | Workspace variable | The selected system's tech level (0-14) | 
| [QQ6](https://elite.bbcelite.com/c64/main/workspace/up.html#qq6) | Workspace variable | The selected system's population in billions * 10 (1-71), so the maximum population is 7.1 billion | 
| [QQ7](https://elite.bbcelite.com/c64/main/workspace/up.html#qq7) | Workspace variable | The selected system's productivity in M CR (96-62480) | 
| [QQ8](https://elite.bbcelite.com/c64/main/workspace/up.html#qq8) | Workspace variable | The distance from the current system to the selected system in light years * 10, stored as a 16-bit number | 
| [QQ9](https://elite.bbcelite.com/c64/main/workspace/up.html#qq9) | Workspace variable | The galactic x-coordinate of the crosshairs in the galaxy chart (and, most of the time, the selected system's galactic x-coordinate) | 
| [QU5](https://elite.bbcelite.com/c64/main/subroutine/br1_part_1_of_2.html) | Start and end | Restart the game using the last saved commander without asking whether to load a new commander file | 
| [qv](https://elite.bbcelite.com/c64/main/subroutine/qv.html) | Equipment | Print a menu of the four space views, for buying lasers | 
| [qw](https://elite.bbcelite.com/c64/main/subroutine/qw.html) | Text | Print a recursive token in the range 128-145 | 
| [R](https://elite.bbcelite.com/c64/main/workspace/zp.html#r) | Workspace variable | Temporary storage, used in a number of places | 
| [R%](https://elite.bbcelite.com/c64/main/variable/r_per_cent.html) | Utility routines | Denotes the end of the first part of the main game code (CODE1), from ELITE A to ELITE C | 
| [R2](https://elite.bbcelite.com/c64/main/workspace/zp.html#r2) | Workspace variable | Temporary storage, used in place of variable R in the line-drawing routines | 
| [R5](https://elite.bbcelite.com/c64/main/subroutine/r5.html) | Text | Make a beep and jump back into the character-printing routine at CHPR | 
| [RAND](https://elite.bbcelite.com/c64/main/workspace/zp.html#rand) | Workspace variable | Four 8-bit seeds for the random number generation system implemented in the DORND routine | 
| [RASTCT](https://elite.bbcelite.com/c64/main/variable/rastct.html) | Drawing the screen | The current raster count, which flips between 0 and 1 on each call to the COMIRQ1 interrupt handler (0 = space view, 1 = dashboard) | 
| [RAT](https://elite.bbcelite.com/c64/main/workspace/zp.html#rat) | Workspace variable | Used to store different signs depending on the current space view, for use in calculating stardust movement | 
| [RAT2](https://elite.bbcelite.com/c64/main/workspace/zp.html#rat2) | Workspace variable | Temporary storage, used to store the pitch and roll signs when moving objects and stardust | 
| [RDKEY](https://elite.bbcelite.com/c64/main/subroutine/rdkey.html) | Keyboard | Scan the keyboard for key presses and the joystick, and update the key logger | 
| [RDLI](https://elite.bbcelite.com/c64/main/variable/rdli.html) | Loader | The OS command string for running the flight code in file D.CODE in the disc version of Elite | 
| [RE2+2](https://elite.bbcelite.com/c64/main/subroutine/bump2.html) | Dashboard | Restore A from T and return from the subroutine | 
| [REDU2](https://elite.bbcelite.com/c64/main/subroutine/redu2.html) | Dashboard | Reduce the value of the pitch or roll dashboard indicator | 
| [refund](https://elite.bbcelite.com/c64/main/subroutine/refund.html) | Equipment | Install a new laser, processing a refund if applicable | 
| [RelocateLoader (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/subroutine/relocateloader.html) | Loader | Load and run the GMA1 loader file | 
| [RES2](https://elite.bbcelite.com/c64/main/subroutine/res2.html) | Start and end | Reset a number of flight variables and workspaces | 
| [RESET](https://elite.bbcelite.com/c64/main/subroutine/reset.html) | Start and end | Reset most variables | 
| [RLINE](https://elite.bbcelite.com/c64/main/variable/rline.html) | Text | The OSWORD configuration block used to fetch a line of text from the keyboard | 
| [RR4](https://elite.bbcelite.com/c64/main/subroutine/chpr.html) | Text | Restore the registers and return from the subroutine | 
| [RR4S](https://elite.bbcelite.com/c64/main/subroutine/rr4s.html) | Text | A jump point that restores the registers and returns from the CHPR subroutine (so we can use a branch instruction to jump to RR4) | 
| [RRafter](https://elite.bbcelite.com/c64/main/subroutine/chpr.html) | Text | A re-entry point from the clss routine to print the character in A | 
| [RTOK (Game data)](https://elite.bbcelite.com/c64/game_data/macro/rtok.html) | Text | Macro definition for recursive tokens in the recursive token table | 
| [RTS111](https://elite.bbcelite.com/c64/main/subroutine/mjp.html) | Flight | Contains an RTS | 
| [RTS2](https://elite.bbcelite.com/c64/main/subroutine/sun_part_4_of_4.html) | Drawing suns | Contains an RTS | 
| [RUGAL (Game data)](https://elite.bbcelite.com/c64/game_data/variable/rugal.html) | Text | The criteria for systems with extended description overrides | 
| [RunGMA (Disk Loader 1)](https://elite.bbcelite.com/c64/disk_loader_1/subroutine/rungma.html) | Loader | Load and run the GMA1 loader file | 
| [RUPLA (Game data)](https://elite.bbcelite.com/c64/game_data/variable/rupla.html) | Text | System numbers that have extended description overrides | 
| [RUTOK (Game data)](https://elite.bbcelite.com/c64/game_data/variable/rutok.html) | Text | The second extended token table for recursive tokens 0-26 (DETOK3) | 
| [S](https://elite.bbcelite.com/c64/main/workspace/zp.html#s) | Workspace variable | Temporary storage, used in a number of places | 
| [S%](https://elite.bbcelite.com/c64/main/subroutine/s_per_cent.html) | Loader | Checksum, decrypt and unscramble the main game code, and start the game | 
| [S1%](https://elite.bbcelite.com/c64/main/variable/s1_per_cent.html) | Save and load | The drive and directory number used when saving or loading a commander file | 
| [S2](https://elite.bbcelite.com/c64/main/workspace/zp.html#s2) | Workspace variable | Temporary storage, used in place of variable S in the line-drawing routines | 
| [safehouse](https://elite.bbcelite.com/c64/main/workspace/up.html#safehouse) | Workspace variable | Backup storage for the seeds for the selected system | 
| [santana](https://elite.bbcelite.com/c64/main/variable/santana.html) | Drawing the screen | Controls whether sprite 1 (the explosion sprite) is drawn in single colour or multicolour mode | 
| [SC](https://elite.bbcelite.com/c64/main/workspace/zp.html#sc) | Workspace variable | Screen address (low byte) | 
| [scacol](https://elite.bbcelite.com/c64/main/variable/scacol.html) | Drawing ships | Ship colours on the scanner | 
| [SCAN](https://elite.bbcelite.com/c64/main/subroutine/scan.html) | Dashboard | Display the current ship on the scanner | 
| [SCH](https://elite.bbcelite.com/c64/main/workspace/zp.html#sch) | Workspace variable | Screen address (high byte) | 
| [sdump (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/sdump.html) | Drawing the screen | Screen RAM colour data for the dashboard | 
| [SESCP](https://elite.bbcelite.com/c64/main/subroutine/sescp.html) | Flight | Spawn an escape pod from the current (parent) ship | 
| [SETL1](https://elite.bbcelite.com/c64/main/subroutine/setl1.html) | Utility routines | Set the 6510 input/output port register to control the memory map | 
| [SetUpFastLoader (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/setupfastloader.html) | Loader | Set up the fast loader so that calls to the Kernal's file functions use the fast loader routines instead | 
| [SetUpGMAFile (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/subroutine/setupgmafile.html) | Loader | Configure the filename parameters to load a specific GMA file | 
| [SETXC](https://elite.bbcelite.com/c64/main/subroutine/setxc.html) | Text | An unused routine to move the text cursor to a specific column | 
| [SETYC](https://elite.bbcelite.com/c64/main/subroutine/setyc.html) | Text | An unused routine to move the text cursor to a specific row | 
| [SEVENS](https://elite.bbcelite.com/c64/main/variable/sevens.html) | Sound | A table for converting the value of Y to 7 * Y | 
| [SFRMIS](https://elite.bbcelite.com/c64/main/subroutine/sfrmis.html) | Tactics | Add an enemy missile to our local bubble of universe | 
| [SFS1](https://elite.bbcelite.com/c64/main/subroutine/sfs1.html) | Universe | Spawn a child ship from the current (parent) ship | 
| [SFS1-2](https://elite.bbcelite.com/c64/main/subroutine/sfs1.html) | Universe | Used to add a missile to the local bubble that that has AI (bit 7 set), is hostile (bit 6 set) and has been launched (bit 0 clear); the target slot number is set to 31, but this is ignored as the hostile flags means we are the target | 
| [SFS2](https://elite.bbcelite.com/c64/main/subroutine/sfs2.html) | Moving | Move a ship in space along one of the coordinate axes | 
| [SFXATK](https://elite.bbcelite.com/c64/main/variable/sfxatk.html) | Sound | The attack and decay length (SID+$5) for each sound effect | 
| [SFXCNT](https://elite.bbcelite.com/c64/main/variable/sfxcnt.html) | Sound | The counter for each sound effect, which defines the duration of the effect in frames | 
| [SFXCR](https://elite.bbcelite.com/c64/main/variable/sfxcr.html) | Sound | The voice control register (SID+$4) for each sound effect | 
| [SFXFQ](https://elite.bbcelite.com/c64/main/variable/sfxfq.html) | Sound | The frequency (SID+$5) for each sound effect | 
| [SFXFRCH](https://elite.bbcelite.com/c64/main/variable/sfxfrch.html) | Sound | The frequency change to be applied to each sound effect in each frame (as a signed number) | 
| [SFXPR](https://elite.bbcelite.com/c64/main/variable/sfxpr.html) | Sound | The priority level for each sound effect | 
| [SFXSUS](https://elite.bbcelite.com/c64/main/variable/sfxsus.html) | Sound | The release length and sustain volume (SID+$6) for each sound effect | 
| [SFXVCH](https://elite.bbcelite.com/c64/main/variable/sfxvch.html) | Sound | The volume change rate for each sound effect, i.e. how many frames need to pass before the sound effect's volume is reduced by one | 
| [shango](https://elite.bbcelite.com/c64/main/variable/shango.html) | Drawing the screen | The raster lines that fire the raster interrupt, so it fires at the top of the screen (51) and the top of the dashboard (51 + 143) | 
| [SHD](https://elite.bbcelite.com/c64/main/subroutine/shd.html) | Flight | Charge a shield and drain some energy from the energy banks | 
| [SHIP_ADDER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_adder.html) | Drawing ships | Ship blueprint for an Adder | 
| [SHIP_ANACONDA (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_anaconda.html) | Drawing ships | Ship blueprint for an Anaconda | 
| [SHIP_ASP_MK_2 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_asp_mk_2.html) | Drawing ships | Ship blueprint for an Asp Mk II | 
| [SHIP_ASTEROID (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_asteroid.html) | Drawing ships | Ship blueprint for an asteroid | 
| [SHIP_BOA (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_boa.html) | Drawing ships | Ship blueprint for a Boa | 
| [SHIP_BOULDER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_boulder.html) | Drawing ships | Ship blueprint for a boulder | 
| [SHIP_CANISTER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_canister.html) | Drawing ships | Ship blueprint for a cargo canister | 
| [SHIP_COBRA_MK_1 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_cobra_mk_1.html) | Drawing ships | Ship blueprint for a Cobra Mk I | 
| [SHIP_COBRA_MK_3 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_cobra_mk_3.html) | Drawing ships | Ship blueprint for a Cobra Mk III | 
| [SHIP_COBRA_MK_3_P (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_cobra_mk_3_p.html) | Drawing ships | Ship blueprint for a Cobra Mk III (pirate) | 
| [SHIP_CONSTRICTOR (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_constrictor.html) | Drawing ships | Ship blueprint for a Constrictor | 
| [SHIP_CORIOLIS (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_coriolis.html) | Drawing ships | Ship blueprint for a Coriolis space station | 
| [SHIP_COUGAR (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_cougar.html) | Drawing ships | Ship blueprint for a Cougar | 
| [SHIP_DODO (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_dodo.html) | Drawing ships | Ship blueprint for a Dodecahedron ("Dodo") space station | 
| [SHIP_ESCAPE_POD (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_escape_pod.html) | Drawing ships | Ship blueprint for an escape pod | 
| [SHIP_FER_DE_LANCE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_fer_de_lance.html) | Drawing ships | Ship blueprint for a Fer-de-Lance | 
| [SHIP_GECKO (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_gecko.html) | Drawing ships | Ship blueprint for a Gecko | 
| [SHIP_KRAIT (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_krait.html) | Drawing ships | Ship blueprint for a Krait | 
| [SHIP_MAMBA (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_mamba.html) | Drawing ships | Ship blueprint for a Mamba | 
| [SHIP_MISSILE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_missile.html) | Drawing ships | Ship blueprint for a missile | 
| [SHIP_MORAY (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_moray.html) | Drawing ships | Ship blueprint for a Moray | 
| [SHIP_PLATE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_plate.html) | Drawing ships | Ship blueprint for an alloy plate | 
| [SHIP_PYTHON (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_python.html) | Drawing ships | Ship blueprint for a Python | 
| [SHIP_PYTHON_P (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_python_p.html) | Drawing ships | Ship blueprint for a Python (pirate) | 
| [SHIP_ROCK_HERMIT (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_rock_hermit.html) | Drawing ships | Ship blueprint for a rock hermit (asteroid) | 
| [SHIP_SHUTTLE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_shuttle.html) | Drawing ships | Ship blueprint for a Shuttle | 
| [SHIP_SIDEWINDER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_sidewinder.html) | Drawing ships | Ship blueprint for a Sidewinder | 
| [SHIP_SPLINTER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_splinter.html) | Drawing ships | Ship blueprint for a splinter | 
| [SHIP_THARGOID (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_thargoid.html) | Drawing ships | Ship blueprint for a Thargoid mothership | 
| [SHIP_THARGON (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_thargon.html) | Drawing ships | Ship blueprint for a Thargon | 
| [SHIP_TRANSPORTER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_transporter.html) | Drawing ships | Ship blueprint for a Transporter | 
| [SHIP_VIPER (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_viper.html) | Drawing ships | Ship blueprint for a Viper | 
| [SHIP_WORM (Game data)](https://elite.bbcelite.com/c64/game_data/variable/ship_worm.html) | Drawing ships | Ship blueprint for a Worm | 
| [SHIPS (Game Loader)](https://elite.bbcelite.com/c64/game_loader/subroutine/ships.html) | Loader | The binaries for the ship blueprints | 
| [SHPPT](https://elite.bbcelite.com/c64/main/subroutine/shppt.html) | Drawing ships | Draw a distant ship as a point rather than a full wireframe | 
| [SIGHT](https://elite.bbcelite.com/c64/main/subroutine/sight.html) | Flight | Draw the laser crosshairs | 
| [sightcol](https://elite.bbcelite.com/c64/main/variable/sightcol.html) | Drawing lines | Colours for the crosshair sights on the different laser types | 
| [SLSP](https://elite.bbcelite.com/c64/main/workspace/up.html#slsp) | Workspace variable | The address of the bottom of the ship line heap | 
| [SNE (Game data)](https://elite.bbcelite.com/c64/game_data/variable/sne.html) | Maths (Geometry) | Sine/cosine table | 
| [SOATK](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#soatk) | Workspace variable | Sound buffer for attack and decay lengths | 
| [SOCNT](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#socnt) | Workspace variable | Sound buffer for sound effect counters | 
| [SOCR](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#socr) | Workspace variable | Sound buffer for voice control register values | 
| [SOFLG](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#soflg) | Workspace variable | Sound buffer for sound effect flags | 
| [SOFLUSH](https://elite.bbcelite.com/c64/main/subroutine/soflush.html) | Sound | Reset the sound buffers and turn off all sound channels | 
| [SOFRCH](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sofrch) | Workspace variable | Sound buffer for frequency change values | 
| [SOFRQ](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sofrq) | Workspace variable | Sound buffer for sound effect frequencies | 
| [SOINT](https://elite.bbcelite.com/c64/main/subroutine/soint.html) | Sound | Process the contents of the sound buffer and send it to the sound chip, to make sound effects as part of the interrupt routine | 
| [SOLAR](https://elite.bbcelite.com/c64/main/subroutine/solar.html) | Universe | Set up various aspects of arriving in a new system | 
| [SOPR](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sopr) | Workspace variable | Sound buffer for sound effect priorities | 
| [SOS1](https://elite.bbcelite.com/c64/main/subroutine/sos1.html) | Universe | Update the missile indicators, set up the planet data block | 
| [SOSUS](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sosus) | Workspace variable | Sound buffer for release length and sustain volume | 
| [SOUL3b](https://elite.bbcelite.com/c64/main/subroutine/soul3b.html) | Sound | Check whether this is the last voice when making sound effects in the interrupt routine, and return from the interrupt if it is | 
| [SOUL8](https://elite.bbcelite.com/c64/main/subroutine/soint.html) | Sound | Process the sound buffer from voice Y to 0 | 
| [Sound variables](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html) | Sound | The sound buffer where the data to be sent to the sound chip is processed | 
| [SOUR1](https://elite.bbcelite.com/c64/main/subroutine/soflush.html) | Sound | Contains an RTS | 
| [SOVCH](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sovch) | Workspace variable | Sound buffer for the volume change rate | 
| [SP1](https://elite.bbcelite.com/c64/main/subroutine/sp1.html) | Dashboard | Draw the space station on the compass | 
| [SP2](https://elite.bbcelite.com/c64/main/subroutine/sp2.html) | Dashboard | Draw a dot on the compass, given the planet/station vector | 
| [spasto](https://elite.bbcelite.com/c64/main/variable/spasto.html) | Universe | Contains the address of the Coriolis space station's ship blueprint | 
| [SPBLB](https://elite.bbcelite.com/c64/main/subroutine/spblb.html) | Dashboard | Light up the space station indicator ("S") on the dashboard | 
| [spc](https://elite.bbcelite.com/c64/main/subroutine/spc.html) | Text | Print a text token followed by a space | 
| [SPIN](https://elite.bbcelite.com/c64/main/subroutine/spin.html) | Universe | Randomly spawn cargo from a destroyed ship | 
| [SPIN2](https://elite.bbcelite.com/c64/main/subroutine/spin.html) | Universe | Remove any randomness: spawn cargo of a specific type (given in X), and always spawn the number given in A | 
| [SPMASK](https://elite.bbcelite.com/c64/main/variable/spmask.html) | Missions | Masks for updating sprite bits in VIC+$10 for the top bit of the 9-bit x-coordinates of the Trumble sprites | 
| [SPRITE2 (Sprites)](https://elite.bbcelite.com/c64/sprites/macro/sprite2.html) | Sprites | Macro definition for a two-colour sprite pixel row | 
| [SPRITE2_BYTE (Sprites)](https://elite.bbcelite.com/c64/sprites/macro/sprite2_byte.html) | Sprites | Macro definition for a two-colour sprite pixel byte | 
| [SPRITE4 (Sprites)](https://elite.bbcelite.com/c64/sprites/macro/sprite4.html) | Sprites | Macro definition for a four-colour sprite pixel row | 
| [SPRITE4_BYTE (Sprites)](https://elite.bbcelite.com/c64/sprites/macro/sprite4_byte.html) | Sprites | Macro definition for a four-colour sprite pixel byte | 
| [spritp (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/spritp.html) | Drawing the screen | Sprite definitions | 
| [spritp (Sprites)](https://elite.bbcelite.com/c64/sprites/variable/spritp.html) | Sprites | Sprite definitions for four laser sights, the explosion sprite and two Trumbles | 
| [sprx](https://elite.bbcelite.com/c64/main/workspace/up.html#sprx) | Workspace variable | Contains the x-coordinate offset for the explosion sprite, i.e. the relative position of the sprite compared to the centre of the explosion, which needs to be set according to the size of the sprite | 
| [spry](https://elite.bbcelite.com/c64/main/workspace/up.html#spry) | Workspace variable | Contains the y-coordinate offset for the explosion sprite, i.e. the relative position of the sprite compared to the centre of the explosion, which needs to be set according to the size of the sprite | 
| [SPS1](https://elite.bbcelite.com/c64/main/subroutine/sps1.html) | Maths (Geometry) | Calculate the vector to the planet and store it in XX15 | 
| [SPS1+1](https://elite.bbcelite.com/c64/main/subroutine/sps1.html) | Maths (Geometry) | A BRK instruction | 
| [SPS2](https://elite.bbcelite.com/c64/main/subroutine/sps2.html) | Maths (Arithmetic) | Calculate (Y X) = A / 10 | 
| [SPS3](https://elite.bbcelite.com/c64/main/subroutine/sps3.html) | Maths (Geometry) | Copy a space coordinate from the K% block into K3 | 
| [SPS4](https://elite.bbcelite.com/c64/main/subroutine/sps4.html) | Maths (Geometry) | Calculate the vector to the space station | 
| [SQUA](https://elite.bbcelite.com/c64/main/subroutine/squa.html) | Maths (Arithmetic) | Clear bit 7 of A and calculate (A P) = A * A | 
| [SQUA2](https://elite.bbcelite.com/c64/main/subroutine/squa2.html) | Maths (Arithmetic) | Calculate (A P) = A * A | 
| [SSPR](https://elite.bbcelite.com/c64/main/workspace/up.html#sspr) | Workspace variable | "Space station present" flag | 
| [STARS](https://elite.bbcelite.com/c64/main/subroutine/stars.html) | Stardust | The main routine for processing the stardust | 
| [STARS1](https://elite.bbcelite.com/c64/main/subroutine/stars1.html) | Stardust | Process the stardust for the front view | 
| [STARS2](https://elite.bbcelite.com/c64/main/subroutine/stars2.html) | Stardust | Process the stardust for the left or right view | 
| [STARS6](https://elite.bbcelite.com/c64/main/subroutine/stars6.html) | Stardust | Process the stardust for the rear view | 
| [startat](https://elite.bbcelite.com/c64/main/subroutine/startat.html) | Sound | Start playing the title music, if configured | 
| [startat2](https://elite.bbcelite.com/c64/main/subroutine/startbd.html) | Sound | Start playing the music at address (A X) + 1 | 
| [startbd](https://elite.bbcelite.com/c64/main/subroutine/startbd.html) | Sound | Start playing the docking music, if configured | 
| [STARTUP](https://elite.bbcelite.com/c64/main/subroutine/startup.html) | Loader | Set the various vectors, interrupts and timers | 
| [STATUS](https://elite.bbcelite.com/c64/main/subroutine/status.html) | Status | Show the Status Mode screen | 
| [stopat](https://elite.bbcelite.com/c64/main/subroutine/stopbd.html) | Sound | Stop playing the current music | 
| [stopbd](https://elite.bbcelite.com/c64/main/subroutine/stopbd.html) | Sound | Stop playing the docking music | 
| [STP](https://elite.bbcelite.com/c64/main/workspace/zp.html#stp) | Workspace variable | The step size for drawing circles | 
| [SUN (Part 1 of 4)](https://elite.bbcelite.com/c64/main/subroutine/sun_part_1_of_4.html) | Drawing suns | Draw the sun: Set up all the variables needed to draw the sun | 
| [SUN (Part 2 of 4)](https://elite.bbcelite.com/c64/main/subroutine/sun_part_2_of_4.html) | Drawing suns | Draw the sun: Start from the bottom of the screen and erase the old sun line by line | 
| [SUN (Part 3 of 4)](https://elite.bbcelite.com/c64/main/subroutine/sun_part_3_of_4.html) | Drawing suns | Draw the sun: Continue to move up the screen, drawing the new sun line by line | 
| [SUN (Part 4 of 4)](https://elite.bbcelite.com/c64/main/subroutine/sun_part_4_of_4.html) | Drawing suns | Draw the sun: Continue to the top of the screen, erasing the old sun line by line | 
| [SUNX](https://elite.bbcelite.com/c64/main/workspace/zp.html#sunx) | Workspace variable | The 16-bit x-coordinate of the vertical centre axis of the sun (which might be off-screen) | 
| [SVC](https://elite.bbcelite.com/c64/main/workspace/up.html#svc) | Workspace variable | The save count | 
| [SVE](https://elite.bbcelite.com/c64/main/subroutine/sve.html) | Save and load | Display the disk access menu and process saving of commander files | 
| [SWAP](https://elite.bbcelite.com/c64/main/workspace/wp.html#swap) | Workspace variable | Temporary storage, used to store a flag that records whether or not we had to swap a line's start and end coordinates around when clipping the line in routine LL145 (the flag is used in places like BLINE to swap them back) | 
| [SWAPPZERO](https://elite.bbcelite.com/c64/main/subroutine/swappzero.html) | Utility routines | A routine that swaps zero page with the page at $CE00, so that zero page changes made by Kernal functions can be reversed | 
| [SWAPPZERO (source disk variant)](https://elite.bbcelite.com/c64/main/subroutine/swappzero_source_disk_variant.html) | Utility routines | A routine that swaps zero page with the page at $CE00, so that zero page changes made by Kernal functions can be reversed | 
| [SX](https://elite.bbcelite.com/c64/main/workspace/wp.html#sx) | Workspace variable | This is where we store the x_hi coordinates for all the stardust particles | 
| [SXL](https://elite.bbcelite.com/c64/main/workspace/wp.html#sxl) | Workspace variable | This is where we store the x_lo coordinates for all the stardust particles | 
| [SY](https://elite.bbcelite.com/c64/main/workspace/wp.html#sy) | Workspace variable | This is where we store the y_hi coordinates for all the stardust particles | 
| [SYL](https://elite.bbcelite.com/c64/main/workspace/wp.html#syl) | Workspace variable | This is where we store the y_lo coordinates for all the stardust particles | 
| [SZ](https://elite.bbcelite.com/c64/main/workspace/wp.html#sz) | Workspace variable | This is where we store the z_hi coordinates for all the stardust particles | 
| [SZL](https://elite.bbcelite.com/c64/main/workspace/wp.html#szl) | Workspace variable | This is where we store the z_lo coordinates for all the stardust particles | 
| [t](https://elite.bbcelite.com/c64/main/subroutine/tt217.html) | Keyboard | As TT217 but don't preserve Y, set it to YSAV instead | 
| [T](https://elite.bbcelite.com/c64/main/workspace/zp.html#t) | Workspace variable | Temporary storage, used in a number of places | 
| [T1](https://elite.bbcelite.com/c64/main/workspace/zp.html#t1) | Workspace variable | Temporary storage, used in a number of places | 
| [T2](https://elite.bbcelite.com/c64/main/workspace/zp.html#t2) | Workspace variable | Temporary storage, used in place of variable T in the line-drawing routines | 
| [T95](https://elite.bbcelite.com/c64/main/subroutine/tt102.html) | Keyboard | Print the distance to the selected system | 
| [TA151](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_7_of_7.html) | Tactics | Make the ship head towards the planet | 
| [TA2](https://elite.bbcelite.com/c64/main/subroutine/tas2.html) | Maths (Geometry) | Calculate the length of the vector in XX15 (ignoring the low coordinates), returning it in Q | 
| [TA9-1](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_7_of_7.html) | Tactics | Contains an RTS | 
| [TACTICS (Part 1 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_1_of_7.html) | Tactics | Apply tactics: Process missiles, both enemy missiles and our own | 
| [TACTICS (Part 2 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_2_of_7.html) | Tactics | Apply tactics: Escape pod, station, lone Thargon, safe-zone pirate | 
| [TACTICS (Part 3 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_3_of_7.html) | Tactics | Apply tactics: Calculate dot product to determine ship's aim | 
| [TACTICS (Part 4 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_4_of_7.html) | Tactics | Apply tactics: Check energy levels, maybe launch escape pod if low | 
| [TACTICS (Part 5 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_5_of_7.html) | Tactics | Apply tactics: Consider whether to launch a missile at us | 
| [TACTICS (Part 6 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_6_of_7.html) | Tactics | Apply tactics: Consider firing a laser at us, if aim is true | 
| [TACTICS (Part 7 of 7)](https://elite.bbcelite.com/c64/main/subroutine/tactics_part_7_of_7.html) | Tactics | Apply tactics: Set pitch, roll, and acceleration | 
| [tal](https://elite.bbcelite.com/c64/main/subroutine/tal.html) | Universe | Print the current galaxy number | 
| [TALLY](https://elite.bbcelite.com/c64/main/workspace/up.html#tally) | Workspace variable | Our combat rank | 
| [TALLYL](https://elite.bbcelite.com/c64/main/workspace/up.html#tallyl) | Workspace variable | Combat rank fraction | 
| [tapeerror](https://elite.bbcelite.com/c64/main/subroutine/tapeerror.html) | Save and load | Print either "TAPE ERROR" or "DISK ERROR" | 
| [TAS1](https://elite.bbcelite.com/c64/main/subroutine/tas1.html) | Maths (Arithmetic) | Calculate K3 = (x_sign x_hi x_lo) - V(1 0) | 
| [TAS2](https://elite.bbcelite.com/c64/main/subroutine/tas2.html) | Maths (Geometry) | Normalise the three-coordinate vector in K3 | 
| [TAS3](https://elite.bbcelite.com/c64/main/subroutine/tas3.html) | Maths (Geometry) | Calculate the dot product of XX15 and an orientation vector | 
| [TAS4](https://elite.bbcelite.com/c64/main/subroutine/tas4.html) | Maths (Geometry) | Calculate the dot product of XX15 and one of the space station's orientation vectors | 
| [TAS6](https://elite.bbcelite.com/c64/main/subroutine/tas6.html) | Maths (Geometry) | Negate the vector in XX15 so it points in the opposite direction | 
| [TBRIEF](https://elite.bbcelite.com/c64/main/subroutine/tbrief.html) | Missions | Start mission 3 | 
| [tek](https://elite.bbcelite.com/c64/main/workspace/up.html#tek) | Workspace variable | The current system's tech level (0-14) | 
| [TENS](https://elite.bbcelite.com/c64/main/variable/tens.html) | Text | A constant used when printing large numbers in BPRNT | 
| [TGINT](https://elite.bbcelite.com/c64/main/variable/tgint.html) | Keyboard | The keys used to toggle configuration settings when the game is paused | 
| [TGT](https://elite.bbcelite.com/c64/main/workspace/zp.html#tgt) | Workspace variable | Temporary storage, typically used as a target value for counters when drawing explosion clouds and partial circles | 
| [THERE](https://elite.bbcelite.com/c64/main/subroutine/there.html) | Missions | Check whether we are in the Constrictor's system in mission 1 | 
| [thiskey](https://elite.bbcelite.com/c64/main/workspace/zp.html#thiskey) | Workspace variable | If a key is being pressed that is not in the keyboard table at KYTB, it can be stored in KL and thiskey (as seen in routine DK4, for example) | 
| [thislong](https://elite.bbcelite.com/c64/main/variable/thislong.html) | Save and load | Contains the length of the most recently entered commander name | 
| [TIDY](https://elite.bbcelite.com/c64/main/subroutine/tidy.html) | Maths (Geometry) | Orthonormalise the orientation vectors for a ship | 
| [TIS1](https://elite.bbcelite.com/c64/main/subroutine/tis1.html) | Maths (Arithmetic) | Calculate (A ?) = (-X * A + (S R)) / 96 | 
| [TIS2](https://elite.bbcelite.com/c64/main/subroutine/tis2.html) | Maths (Arithmetic) | Calculate A = A / Q | 
| [TIS3](https://elite.bbcelite.com/c64/main/subroutine/tis3.html) | Maths (Arithmetic) | Calculate -(nosev_1 * roofv_1 + nosev_2 * roofv_2) / nosev_3 | 
| [TITLE](https://elite.bbcelite.com/c64/main/subroutine/title.html) | Start and end | Display a title screen with a rotating ship and prompt | 
| [TKN1 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/tkn1.html) | Text | The first extended token table for recursive tokens 0-255 (DETOK) | 
| [TKN2](https://elite.bbcelite.com/c64/main/variable/tkn2.html) | Text | The extended two-letter token lookup table | 
| [tnpr](https://elite.bbcelite.com/c64/main/subroutine/tnpr.html) | Market | Work out if we have space for a specific amount of cargo | 
| [tnpr1](https://elite.bbcelite.com/c64/main/subroutine/tnpr1.html) | Market | Work out if we have space for one tonne of cargo | 
| [TOKN (Game data)](https://elite.bbcelite.com/c64/game_data/macro/tokn.html) | Text | Macro definition for standard tokens in the extended token table | 
| [TP](https://elite.bbcelite.com/c64/main/workspace/up.html#tp) | Workspace variable | The current mission status | 
| [TR1](https://elite.bbcelite.com/c64/main/subroutine/tr1.html) | Save and load | Copy the last saved commander's name from NA% to INWK | 
| [trackSector (Disk Loader 2)](https://elite.bbcelite.com/c64/disk_loader_2/variable/tracksector.html) | Loader | Track and sector numbers for all the files on the disk, for use in the fast loader | 
| [TRADEMODE](https://elite.bbcelite.com/c64/main/subroutine/trademode.html) | Drawing the screen | Clear the screen and set up a trading screen | 
| [TRANTABLE](https://elite.bbcelite.com/c64/main/variable/trantable.html) | Keyboard | Translation table from internal key number to ASCII | 
| [TRIBBLE](https://elite.bbcelite.com/c64/main/workspace/up.html#tribble) | Workspace variable | The number of Trumbles in the cargo hold | 
| [TRIBCT](https://elite.bbcelite.com/c64/main/workspace/up.html#tribct) | Workspace variable | Contains the number of Trumble sprites that we are showing on-screen, in the range 0 to 6 | 
| [TRIBDIR](https://elite.bbcelite.com/c64/main/variable/tribdir.html) | Missions | The low byte of the four 16-bit directions in which Trumble sprites can move | 
| [TRIBDIRH](https://elite.bbcelite.com/c64/main/variable/tribdirh.html) | Missions | The high byte of the four 16-bit directions in which Trumble sprites can move | 
| [TRIBMA](https://elite.bbcelite.com/c64/main/variable/tribma.html) | Missions | A table for converting the number of Trumbles in the hold into a sprite-enable flag to use with VIC register $15 | 
| [TRIBTA](https://elite.bbcelite.com/c64/main/variable/tribta.html) | Missions | A table for converting the number of Trumbles in the hold into a number of sprites in the range 0 to 6 | 
| [TRIBVX](https://elite.bbcelite.com/c64/main/workspace/up.html#tribvx) | Workspace variable | Contains the low byte of the 16-bit x-axis velocity of each of the Trumbles | 
| [TRIBVXH](https://elite.bbcelite.com/c64/main/workspace/up.html#tribvxh) | Workspace variable | Contains the high byte of the 16-bit x-axis velocity of each of the Trumbles | 
| [TRIBXH](https://elite.bbcelite.com/c64/main/workspace/up.html#tribxh) | Workspace variable | Contains bit 8 of the x-coordinate for each of the Trumble sprites (as x-coordinates are 9-bit values) | 
| [TRNME](https://elite.bbcelite.com/c64/main/subroutine/trnme.html) | Save and load | Copy the last saved commander's name from INWK to NA% | 
| [TT100](https://elite.bbcelite.com/c64/main/subroutine/main_game_loop_part_2_of_6.html) | Main loop | The entry point for the start of the main game loop, which calls the main flight loop and the moves into the spawning routine | 
| [TT102](https://elite.bbcelite.com/c64/main/subroutine/tt102.html) | Keyboard | Process function key, save key, hyperspace and chart key presses and update the hyperspace counter | 
| [TT103](https://elite.bbcelite.com/c64/main/subroutine/tt103.html) | Charts | Draw a small set of crosshairs on a chart | 
| [TT105](https://elite.bbcelite.com/c64/main/subroutine/tt105.html) | Charts | Draw crosshairs on the Short-range Chart, with clipping | 
| [TT11](https://elite.bbcelite.com/c64/main/subroutine/tt11.html) | Text | Print a 16-bit number, left-padded to n digits, and optional point | 
| [TT110](https://elite.bbcelite.com/c64/main/subroutine/tt110.html) | Flight | Launch from a station or show the front space view | 
| [TT111](https://elite.bbcelite.com/c64/main/subroutine/tt111.html) | Universe | Set the current system to the nearest system to a point | 
| [TT111-1](https://elite.bbcelite.com/c64/main/subroutine/tt111.html) | Universe | Contains an RTS | 
| [TT113](https://elite.bbcelite.com/c64/main/subroutine/mcash.html) | Maths (Arithmetic) | Contains an RTS | 
| [TT114](https://elite.bbcelite.com/c64/main/subroutine/tt114.html) | Charts | Display either the Long-range or Short-range Chart | 
| [TT123](https://elite.bbcelite.com/c64/main/subroutine/tt123.html) | Charts | Move galactic coordinates by a signed delta | 
| [TT128](https://elite.bbcelite.com/c64/main/subroutine/tt128.html) | Drawing circles | Draw a circle on a chart | 
| [TT14](https://elite.bbcelite.com/c64/main/subroutine/tt14.html) | Drawing circles | Draw a circle with crosshairs on a chart | 
| [TT146](https://elite.bbcelite.com/c64/main/subroutine/tt146.html) | Universe | Print the distance to the selected system in light years | 
| [TT147](https://elite.bbcelite.com/c64/main/subroutine/tt147.html) | Flight | Print an error when a system is out of hyperspace range | 
| [TT15](https://elite.bbcelite.com/c64/main/subroutine/tt15.html) | Drawing lines | Draw a set of crosshairs | 
| [TT151](https://elite.bbcelite.com/c64/main/subroutine/tt151.html) | Market | Print the name, price and availability of a market item | 
| [TT152](https://elite.bbcelite.com/c64/main/subroutine/tt152.html) | Market | Print the unit ("t", "kg" or "g") for a market item | 
| [TT16](https://elite.bbcelite.com/c64/main/subroutine/tt16.html) | Charts | Move the crosshairs on a chart | 
| [TT160](https://elite.bbcelite.com/c64/main/subroutine/tt160.html) | Market | Print "t" (for tonne) and a space | 
| [TT161](https://elite.bbcelite.com/c64/main/subroutine/tt161.html) | Market | Print "kg" (for kilograms) | 
| [TT162](https://elite.bbcelite.com/c64/main/subroutine/tt162.html) | Text | Print a space | 
| [TT162+2](https://elite.bbcelite.com/c64/main/subroutine/tt162.html) | Text | Jump to TT27 to print the text token in A | 
| [TT163](https://elite.bbcelite.com/c64/main/subroutine/tt163.html) | Market | Print the headers for the table of market prices | 
| [TT167](https://elite.bbcelite.com/c64/main/subroutine/tt167.html) | Market | Show the Market Price screen | 
| [TT16a](https://elite.bbcelite.com/c64/main/subroutine/tt16a.html) | Market | Print "g" (for grams) | 
| [TT17](https://elite.bbcelite.com/c64/main/subroutine/tt17.html) | Keyboard | Scan the keyboard for cursor key or joystick movement | 
| [TT170](https://elite.bbcelite.com/c64/main/subroutine/tt170.html) | Start and end | Main entry point for the Elite game code | 
| [TT18](https://elite.bbcelite.com/c64/main/subroutine/tt18.html) | Flight | Try to initiate a jump into hyperspace | 
| [TT180](https://elite.bbcelite.com/c64/main/subroutine/tt123.html) | Charts | Contains an RTS | 
| [TT20](https://elite.bbcelite.com/c64/main/subroutine/tt20.html) | Universe | Twist the selected system's seeds four times | 
| [TT208](https://elite.bbcelite.com/c64/main/subroutine/tt208.html) | Market | Show the Sell Cargo screen | 
| [TT210](https://elite.bbcelite.com/c64/main/subroutine/tt210.html) | Market | Show a list of current cargo in our hold, optionally to sell | 
| [TT213](https://elite.bbcelite.com/c64/main/subroutine/tt213.html) | Market | Show the Inventory screen | 
| [TT214](https://elite.bbcelite.com/c64/main/subroutine/tt214.html) | Keyboard | Ask a question with a "Y/N?" prompt and return the response | 
| [TT217](https://elite.bbcelite.com/c64/main/subroutine/tt217.html) | Keyboard | Scan the keyboard until a key is pressed | 
| [TT219](https://elite.bbcelite.com/c64/main/subroutine/tt219.html) | Market | Show the Buy Cargo screen | 
| [TT22](https://elite.bbcelite.com/c64/main/subroutine/tt22.html) | Charts | Show the Long-range Chart | 
| [TT23](https://elite.bbcelite.com/c64/main/subroutine/tt23.html) | Charts | Show the Short-range Chart | 
| [TT24](https://elite.bbcelite.com/c64/main/subroutine/tt24.html) | Universe | Calculate system data from the system seeds | 
| [TT25](https://elite.bbcelite.com/c64/main/subroutine/tt25.html) | Universe | Show the Data on System screen | 
| [TT26](https://elite.bbcelite.com/c64/main/subroutine/tt26.html) | Text | Print a character at the text cursor, with support for verified text in extended tokens | 
| [TT27](https://elite.bbcelite.com/c64/main/subroutine/tt27.html) | Text | Print a text token | 
| [TT41](https://elite.bbcelite.com/c64/main/subroutine/tt41.html) | Text | Print a letter according to Sentence Case | 
| [TT42](https://elite.bbcelite.com/c64/main/subroutine/tt42.html) | Text | Print a letter in lower case | 
| [TT43](https://elite.bbcelite.com/c64/main/subroutine/tt43.html) | Text | Print a two-letter token or recursive token 0-95 | 
| [TT44](https://elite.bbcelite.com/c64/main/subroutine/tt42.html) | Text | Jumps to TT26 to print the character in A (used to enable us to use a branch instruction to jump to TT26) | 
| [TT45](https://elite.bbcelite.com/c64/main/subroutine/tt45.html) | Text | Print a letter in lower case | 
| [TT46](https://elite.bbcelite.com/c64/main/subroutine/tt46.html) | Text | Print a character and switch to capitals | 
| [TT48](https://elite.bbcelite.com/c64/main/subroutine/ex.html) | Text | Contains an RTS | 
| [TT54](https://elite.bbcelite.com/c64/main/subroutine/tt54.html) | Universe | Twist the selected system's seeds | 
| [TT60](https://elite.bbcelite.com/c64/main/subroutine/tt60.html) | Text | Print a text token and a paragraph break | 
| [TT66](https://elite.bbcelite.com/c64/main/subroutine/tt66.html) | Drawing the screen | Clear the screen and set the current view type | 
| [TT66simp](https://elite.bbcelite.com/c64/main/subroutine/tt66simp.html) | Drawing the screen | Clear the whole screen inside the border box, and move the text cursor to the top-left corner | 
| [TT67](https://elite.bbcelite.com/c64/main/subroutine/tt67.html) | Text | Print a newline | 
| [TT67K](https://elite.bbcelite.com/c64/main/subroutine/tt67k.html) | Text | Print a newline | 
| [TT68](https://elite.bbcelite.com/c64/main/subroutine/tt68.html) | Text | Print a text token followed by a colon | 
| [TT69](https://elite.bbcelite.com/c64/main/subroutine/tt69.html) | Text | Set Sentence Case and print a newline | 
| [TT70](https://elite.bbcelite.com/c64/main/subroutine/tt70.html) | Universe | Display "MAINLY " and jump to TT72 | 
| [TT72](https://elite.bbcelite.com/c64/main/subroutine/tt25.html) | Universe | Used by TT70 to re-enter the routine after displaying "MAINLY" for the economy type | 
| [TT73](https://elite.bbcelite.com/c64/main/subroutine/tt73.html) | Text | Print a colon | 
| [TT74](https://elite.bbcelite.com/c64/main/subroutine/tt74.html) | Text | Print a character | 
| [TT81](https://elite.bbcelite.com/c64/main/subroutine/tt81.html) | Universe | Set the selected system's seeds to those of system 0 | 
| [TTX110](https://elite.bbcelite.com/c64/main/subroutine/ttx110.html) | Flight | Set the current system to the nearest system and return to hyp | 
| [TTX111](https://elite.bbcelite.com/c64/main/subroutine/hyp.html) | Flight | Used to rejoin this routine from the call to TTX110 | 
| [TTX66](https://elite.bbcelite.com/c64/main/subroutine/ttx66.html) | Drawing the screen | Clear the top part of the screen, draw a border box and configure the specified view | 
| [TTX66K](https://elite.bbcelite.com/c64/main/subroutine/ttx66k.html) | Drawing the screen | Clear the whole screen or just the space view (as appropriate), draw a border box, and if required, show the dashboard | 
| [TTX69](https://elite.bbcelite.com/c64/main/subroutine/ttx69.html) | Text | Print a paragraph break | 
| [TWFL](https://elite.bbcelite.com/c64/main/variable/twfl.html) | Drawing lines | Ready-made character rows for the left end of a horizontal line in the space view | 
| [TWFR](https://elite.bbcelite.com/c64/main/variable/twfr.html) | Drawing lines | Ready-made character rows for the right end of a horizontal line in the space view | 
| [TWOK (Game data)](https://elite.bbcelite.com/c64/game_data/macro/twok.html) | Text | Macro definition for two-letter tokens in the token table | 
| [TWOS](https://elite.bbcelite.com/c64/main/variable/twos.html) | Drawing pixels | Ready-made single-pixel character row bytes for the space view | 
| [TWOS2](https://elite.bbcelite.com/c64/main/variable/twos2.html) | Drawing pixels | Ready-made double-pixel character row bytes for the space view | 
| [TYPE](https://elite.bbcelite.com/c64/main/workspace/zp.html#type) | Workspace variable | The current ship type | 
| [U](https://elite.bbcelite.com/c64/main/workspace/zp.html#u) | Workspace variable | Temporary storage, used in a number of places | 
| [U%](https://elite.bbcelite.com/c64/main/subroutine/u_per_cent.html) | Keyboard | Clear the key logger and reset a number of flight variables | 
| [UNIV](https://elite.bbcelite.com/c64/main/variable/univ.html) | Universe | Table of pointers to the local universe's ship data blocks | 
| [UP](https://elite.bbcelite.com/c64/main/workspace/up.html) | Workspaces | Configuration variables | 
| [UPO](https://elite.bbcelite.com/c64/main/workspace/wp.html#upo) | Workspace variable | This byte appears to be unused | 
| [V](https://elite.bbcelite.com/c64/main/workspace/zp.html#v) | Workspace variable | Temporary storage, typically used for storing an address pointer | 
| [V% (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/v_per_cent.html) | Utility routines | Denotes the end of the second block of loader code, as used in the encryption/decryption process | 
| [value0](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value0) | Workspace variable | An unused counter that increments every time we process music command <#6> | 
| [value1](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value1) | Workspace variable | Stores the voice control register for voice 1 | 
| [value2](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value2) | Workspace variable | Stores the voice control register for voice 2 | 
| [value3](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value3) | Workspace variable | Stores the voice control register for voice 3 | 
| [value4](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value4) | Workspace variable | Stores the rest length for commands #8 and #15 | 
| [value5](https://elite.bbcelite.com/c64/main/workspace/music_variables.html#value5) | Workspace variable | The address before the start of the music data for the tune that is configured to play for docking, so this can be changed to alter the docking music | 
| [var](https://elite.bbcelite.com/c64/main/subroutine/var.html) | Market | Calculate QQ19+3 = economy * |economic_factor| | 
| [VCSU1](https://elite.bbcelite.com/c64/main/subroutine/vcsu1.html) | Maths (Arithmetic) | Calculate vector K3(8 0) = [x y z] - coordinates of the sun or space station | 
| [VCSUB](https://elite.bbcelite.com/c64/main/subroutine/vcsub.html) | Maths (Arithmetic) | Calculate vector K3(8 0) = [x y z] - coordinates in (A V) | 
| [VERTEX (Game data)](https://elite.bbcelite.com/c64/game_data/macro/vertex.html) | Drawing ships | Macro definition for adding vertices to ship blueprints | 
| [vibrato2](https://elite.bbcelite.com/c64/main/workspace/zp.html#vibrato2) | Workspace variable | The vibrato counter for voice 2 | 
| [vibrato3](https://elite.bbcelite.com/c64/main/workspace/zp.html#vibrato3) | Workspace variable | The vibrato counter for voice 3 | 
| [VIEW](https://elite.bbcelite.com/c64/main/workspace/up.html#view) | Workspace variable | The number of the current space view | 
| [voice2hi1](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice2hi1) | Workspace variable | The low byte of the first vibrato frequency for voice 2, which contains the lower frequency | 
| [voice2hi2](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice2hi2) | Workspace variable | The low byte of the second vibrato frequency for voice 2, which contains the higher frequency | 
| [voice2lo1](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice2lo1) | Workspace variable | The high byte of the first vibrato frequency for voice 2, which contains the lower frequency | 
| [voice2lo2](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice2lo2) | Workspace variable | The high byte of the second vibrato frequency for voice 2, which contains the higher frequency | 
| [voice3hi1](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice3hi1) | Workspace variable | The low byte of the first vibrato frequency for voice 3, which contains the lower frequency | 
| [voice3hi2](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice3hi2) | Workspace variable | The low byte of the second vibrato frequency for voice 3, which contains the higher frequency | 
| [voice3lo1](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice3lo1) | Workspace variable | The high byte of the first vibrato frequency for voice 3, which contains the lower frequency | 
| [voice3lo2](https://elite.bbcelite.com/c64/main/workspace/zp.html#voice3lo2) | Workspace variable | The high byte of the second vibrato frequency for voice 3, which contains the higher frequency | 
| [VOWEL](https://elite.bbcelite.com/c64/main/subroutine/vowel.html) | Text | Test whether a character is a vowel | 
| [W% (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/w_per_cent.html) | Utility routines | Denotes the start of the first block of loader code, as used in the encryption/decryption process | 
| [wantdials](https://elite.bbcelite.com/c64/main/subroutine/wantdials.html) | Drawing the screen | Show the dashboard on-screen | 
| [WARP](https://elite.bbcelite.com/c64/main/subroutine/warp.html) | Flight | Perform an in-system jump | 
| [welcome](https://elite.bbcelite.com/c64/main/variable/welcome.html) | Drawing the screen | The background colour for the upper and lower parts of the screen, used by the energy bomb to flash the screen's background colour | 
| [WHITETEXT](https://elite.bbcelite.com/c64/main/subroutine/whitetext.html) | Text | Switch to white text | 
| [widget](https://elite.bbcelite.com/c64/main/workspace/zp.html#widget) | Workspace variable | Temporary storage, used to store the original argument in A in the logarithmic FMLTU and LL28 routines | 
| [WP](https://elite.bbcelite.com/c64/main/workspace/wp.html) | Workspaces | Variables | 
| [WP1](https://elite.bbcelite.com/c64/main/subroutine/wp1.html) | Drawing planets | Reset the ball line heap | 
| [WPLS](https://elite.bbcelite.com/c64/main/subroutine/wpls.html) | Drawing suns | Remove the sun from the screen | 
| [WPLS-1](https://elite.bbcelite.com/c64/main/subroutine/wpls.html) | Drawing suns | Contains an RTS | 
| [WPLS2](https://elite.bbcelite.com/c64/main/subroutine/wpls2.html) | Drawing planets | Remove the planet from the screen | 
| [WPSHPS](https://elite.bbcelite.com/c64/main/subroutine/wpshps.html) | Dashboard | Clear the scanner, reset the ball line and sun line heaps | 
| [WSCAN](https://elite.bbcelite.com/c64/main/subroutine/wscan.html) | Drawing the screen | Wait for the vertical sync | 
| [wW](https://elite.bbcelite.com/c64/main/subroutine/ww.html) | Flight | Start a hyperspace countdown | 
| [wW2](https://elite.bbcelite.com/c64/main/subroutine/ww.html) | Flight | Start the hyperspace countdown, starting the countdown from the value in A | 
| [X% (Game Loader)](https://elite.bbcelite.com/c64/game_loader/variable/x_per_cent.html) | Utility routines | Denotes the end of the first block of loader code, as used in the encryption/decryption process | 
| [X1](https://elite.bbcelite.com/c64/main/workspace/zp.html#x1) | Workspace variable | Temporary storage, typically used for x-coordinates in the line-drawing routines | 
| [X2](https://elite.bbcelite.com/c64/main/workspace/zp.html#x2) | Workspace variable | Temporary storage, typically used for x-coordinates in the line-drawing routines | 
| [XC](https://elite.bbcelite.com/c64/main/workspace/zp.html#xc) | Workspace variable | The x-coordinate of the text cursor (i.e. the text column), which can be from 0 to 32 | 
| [XP](https://elite.bbcelite.com/c64/main/workspace/wp.html#xp) | Workspace variable | This byte appears to be unused | 
| [XSAV](https://elite.bbcelite.com/c64/main/workspace/zp.html#xsav) | Workspace variable | Temporary storage for saving the value of the X register, used in a number of places | 
| [XSAV2](https://elite.bbcelite.com/c64/main/workspace/up.html#xsav2) | Workspace variable | Temporary storage, used for storing the value of the X register in the CHPR routine | 
| [XX](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx) | Workspace variable | Temporary storage, typically used for storing a 16-bit x-coordinate | 
| [XX0](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx0) | Workspace variable | Temporary storage, used to store the address of a ship blueprint. For example, it is used when we add a new ship to the local bubble in routine NWSHP, and it contains the address of the current ship's blueprint as we loop through all the nearby ships in the main flight loop | 
| [XX1](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx1) | Workspace variable | This is an alias for INWK that is used in the main ship-drawing routine at LL9 | 
| [XX12](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx12) | Workspace variable | Temporary storage for a block of values, used in a number of places | 
| [XX13](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx13) | Workspace variable | Temporary storage, typically used in the line-drawing routines | 
| [XX14](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx14) | Workspace variable | This byte appears to be unused | 
| [XX15](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx15) | Workspace variable | Temporary storage, typically used for storing screen coordinates in line-drawing routines | 
| [XX16](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx16) | Workspace variable | Temporary storage for a block of values, used in a number of places | 
| [XX17](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx17) | Workspace variable | Temporary storage, used in BPRNT to store the number of characters to print, and as the edge counter in the main ship-drawing routine | 
| [XX18](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx18) | Workspace variable | Temporary storage used to store coordinates in the LL9 ship-drawing routine | 
| [XX19](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx19) | Workspace variable | XX19(1 0) shares its location with INWK(34 33), which contains the address of the ship line heap | 
| [XX2](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx2) | Workspace variable | Temporary storage, used to store the visibility of the ship's faces during the ship-drawing routine at LL9 | 
| [XX20](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx20) | Workspace variable | Temporary storage, used in a number of places | 
| [XX21 (Game data)](https://elite.bbcelite.com/c64/game_data/variable/xx21.html) | Drawing ships | Ship blueprints lookup table | 
| [XX24](https://elite.bbcelite.com/c64/main/workspace/wp.html#xx24) | Workspace variable | This byte appears to be unused | 
| [XX3](https://elite.bbcelite.com/c64/main/workspace/xx3.html) | Workspaces | Temporary storage space for complex calculations | 
| [XX4](https://elite.bbcelite.com/c64/main/workspace/zp.html#xx4) | Workspace variable | Temporary storage, used in a number of places | 
| [Y1](https://elite.bbcelite.com/c64/main/workspace/zp.html#y1) | Workspace variable | Temporary storage, typically used for y-coordinates in line-drawing routines | 
| [Y2](https://elite.bbcelite.com/c64/main/workspace/zp.html#y2) | Workspace variable | Temporary storage, typically used for y-coordinates in line-drawing routines | 
| [YC](https://elite.bbcelite.com/c64/main/workspace/zp.html#yc) | Workspace variable | The y-coordinate of the text cursor (i.e. the text row), which can be from 0 to 23 | 
| [YESNO](https://elite.bbcelite.com/c64/main/subroutine/yesno.html) | Keyboard | Wait until either "Y" or "N" is pressed | 
| [yetanotherrts](https://elite.bbcelite.com/c64/main/subroutine/yetanotherrts.html) | Tactics | Contains an RTS | 
| [ylookuph](https://elite.bbcelite.com/c64/main/variable/ylookuph.html) | Drawing pixels | Lookup table for converting a pixel y-coordinate to the high byte of a screen address (within the 256-pixel wide game screen) | 
| [ylookupl](https://elite.bbcelite.com/c64/main/variable/ylookupl.html) | Drawing pixels | Lookup table for converting a pixel y-coordinate to the low byte of a screen address (within the 256-pixel wide game screen) | 
| [YP](https://elite.bbcelite.com/c64/main/workspace/wp.html#yp) | Workspace variable | This byte appears to be unused | 
| [ypl](https://elite.bbcelite.com/c64/main/subroutine/ypl.html) | Universe | Print the current system name | 
| [ypl-1](https://elite.bbcelite.com/c64/main/subroutine/ypl.html) | Universe | Contains an RTS | 
| [YS](https://elite.bbcelite.com/c64/main/workspace/wp.html#ys) | Workspace variable | This byte appears to be unused | 
| [YSAV](https://elite.bbcelite.com/c64/main/workspace/zp.html#ysav) | Workspace variable | Temporary storage for saving the value of the Y register, used in a number of places | 
| [YSAV2](https://elite.bbcelite.com/c64/main/workspace/up.html#ysav2) | Workspace variable | Temporary storage, used for storing the value of the Y register in the CHPR routine | 
| [Yx2M1](https://elite.bbcelite.com/c64/main/workspace/zp.html#yx2m1) | Workspace variable | This is used to store the number of pixel rows in the space view minus 1, which is also the y-coordinate of the bottom pixel row of the space view (it is set to 191 in the RES2 routine) | 
| [YY](https://elite.bbcelite.com/c64/main/workspace/zp.html#yy) | Workspace variable | Temporary storage, typically used for storing a 16-bit y-coordinate | 
| [Ze](https://elite.bbcelite.com/c64/main/subroutine/ze.html) | Universe | Initialise the INWK workspace to a fairly aggressive ship | 
| [ZEBC](https://elite.bbcelite.com/c64/main/subroutine/zebc.html) | Utility routines | Zero-fill pages $B and $C | 
| [zebop](https://elite.bbcelite.com/c64/main/variable/zebop.html) | Drawing the screen | The value for VIC register $18 to set the screen RAM address for a raster count of 0 in the interrupt routine (i.e. the space view) | 
| [ZEKTRAN](https://elite.bbcelite.com/c64/main/subroutine/zektran.html) | Keyboard | Clear the key logger | 
| [ZERO](https://elite.bbcelite.com/c64/main/subroutine/zero.html) | Utility routines | Reset the local bubble of universe and ship status | 
| [ZES1](https://elite.bbcelite.com/c64/main/subroutine/zes1.html) | Utility routines | Zero-fill the page whose number is in X | 
| [ZES1k](https://elite.bbcelite.com/c64/main/subroutine/zes1k.html) | Utility routines | Zero-fill the page whose number is in X | 
| [ZES2](https://elite.bbcelite.com/c64/main/subroutine/zes2.html) | Utility routines | Zero-fill a specific page | 
| [ZES2k](https://elite.bbcelite.com/c64/main/subroutine/zes2k.html) | Utility routines | Zero-fill a specific page | 
| [ZESNEW](https://elite.bbcelite.com/c64/main/subroutine/zesnew.html) | Utility routines | Zero-fill memory from SC(1 0) to the end of the page | 
| [ZINF](https://elite.bbcelite.com/c64/main/subroutine/zinf.html) | Universe | Reset the INWK workspace and orientation vectors | 
| [zonkscanners](https://elite.bbcelite.com/c64/main/subroutine/zonkscanners.html) | Drawing the screen | Hide all ships on the scanner | 
| [ZP](https://elite.bbcelite.com/c64/main/workspace/zp.html) | Workspaces | Lots of important variables are stored in the zero page workspace as it is quicker and more space-efficient to access memory here | 
| [ZP (Game Loader)](https://elite.bbcelite.com/c64/game_loader/workspace/zp.html) | Workspaces | Important variables used by the loader | 
| [ZP2 (Game Loader)](https://elite.bbcelite.com/c64/game_loader/workspace/zp.html#zp2) | Workspace variable | Stores addresses used for moving content around | 
| [ZZ](https://elite.bbcelite.com/c64/main/workspace/zp.html#zz) | Workspace variable | Temporary storage, typically used for distance values | 
| [zZ+1](https://elite.bbcelite.com/c64/main/subroutine/ghy.html) | Flight | Contains an RTS |

---
*Fonte originale: [https://elite.bbcelite.com/c64/indexes/a-z.html](https://elite.bbcelite.com/c64/indexes/a-z.html)*
