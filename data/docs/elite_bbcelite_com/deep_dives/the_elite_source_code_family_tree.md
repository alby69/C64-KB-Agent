---
title: The Elite source code family tree
source_url: https://elite.bbcelite.com/deep_dives/the_elite_source_code_family_tree.html
category: source-code
topics:
- basic
- assembly
- graphics
- memory management
- input handling
difficulty: beginner
language: mixed
hardware:
- BASIC ROM
- CIA
- SID
- CPU
- KERNAL
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

# The Elite source code family tree

## Tracing the development history of 6502 Elite from the BBC Micro to the NES

Elite has a long development history on the 6502. The game was first released on the BBC Micro in 1984, when it looked like this:

![The title screen in the BBC Micro version of Elite](https://elite.bbcelite.com/images/cassette/title.png) 

						Versions were then released for the Acorn Electron, 6502 Second Processor, Commodore 64, Apple II, BBC Master 128 and BBC Master Compact, before the last official version landed on the NES in 1991, when it looked like this:

![The title screen in NES Elite](https://elite.bbcelite.com/images/nes/general/title.png) 

						In all, ten official versions were released for 6502-based machines (if you include the Demonstration Disc for the BBC Micro). There were, of course, plenty of conversions to non-6502 machines as well, such as the ZX Spectrum and IBM PC, but for the purposes of this article (and, indeed, this site) I'm going to stick with the 6502. I'm also going to include the unofficial game Elite-A, because it's contemporary to the original versions, is documented on this site, and is so damn epic.

Almost all of the code across these different 6502 versions was written by Ian Bell and David Braben; notable exceptions include the sound and music in later versions, the disc routines in the Apple II version, and some of the bitmap graphics and text translations on the NES. The authors used the same core source code for all of these versions, using a BBC Micro with a second processor to build the game binaries; the only version that wasn't developed on the BBC Micro was the NES version, and even then the same BBC-based source code was used as a starting point.

In this article, I'm going to try to work out exactly how 6502 Elite was developed over the years, by looking for clues in the original source code and digging through the game binaries. Software archaeology, here we come...

## Source code family tree

													 -----------------------

						It's hard to pinpoint the exact date when 8-bit Elite came into being, as it organically grew out of David Braben's 3D ship routines and Ian Bell's prior experience with his Acornsoft-published game Free Fall. But the pair met soon after they started at Cambridge University in autumn 1982, so people tend to regard the development process as starting around then and taking a couple of years before it was finally released.

At the other end of the timeline, following the NES release in 1991, the authors continued to work on an NTSC version, though that would never be released. The emulated NTSC version on Ian Bell's site has a version date of 24 April 1992, so we know that development continued until at least then.

So the development of Elite on the 6502 spans a whole decade from 1982 to 1992. And given that the same source code was used as the basis for each version, with new features being added in some versions and bugs being fixed in others, can we work out a definitive family tree of the Elite codebase?

To answer this question, I've analysed the various source codes and game binaries, and I've come up with the following family tree:

```
              Acorn Electron                  NES
            /                \              / 
           /                   Commodore 64
  Cassette                   /              \ 
   \       \         6502 SP                  Apple II -> Master -> Compact
    \       \      /
      Demo <- Disc
                   \
                     Elite-A
```
						This tree shows how each version is derived from its predecessors, with the direction of development moving from left to right (unless shown otherwise). In terms of modern development, you can think of this as a git branching diagram, or even a git forking diagram showing upstream repositories to the left and downstream repositories to the right.

Note that in the above, "Cassette" refers to the BBC Micro cassette version of Elite, "Disc" refers to the BBC Micro disc version, and "Demo" refers to the Elite Demonstration Disc for the BBC Micro. I should also mention the spelling of "disc", as the BBC Micro had floppy discs with a "c", while the Commodore 64 and Apple II had floppy disks with a "k". Throughout this site I have tried to use the appropriate spelling for the platform being discussed, but as all versions of 6502 Elite (bar the NES) were developed on a BBC Micro - even the Commodore 64 and Apple II versions - I'll be referring to "discs" in the following, even when talking about the non-BBC versions.

I'm going to spend the rest of this article trying to justify this family tree by searching for clues in the original source code, but first let's have a quick chat about dates and why we probably want to ignore them.

## A quick word about dates

													 ------------------------

						These days, pretty much everything has a timestamp. Emails, photographs, files, repository commits - they all have a time and date embedded in them somewhere. The technology world runs on a schedule, and although things can go wrong with digital dates, most modern data repositories have quite a bit of date information captured alongside the data.

This is not the case on the BBC Micro, as it doesn't have a real-time clock; this would be rectified with the BBC Master, but even then, discs saved on a Master still don't have timestamps. As a result, floppy discs created by the BBC's Disc Filing System (DFS), such as the Elite source discs, contain absolutely no time or date information, outside of any manually added titles that might contain date clues, like this one on the Commodore 64 source disc:

![A catalogue of drive 0 of the Commodore 64 source disk](https://elite.bbcelite.com/images/c64/source_drive_0.png) 

						But these kinds of clues are open to interpretation, so at the end of this article I've summarised of all the date information I have managed to glean from disc titles, source code images and the contemporary press, but I suggest we leave all these dates to one side and see if we can work out the structure of the Elite source code family tree by examining the code itself.

## Building the source code family tree

													 ------------------------------------

						In building the family tree above, let's start with an unordered list of all eleven versions that we're analysing:

Acorn Electron Cassette Disc Demo 6502 SP Commodore 64 Apple II Master Compact NES Elite-A

Let's now work through the ten pieces of evidence that can help us sort this unordered list into a source code family tree.

## Exhibit 1 of 10: Before and after September 1984

													 ------------------------------------------------

						The first piece of evidence is the reasonably well documented release history of the very first Elite.

Elite was announced in September 1984 for the BBC Micro (cassette and disc) and the Acorn Electron, so we can assume that these three versions were being worked on before that date. The demo was released at the same time as the original game, so we can include that one too.

The BBC Master and the PAL version of the NES didn't even exist in September 1984, so clearly these versions weren't in development until after that date.

The Commodore 64 version followed on from the authors' relationship with Firebird, and that only came about because of the success of Elite on the BBC Micro. Sure, their contracts with Acornsoft had cannily reserved the rights for other platforms, leading to the auction that led to Firebird winning the prize, so they always had plans for converting the game. But it seems clear that prior to the September 1984 event, Bell and Braben were fully focused on finishing off the three original Acornsoft versions, and that the Commodore 64 came later, after the original BBC and Electron versions were released and everybody started clamouring for conversions.

The Apple II version was commissioned even later, to help with Firebird's push into the US market, so it's pretty safe to say that it also hadn't been worked on by the time of the original release in September 1984.

Elite-A was developed from a disassembly of the released BBC Micro disc version, so it was clearly built after September 1984.

There is one unknown: the 6502 Second Processor version. It isn't yet clear where this fits into the original release schedule, so let's leave that one aside for now.

We can therefore split our list of versions into those that were being developed before the initial release in September 1984, and those that clearly came afterwards. That gives us our first refinement of the family tree:

```
  Acorn Electron -> Commodore 64           6502 SP
  Cassette          Apple II
  Disc              Master
  Demo              Compact
                    NES
                    Elite-A
```
						It's a start, so now let's pick off one of the most obvious relationships in the whole family tree.

## Exhibit 2 of 10: Angus Duggan's epic disassembly

													 ------------------------------------------------

						The second piece of evidence is the development history of Elite-A.

Elite-A is the poster child for forking; it is a supreme example of taking an existing game and modding it into the future. Back in the late 1980s, Angus Duggan took the BBC Micro disc version, disabled the disc protection, disassembled the game binaries on a BBC micro with a 6502 Second Processor using his own homebrew disassembler ROM, and added all the features we know and love from this epic mod.

Looking at the code, this development history is patently clear, as Elite-A retains the original code and structure of the disc version, with its own tweaked versions of the [docked](https://elite.bbcelite.com/elite-a/all/workspaces_docked.html) and [flight](https://elite.bbcelite.com/elite-a/all/workspaces_flight.html) code, to which Angus added the [encyclopedia](https://elite.bbcelite.com/elite-a/all/workspaces_encyclopedia.html) as a third game binary. And Elite-A still loads all its ship blueprints from [blueprint files](https://elite.bbcelite.com/elite-a/all/elite_ships_a.html), just like the disc version, though there are more ships and more blueprint files in Elite-A. These two are the only contemporary versions to do this, and the derivation of Elite-A from the disc version is undeniable.

Elite-A also comes with a version for the 6502 Second Processor, though it doesn't include any code from the official version. Instead, the co-processor version of Elite-A is essentially the same as the standard version, except all the code and ship data is loaded into memory at once, along with a different ship-spawning routine. Angus invented his own API for communication over the Tube, so while Elite-A does have a 6502 Second Processor version, it isn't derived from the Acornsoft version.

So Elite-A is obviously and provably a descendant of the disc version, so it fits into the family tree as follows:

```
  Acorn Electron -> Commodore 64           6502 SP
  Cassette          Apple II
  Demo              Master
  Disc              Compact
       \            NES
         Elite-A
```
						Now let's see if we can work out where the 6502 Second Processor version fits in.

## Exhibit 3 of 10: The persistence of co-processor code

													 -----------------------------------------------------

						The third piece of evidence is the existence of the SETXC/SETYC, DOXC/DOYC and PUTBACK routines.

The 6502 Second Processor version takes all the features of the BBC Micro disc version and restructures the code to work with a second processor that's attached to the BBC Micro via the Tube interface. This process splits the codebase into two parts: the graphics, keyboard, sound and disc routines live in the I/O processor (i.e. the BBC Micro host, on the left in the picture below), and the main game binary lives in the parasite (i.e. the second processor, on the right).

![The 6502 Second Processor](https://elite.bbcelite.com/images/6502sp/second_processor.jpg) 

						To implement this two-machine system, the authors created an API to enable the I/O processor and parasite to communicate across the Tube (see the deep dive on [6502 Second Processor Tube communication](https://elite.bbcelite.com/6502sp_tube_communication.html) for details). One example of the API in action concerns the position of the text cursor. In the original versions of Elite, the text cursor's position on-screen is stored in two zero page variables, XC and YC, so the code can print text at a specific position by setting these variables and calling the relevant text-printing routine. You therefore see lots of STA XC and STA YC instructions in the code, whenever text is being printed on-screen.

In the 6502 Second Processor version, the text-printing routines live in the I/O processor, so we need a way of sending the text cursor position from the main code in the parasite to the I/O Processor. The solution is to replace the STA XC and STA YC instructions with calls to new subroutines called [DOXC](https://elite.bbcelite.com/6502sp/main/subroutine/doxc.html) and [DOYC](https://elite.bbcelite.com/6502sp/main/subroutine/doyc.html), which implement the more complicated process of transmitting the values across the Tube. When these values arrive at the I/O processor, they are stored by two new subroutines called [SETXC](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/setxc.html) and [SETYC](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/setyc.html) which store the values and return control via the [PUTBACK](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/putback.html) routine. This all means that when text needs to be printed, the I/O processor knows the cursor position.

The 6502 Second Processor version contains these routines, while none of the other three original versions do (BBC cassette, BBC disc and Electron). Parts of the DOXC and SETXC routines remain in the Commodore 64, Apple II and Master versions, so these versions must all have been derived from the 6502 Second Processor version, as it would make absolutely no sense to add this extra layer of JSR DOXC and JSR SETXC instructions to these single-machine versions.

The NES version doesn't contain any traces of these routines, but the PAL machine that Elite requires wasn't launched until September 1986, well after the 6502 Second Processor of Elite, so it also has to come after the 6502 SP entry in our family tree.

To see what I mean, check out the remnants of the [DOXC](https://elite.bbcelite.com/c64/main/subroutine/doxc.html), [SETXC](https://elite.bbcelite.com/c64/main/subroutine/setxc.html) and [PUTBACK](https://elite.bbcelite.com/c64/main/subroutine/putback.html) routines in the Commodore 64 source; these have to come from the 6502 Second Processor version's own [DOXC](https://elite.bbcelite.com/6502sp/main/subroutine/doxc.html), [DOYC](https://elite.bbcelite.com/6502sp/main/subroutine/doyc.html) and [PUTBACK](https://elite.bbcelite.com/6502sp/i_o_processor/subroutine/putback.html) routines, and the Commodore code even contains commented out instructions that are unique to the co-processor implementation.

These aren't the only ones: the Commodore 64's [TTX66](https://elite.bbcelite.com/c64/main/subroutine/ttx66.html) routine is another good example, as it still contains references to the buffers ([LBUF](https://elite.bbcelite.com/6502sp/main/variable/lbuf.html)) and routines ([PBZE](https://elite.bbcelite.com/6502sp/main/subroutine/pbze.html), [HBZE](https://elite.bbcelite.com/6502sp/main/subroutine/hbze.html)) used to transmit data across the Tube.

So it's clear that the Commodore 64 source was derived from the 6502 Second Processor version, and those remnants of code persisted into the other versions in the right half of our diagram, so we can now reorder our family tree like this:

```
  Acorn Electron -> 6502 SP -> Commodore 64
  Cassette                     Apple II
  Demo                         Master
  Disc                         Compact
       \                       NES
         Elite-A
```
						It's progress; all the versions are included now, so let's see if we can improve the left column.

## Exhibit 4 of 10: Disc enhancements

													 ----------------------------------

						The fourth piece of evidence is the [Elite Players' Guide](http://www.elitehomepage.org/playguide.htm) that you can read on Ian Bell's personal website.

This document is dated 24 March 1984, a good six months before Elite's official launch in September 1984, and it describes the game's many features. It was sent to Acornsoft to be used when writing the manual and novella.

The guide clearly describes the BBC Micro cassette version. It talks about "saving to tape". It mentions that "the auto-docking sequence is triggered by the C key and, due to lack of memory, has no graphic effect". And the real giveaway? "We suggest that you skim-read this manual while the game is loading." We are definitely talking about tape-loading here.

The main clue comes towards the end, in this section:

IT'S PREVIEW TIME!

Described below are some items and ideas that may well find their way into Second Processor and Disk Elite (and possibly the Electron version). We list them here for consideration when preparing artwork and The Novel.


This shows that at this point in development, all four Acorn versions were being discussed. But while the cassette version was close enough to completion to be the subject of the manual, the features in the other versions were still being thought up. In other words, the BBC Micro cassette version appears to have been the first version to be properly developed; it appears to be the original Elite.

This view is backed up by the source code. The BBC Micro disc version is clearly the cassette version, but with a lot of features added or extended. The core routines, such as the ship-drawing code or the line-drawing algorithm, are identical, but the code has been split up into docked code, flight code and ship blueprints, and extra features have been added, such as missions, a proper docking computer, and loads of new ships. Here's the game disc, which shows just how many separate parts the disc version has been split into:

![The contents of the disc for the BBC Micro disc version of Elite](https://elite.bbcelite.com/images/disc/disc_contents.png) 

						It simply wouldn't make sense to build an all-singing, all-dancing disc-based version, and only then try to shoehorn this multi-file game into a memory-starved cassette-based machine. Both the disc and the cassette sources are crammed with space-saving techniques, such as tail calls, conditionals that use BIT instructions, text tokenisation and so on. These are even present in code that only runs when docked, and as the disc version's docked code has quite a bit of memory to spare, this indicates that the code must have come from a more constrained environment, namely the cassette version.

The Demonstration Disc, meanwhile, is structured in the exact same way as the cassette version, and it loads itself into memory in one go, though it does contain some code from the disc version, so this will need to be included. We'll cover the demo in exhibit 6, but for now let's leave it grouped with the cassette version, as that's its closest relative.

So we can refine our family tree even further:

```
                           6502 SP -> Commodore 64
                         /            Apple II
  Acorn Electron -> Disc              Master
  Cassette               \            Compact
  Demo                     Elite-A    NES
```
						It's shaping up, but how can we be sure which came first: the BBC Micro cassette or the Electron?

## Exhibit 5 of 10: Cassette before Electron

													 -----------------------------------------

						The fifth piece of evidence is the Acorn Electron game binary (we don't have the original source code for the Electron, so the binary will have to do).

Code-wise, the Electron version appears to be the BBC Micro cassette version with blocks of code simply removed to fit it into a smaller memory footprint (suns, Thargoids, witchspace - they all ended up on the cutting room floor). There are literally hundreds of examples of code that matches between the Electron and BBC Micro cassette versions, but which is different in the BBC Micro disc version and all the later versions. For example:

- The Electron and cassette versions encode carriage returns in text tokens using control code 13, while all the other versions of 6502 Elite use control code 12.
- The Electron and cassette versions have the same set of text tokens, which differ noticeably from all the other versions (as those versions also support extended text tokens).
- The Electron and cassette versions have the same ship data, and it differs from all the other versions; for example, Pythons in the cassette and Electron versions have a larger targetable area (120 x 120) than in all other versions (80 x 80).

But having similar code doesn't tell us which version came first, it only tells us that the Electron and cassette versions are very closely related; in theory, it could still be possible that the Electron version came first and the cassette version simply bolted on a load of extra features. And because we don't have the original source disc for the Electron, we can't find any clues in any commented-out code, as the game binary doesn't contain that level of detail. So instead we have to look deeper for clues.

The smoking gun can be found in the BBC-specific code that was left behind in the Electron's binary during the stripping process. One example is in the code for the Electron's planets, which appear as plain circles like this:

![A planet in Electron Elite](https://elite.bbcelite.com/images/electron/planet.png) 

						But this isn't the only bit of evidence - there's a whole selection of clues:

- The Electron version's [ACT](https://elite.bbcelite.com/electron/main/variable/act.html)variable and[ARCTAN](https://elite.bbcelite.com/electron/main/subroutine/arctan.html)routine contain code that is only used when drawing planet meridians and craters. The planets in Electron Elite are simple circles and don't have meridians and craters.
- The Electron version's [DKS2](https://elite.bbcelite.com/electron/main/subroutine/dks2.html)routine reads the BBC Micro joystick. The Electron doesn't have a joystick port.
- The Electron version's [TT17](https://elite.bbcelite.com/electron/main/subroutine/tt17.html)routine contains joystick code that is never run because joysticks are never configured.
- The Electron version's [LL164](https://elite.bbcelite.com/electron/main/subroutine/ll164.html)routine sets the[HFX](https://elite.bbcelite.com/electron/main/workspace/wp.html#hfx)variable, which disables the split-screen mode to make the hyperspace effect, but the Electron doesn't have a split screen.

The fact that these bits of code are still hanging around in the Electron version is proof that the Electron version is derived from the BBC Micro cassette version. And because the Electron version and BBC Micro cassette version overlap in such a unique way, and we can make the following change to the family tree, extracting the Electron version into its own branch:

```
            Acorn Electron
          /
  Cassette         6502 SP -> Commodore 64
  Demo     \      /           Apple II
            Disc              Master
                 \            Compact
                   Elite-A    NES
```
						Now let's finish off the left part of our tree by looking at the Demonstration Disc.

## Exhibit 6 of 10: Forking the demo disc

													 --------------------------------------

						The sixth piece of evidence is in the overall structure of the code in the Demonstration Disc, and the remnants left over from the cassette version.

If you look at the code, the demo is clearly a fork of the cassette version: it has the exact same structure as the cassette version, just with some routines removed and others added (see the deep dive on [code changes in the Demonstration Disc](https://elite.bbcelite.com/code_changes_in_the_demonstration_disc.html) for details). The whole thing loads into memory in one go and the functionality is obviously a minor variant of the cassette version; for example, they have the exact same range of ships, and both versions have a Mamba on the second title screen (unlike the disc version, which has a Krait):

![Elite Demonstration Disc title screen screenshot](https://elite.bbcelite.com/images/demo/demo_title_screen.png) 

						The smoking gun is that when the authors removed routines from the cassette version to create enough room for the extra demo-related code, they removed some routines entirely, but for others they left remnants behind. The most obvious remnant is the [SVE](https://elite.bbcelite.com/demo/main/subroutine/sve.html) routine, which exists in the demo only as a partial snippet of the [original routine](https://elite.bbcelite.com/demo/main/subroutine/sve_removed.html) from the cassette version. This means that the demo version must have been created by taking the cassette version and chopping out aspects that weren't needed (such as the save routine).

That said, the demo version does contain a number of routines that have been copied directly from the disc version. These are the docking computer routines like [DOCKIT](https://elite.bbcelite.com/demo/main/subroutine/dockit.html) and [DCS1](https://elite.bbcelite.com/demo/main/subroutine/dcs1.html), which are used to implement the combat autopilot in the self-playing demo. As this code arguably implements the core aspect of the demo - i.e. ship combat - it's worth capturing this relationship with a link from the disc version to the demo, as well as from the cassette version to the demo.

So we can now update the demo in the family tree, as follows:

```
            Acorn Electron
          /
  Cassette         6502 SP -> Commodore 64
   \       \      /           Apple II
    Demo <-  Disc              Master
                 \            Compact
                   Elite-A    NES
```
						The left half is looking pretty good, so let's move on to the right half, and the bulk of the non-Acorn versions.

## Exhibit 7 of 10: The NES version

													 --------------------------------

						The seventh piece of evidence is the FLKB routine in the original NES source code.

When I first analysed the NES version of Elite back in 2023, the original source code wasn't available, so I had to disassemble the game ROM and work with that. So when Ian Bell added the original [Programmer's Development System (PDS) source files](http://www.elitehomepage.org/archive/a/b7120580.zip) to his site for the [40th anniversary of Elite](http://www.elitehomepage.org/fourty/index.htm), I couldn't resist jumping in and looking for clues for the family tree.

I didn't have to look far. Here's an excerpt from the ELITEB.PDS file in the original source's JOEL1 folder:

```
  FLKB    LDA     #15
          TAX
          ;JMPOSBYTE
          RTS
```
						This looks pretty familiar: it's the same as the [Commodore 64 version of the FLKB routine](https://elite.bbcelite.com/c64/main/subroutine/flkb.html), even down to the commented-out BBC call to OSBYTE.

So is the NES version derived from the Commodore 64 version? This appears to be the case, as the FLKB routine is quite different in all the other versions that are derived from the 6502 Second Processor. The Apple II version has completely different code in [FLKB](https://elite.bbcelite.com/apple/main/subroutine/flkb.html), and both of the Master versions have a stubbed-out [FLKB](https://elite.bbcelite.com/master/main/subroutine/flkb.html) routine that only contains an RTS. So the copy of FLKB in the NES source code must have come either from the Commodore 64 source, or possibly from an earlier Acorn version.

So is the NES version derived from one of the earlier Acorn-based versions instead? It's very unlikely, as the NES source code contains even more code that is specific to the Commodore 64. For example:

- Both sources use sound effect variables of the form #sfxecm or #sfxhyp1, a format that is not used in any other versions.
- The antilogODD calculation at the end of [DVID4](https://elite.bbcelite.com/c64/main/subroutine/dvid4.html#noddlog22)only appears in the Commodore 64 and NES versions.
- The NES version contains features that were first introduced in the Commodore 64 version - music and the Trumbles mission, for example.

So it seems pretty clear that the NES source code was derived from the Commodore 64 source code, and we can update the family tree as follows:

```
            Acorn Electron                   NES
          /                                /
  Cassette         6502 SP -> Commodore 64
   \      \      /            Apple II
    Demo <-  Disc              Master
                 \            Compact
                   Elite-A
```
						We're getting there, so let's turn our attention to the Apple II version.

## Exhibit 8 of 10: Scaling the system charts

													 ------------------------------------------

						The eighth piece of evidence comes in the form of the SCALEX, SCALEY and SCALEY2 routines.

Both the Commodore 64 and Apple II versions of Elite had to cope with much smaller screen sizes than the BBC Micro: the BBC's space view is 192 pixels tall, but it's only 144 pixels tall in the Commodore 64 version, and only 136 pixels tall in the Apple II version. Because of this, the original Acorn versions all leave the dashboard permanently on-screen, and display all the system charts and trading screens in the top section of the screen, above the dashboard.

![The Long-range Chart in the BBC Micro cassette version of Elite](https://elite.bbcelite.com/images/cassette/long-range_chart.png) 

						The Commodore 64 version can't fit all the text of the trading screens into its smaller space view, so it removes the dashboard from the screen and uses the whole screen for displaying the system charts, market prices and the like. It works well, and there's enough memory to store a copy of the dashboard image for copying back into screen memory when we return to the space view.

![The Long-range Chart in Commodore 64 Elite](https://elite.bbcelite.com/images/c64/long-range_chart.png) 

						The Apple II version takes a different approach, and uses the Apple's text screen mode to display the trading screens. This happily coexists with the high-resolution graphics mode, so switching to the text mode doesn't clear the graphics screen, it just shows the text screen instead, so it's easy to return to the space view with everything still intact. But what about the system charts, which need a graphics view, but which don't fit into the 136-pixel space view above the dashboard?

There isn't enough free memory to store a copy of the dashboard, so instead of using the entire high-resolution screen for displaying the charts, the Apple version scales the charts down so they fit into the upper part of the screen. It does this by adding three new subroutines: [SCALEX](https://elite.bbcelite.com/apple/main/subroutine/scalex.html), [SCALEY](https://elite.bbcelite.com/apple/main/subroutine/scaley.html) and [SCALEY2](https://elite.bbcelite.com/apple/main/subroutine/scaley2.html). The chart code is amended to call these routines to scale the pixel coordinates, so the charts are drawn at 75% of the size of the originals, which ensures that they fit into the available space.

![The long-range Chart in Apple II Elite](https://elite.bbcelite.com/images/apple/long-range_chart.png) 

						These subroutines do not exist in the Commodore 64 version, which indicates that the Apple II version was derived from the Commodore 64 version. And a further clue is that these routines are still present in the BBC Master versions of Elite, but here the [SCALEX](https://elite.bbcelite.com/master/main/subroutine/scalex.html) and [SCALEY2](https://elite.bbcelite.com/master/main/subroutine/scaley2.html) routines have been stubbed-out so they only contain RTS instructions, and the [SCALEY](https://elite.bbcelite.com/master/main/subroutine/scaley.html) routine simply halves the value passed to it (which is used to make the Long-range Chart half as tall as it is wide). In isolation, this approach would makes no sense at all, as the code contains JSRs that either do nothing, or simply so what an LSR A instruction would do, but with extra jumps and returns; but if the Master source code was derived from the Apple II source code, this would be a simple fix to undo the scaling process but without having to weed out all those extra JSR calls.

So the Apple II version is derived from the Commodore 64 version, and the Master versions are derived from the Apple II version. We can therefore update our family tree as follows:

```
            Acorn Electron                   NES
          /                                /
  Cassette         6502 SP -> Commodore 64
   \      \      /                         \ 
     Demo <- Disc                             Apple II -> Master
                 \                                       Compact
                   Elite-A
```
						We're on the home straight now, so let's pick off the two closely related BBC Master versions on the right.

## Exhibit 9 of 10: The Compact variant

													 ------------------------------------

						The ninth piece of evidence is the extra code that's been added to the Compact variant, and the changes made to squeeze it in.

From a historical viewpoint, it's obvious that the version of Elite for the BBC Master Compact came later than the BBC Master version, as the Compact version is the only one to have been exclusively released by Superior Software when they licensed Acornsoft's titles and republished them under a joint name. Acornsoft itself never released a version for the Compact, as by that point the company didn't really exist anymore.

From a feature viewpoint, it's obvious that the Compact is a development of the Master version, adding support for ADFS (as the Compact doesn't support DFS) and digital joysticks (again, only on the Compact).

But can we prove that the Compact version is derived from the Master version? Well, look at the Compact's [ECMOF](https://elite.bbcelite.com/master/main/subroutine/ecmof.html) and [TTX66](https://elite.bbcelite.com/master/main/subroutine/ttx66.html) routines, for example. Adding the extra code to cope with ADFS and digital joysticks was a bit of a squeeze, so something had to give, and these two routines contain examples of this: variables are zeroed using the STZ instruction, which takes up less memory than the more usual pairing of LDA #0 and STA that the original versions use (because the standard 6502 doesn't support the STZ instruction). The BBC Master version uses the same LDA/STA approach as all the earlier versions, even though its CPU supports the STZ instruction; only the Compact version uses STZ here, so the Compact version must have been derived from the Master, because if it were the other way around, they would both use STZ.

So we can separate the two Master-related versions, as follows:

```
            Acorn Electron                   NES
          /                                /
  Cassette         6502 SP -> Commodore 64
   \      \      /                         \ 
    Demo <-  Disc                             Apple II -> Master -> Compact
                 \
                   Elite-A
```
						Our family tree is almost complete, but there is one more line to add, so let's do that now.

## Exhibit 10 of 10: Calculating 320-pixel rows

													 --------------------------------------------

						The final piece of evidence is the 320-pixel wide screen mode in the Acorn Electron version.

The original BBC Micro version of Elite saved a big chunk of memory by defining a custom screen mode. Based on mode 4 but with a width of just 256 pixels rather than the 320 pixels of the standard mode, this custom mode not only saves around 2K of RAM of screen memory, but it also simplifies the graphics routines. In particular, as each character row in the custom mode takes up exactly 256 bytes instead of 320, this makes it easy to work out the screen address of the start of a specific character row, and moving down to the next character row is a simple matter of increasing the high byte of the screen memory address - a very simple bit of code.

The Acorn Electron doesn't contain the 6845 chip that enables this wizardry in the BBC, so it has to use standard mode 4, giving us the Electron's uniquely monochrome game screen:

![Electron Elite screenshot](https://elite.bbcelite.com/images/general/Elite-Electron.png) 

						The game itself is still 256 pixels wide, but there's a 32-pixel wide black border to each side of the space view and dashboard, to pad the game out to the full 320-pixel width. As a result, if we have to move down a character row when drawing lines, we now have to add 320 to the screen memory address; to move up, we need to subtract 320. This multi-byte arithmetic is slower and less elegant than in the BBC Micro, but there's no way around it with a 320-pixel wide screen.

Interestingly, the Commodore 64's screen bitmap has the exact same layout in memory as the Electron's mode 4, so the code that moves up or down a character row is the same in the Commodore 64 version as it is in the Acorn Electron version. And the Electron did it first, so we can add another relationship between the Electron and the Commodore 64, as follows:

```
              Acorn Electron                  NES
            /                \              / 
           /                   Commodore 64
  Cassette                   /              \ 
   \       \         6502 SP                  Apple II -> Master -> Compact
    \       \      /
      Demo <- Disc
                   \
                     Elite-A
```
						And that, finally, gives us our complete Elite source code family tree.

## Honourable mentions

													 -------------------

						Of course, this family tree doesn't show all of the source code pathways, though it does capture the major relationships. Here are some further code relationships that are worth mentioning:

- The graphics routines in the BBC Master version are derived from those in the 6502 Second Processor version. This is no surprise as both versions use a custom split-screen mode that's based on mode 1 for the space view (four colours) and mode 2 for the dashboard (eight colours).
- The ship hangar code from the original BBC Micro disc version and 6502 Second Processor version made its way into the Master versions and the NES versions.
- The BBC-specific routines for saving and loading commander files and handling the keyboard also migrated from the 6502 Second Processor version to the Master versions.
- The NES version cherry picks the best features from its predecessors, so not only does it include the ship hangar, it also includes the 3D scroll text from the 6502 Second Processor, and it incorporates bug fixes from the Apple II and Master versions, despite being based on the Commodore 64 source.

It's perhaps no surprise that the BBC-specific routines for graphics, file operations and keyboard would make their way into the later BBC versions, but it's worth noting that the sound routines did not make a similar leap. Instead, the sound routines in the BBC Master versions are heavily based on the Commodore 64 sound routines, and they don't rely on the operating system's OSWORD function, unlike the original BBC Micro versions.

For more comparisons between the codebases, you can [compare the code for the different versions](https://elite.bbcelite.com/compare/how_to_compare.html).

## Release dates, hidden dates and title dates

													 -------------------------------------------

						As mentioned above, the BBC Micro doesn't have any concept of date and time, so there are no clues built into the source discs themselves. There is just one glimmer of hope: the Elite authors sometimes put a date into the disc title. Trawling through the source discs from Ian Bell's website, we have the following titles:

| Source disc | Drive 0 title | Drive 2 title | 
|---|---|---|
| Ship sources | Dks Shps10/6 | - | 
| BBC Micro cassette | 14/7BBCtape | SHIPS B/K 5/2 | 
| Acorn Electron | ELECTRON - I | - | 
| 6502 Second Processor | 10/4/85 2P | - | 
| Commodore 64 | C64 16/5/85 | - | 
| Apple II | AP 23/9/85 | - | 
| BBC Master | 23/1/86 | - | 

Of course, these dates could mean nothing: one might assume that they are version dates of some kind, but there isn't any evidence that this is the case. But they're still evidence of a sort, and if they are development dates, they do at least fit nicely into the family tree.

Perhaps more interesting are the dates that are embedded into three of the game binaries. The 6502 Second Processor and Commodore 64 versions have a completion date branded into a BBC Micro-format image that's included in the game binary but is never displayed (perhaps this was a way of obfuscating the date, for some reason). The Apple II version on the source disc also has a date image, but this time it's shown on the loading screen (this date was replaced by the Firebird logo in the official version).

The date images contain the following text:

| Version | Date | 
|---|---|
| 6502 Second Processor | 2nd Pro ELITE -Finished 13/12/84 | 
| Commodore 64 | Comm 64 ELITE-Finished 19/4/85 | 
| Apple II | 23 SEPT 1985 | 

If these are indeed completion dates of some kind, then they would imply a much earlier development date for the 6502 Second Processor version than that given in the disc title (13 December 1984 vs 10 April 1985).

Indeed, there's another clue on the source discs for the aborted sequel Elite II, which are also on Ian Bell's site. There's a VIEW word processor file called V.LETDAV2 ("letter to David 2") where Bell talks about the ongoing development of the 6502 Second Processor version, and mentions specifics like changing the "A*****R" extended system message to "C**** A*****" (i.e. from Aviator to Cylon Attack). The date of this letter is 27 August 1984, which is about three weeks before the announcement of the BBC Micro version - so the 6502 Second Processor version was indeed being developed early on, and the December completion date in the date image seems more likely.

This earlier development date still fits into the family tree, so that's a relief.

The date in the Apple II image also fits into the family tree, but it's worth bearing in mind that the version on the Apple II source disc has quite a few code differences to the released version, so even though the disc title and loading screen dates match, there was still an unknown amount of development time to go before the game was finished. So it's not that clear what this date signifies other than development was clearly happening around this time.

A final date that is worth taking into account is the release date for each version. But here, time's blur is the problem, and it turns out to be pretty difficult to pin down exact release dates for these old games.

For example, the 6502 Second Processor version of Elite was first shown off to the public at the Acorn User Show on 25 July 1985, and that matches the date of the source disc title reasonably well. But a news item in the April 1986 version of Acorn User about the reorganisation of Acornsoft casually mentions that "the upgraded version of Elite for the 6502 second processor with colour, Elite II, has yet to appear". So when was it actually released? I haven't found the answer yet.

Even the date of the launch party for the original version seems up for debate, with some claiming it was 20 September 1984 ([BBC](http://news.bbc.co.uk/1/hi/technology/8261272.stm), [Wikipedia](https://en.wikipedia.org/wiki/Elite_(video_game))), and others claiming it was 22 September 1984 ([Stardot](https://stardot.org.uk/forums/viewtopic.php?t=22023&start=30), [Drew Wagar](https://canonn.science/lore/drewwagar-history-the-original-elite/)). I've always thought it was the latter, but I haven't managed to prove it either way.

Incidentally, the V.LETDAV2 file from the Elite II source disc also says "PRESS LAUNCH NOW ON THURSDAY 13th." This must refer to 13 September 1984, so presumably there was a press-only day at Acorn the week before the public announcement, where journalists had a chance to play the game. So that's yet another date...

Meanwhile the Apple II version was either released in 1985 ([MobyGames](https://www.mobygames.com/game/1324/elite/)) or 1986 ([Frontier Astro](https://www.frontierastro.co.uk/Elite/apple.html), [Ian Bell](http://www.elitehomepage.org/c64/index.htm)) depending on who you ask. The only [contemporary review](https://mirrors.apple2.org.za/ftp.apple.asimov.net/documentation/magazines/washington_apple_journal/washingtonapplepijournal198605.pdf) I've managed to find is from May 1986, so it does feel as if 1986 is the correct year (especially as Ian Bell has this date on his site), but it's a good example of how you can't believe everything you read on the internet.

One thing's certain, though: tracking down reliable Elite-related dates is a bit of a challenge, so it's a good job we've got the source code to analyse... and so far none of the dates I've found have contradicted the family tree, so hopefully it's accurate.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron                  NES
            /                \              / 
           /                   Commodore 64
  Cassette                   /              \ 
   \       \         6502 SP                  Apple II -> Master -> Compact
    \       \      /
      Demo <- Disc
                   \
                     Elite-A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron
  Cassette
  Disc
  Demo
  6502 SP
  Commodore 64
  Apple II
  Master
  Compact
  NES
  Elite-A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron -> Commodore 64           6502 SP
  Cassette          Apple II
  Disc              Master
  Demo              Compact
                    NES
                    Elite-A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron -> Commodore 64           6502 SP
  Cassette          Apple II
  Demo              Master
  Disc              Compact
       \            NES
         Elite-A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron -> 6502 SP -> Commodore 64
  Cassette                     Apple II
  Demo                         Master
  Disc                         Compact
       \                       NES
         Elite-A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
6502 SP -> Commodore 64
                         /            Apple II
  Acorn Electron -> Disc              Master
  Cassette               \            Compact
  Demo                     Elite-A    NES
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron
          /
  Cassette         6502 SP -> Commodore 64
  Demo     \      /           Apple II
            Disc              Master
                 \            Compact
                   Elite-A    NES
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron
          /
  Cassette         6502 SP -> Commodore 64
   \       \      /           Apple II
    Demo <-  Disc              Master
                 \            Compact
                   Elite-A    NES
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`FLKB`** (unknown): No description available

```assembly
FLKB    LDA     #15
          TAX
          ;JMPOSBYTE
          RTS
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron                   NES
          /                                /
  Cassette         6502 SP -> Commodore 64
   \      \      /            Apple II
    Demo <-  Disc              Master
                 \            Compact
                   Elite-A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron                   NES
          /                                /
  Cassette         6502 SP -> Commodore 64
   \      \      /                         \ 
     Demo <- Disc                             Apple II -> Master
                 \                                       Compact
                   Elite-A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron                   NES
          /                                /
  Cassette         6502 SP -> Commodore 64
   \      \      /                         \ 
    Demo <-  Disc                             Apple II -> Master -> Compact
                 \
                   Elite-A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Acorn Electron                  NES
            /                \              / 
           /                   Commodore 64
  Cassette                   /              \ 
   \       \         6502 SP                  Apple II -> Master -> Compact
    \       \      /
      Demo <- Disc
                   \
                     Elite-A
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_elite_source_code_family_tree.html](https://elite.bbcelite.com/deep_dives/the_elite_source_code_family_tree.html)*
