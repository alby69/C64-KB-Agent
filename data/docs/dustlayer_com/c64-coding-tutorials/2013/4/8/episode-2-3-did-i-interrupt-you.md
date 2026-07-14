---
title: ''
source_url: https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-3-did-i-interrupt-you
category: tutorial
topics:
- assembly
- basic
- raster interrupts
- sprite programming
difficulty: beginner
language: mixed
hardware:
- SID
- KERNAL
- CPU
- VIC-II
- CIA
related:
- kernal-routines
- keyboard-handling
- sprite-programming
- sound-programming
- joystick-reading
- raster-interrupts
- sid-registers
- cia-registers
- music-player
- memory-map
- vic-ii-registers
scraped_at: '2026-07-14'
---


# 

# Episode 2-3: Did I interrupt you?

**Topics:** Many C64 programmers did avoid dealing with interrupts yet it is only thing that lets us create really cool things on the C64. There are various types of interrupts, we start with a very simple one.  

**Download via  dust:** $ dust tutorials (select 'first intro') 

**Github Repository:**

[First Intro on Github](https://github.com/actraiser/dust-tutorial-c64-first-intro)

- [Episode 2-1: Let's compile and run C64 code](http://dustlayer.com/c64-coding-tutorials/2013/2/17/a-simple-c64-intro)
- [Episode 2-2: Writing to the C64 Screen](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-2-writing-to-the-c64-screen)
- **Episode 2-3: Did I interrupt you?**
- [Episode 2-4: Effects using a table of data](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-4-reading-from-a-data-table)
- [Episode 2-5: Understanding and including music](http://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-5-understanding-and-including-music)

### The problem we want to solve

Our intro must print two lines of text to the screen, do a color wash effect on top of it and play music. While we can print our text once at the start and leave as is the color washer and the music on the other hand must be triggered continuously during execution. How would we manage this? This obviously requires some sort of timing capability - we need to find a clock or any other predictable event in the system to help us to execute our subroutines for music or color effects at a specific time while the intro runs.

It turns out that the C64 is a very organized computer following a specific procedure which involves triggering a so-called system interrupt routine about every 1/60 of a second on NTSC Machines and a about 1/50 of a second on PAL systems. What does this mean? Continuously the C64 freezes the current program to rather run some other code. After this code has been worked off, it will continue at the point it stopped before. From a perspective of the original frozen program nothing has changed. It does not know it was interrupted. You can read more about [Clock Rates on NTSC and Pal machines in a dedicated article](https://dustlayer.com/c64-architecture/2013/5/7/hardware-basics-part-1-tick-tock-know-your-clock).

This interruption of the system is happening so fast that as a user you do not realize either. For example the blinking cursor is actually a routine which is executed within the system interruption routine. Let's look at that routine a bit closer.

The system routine starts at memory address $EA31. It checks for example if the RUN-STOP key has been pressed which is instrumental when you want to stop a BASIC program. It also takes care that your cursor blinks three times per second by decrementing a counter from 20 once per interrupt. When zero is reached, it will reverse the cursor and the counting down restarts. Since the interrupt is triggered 60 times per second on NTSC respectively 50 times per second on PAL machines the cursor will therefor blink about three times in that period.

We now know two things - we have a system wide interruption that automatically occurs a number of times per second and there is a pattern for the C64 to make sure that things happening during that interrupt can be fine-controlled, in it's simplest form by using a countdown to skip execution of a subroutine within the interruption . With this we have the reliable recurring event we were looking for. We want to hop on that interval and execute our own code. 

### Hijacking the System Interrupt

So since there is already something happening on a repeating basis, why not just use this to our advantage - let's hijack the system interrupt and execute our own subroutines in addition to the general interrupt routines. Before we do anything though we should understand how the interrupt is executed and where we can actually hook up.

### The Commodore Jump Table

There are two important vectors which point to some part of the triggered system routine. A vector is simply a memory location stored in two bytes. Using a special jump instruction the C64 will use the address it finds in that vector to hop to that specific location.

Why not jump directly to the routine but use a vector instead you may ask? This is a design pattern by Commodore to help developers across their machines to rely on specific entry points for executing various main system routines available on all computers. For that they added a so-called jump table into the ROM which holds all the different vectors with addresses to those general system routines. That basically means that the actual system routine jumped to may be located at different memory locations depending on the machine but the entry vector to get to this location would be the same across systems. For example jumping to the vector at $FFF0/$FFF1 is used to set the cursor position on all those machines back then though the actual memory location of PLOT varies from system to system.

### Time for boarding

So the system interrupts first action every 1/60 of a second is to jump to the vector $FFFE/$FFFF. This vector is residing in ROM, so we can not change it to point to our own routines. What it does is to save the current status registers and index registers before pointing to $0314/$0315 - which is another vector pointing to our actual system interrupt routine. Why does it save all registers? Because during that interrupt registers will change for various reasons but the system wants to continue the frozen program in the same state it was interrupted before. After the system routine has done it's work, all saves registers are restored.

Now the second vector $0314/$0315 as opposed to $FFFE/$FFFF is located in RAM. We can just change the address in those two bytes to point to our own custom routine. Once our routine has finished execution we continue normal operation by pointing to the real system service routine at $EA31 which was the original target stored in $0314/$0315.

### Slowing down

Our custom routine is now executed 60 times per second - which is way too fast. We need to control this. We could use a counter like the interrupt service routine does for the cursor blinking but this does not give us the degree of accuracy we require plus it is not really convenient. Our music and color effect routine need to be executed exactly once per screen refresh - how do we sync to that refresh rate?

Luckily there is not only the automatic system interrupt but lots of other sources in the C64 which can be asked to trigger an interruption of the system when a certain event takes place. One of those sources is the VIC-II, our Video Controller Chip. It has a few special registers which lets us request a notification when for example two sprites collide on the screen - because in a game you may want to update scores exactly when this happens. Another possibility is to request notification when the raster beam which is generating the screen output continuously has reached a specific line on the monitor. In fact this option is a popular method to sync custom routines to whatever happens on the screen.

**Let's clarify what we need to do:**

- change a vector within the regular system interrupt process to point to some custom code every time the system interrupt is triggered
- we want to execute subroutines when reaching a defined moment in time, in our case when the raster beam has reached a certain line on the screen. We have to do this because executing our subroutines 60 times per second respectively 50 times per second is usually too fast.
- when the subroutines have completed execution we point back to the regular system interrupt routine which is $EA31 - **we have come full circle**!

To meet this behaviour we need to do only two things. Setup the hijacking of the system interrupt and within that ask the VIC-II controller to let us know when the raster beam has reached a certain position. Let's check the example code.

**Open code/main.asm!**


We start with the first part of the code in the main routine.

In the setup code we first need to tell the C64 to stop triggering interrupts for a brief moment. Why is this of importance? Think about that we change the vector at $314/$315 to point to our own routine. For that we consecutively change the byte in $314 and then in $315. But what happens when an interrupt just occurs after we wrote to $314? The vector will point to the wrong address and the system will probably crash. To avoid this there is the machine language command SEI. It sets the *Interrupt Disable Flag* in the status register to 1 and from that point on no interrupt is triggered until the flag has been cleared again using the complementary command *CLI *which clears that **disabling** flag again. hile we turn off the system interrupt there will be no cursor  blinking and RUN-STOP key will not function either. Of course since we only disable the interrupt for a fraction of a second, we will not notice this as a user. 

Before we finally redirect the system interrupt vector we also take the opportunity and do some one time initializations like clearing the screen, then writing the two lines of text for our intro and we also initialize the SID music routine. Those are the parts of our intro that only need to be executed once so we don't want that to be included in the routines happening 60 times per second.

After this there follows a block which disables other sources of interrupts and does some clean up work so there are no interferences to be expected. I will go into the various sources of interrupts in a dedicated Interrupt article at some point.

The important part of the setup code as far as the hijacking idea plan goes is where we finally load the accumulator and the X-Index-Register with the memory location the label *irq is pointing to and  store it into $314/$315. *

**There we have hijacked the system interrupt routine!**

### Syncing to the raster beam

We need to make sure that our routine is only executed once per screen refresh otherwise the music would be way too fast and the color wash effect would look like a strobe light. You can in fact test how this would look. Just remove the dec $d019 command, but do not delete the label *irq*. Then build and run index.asm  and watch the intro being played back in Warp9 speed. This also means that $d019 is somewhat important to make sure that the notification request for the raster beam is refreshed - I will explain in a bit.

To get the optimal speed for our intro we want to run our subroutines once per screen refresh. But how do we determine this? e will register a request with the VIC-II chip. We need to tell the Video Controller what type of interrupt we want to be informed of and of course at what point the notification should happen. In the address $D01A we set Bit 0 to let the VIC-II know that we want to request a notification from a raster beam event. $D012 is the place where we define at what line number the interrupt should be triggered - for our intro that would be line zero. We could have used any other line number as we are only concerned to get a notification once per screen refresh no matter where it occurs.

Last but not least we need to consider that the C64 has a mechanism to check if the raster beam has passed line 255. As you know one Byte can hold only up to 256 values - so we can very easily check if the raster beam is somewhere between line 0 and line 255 - **but the C64 has more horizontal lines**.  How would the C64 know that we are on line 300 for instance?

We actually need 9 Bits to really check all available raster lines. And that is exactly what the C64 is asking for. It borrows Bit#7 of the register $d011 to use it as extra Bit. When the raster beam has passed the 256 possible values in $d012 it will set Bit#0 on $d011 and restarts counting in $d012 until it reached the end of the screen. Then it clears Bit#0 in $d011 again. As we know that our text is written somewhere in the middle of the screen we want to make sure that Bit#0 in $d011 is not set by accident when we start our intro. This could be the case when for example certain Fastloader cartridges are inserted.


Our setup code is complete - whenever the raster beam reaches line zero, our custom routine at label *irq *is executed.


### The custom IRQ routine

Our custom IRQ routine is actually very simple. All it does is acknowledging the IRQ and reset the register then it runs two sub routines. One is for the color wash effect and the other is for playing back the music. Once both subroutines have returned we jump to $EA31, the original system interrupt routine.

The acknowledging command **dec $d019 **might actually be confusing and needs clarification.

What we need to do every time our custom IRQ routine is executed is to tell via register $d019 that everything is fine and that we want another notification with the next screen refresh, that is the next time the raster beam reaches line zero on the screen. To make this happen the process is to read the content of $d019 and write it back to the same register. This will reset $d019 and our interrupt triggered from the VIC-II chip will be executed again as configured in $d012 before. The Read/Write pattern to do the reset is a special behavior of that $d019 register.

Now as coders are looking for optimization all the time somebody found out that the decrement command *dec* can be used to do both operations with just one single command. This works because dec is a so-called Read-Modify-Write command that writes back the original value during the modify cycle.

Using *dec $d019* instead of  executing the two consecutive commands *lda $d019* and* sta $d019* will save us some time in typing and system cycles. 

This is all you need to know about the interrupt for this first example intro. In the next two chapters we will look at the two subroutines we execute on our raster beam interrupt.

-act

---
*Fonte originale: [https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-3-did-i-interrupt-you](https://dustlayer.com/c64-coding-tutorials/2013/4/8/episode-2-3-did-i-interrupt-you)*


### Collegamenti e Riferimenti Hardware
- **$D011 (VIC Control Register 1)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d011).
- **$D012 (Raster Counter)**: Associato al chip VIC-II. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#d012).
- **$0314 (IRQ Vector)**: Associato al chip KERNAL. Vedere [Mappa di Memoria](../sta_c64/cbm64mem.md#0314).
