---
title: 6502 Second Processor Tube communication
source_url: https://elite.bbcelite.com/deep_dives/6502sp_tube_communication.html
category: deep-dive
topics:
- sprite programming
- basic
- assembly
- memory management
- graphics
difficulty: intermediate
language: mixed
hardware:
- CPU
- KERNAL
- CIA
- VIC-II
related:
- keyboard-handling
- joystick-reading
- raster-interrupts
- memory-map
- sprite-programming
- vic-ii-registers
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
---

# 6502 Second Processor Tube communication

## How the 6502 Second Processor version of Elite talks over the Tube

One of the more intriguing features of the BBC Micro is the Tube interface, which allows users to expand their systems by adding "Second Processors". Sporting a distinctive wedge-shaped box design, this range of expansion boxes included 6502, Z80 and 32016 Second Processor options, and by 1986 there was even an ARM Evaluation System available containing a 6.66 Mhz ARM1 processor, the first version of the now ubiquitous ARM processor.

![The 6502 Second Processor](https://elite.bbcelite.com/images/6502sp/second_processor.jpg) 

						The basic concept of the Tube system is that the fast processor in the expansion box runs the majority of tasks, delegating input and output to the attached BBC Micro (input and output in this context meaning keyboard, display, keyboard, sound and so on). In this relationship the BBC Micro is known as the "I/O processor" (or sometimes the "host"), while the Second Processor is known as the "parasite". Communication between the two is via the high-speed Tube interface, and both computers run independently using their own CPUs and memory.

The 6502 Second Processor version of Elite has become the poster child for the Tube system. The main game code runs on the 6502 Second Processor, with its 3 MHz 65C02 processor and 64K of RAM, and it uses the BBC Micro, with its 2 Mhz 6502 processor and 32K of RAM, to manage the display and keyboard. This enables the game to have more colours with faster graphics, and the extra memory in the parasite lets the game load all the ship blueprints at once, as well as supporting nearly twice as many concurrent ships in the local bubble.

One of the reasons for Elite's reputation as a Second Processor killer app is that it is naturally suited to such a split. Most games from this era were based on bitmap graphics, from space-invading sprites to platform-jumping cavemen, but the 3D universe at the heart of Elite is mathematical, and it's drawn using vector graphics that are made up of lines rather than dots. A line can be described succinctly using just four bytes - two bytes for the (X1, Y1) start point and two more for the (X2, Y2) endpoint - and this lends itself beautifully to the Second Processor setup. The parasite does all the complicated vector mathematics with its faster processor, and it sends the results to the I/O processor as relatively small bundles of coordinate data, which the BBC Micro then draws on-screen. It's a perfect fit for the Tube-based system.

## Talking over the Tube

													 ---------------------

						There are various ways that the parasite and I/O processor can communicate, and for programs that use the standard OS commands, most of the heavy lifting is done by the Tube code that's built into the system. For example, when saving and loading commander files in the [QUS1](https://elite.bbcelite.com/6502sp/main/subroutine/qus1.html) routine, the parasite just calls the standard OSFILE routine and the system takes care of the rest - there's no need to contact the I/O processor explicitly.

Elite, however, needs to tell the I/O processor what to do, and for that the parasite needs to be able to communicate with its host. It uses two broadly similar approaches, one using OSWRCH to send single bytes to the I/O processor, and the other using OSWORD to send and receive larger blocks of data. The idea behind the two approaches is the same: the parasite issues commands to the I/O processor to get it to update the screen, scan the keyboard and so on, thus splitting up the work in an efficient manner. When it comes to 6502 Second Processor Elite, two heads are better than one.

These special commands are implemented by custom OSWRCH and OSWORD handlers in the I/O processor. These are installed in the usual manner by redirecting the WRCHV and WORDV vectors to custom handlers, in this case to the [USOSWRCH](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/usoswrch.html) and [NWOSWD](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/nwoswd.html) routines. These routines use the address tables at [JMPTAB](https://elite.bbcelite.com/6502sp/i_o_processor/variable/jmptab.html) and [OSWVECS](https://elite.bbcelite.com/6502sp/i_o_processor/variable/oswvecs.html) to jump to the relevant routines in the I/O processor code to implement the specified commands.

## The OSWRCH commands

													 -------------------

						Elite implements custom OSWRCH commands for values of A from 128 to 147. In the commentary, we might therefore refer to the OSWRCH 129 command (which tells the I/O processor we are about to send over a batch of line coordinates for drawing), or the OSWRCH 130 command (which sends one of those line coordinates, and tells the I/O processor to draw the line once the last coordinate is sent). Some of these commands have associated configuration variables for their numbers, so we might talk about the #SETXC command, which moves the text cursor to a specific column, for example. The SETXC variable has the value 133, so this is the same as the OSWRCH 133 command, but using the variable name makes things a bit easier to follow. Here's a list of supported commands:

| Offset | Variable | OSWRCH # | Action | I/O routine | 
|---|---|---|---|---|
| 0 | 128 (&80) | Put back to USOSWRCH | [USOSWRCH](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/usoswrch.html) | |
| 1 | 129 (&81) | Begin drawing a line | [BEGINLIN](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/beginlin.html) | |
| 2 | 130 (&82) | Add line byte/draw line | [ADDBYT](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/addbyt.html) | |
| 3 | #DOFE21 | 131 (&83) | Show energy bomb effect | [DOFE21](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dofe21.html) | 
| 4 | #DOhfx | 132 (&84) | Show hyperspace colours | [DOHFX](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dohfx.html) | 
| 5 | #SETXC | 133 (&85) | Set text cursor column | [SETXC](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/setxc.html) | 
| 6 | #SETYC | 134 (&86) | Set text cursor row | [SETYC](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/setyc.html) | 
| 7 | #clyns | 135 (&87) | Clear bottom of screen | [CLYNS](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/clyns.html) | 
| 8 | #RDPARAMS | 136 (&88) | Update dashboard | [RDPARAMS](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/rdparams.html) | 
| 9 | 137 (&89) | Add dashboard parameter | [ADPARAMS](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/adparams.html) | |
| 10 | #DODIALS | 138 (&8A) | Show or hide dashboard | [DODIALS](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dodials.html) | 
| 11 | #VIAE | 139 (&8B) | Set 6522 System VIA IER | [DOVIAE](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/doviae.html) | 
| 12 | #DOBULB | 140 (&8C) | Toggle dashboard bulb | [DOBULB](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dobulb.html) | 
| 13 | #DOCATF | 141 (&8D) | Set disc catalogue flag | [DOCATF](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/docatf.html) | 
| 14 | #SETCOL | 142 (&8E) | Set the current colour | [DOCOL](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/docol.html) | 
| 15 | #SETVDU19 | 143 (&8F) | Change mode 1 palette | [SETVDU19](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/setvdu19.html) | 
| 16 | #DOsvn | 144 (&90) | Set file saving flag | [DOSVN](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dosvn.html) | 
| 17 | 145 (&91) | Execute BRK instruction | [DOBRK](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dobrk.html) | |
| 18 | #printcode | 146 (&92) | Write to printer/screen | [printer](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/printer.html) | 
| 19 | #prilf | 147 (&93) | Blank line on printer | [prilf](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/prilf.html) | 

OSWRCH transmits just one byte to the I/O processor, the value of A, so that's the only parameter that's available to the handler in USOSWRCH. The I/O processor supports parameters for OSWRCH commands by switching the handler address to that in the JMPTAB jump table (i.e. the routine in the last column above), and the handler accepts subsequent OSWRCH calls until all the expected parameters have been received, at which point it switches the handler back to USOSWRCH by calling the [PUTBACK](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/putback.html) routine. This means that although each OSWRCH command only passes one byte, we can use multiple OSWRCH calls to pass multiple parameters - they just get passed one call at a time. (It also means that OSWRCH calls that don't take a parameter, such as the #RDPARAMS command, still need to call OSWRCH twice, as we need a second call to put the USOSWRCH handler back, even though the second call does nothing else.)

For example, the aforementioned #SETXC command takes an argument containing the new column number for the text cursor (we can refer to the full version as the #SETXC <col> command). The full command gets sent by two calls to OSWRCH, as in this example, which moves the text cursor to column 10:

LDA #SETXC \ Send the first part of a #SETXC command to the I/O JSR OSWRCH \ processor LDA #10 \ Send the column number to the I/O processor JSR OSWRCH

The most extreme example of an OSWRCH call with parameters is the #RDPARAMS command, which tells the I/O processor to expect a set of 15 dashboard values, such as speed and altitude. Once all 15 are received, the I/O processor updates the various dials on the dashboard. You can see these OSWRCH calls in the parasite's [DIALS](https://elite.bbcelite.com/6502sp/main/subroutine/dials.html) routine, each of which triggers either the I/O processor's [RDPARAMS](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/rdparams.html) routine (for the first command, which tells the I/O processor to expect a batch of dashboard values) or the [ADPARAMS](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/adparams.html) routine (for all the calls that actually send those values).

## The OSWORD commands

													 -------------------

						The other approach to Tube communication in Elite is via the OSWORD command. While the OSWRCH command can send one byte of information in one direction (to the I/O processor) with each call, OSWORD commands can both send and receive entire blocks of data, with up to 128 bytes being transmitted between the parasite and I/O processor as part of each call. For OSWORD calls with A >= 128, this data transmission is automatically handled by the Tube's own host code, so it's an ideal way to pass large amounts of data between the second processor and the BBC Micro. Here's a list of supported commands:

| Offset | Variable | OSWORD # | Action | I/O routine | 
|---|---|---|---|---|
| 0 | 240 (&F0) | Scan the keyboard | [KEYBOARD](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/keyboard.html) | |
| 1 | 241 (&F1) | Draw space view pixels | [PIXEL](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/pixel.html) | |
| 2 | #DOmsbar | 242 (&F2) | Update missile indicators | [MSBAR](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/msbar.html) | 
| 3 | #wscn | 243 (&F3) | Wait for vertical sync | [WSCAN](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/wscan.html) | 
| 4 | #onescan | 244 (&F4) | Draw a ship on the 3D scanner | [SC48](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/sc48.html) | 
| 5 | #DOdot | 245 (&F5) | Draw a dot on the compass | [DOT](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dot.html) | 
| 6 | #DODKS4 | 246 (&F6) | Scan for a specific key | [DODKS4](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/dodks4.html) | 
| 7 | 247 (&F7) | Draw orange sun lines | [HLOIN](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/hloin.html) | |
| 8 | 248 (&F8) | Display the ship hangar | [HANGER](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/hanger.html) | |
| 9 | 249 (&F9) | Copy protection | [SOMEPROT](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/someprot.html) | 

Elite implements OSWORD commands for values of A from 240 to 249, and as with OSWRCH, some have associated variables, so we might talk about the OSWORD 240 command that scans the keyboard and returns the result, or the #onescan command that draws a ship on the 3D scanner, for example.

When the parasite calls OSWORD to send a command to the I/O processor, it sets (Y X) to point to the parameter block. The first byte of the block contains the number of bytes that will be transmitted with this command, while the second byte contains the number of bytes that will be sent back from the I/O processor once the command has finished executing (both of these counts should include these two bytes, so a value of 2 indicates that no parameters are transmitted in that direction). When the call is made to OSWORD, a block the size of the first parameter is copied from the parasite to the I/O processor, and the OSWORD handler is called with (Y X) pointing to the copied bytes. When the handler finishes, a block the size of the second parameter is copied from the I/O processor back to the parasite, overwriting the original parameter block. Up to 128 bytes can be transmitted either way using this approach.

Apart from the payload size, there's another important difference between OSWRCH and OSWORD. Calls to OSWRCH return immediately, so when the parasite issues an OSWRCH command, the I/O processor starts working on it while the parasite goes back about its business. It's a bit like having a two-core processor on-hand, and it means that when the parasite sends the last coordinate in a long sequence of lines, or it sends the last value in a dashboard update, then the main game running on the parasite can get straight back to running the game while the BBC Micro updates the screen. OSWORD calls, on the other hand, do not have this kind of parallel processing, and instead the parasite will stop and wait after sending the OSWORD command, until the I/O processor responds by returning an updated parameter block. It's a bit like the difference between simply issuing an order (OSWRCH) and having a conversation (OSWORD).

## Putting it all together

													 -----------------------

						So the parasite and I/O processor communicate, and code runs on both processors at various times, but how does Elite set up this meeting of digital minds? It's all in the loader, which, once it has configured things like the screen mode and sound effects and drawn the loading screen, then *RUNs not one but two different binaries:

- I.CODE is the I/O processor's game code, which loads at &2400 in the BBC Micro (the file has a load address of &FFFF2400, and the &FFFF part specifies it should load into the I/O processor)
- P.CODE is the parasite's game code, which loads at &1000 in the Second Processor (the file has a load address of &00001000, and the &0000 part specifies it should load into the parasite)

When I.CODE is run in the I/O processor, it sets up the vector handlers mentioned above and terminates, leaving the BBC Micro just sitting there, twiddling its thumbs. Meanwhile P.CODE starts up on the parasite, and starts issuing OSWRCH and OSWORD commands across the Tube, asking the I/O processor to update the screen, scan the keyboard and so on, at which point the BBC Micro perks up and does what it's told.

It's almost as if the 6502 Second Processor is the quick-thinking pilot, while the BBC Micro is the ship, with its sensors and screens and chattering disc drives...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDA #SETXC            \ Send the first part of a #SETXC command to the I/O
  JSR OSWRCH            \ processor

  LDA #10               \ Send the column number to the I/O processor
  JSR OSWRCH
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/6502sp_tube_communication.html](https://elite.bbcelite.com/deep_dives/6502sp_tube_communication.html)*
