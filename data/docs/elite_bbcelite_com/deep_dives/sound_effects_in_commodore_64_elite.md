---
title: Sound effects in Commodore 64 Elite
source_url: https://elite.bbcelite.com/deep_dives/sound_effects_in_commodore_64_elite.html
category: deep-dive
topics:
- raster interrupts
- assembly
- sound generation
- basic
difficulty: beginner
language: mixed
hardware:
- KERNAL
- SID
- CIA
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

# Sound effects in Commodore 64 Elite

## Making the most of the SID sound synthesiser

Even the biggest fans of BBC Micro Elite will have to admit that the sound effects aren't the game's strongest point. Sure, for those of us who played it relentlessly back in the day, we'll never forget the distinctive sound of being strafed by lasers, or the chirping of the E.C.M. as another missile explodes with a crash. But just because those sounds are ingrained, it doesn't mean they're Oscar-worthy.

The sound effects on the Commodore 64 version are noticeably better than on the BBC Micro, which is not a big surprise when you consider the system's excellent SID sound synthesiser chip. The Commodore 64 version has a brand new set of sound routines, so let's take a look at how it all works.

## The sound effects

													 -----------------

						The BBC Micro defines just [four sound envelopes](https://elite.bbcelite.com/cassette/loader/variable/e_per_cent.html) for the whole game, which uses a total of ten different sounds, as defined in the [SFX](https://elite.bbcelite.com/cassette/main/variable/sfx.html) table. The Commodore 64 version bumps this up to 16 sound effects, as follows:
						

| # | Variable | Description | 
|---|---|---|
| 0 | sfxplas | Pulse lasers fired by us | 
| 1 | sfxelas | Being hit by lasers 1 | 
| 2 | sfxhit | Other ship exploding | 
| 3 | sfxexpl | We died / Collision | 
| 4 | sfxwhosh | Missile launched / Ship launch | 
| 5 | sfxbeep | Short, high beep | 
| 6 | sfxboop | Long, low beep | 
| 7 | sfxhyp1 | Hyperspace drive engaged 1 | 
| 8 | sfxeng | This sound is not used | 
| 9 | sfxecm | E.C.M. on | 
| 10 | sfxblas | Beam lasers fired by us | 
| 11 | sfxalas | Military lasers fired by us | 
| 12 | sfxmlas | Mining lasers fired by us | 
| 13 | sfxbomb | Energy bomb | 
| 14 | sfxtrib | Trumbles dying | 
| 15 | sfxelas2 | Being hit by lasers 2 | 

The variables can be passed in the Y register to the [NOISE](https://elite.bbcelite.com/c64/main/subroutine/noise.html) routine to make the specified sound effect, so this is how we can make the sound of the E.C.M. starting up, for example:

LDY #sfxecm JSR NOISE

Associated with the sound effects are a number of SFX tables, each of which contributes an aspect of each sound effect.

| Variable | Description | 
|---|---|
| [SFXPR](https://elite.bbcelite.com/c64/main/variable/sfxpr.html) | The priority level for each sound effect | 
| [SFXCNT](https://elite.bbcelite.com/c64/main/variable/sfxcnt.html) | The counter for each sound effect, which defines the duration of the effect in frames | 
| [SFXFQ](https://elite.bbcelite.com/c64/main/variable/sfxfq.html) | The frequency (SID+$5) for each sound effect | 
| [SFXCR](https://elite.bbcelite.com/c64/main/variable/sfxcr.html) | The voice control register (SID+$4) for each sound effect | 
| [SFXATK](https://elite.bbcelite.com/c64/main/variable/sfxatk.html) | The attack and decay length (SID+$5) for each sound effect | 
| [SFXSUS](https://elite.bbcelite.com/c64/main/variable/sfxsus.html) | The release length and sustain volume (SID+$6) for each sound effect | 
| [SFXFRCH](https://elite.bbcelite.com/c64/main/variable/sfxfrch.html) | The frequency change to be applied to each sound effect in each frame (as a signed number) | 
| [SFXVCH](https://elite.bbcelite.com/c64/main/variable/sfxvch.html) | The volume change rate for each sound effect, i.e. how many frames need to pass before the sound effect's volume is reduced by one | 

When a sound effect is triggered by a call to the NOISE routine, the first thing we do is try to find a voice where we can make that sound effect. The SID chip provides three voices, numbered 0 to 2, so we work through each voice to check whether this sound effect is already playing, and if it is, we can reuse that voice (if this effect is configured to allow this). Otherwise we keep looking to find a voice that's either unused or at a lower priority than the sound effect we want to make, and assuming we find one, we start the process of making the sound effect on that voice.

The first step is to initialise the sound variables for this voice, which can be found in the [sound variables workspace](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html). This workspace contains a set of variables that consist of three bytes, one for each voice, so to start making a sound effect, we copy the relevant data for this sound effect from the SFX tables above, and put the data into the sound workspace variables for the chosen voice.

These are the relevant variables from the workspace, along with the SFX tables from which they are initialised:

| Variable | Description | Source | 
|---|---|---|
| [SOFLG](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#soflg) | Sound effect number and "new sound" flag | - | 
| [SOCNT](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#socnt) | Counter | SFXCNT | 
| [SOPR](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sopr) | Priority | SFXPR | 
| [SOFRCH](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sofrch) | Frequency change | SFXFRCH | 
| [SOFRQ](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sofrq) | Frequency | SFXFQ | 
| [SOCR](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#socr) | Voice control register values | SFXCR | 
| [SOATK](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#soatk) | Attack and decay lengths | SFXATK | 
| [SOSUS](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sosus) | Release length and sustain volume | SFXSUS | 
| [SOVCH](https://elite.bbcelite.com/c64/main/workspace/sound_variables.html#sovch) | Volume change rate | SFXVCH | 

Like the game's music, the actual sounds are made during the [COMIRQ1](https://elite.bbcelite.com/c64/main/subroutine/comirq1.html) interrupt routine that's called twice every screen refresh. If there is no music playing, then this calls the [SOINT](https://elite.bbcelite.com/c64/main/subroutine/soint.html) routine on every other interrupt, so that's once every screen refresh (if music is playing, then sound effects are disabled). This means that the routine is called 50 times a second on PAL systems or 60 times a second on NTSC systems, so sound effects are shorter and snappier on the latter.

The SOINT routine actually makes the sound effects on each voice, using the values in the sound workspace. It starts a new sound effect by sending the relevant values to the SID chip and setting a flag in the SOFLG variable so we don't initialise the effect twice. On each call to the routine, it decrements the sound's priority, moves the counter on, and implements features like the frequency change in SOFRCH/SFXFRCH and the volume change in SOVCH/SFXVCH, which are not automatically supported by the SID. When the counter runs out, it terminates the sound and clears the voice, so it's ready for the next sound effect.

This system was carried forward into the BBC Master version, where the SID-specific code was converted to send values to the Master's SN76489 sound chip instead of the SID. As a result, the BBC Master has more sophisticated sound effects than the original, and it's all thanks to the Commodore 64 and its legendary sound capabilities.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
LDY #sfxecm
  JSR NOISE
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/sound_effects_in_commodore_64_elite.html](https://elite.bbcelite.com/deep_dives/sound_effects_in_commodore_64_elite.html)*
