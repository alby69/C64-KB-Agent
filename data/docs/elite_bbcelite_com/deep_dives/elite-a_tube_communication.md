---
title: Tube communication in Elite-A
source_url: https://elite.bbcelite.com/deep_dives/elite-a_tube_communication.html
category: deep-dive
topics:
- basic
- assembly
- input handling
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

# Tube communication in Elite-A

## How the 6502 Second Processor version of Elite-A talks over the Tube

Perhaps it was because Angus Duggan developed Elite-A on a BBC Micro with a 6502 Second Processor, but when he took the [disc version of Elite](https://elite.bbcelite.com/disc/) and added all that extra functionality to the game, he also assembled a separate version of the game for the 6502 Second Processor that loads automatically if active Tube hardware is detected.

![The 6502 Second Processor](https://elite.bbcelite.com/images/6502sp/second_processor.jpg) 

						The Second Processor has lots of memory, so this version doesn't have to access the disc when jumping between the docked, flight and encyclopedia codebases, and instead can load all three in memory at the same time. It also has a [more sophisticated ship blueprints system](https://elite.bbcelite.com/elite-a_ship_blueprints.html) that doesn't have to rely on loading files from disc, and because the 6502 Second Processor has a faster processor than the BBC Micro, it runs more smoothly, too.

Just like the [official 6502 Second Processor version of Elite](https://elite.bbcelite.com/6502sp/), the Second Processor version of Elite-A splits the codebase into two, with one part running on the parasite (the Second Processor) and the other part on the I/O processor (the BBC Micro). The former contains all the game logic, while the latter deals with input and output, such as drawing, scanning the keyboard and making sound effects. The two parts communicate with each over via the Tube - the data bus that connects the I/O processor to the parasite - and in this way the sophisticated game algorithms benefit from the faster processor and larger memory of the parasite, while the BBC Micro can concentrate on interfacing with the world and managing the screen.

## Talking over the Tube

													 ---------------------

						Not surprisingly, the official Acornsoft version of 6502 Second Processor Elite uses the Acorn-recommended approach to communication across the Tube, hooking into the WRCHV and WORDV vectors to allow single-byte and block-based commands to be transmitted between the two using custom calls to the standard OSWRCH and OSWORD routines (see the deep dive on ["6502 Second Processor Tube communication"](https://elite.bbcelite.com/6502sp_tube_communication.html) for details). The details of how the Tube works are hidden from the game code; everything just works.

Elite-A, on the other hand, communicates over the Tube in a much more bare-bones manner, without relying on the operating system's own routines. The result is a simple and very effective system that, surprisingly, is quite a bit easier to understand than the official version.

Let's start with a quick look at how the Tube actually works.

The Tube is a two-way data bus that supports four communication channels, each of which can pass a byte of data in either direction. All four channels are memory-mapped to addresses in the MOS space, so as far as the code is concerned, we just need to access these mapped locations to transmit data over the Tube or check a channel's status.

The communication channels are all FIFOs ("First In, First Out"), so we refer to them as FIFO 1, FIFO 2, FIFO 3 and FIFO 4. Each end of each of these FIFOs has both a memory-mapped status register and memory-mapped data register - the first tells us whether the FIFO is empty or not, while the second contains the actual data. For example, the I/O processor maps the FIFO 1 status and data registers to &FEE0 and &FEE1, while the parasite maps its FIFO 1 status and data registers to &FEF8 and &FEF9.

Now let's take a look at how Elite-A uses the FIFOs to connect the parasite and the I/O processor codebases together.

## Elite-A's Tube protocol

													 -----------------------

						To see how Elite-A uses the FIFO registers to transmit data over the Tube, let's consider the specific example of sending a byte from the parasite to the I/O processor using FIFO 1. Here's how the process breaks down:

- On the parasite side, we check the FIFO 1 status register to make sure it's empty. If it isn't empty, then we simply wait until it is, using a polling loop.
- Still on the parasite side, we now set the FIFO 1 data register to the value we want to transmit.
- If we are not expecting a response from the I/O processor, then our work here is done, and we can go off and do something else. If we are expecting a response from the I/O processor, then we wait until we receive it, again using a polling loop, but this time monitoring the FIFO 2 channel's status and data registers for the response.
- Meanwhile, the I/O processor has already been set up to listen for communication from the parasite on FIFO 1 (as discussed in the next section), so the above activity in the parasite triggers a handler on the I/O processor, which checks the FIFO 1 status register, and waits until it is showing as full.
- The I/O processor then reads the transmitted value from the FIFO 1 data register, and processes it accordingly (see the section on Tube commands below).
- If the parasite is expecting a reply, then the I/O processor sends it back to the parasite using a similar process, but using FIFO 2.

This exact process is implemented by two routines. The [tube_write](https://elite.bbcelite.com/elite-a/parasite/subroutine/tube_write.html) routine on the parasite sends a byte to the I/O processor using FIFO 1, and this byte gets read from FIFO 1 by the [tube_get](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_get.html) routine on the I/O processor side.

The process for sending data back to the parasite is pretty similar, but the sender and receiver are the other way round and FIFO 2 is used. In this case, the [tube_put](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_put.html) routine on the I/O processor sends a byte to the parasite using FIFO 2, and this byte gets read from FIFO 2 by the [tube_read](https://elite.bbcelite.com/elite-a/parasite/subroutine/tube_read.html) routine on the parasite side.

The following table summarises this protocol:

| Parasite -> I/O processor | I/O processor -> Parasite | |
|---|---|---|
| Channel | FIFO 1 | FIFO 2 | 
| Send routine | [tube_write](https://elite.bbcelite.com/elite-a/parasite/subroutine/tube_write.html)(Parasite) | [tube_put](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_put.html)(I/O processor) | 
| Receive routine | [tube_get](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_get.html)(I/O processor) | [tube_read](https://elite.bbcelite.com/elite-a/parasite/subroutine/tube_read.html)(Parasite) | 

So, to keep things simple and to avoid traffic collisions, Elite-A only transmits in one direction on each of FIFOs 1 and 2, and it doesn't use FIFOs 3 or 4 at all. This restricts communication to a minimal set of one-byte transmissions, which is a lot simpler than in the official 6502 Second Processor version.

## Listening using WRCHV

													 ---------------------

						There is one more important aspect to this process. Most of the time, the main game is running independently on the parasite, while the I/O processor sits there relatively idle, waiting for commands from the parasite. This behaviour is set up by the Tube's own host code, which sets up a default listener on FIFO 1 to process any bytes that are received. This means that as soon as the computer is turned on and has started up, the I/O processor starts listening to the parasite.

The default listener is pointed to by the WRCHV vector, which is the handler for OSWRCH, and this is no coincidence - by default, OSWRCH calls on the parasite just send their arguments to the I/O processor on FIFO 1, which runs the handler in WRCHV to write that character. So all we need to do in Elite-A to set up our custom Tube communication protocol is to hook into WRCHV on the I/O processor, and then our handler will be called whenever a byte is sent from the parasite to the I/O processor.

Indeed, the code in the parasite's [tube_write](https://elite.bbcelite.com/elite-a/parasite/subroutine/tube_write.html) routine, which is the one that sends a byte from the parasite to the I/O processor, is 100% identical to Acorn's MOS routine that runs on the parasite to implement OSWRCH across the Tube, while [tube_get](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_get.html) contains the same code as the MOS when it fetches the transmitted data on the I/O processor end.

The hook into the I/O processor's WRCHV handler is set up by the [tube_elite](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_elite.html) routine that runs when the Elite-A I/O processor code first loads. This points WRCHV to the [tube_wrch](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_wrch.html) routine, which handles all bytes received from the parasite on FIFO 1. If a byte received on FIFO 1 has bit 7 set (i.e. it is >= 128, or >= &80), then this means it represents an Elite-A Tube command rather than an ASCII character to be printed, so it gets passed to the [tube_func](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_func.html) routine, which in turn calls the relevant routine from the lookup table in [tube_table](https://elite.bbcelite.com/elite-a/i_o_processor/variable/tube_table.html). Otherwise the character is processed as an ASCII character, and is written to the screen (or makes a beep, or whatever is appropriate for that ASCII code).
						

As discussed in the previous section, the same communication protocol is used in [tube_put](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_put.html) and [tube_read](https://elite.bbcelite.com/elite-a/parasite/subroutine/tube_read.html) to return data to the parasite, except they use FIFO 2 instead of FIFO 1. Using FIFO 2 means that transmission from the I/O processor to the parasite does not trigger any kind of handler in the parasite, so if we want to send data from the I/O processor to the parasite, we have to make sure we are listening on the parasite end by explicitly calling tube_read, which blocks the parasite until a value is received on FIFO 2. If we didn't do this, FIFO 2 would store the data but it would never empty out, thus stopping anything else being transmitted on that channel and bringing the game to a halt.

## Elite-A's Tube commands

													 -----------------------

						Now that we know how Elite-A communicates over the Tube, let's take a look at what it actually does with that communication. Like the official version, Elite-A supports a set of commands that the parasite can send to the I/O processor, and some of these commands return values back to the parasite. Unlike the official version, all the Elite-A commands are sent as simple sequences of single bytes, one after the other, which makes things a lot simpler to follow.

The following table lists all the commands that can be sent. Each command has a unique number, shown in the first column, that is sent as the first byte, and this is followed up by the command parameters, in the order shown in brackets. So, to send a draw_line(x1, y1, x2, y2) command to the I/O processor to tell it to draw a line on-screen, the parasite would first send the command number, &80, followed by x1, y1, x2 and y2 (the line's start and end coordinates). When the parasite receives the first byte, this triggers a call to [tube_wrch](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_wrch.html), as described in the previous section. This calls [LL30](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/loin_part_1_of_7.html) - the corresponding I/O processor routine for this command as shown in the table - which then fetches the parameters from the parasite using [tube_get](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_get.html), and draws the line. See the parasite's [LL30](https://elite.bbcelite.com/elite-a/parasite/subroutine/ll30.html) routine for an example of this in action.

Most commands just perform a task ("draw a line", "clear the screen" and so on), but some commands need to return data to the parasite. These commands have an = sign before the command name, as in =scan_xin(key_number), which scans the keyboard for the specified key and returns the result to the parasite. In this case the process is as follows. The parasite sends the command number, &8B, followed by the parameter, which is the internal number of the key to be scanned, and it then calls the [tube_read](https://elite.bbcelite.com/elite-a/parasite/subroutine/tube_read.html) routine to wait for the result. Meanwhile, the I/O processor receives the command number and calls [scan_xin](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/scan_xin.html), which receives the parameter, calls the [DKS4](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/dks4.html) routine to scan the keyboard, and sends the result back to the parasite by calling [tube_put](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_put.html). See the parasite's [DKS4](https://elite.bbcelite.com/elite-a/parasite/subroutine/dks4.html) routine for an example of this in action.

Here, then, is the complete set of Elite-A Tube commands:

| # | Command | Action | Routine | 
|---|---|---|---|
| &80 | draw_line(x1, y1, x2, y2) | Draw a line | [LL30](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/loin_part_1_of_7.html) | 
| &81 | draw_hline(x1, y1, x2) | Draw a horizontal line | [HLOIN](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/hloin.html) | 
| &82 | draw_pixel(x, y, distance) | Draw space view pixels | [PIXEL](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/pixel.html) | 
| &83 | clr_scrn() | Clear the screen | [clr_scrn](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/clr_scrn.html) | 
| &84 | clr_line() | Clear bottom of screen | [CLYNS](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/clyns.html) | 
| &85 | =sync_in() | Wait for vertical sync | [sync_in](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/sync_in.html) | 
| &86 | draw_bar(value, colour, screen_low, screen_high) | Update bar-based dashboard indicator | [DILX](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/dilx.html) | 
| &87 | draw_angle(value, screen_low, screen_high) | Update roll/pitch dashboard indicator | [DIL2](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/dil2.html) | 
| &88 | put_missle(number, colour) | Update missile indicator | [MSBAR](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/msbar.html) | 
| &89 | =scan_fire() | Check joystick fire button | [scan_fire](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/scan_fire.html) | 
| &8A | =write_fe4e(value) | Set 6522 System VIA IER | [write_fe4e](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/write_fe4e.html) | 
| &8B | =scan_xin(key_number) | Scan the keyboard for a specific key | [scan_xin](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/scan_xin.html) | 
| &8C | =scan_10in() | Scan the keyboard | [scan_10in](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/scan_10in.html) | 
| &8D | =get_key() | Wait for keypress | [get_key](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/get_key.html) | 
| &8E | write_xyc(x, y, char) | Write character to screen | [CHPR](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/chpr.html) | 
| &8F | write_pod(escp, hfx) | Set escape pod/hyperspace palette | [write_pod](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/write_pod.html) | 
| &90 | draw_blob(x, y, colour) | Draw a dot on the dashboard | [draw_blob](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/draw_blob.html) | 
| &91 | draw_tail(x, y, base_colour, alt_colour, height) | Draw a ship on the 3D scanner | [draw_tail](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/draw_tail.html) | 
| &92 | draw_S() | Toggle S dashboard bulb | [SPBLB](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/spblb.html) | 
| &93 | draw_E() | Toggle E dashboard bulb | [ECBLB](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/ecblb.html) | 
| &94 | draw_mode() | Switch line-drawing logic (EOR/OR) | [UNWISE](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/unwise.html) | 
| &95 | write_crtc(rows) | Show or hide the dashboard | [DET1](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/det1.html) | 
| &96 | =scan_y(key_offset, delta_14b) | Scan the keyboard for a flight key | [scan_y](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/scan_y.html) | 
| &97 | write_0346(value) | Update LASCT | [write_0346](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/write_0346.html) | 
| &98 | =read_0346() | Read LASCT | [read_0346](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/read_0346.html) | 
| &99 | return() | Do nothing | [return](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/tube_func.html#return) | 
| &9A | picture_h(line_count, multiple_ships) | Draw horizontal lines for hangar | [HANGER](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/hanger.html) | 
| &9B | picture_v(line_count) | Draw vertical lines for hangar | [HA2](https://elite.bbcelite.com/elite-a/i_o_processor/subroutine/ha2.html) | 

For more information on what each command does, click on the routine name to see the relevant I/O processor code, as this shows the code that is executed when the parasite sends that command.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/elite-a_tube_communication.html](https://elite.bbcelite.com/deep_dives/elite-a_tube_communication.html)*
