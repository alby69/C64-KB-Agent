---
title: Secrets of the Executive version
source_url: https://elite.bbcelite.com/deep_dives/secrets_of_the_executive_version.html
category: manual
topics:
- basic
- assembly
difficulty: intermediate
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

# Secrets of the Executive version

## Infinite jumps, retro-futuristic fonts, speech support... and Pizzasoft?

*Note that in the following article, there may be a swearword or two, so I guess it should come with a NSFW warning. I never thought I'd be writing that in an article about Elite, but there you go!*

The Executive version of Elite has always had a whiff of mystery about it. According to the [alt.fan.elite FAQ](http://bbc.nvg.org/doc/games/EliteFAQ.htm#3.4), it was coded up by Ian Bell and given out to just a handful of people, and it was never intended for official release. This makes sense when you consider some of the more risqué aspects of this version, but as some of the new features are clearly there to make life easier for players - such as a maxed-out commander and infinite jumps - there's a possibility that it's a special version aimed at reviewers, so they could check out the more advanced features of the game without having to spend days grinding their way to a decent ship.

![The Executive version of 6502 Second Processor Elite](https://elite.bbcelite.com/images/6502sp/executive.png) 

						Although its true purpose has never been confirmed, one thing is sure: it's never been particularly clear what the differences are between this version and the standard 6502 Second Processor version on which is it based. Let's see if we can rectify this, with a comprehensive run-down of what makes the Executive version so... "executive", I guess.

## Obvious changes

													 ---------------

						Some of the differences in Executive Elite are pretty obvious, so let's cover those first.

- As soon as the game has finished loading, the demo kicks in, whether you like it or not (see the next section for a discussion of what's different in the demo itself).
- The game uses a totally different font to the other versions, which all use the standard BBC character set. The character set in the Executive version is based on the 1960s Westminster font, which is similar to the machine-readable numbers printed on cheques - "retro-futuristic" is probably what we'd call it these days, though I suspect it was a little more "futuristic" back in 1984.
								![The different font of 6502 Second Processor Elite](/images/6502sp/executive_status_mode.png)  
- You start out with a maxed-out commander, called Firebud instead of Jameson. The name is presumably a seven-character riff on "Firebird", the publishers of the non-Acorn versions of Elite, and there's also a "Firebird" string buried in the code, so presumably this version has more to do with Firebird rather than Acornsoft, though it isn't clear why.
- The in-flight messages are rather more polite, saying "ENERGY LOW,SIR" and "INCOMING MISSILE,SIR" when things start getting hairy.
- Lave and Riedquat have extended system description overrides that are unique to this version, and which you can see by landing at those systems and looking at the Data on System (see the full feature list below for more details, but you can see the Lave override by pressing f6 after starting the game).

Now these are out of the way, let's look at the demo in more detail, as that's the very first thing you see in this version.

## Pizzasoft

													 ---------

						Anyone who has fired up the Executive version will know about its most blatant change. As soon as the game finishes loading, it jumps straight into the demo mode that was first introduced in the official 6502 Second Processor release, though the Executive version has quite a few differences in the scroll text.

The very first part sets the scene, announcing "PIZZASOFT PRESENTS" instead of "ACORNSOFT PRESENTS" - presumably to underline the fact that this is far from an official release. The scroll text then introduces "THE EXECUTIVE VERSION", and instead of talking about the galaxy being in turmoil, as the standard release does, it goes on to say "CONGRATULATIONS ON OBTAINING A COPY OF THIS ELUSIVE PRODUCT."

Note that it says "ELUSIVE", not "EXCLUSIVE". It's all part of the mystery, I guess. Who wouldn't want to get their hands on an elusive piece of gaming history?

(Also, it's worth noting that the interactive "mock battle" that's described in the [alt.fan.elite FAQ](http://bbc.nvg.org/doc/games/EliteFAQ.htm#3.4) doesn't actually exist. The demo is still just the standard 6502 Second Processor demo, which is not interactive in any way; the only differences are in the scroll text.)

## Infinite jumps

													 --------------

						The Executive version has a new configuration option that lets you jump an infinite distance with your hyperspace drive, and without using any fuel. To enable this option, pause the game and press "@"; you will hear a ping when it is enabled, just as with all the other configuration options.

Once enabled, you can move the crosshairs to any system in the galaxy, and can use your hyperspace drive to jump there. No fuel will be used, and although the jump range circle is still shown on the charts, it is ignored.

This is a particularly useful feature if you want to check out all the extended system description overrides, which only get shown once you dock at the relevant system. Using the system search feature ("F" in the system charts), you can search for a system and jump straight there, so the only challenge is getting to the space station (though given the maxed-out Firebud commander, you can just use your escape pod to dock instantly). It's much easier than hacking your commander file.

There is a subtle clue to this functionality in-game: the extended system description override for Riedquat says "Only this executive version has the @ toggle", though you do have to be docked there to see this.

## Sweary speech support

													 ---------------------

						The Executive version supports speech, but only if you have the Watford Electronics Beeb Speech Synthesiser fitted. You also have to enable speech, which you can do by pausing the game and pressing ":".

A warning: if you enable speech and don't have a Beeb Speech Synthesiser plugged into the user port, the game will crash with a Bad Command error whenever the game tries to speak.

For those of us without a real BBC Micro/6502 Second Processor/Watford Electronics Beeb Speech Synthesiser combo - so that's most of us, I guess - emulation is the best way to experience this feature; see the next section for details of how to set this up.

If you just want to hear the speech, then here are some recordings taken from Executive Elite running in the MAME emulator. There are four phrases that are implemented, as follows:

- It says "Elite" when the title screen is displayed:
- It says "Incoming missile" every time the "INCOMING MISSILE,SIR" message flashes on-screen:
- It says "Energy low" every time the "ENERGY LOW,SIR" message flashes on-screen:
- It says "Oh shit, it's a mis-jump" when we mis-jump into witchspace (this happens with both accidental and manually triggered mis-jumps):

Given the last one, I think it's pretty obvious why this version was never considered for an official release. I mean, that pronunciation of "jump" is just *terrible*...

## Emulating speech in MAME

													 ------------------------

						If you want to try out the speech feature for yourself, then at the time of writing there's only one emulator that I know of that can emulate everything we need: version 0.280 of MAME. This version can emulate both the required BBC Micro and the Beeb Speech Synthesiser, which is absolutely amazing given how esoteric this hardware combination is. Earlier versions of MAME can emulate the speech synthesiser but can't run Elite properly, so make sure you have the correct version.

To set things up, you first need to [download and install MAME](https://www.mamedev.org/). Then you need to track down the latest set of BBC ROMs on Stardot, which should appear in this [forum search](https://stardot.org.uk/forums/search.php?keywords=MAME+%22System+roms+for+all+Acorn+machines%22&terms=all&author=&fid%5B%5D=4&sc=1&sf=firstpost&sr=posts&sk=t&sd=d&st=0&ch=300&t=0&submit=Search) in a post with a name like "MAME 0.xxx - System roms for all Acorn machines" (if you can't search the forum, then here's a [direct link to the ROMs that work with version 0.280](https://stardot.org.uk/forums/viewtopic.php?p=363297)).

Once you have extracted the ROMs into the roms folder within MAME, you can then fire up the emulator. Open up the command line or terminal and change directory into the folder where you installed MAME. Then try running MAME with the following command:

mame bbcb -userport beebspch -window

This should open up a window showing an emulated BBC Micro. If you want to test the speech synthesiser, you can enter the following commands to hear the above phrases, which are broken down into allophones like this:

*TALK EH LL EY TT1 *TALK A NN1 PA2 KK3 AA MM IH NG PA4 MM IH SS I LL *TALK N ER1 G PA4 LOW *TALK O PA2 SH IH TT1 PA5 IH TT1 SS PA4 A PA4 MM IS PA2 JH UW1 MM PP

This is exactly what Elite does - you can see these phrase commands in the [SPEECH](https://elite.bbcelite.com/6502sp/main/variable/speech.html) variable, while the [TALK](https://elite.bbcelite.com/6502sp/main/subroutine/talk.html) routine actually sends these commands to the speech synthesiser. And if you want to improve the pronunciation in the last one, try ending it with "JH AX MM PP" instead - that's noticeably better.

To play the Executive version of Elite in MAME, first you need to download the [Executive Elite disc image](https://elite.bbcelite.com/versions/elite/elite-6502sp-executive.ssd) and save it to your computer. You can then run MAME like this (entering the command all on one line):

```
  mame bbcb -fdc acorn1770 -userport beebspch -tube 6502 -window
            -flop1 <path_to_ssd>
```
						Change <path_to_ssd> to the full pathname of the disc image you just downloaded, so if you are on Windows and you downloaded the disc image into your Downloads folder and your name is Mark, you might run MAME like this:

```
  mame bbcb -fdc acorn1770 -userport beebspch -tube 6502 -window
            -flop1 C:\Users\Mark\Downloads\elite-6502sp-executive.ssd
```
						This should open up a window showing an emulated BBC Micro and with the Executive disc loaded in drive 0.

The next step is to work out which key on your keyboard maps to the ":" key on the emulated BBC Micro. On my British PC keyboard, for example, it maps to the apostrophe key, but it's best if you work it out for yourself, as this is the key you'll need to press in-game to enable speech. Try pressing a few; eventually you'll find one that prints a colon in the BBC Micro window.

Once you've worked out which key to press, boot the game disc by pressing SHIFT-F12. Executive Elite should start up, and you have to sit through the demo (annoyingly you can't skip it). When you get to the title screen, press the space bar twice to get to the Status Mode screen. Pause the game by pressing End (which maps to COPY on the BBC Micro), then toggle speech by tapping the key you discovered above, the one that maps to ":" on the BBC Micro. You should hear a beep, so now press Escape to restart the game with speech enabled.

If everything has worked, you should hear the computer say "Elite" when it shows the title screen. And you can also enjoy the three other speech effects shown above, though you'll have to dive into the game to trigger those.

Welcome to the future, Commander!

## A full list of unique features in the Executive version

													 -------------------------------------------------------

						That's all the main features covered. For a full and comprehensive list of all differences in the Executive version when compared to the Acornsoft SNG45 release, see the list of [all 6502 Second Processor variants](https://elite.bbcelite.com/6502sp/releases.html).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
mame bbcb -userport beebspch -window
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
*TALK EH LL EY TT1

  *TALK A NN1 PA2 KK3 AA MM IH NG PA4 MM IH SS I LL

  *TALK N ER1 G PA4 LOW

  *TALK O PA2 SH IH TT1 PA5 IH TT1 SS PA4 A PA4 MM IS PA2 JH UW1 MM PP
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
mame bbcb -fdc acorn1770 -userport beebspch -tube 6502 -window
            -flop1 <path_to_ssd>
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
mame bbcb -fdc acorn1770 -userport beebspch -tube 6502 -window
            -flop1 C:\Users\Mark\Downloads\elite-6502sp-executive.ssd
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/secrets_of_the_executive_version.html](https://elite.bbcelite.com/deep_dives/secrets_of_the_executive_version.html)*
