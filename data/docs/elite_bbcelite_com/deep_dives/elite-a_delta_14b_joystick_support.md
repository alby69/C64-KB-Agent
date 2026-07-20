---
title: Delta 14B joystick support
source_url: https://elite.bbcelite.com/deep_dives/elite-a_delta_14b_joystick_support.html
category: deep-dive
topics:
- memory management
- assembly
- input handling
- basic
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
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

# Delta 14B joystick support

## All the controls of Elite in one single handset - the future is here!

Back in the day, I lived and breathed Elite. I first reached the heady rank of Elite on the BBC Micro cassette version, after months of dedicated flight, huddled away in my teenage bedroom. Eventually I'd saved up enough pocket money to graduate to the disc version, where I started all over again, utterly entranced by the enhanced features. But this time round I thought I'd step it up a notch by buying a joystick, and I settled on the Delta 14B, because it was positively covered in buttons. "I bet I can get this keypad to work with Elite," I thought... incorrectly, it turns out. Still, it was a great joystick, and I made it to Elite all over again, this time as a stick pilot rather than a keyboard jockey.

![The Voltmace Delta 14B joystick and 14B/1 adaptor box](https://elite.bbcelite.com/images/elite_compendium/delta_14b_and_adaptor.jpg) 

						I now realise that it was hopeless to try to get the Delta 14B keypad working with Elite. Elite has no spare memory for the sample code that comes with the joystick, which I thought would let me map joystick buttons to key presses, so that idea fizzled out pretty quickly. Not only that, but I hadn't realised that for the Delta 14B keypad to work at all, you need a separate adaptor box (the Delta 14B/1) that plugs into the BBC Micro's user port. I didn't have that box, so the whole enterprise was doomed from the start.

Angus Duggan no doubt saw the same potential in the Delta 14B keypad, because Elite-A supports it fully. You need the aforementioned adaptor box as well as the joystick, but if you've got the hardware, then the joystick's keypad supports the following layout (the top two fire buttons are treated the same as the top button in the middle row):

Fire laser Fire laser Slow down Fire laser Speed up Unarm missile Fire missile Target missile Hyperspace Unit E.C.M. Escape pod Docking computer off In-system jump Docking computer on

Note that this is different to the layout in [Angus's documentation](http://knackered.org/angus/beeb/elite.html#Delta-14B%20controls), as he has the docking computer buttons the wrong way around in his instructions.

Let's see how Angus added this dream functionality to Elite-A.

## Rows and columns

													 ----------------

						The user guide for the Delta 14B explains how to program the BBC Micro to detect key presses on the joystick's keypad. If you fancy a walk down memory lane you can [view it as a PDF](https://elite.bbcelite.com/pdfs/Delta_14b_Handset_System.pdf), but to save you wading through all the photocopier artifacts in the paper version, here's how to do it.

Before doing anything else, we have to configure the user port so we can use it to read the joystick buttons. We do this in the [loader](https://elite.bbcelite.com/elite-a/loader/subroutine/elite_loader_part_1_of_3.html) by setting the Data Direction Register (DDR) of port B of the user port so we can read the button states. We set PB4 to PB7 as output (so we can write to the button columns to select the column we are interested in) and PB0 to PB3 as input (so we can read from the button rows to see if anything in that column is being pressed). Let's see why we set it up this way.

First, there are actually two ports on the adaptor box, for two joysticks. There is a side socket, and a rear socket. We don't know which one our joystick is plugged into, so we need to check both.

Next, we can't just ask the joystick which button is being pressed - instead, we have to scan for specific keys. So, if we want to find out if anything is being pressed, we have to loop through all the keys, doing this once for the side socket joystick and a second time for the rear socket joystick.

To scan for a specific key on a specific joystick, we need to ask the adaptor to scan a specific column of keys on the correct socket, and then we have to read the response to determine whether any of the buttons in that column are being pressed. We do this by sending PB4 to PB7 (i.e. bits PB4 = bit 4 to PB7 = bit 7) to the user port, as follows.

If we want to check the side socket joystick (bit 7 set):

%1110xxxx = read buttons in left column (bit 4 clear) %1101xxxx = read buttons in middle column (bit 5 clear) %1011xxxx = read buttons in right column (bit 6 clear)

If we want to check the rear socket joystick (bit 7 clear):

%0110xxxx = read buttons in left column (bit 4 clear) %0101xxxx = read buttons in middle column (bit 5 clear) %0011xxxx = read buttons in right column (bit 6 clear)

Having told the adaptor which column and which joystick we want to scan, we now have to read the result. We do this by reading PB0 to PB3 from the user port (PB0 = bit 0 to PB3 = bit 4), which tells us whether any buttons in the specified column are being pressed, and if they are, in which row. The values read are as follows:

%1111 = no button is being pressed in this column %1110 = button pressed in top row (bit 0 clear) %1101 = button pressed in second row (bit 1 clear) %1011 = button pressed in third row (bit 2 clear) %0111 = button pressed in bottom row (bit 3 clear)

In other words, if a button is being pressed in the top row in the previously specified column, then PB0 (bit 0) will go low in the value we read from the user port.

## Integrating into Elite-A

													 ------------------------

						Angus integrated this whole process into Elite-A in the [b_14](https://elite.bbcelite.com/elite-a/flight/subroutine/b_14.html) routine, which scans the joystick to see if a specified flight key is being pressed. It's a very efficient bit of programming, which is essential as free space in the flight code is really tight (see the deep dive on [making room for the modifications in Elite-A](https://elite.bbcelite.com/elite-a_making_room_for_the_modifications.html) for the gory details).

The b_14 routine looks up a corresponding byte for the specified flight key from the [b_table](https://elite.bbcelite.com/elite-a/flight/variable/b_table.html) table, which returns a byte containing the row and column of the corresponding Delta 14B button. Bits 4-6 of the top nibble of the value gives the column:

&6x = %x110xxxx = left column &5x = %x101xxxx = middle column &3x = %x011xxxx = right column

while the lower nibble gives the row:

&x1 = %xxxx0001 = top row &x2 = %xxxx0010 = second row &x4 = %xxxx0100 = third row &x8 = %xxxx1000 = bottom row

The routine then sends the column details to the adaptor box and checks the results, first with bit 7 set (for the side socket) and again with bit 7 clear (for the rear socket). The values in b_table are also designed to stop the routine from scanning the adaptor if the specified flight key is a roll or pitch key. These are dealt with separately by the game's normal joystick code, as the stick part of the Delta 14B is read via the standard analogue port, just like any other joystick.

Somehow, after all these years, reading the code that makes the Delta 14B work in Elite gives me great pleasure; it is a feature I would have been thrilled to experience back in the mid-1980s, and it's still impressive, despite the intervening decades. All I need to do is track down one of those adaptor boxes, which are rarer than hen's teeth.

But there is good news! You can buy a modern recreation of the Delta 14B/1 adaptor box from Stardot user ukwebb (see [this thread for details](https://stardot.org.uk/forums/viewtopic.php?t=24981)). I am happy to report that it works a treat, so that's another childhood dream ticked off the list. Thank you ukwebb, what a great product; finally, I get to play Elite using all the buttons on my trusty Delta 14B keypad. The future has definitely arrived...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Fire laser                                    Fire laser
  Slow down              Fire laser             Speed up
  Unarm missile          Fire missile           Target missile
  Hyperspace Unit        E.C.M.                 Escape pod
  Docking computer off   In-system jump         Docking computer on
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
%1110xxxx = read buttons in left column   (bit 4 clear)
  %1101xxxx = read buttons in middle column (bit 5 clear)
  %1011xxxx = read buttons in right column  (bit 6 clear)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
%0110xxxx = read buttons in left column   (bit 4 clear)
  %0101xxxx = read buttons in middle column (bit 5 clear)
  %0011xxxx = read buttons in right column  (bit 6 clear)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
%1111 = no button is being pressed in this column
  %1110 = button pressed in top row    (bit 0 clear)
  %1101 = button pressed in second row (bit 1 clear)
  %1011 = button pressed in third row  (bit 2 clear)
  %0111 = button pressed in bottom row (bit 3 clear)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
&6x = %x110xxxx = left column
  &5x = %x101xxxx = middle column
  &3x = %x011xxxx = right column
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
&x1 = %xxxx0001 = top row
  &x2 = %xxxx0010 = second row
  &x4 = %xxxx0100 = third row
  &x8 = %xxxx1000 = bottom row
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/elite-a_delta_14b_joystick_support.html](https://elite.bbcelite.com/deep_dives/elite-a_delta_14b_joystick_support.html)*
