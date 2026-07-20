---
title: Technical information for musical Acornsoft Elite
source_url: https://elite.bbcelite.com/hacks/bbc_elite_with_music_technical_information.html
category: source-code
topics:
- raster interrupts
- memory management
- basic
- assembly
- sound generation
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CPU
related:
- sid-registers
- sound-programming
- vic-ii-registers
- memory-map
- kernal-routines
- music-player
- sprite-programming
- raster-interrupts
scraped_at: '2026-07-20'
---

# Technical information for musical Acornsoft Elite

## How the Commodore 64's music was ported to Elite on the BBC Micro and Electron

Most of the heavy lifting in this hack was done by the amazing coders of the [Bitshifters collective](https://bitshifters.github.io/), who created the music player and ported the music. I merged their work into Elite, which I describe in more detail below, but without these guys, none of this would have happened.

In this article we'll take a look at how this particular plan came together, and how we produced a loading sequence and in-game music like this:

## Creating the music ROM

													 ----------------------

						The music player in this hack is based on the VGM music player for the BBC Micro by Simon Morris, which you can read all about in the [project's GitHub page](https://github.com/simondotm/vgm-player-bbc). Huffman encoding is not used in this instance, as we need all the memory we can get.

The idea to use Simon's player in Elite was down to Kieran Connell; he was also the inspiration for [Teletext Elite](https://elite.bbcelite.com/teletext_elite.html) and [Elite 3D](https://elite.bbcelite.com/elite_3d.html), and it was Kieran who [got me into disassembling Elite in the first place](https://elite.bbcelite.com/about_site/about_this_project.html), so he has form! After we had a quick chat about what might be possible, Kieran refactored Simon's player to work in sideways RAM, as there is simply no spare memory when Elite is running, so sideways RAM is the only viable option for storing the music (see the deep dive on the [Elite memory map](https://elite.bbcelite.com/deep_dives/the_elite_memory_map.html) to see what I mean).

Kieran then enlisted help from [Negative Charge](https://negativecharge.github.io), the Bitshifters' resident Beeb music conversion expert, who converted the original Elite tunes from the Amstrad CPC, Atari ST, Commodore 64, Commodore 128 and NES versions of the game. After listening to all the candidates, they decided that the Commodore 64 tunes sounded the best, so those are the ones included in this hack. The conversion doesn't use the player code or music data from the Commodore 64 source, but is a conversion of the data bytes that get sent to the C64's SID sound chip by the game, and these are converted into data bytes that can be sent to the BBC Micro's SN76489 chip. This is all then heavily compressed, but it still comes out as quite a large file because it can't account for repeated patterns like a dedicated music driver could.

The result of all this work was a ROM image that I could load into sideways RAM, and which provided three addresses that I could call, one to select the title music, one to select the docking music, and another to play the currently selected tune. You can see this ROM in action in Kieran's original [elite-music repository](https://github.com/kieranhj/elite-music), where you can download a disc image that demonstrates both tunes playing.

## Adding music to BBC Micro disc Elite

													 ------------------------------------

						The next stage was to add this music to the game code for the BBC Micro disc version of Elite. I took Kieran's ROM image, loaded it into sideways RAM, and modded the Elite source to incorporate calls to the music player at the relevant points in the game. So I added a set of ROM calls into the docked code to make the title music play alongside the spinning Cobra on the title screen, and I added a second set of calls into the flight code to switch the Blue Danube on and off along with the docking computer.

That makes it sound easy, but memory is astonishingly tight in Elite, so not only is it a real challenge to add any new code at all, but if that code needs variable storage stage - as is the case with the music ROM - then things can get quite difficult, quite quickly.

The hardest part of the modding process involved freeing up ten free bytes of storage in zero page; the disc version of Elite uses all but one byte of zero page, so this took some time, but was essential to make the hack work. The music ROM needs eight bytes in zero page for the music player; it needs another byte to store the ROM number where the loading process puts the ROM image; and it needs a further byte to store a flag that records whether or not we should be playing music. The key was to work out how all the zero page variables are used, and to share zero page addresses between variables that are not used at the same time; you can see how I did this in the zero page section of the [elite-source-docked.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/blob/music/1-source-files/main-sources/elite-source-docked.asm) and [elite-source-flight.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/blob/music/1-source-files/main-sources/elite-source-flight.asm) source files in the [music branch of the elite-source-code-bbc-micro-disc repository](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/tree/music) (search the source for "Mod:" to see all the modifications I made).

I also had to build a routine for calling the music routines in the sideways RAM image (I ended up calling this routine PlayMusic). This routine needs to switch the music ROM into memory at &8000, call the relevant music routine in the ROM, and then switch the music ROM back out, with the switching done by changing the value of ROMSEL in SHEILA &FE30 (and the RAM copy in &F4). The version of the music ROM that Kieran provided had three entry points - &8000 to select the title music, &8003 to select the docking music, and &8006 to play the music - so I figured I could save a few bytes by building a generic PlayMusic routine that would take an argument giving the ROM routine to call. The argument is simply the offset from &8000 of the routine, so that's 0 to select the title music, 3 to select the docking music, and 6 to play the music (which we do as part of the vertical sync interrupt - see below). I also added a new routine at &8009 to let us stop the currently playing music, and another routine at &800C to manage the new music-related game configuration options, and at the same time I repointed the zero space variables used by the ROM routines into the space I'd managed to free up. The resulting Elite-friendly version of the music ROM can be found in [my fork of the elite-music repo](https://github.com/markmoxon/elite-music).

Next, I had to hook the play routine (i.e. the PlayMusic routine with argument 6) into the vertical sync interrupt handler, so the currently selected music could play in the background. To do this, I patched a jump instruction into the vertical sync handler that's part of Elite's split-screen mode system (see the deep dive on the [split-screen mode](https://elite.bbcelite.com/deep_dives/the_split-screen_mode.html) for information); this injected jump instruction calls a new routine called IRQMusic on every vertical sync, which checks whether we are playing music, and if so processes the call to PlayMusic.

There is one more subtle point to consider. The BBC Micro disc version of Elite flips between the docked and flight code, and in doing so it loads a different game binary. These binaries load at address &11E3, and the interrupt handler and various other routines live below this address, and are therefore unchanged between the two different codebases. However, there is no free space in this section of memory, so I had to add both IRQMusic and PlayMusic above address &11E3, so they are part of both the docked and flight code. I therefore had to make sure they both have the same address in the docked and flight code, so the vertical sync handler keeps working whichever of the two different codebases are loaded.

Similarly, to support volume control of both music and sound effects on the BBC Micro, I had to move the [SFX](https://elite.bbcelite.com/disc/docked/variable/sfx.html) sound effect definitions so they also stay in the same location between the two codebases, as then the music ROM can patch the sound volume according to the current setting (otherwise the sound effects would reset to the default volume settings on each flip between docked and flight). Ensuring that SFX is always at the same address means we can run a routine after switching codebases that updates SFX with the new settings, as we always know where the table is in memory. Luckily the envelope definitions are stored by the MOS at address &08C0, so they can be altered in-place to change volume levels without having to worry about them being overwritten.

The final step was to put the game code together with a boot loader. The loader confirms the presence of sideways RAM, loads the ROM image into a sideways RAM bank, and stores the ROM number for use by the PlayMusic routine. To get this working, I wrote a sideways RAM loader that works across the Tube and doesn't use RAM banks that already contain ROM images. This means you can load the game from a filing system whose ROM is in sideways RAM, and without worrying about the ROM being overwritten.

## Adding music to other versions

													 ------------------------------

						There is also a BBC Master version of musical Elite that works in the same way as the disc version, except the code doesn't have to worry about staying in place between the docked and flight code, as the entire game is resident in memory the whole time. On top of this, the loader can use the Master's built-in SRLOAD command to load the ROM. The only other gotcha is that Elite uses sideways RAM bank 6 for the game itself, so we have to make sure not to use that one for the music (though the Master has three other RAM banks, so this isn't much of a problem). See the [music branch](https://github.com/markmoxon/elite-source-code-bbc-master/tree/music) of the repository for details.

Also, there's a version for the BBC Micro with 6502 Second Processor and 16K of sideways RAM. Surprisingly there isn't enough spare memory to load the music into main memory, as Elite only leaves 3.2K free in the parasite and 3.7K free in the I/O Processor; the music takes up around 13K, so we still need to have 16K of sideways RAM to load it. The sideways RAM detection and loading routines need to check memory in the I/O Processor, on the other side of the Tube, and the 6502 version's API needs to be extended to support playing music, stopping music, swapping tunes and so on. Luckily there are enough free OSWORD calls to support these new functions, which you can see in the [OSWVECS routine in the elite-z.asm source](https://github.com/markmoxon/elite-source-code-6502-second-processor/blob/music/1-source-files/main-sources/elite-z.asm#L6521-L6525) in the [music branch](https://github.com/markmoxon/elite-source-code-6502-second-processor/tree/music) of the repository.

Then there's a version for the BBC Micro B+128 (or the BBC Micro B+ with 16K of sideways RAM). The B+128 comes with four banks of sideways RAM as standard, and the B+128 version of the backported BBC Master Elite uses this to store the music ROM. The loader doesn't use the BBC+128's SRLOAD and SRWRITE commands, as the original B+ didn't come with these commands, and I wanted to support the upgraded B+ with sideways RAM. That aside, the B+128 musical version of BBC Master Elite works in the same way as the original BBC Master version. See the [bbc-micro-b-plus-music branch](https://github.com/markmoxon/elite-source-code-bbc-master/tree/bbc-micro-b-plus-music) of the repository for details.

It's worth noting that the exact same music ROM image is used on all three BBC platforms. There's a lookup table at the start of the ROM, just after the jump table, that contains various addresses of Elite routines, and internal key numbers for the configuration options. By default these values are set up for the BBC Micro disc version, so the BBC Master and 6502 Second Processor versions patch these values after the ROM image is loaded into sideways RAM, so they point to the correct addresses and key numbers for that version of Elite.

Finally, the ROM image must be loaded into sideways RAM, as it uses its own space for storing data, and contains a fair amount of self-modifying code. It won't work as a ROM, or in write-protected sideways RAM; it has to be writeable, or it won't work.

The Acorn Electron version works along similar lines to the BBC versions, except the music data and driver are loaded into memory at &0E00 rather then sideways RAM. This lets us add music to the Compendium version of Elite, which runs at &1D00. As a result the musical variant needs to be run with an E00 version of DFS, MMFS or ADFS, so that the memory from &0E00 to &1D00 can be used for the music. The Elite-friendly version of the music driver can be found in [my fork of the elk-elite-music repo](https://github.com/markmoxon/elk-elite-music).
						

Note that the music in the Electron version is single-channel, and the music is based on the [MIDI files of the original music](https://www.dream-ware.co.uk/elite/music/), which have been backported by Negative Charge. The music doesn't have the grace of the original Commodore 64 score - indeed, single-channel music is perhaps an acquired taste - but this is still the music from Commodore 64 Elite on an Electron, and that on its own is an astounding technical achievement.

The results are music to Acornsoft players' ears, I'm sure you'll agree.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/bbc_elite_with_music_technical_information.html](https://elite.bbcelite.com/hacks/bbc_elite_with_music_technical_information.html)*
