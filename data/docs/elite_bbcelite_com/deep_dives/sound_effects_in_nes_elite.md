---
title: Sound effects in NES Elite
source_url: https://elite.bbcelite.com/deep_dives/sound_effects_in_nes_elite.html
category: deep-dive
topics:
- basic
- sound generation
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

# Sound effects in NES Elite

## The largest set of sound effects in all the 6502 Elites

The original Elite isn't particularly well-known for its sound effects - space, it turns out, is pretty quiet most of the time. NES Elite doesn't break with this trend, but it does have a lot more sound effects than in the earlier versions, so that's something.

(Incidentally, Elite Dangerous is completely the other way around; the sound design in E:D is really quite special, and deserves all the praise it gets.)

As with the music routines in NES Elite, the sound routines were written by David Whittaker, one of the most prolific sound artists of the 8-bit era. His CV is quite astonishing - here's a biography that includes a [list of games on which he worked](https://www.vgmpf.com/Wiki/index.php?title=David_Whittaker). Warning: it's a very long list.

Let's see how these sound effects work.

## The sound effects

													 -----------------

						The [NOISE](https://elite.bbcelite.com/nes/bank_7/subroutine/noise.html) routine generates all the sound effects in the game. It takes the sound number as an argument, and the full list of sound effects is as follows, along with the names of the routines that initiate them:

| # | Description | Initiated by | 
|---|---|---|
| 0 | Unused | - | 
| 1 | Fuel scoop | [MakeScoopSound](https://elite.bbcelite.com/nes/bank_7/subroutine/makescoopsound.html) | 
| 2 | E.C.M. | [ECBLB2](https://elite.bbcelite.com/nes/bank_7/subroutine/ecblb2.html) | 
| 3 | Short, high beep | [BEEP](https://elite.bbcelite.com/nes/bank_7/subroutine/beep.html) | 
| 4 | Long, low beep | [BOOP](https://elite.bbcelite.com/nes/bank_7/subroutine/boop.html) | 
| 5 | Trumbles in the hold sound 1, 75% chance | [Main game loop (Part 5)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_game_loop_part_5_of_6.html) | 
| 6 | Trumbles in the hold sound 2, 25% chance | [Main game loop (Part 5)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_game_loop_part_5_of_6.html) | 
| 7 | Low energy beep | [Main flight loop (Part 15)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_15_of_16.html) | 
| 8 | Energy bomb | [Main flight loop (Part 3)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_3_of_16.html) | 
| 9 | Missile launch | [FRMIS](https://elite.bbcelite.com/nes/bank_0/subroutine/frmis.html),[SFRMIS](https://elite.bbcelite.com/nes/bank_0/subroutine/sfrmis.html) | 
| 10 | Us making a hit or kill | [EXNO](https://elite.bbcelite.com/nes/bank_0/subroutine/exno.html) | 
| 11 | Us being hit by lasers | [TACTICS (Part 6)](https://elite.bbcelite.com/nes/bank_0/subroutine/tactics_part_6_of_7.html) | 
| 12 | First launch sound | [LAUN](https://elite.bbcelite.com/nes/bank_0/subroutine/laun.html) | 
| 13 | Explosion/collision sound | [EXNO3](https://elite.bbcelite.com/nes/bank_7/subroutine/exno3.html) | 
| Ship explosion at distance z_hi < 6 | [EXNO2](https://elite.bbcelite.com/nes/bank_0/subroutine/exno2.html) | |
| 14 | Ship explosion at distance z_hi >= 6 | [EXNO2](https://elite.bbcelite.com/nes/bank_0/subroutine/exno2.html) | 
| 15 | Military laser firing | [Main flight loop (Part 3)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_3_of_16.html) | 
| 16 | Mining laser firing | [Main flight loop (Part 3)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_3_of_16.html) | 
| 17 | Beam laser firing | [Main flight loop (Part 3)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_3_of_16.html) | 
| 18 | Pulse laser firing | [Main flight loop (Part 3)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_3_of_16.html) | 
| 19 | Escape pod launching | [ESCAPE](https://elite.bbcelite.com/nes/bank_0/subroutine/escape.html) | 
| 20 | Unused | - | 
| 21 | Hyperspace | [MakeHyperSound](https://elite.bbcelite.com/nes/bank_7/subroutine/makehypersound.html) | 
| 22 | Galactic hyperspace | [Ghy](https://elite.bbcelite.com/nes/bank_0/subroutine/ghy.html) | 
| 23 | Ship explosion at distance z_hi >= 8 | [LAUN](https://elite.bbcelite.com/nes/bank_0/subroutine/laun.html) | 
| Ship explosion at distance z_hi >= 8 | [EXNO2](https://elite.bbcelite.com/nes/bank_0/subroutine/exno2.html) | |
| 24 | Second launch sound | [LAUN](https://elite.bbcelite.com/nes/bank_0/subroutine/laun.html) | 
| 25 | Unused | - | 
| 26 | No noise | [FlushSoundChannel](https://elite.bbcelite.com/nes/bank_7/subroutine/flushsoundchannel.html) | 
| 27 | Ship explosion at a distance of z_hi >= 16 | [EXNO2](https://elite.bbcelite.com/nes/bank_0/subroutine/exno2.html) | 
| 28 | Trill noise to indicate a purchase | [BuyAndSellCargo](https://elite.bbcelite.com/nes/bank_0/subroutine/buyandsellcargo.html) | 
| 29 | First mis-jump sound | [MJP](https://elite.bbcelite.com/nes/bank_0/subroutine/mjp.html) | 
| 30 | Second mis-jump sound | [MJP](https://elite.bbcelite.com/nes/bank_0/subroutine/mjp.html) | 
| 31 | Trumbles being killed by the sun | [Main flight loop (Part 15)](https://elite.bbcelite.com/nes/bank_0/subroutine/main_flight_loop_part_15_of_16.html) | 

The NOISE routine works by first fetching the list of APU channels that the sound effect requires from the [soundChannel](https://elite.bbcelite.com/nes/bank_7/variable/soundchannel.html) table; sound effects can use the SQ1, SQ2 and NOISE channels (sound effects in NES Elite don't use the TRI channel). It then checks to see if an existing effect is already being made on those channels; if a channel is empty then the new effect is made, but if there is an existing sound effect being made on a channel, the code compares the priority of the existing effect with the new one, as defined for each effect in the [soundPriority](https://elite.bbcelite.com/nes/bank_7/variable/soundpriority.html) table. The higher priority sound effect wins out. (Note that sound effects always take priority over music, but this is controlled by the music routines, rather than using the soundPriority - at this stage we are only prioritising between sound effects.)

Sound effects are actually made via the [StartEffect](https://elite.bbcelite.com/nes/bank_6/subroutine/starteffect.html) routine, which gets called once for each channel that the new sound effect uses. StartEffect then calls [StartEffectOnSQ1](https://elite.bbcelite.com/nes/bank_6/subroutine/starteffectonsq1.html), [StartEffectOnSQ2](https://elite.bbcelite.com/nes/bank_6/subroutine/starteffectonsq2.html) or [StartEffectOnNOISE](https://elite.bbcelite.com/nes/bank_6/subroutine/starteffectonnoise.html) as appropriate, to start making the correct sounds on the SQ1, SQ2 and NOISE channels as required.

The Start routines set up the sound effect and send the first batch of data to the APU, but it's the NMI handler that continues the good work. The NMI handler calls the [MakeSounds](https://elite.bbcelite.com/nes/bank_6/subroutine/makesounds.html) routine in every VBlank, which then calls the [MakeSound](https://elite.bbcelite.com/nes/bank_6/subroutine/makesound.html) routine to make the configured sound effects. This in turn calls the [UpdateVibratoSeeds](https://elite.bbcelite.com/nes/bank_6/subroutine/updatevibratoseeds.html) routine to randomise the seeds that are used to make a vibrato effect, and then it calls [MakeSoundOnSQ1](https://elite.bbcelite.com/nes/bank_6/subroutine/makesoundonsq1.html), [MakeSoundOnSQ2](https://elite.bbcelite.com/nes/bank_6/subroutine/makesoundonsq2.html) and [MakeSoundOnNOISE](https://elite.bbcelite.com/nes/bank_6/subroutine/makesoundonnoise.html) to send the sound effect data to the APU.

The data that is sent to the APU for each sound effect is defined in that sound's data block. This defines all sorts of aspects of the sound effect, so let's take a look at that next.

## Sound data format

													 -----------------

						Each of the above sound effects has an associated data block in the [soundData](https://elite.bbcelite.com/nes/bank_6/variable/sounddata.html) table. Each sound data block is made up of 14 bytes, which are copied to the [soundByteSQ1](https://elite.bbcelite.com/nes/common/workspace/wp.html#soundbytesq1), [soundByteSQ2](https://elite.bbcelite.com/nes/common/workspace/wp.html#soundbytesq2) or [soundByteNOISE](https://elite.bbcelite.com/nes/common/workspace/wp.html#soundbytenoise) blocks (one for each channel) where they can be manipulated. This is so counters within the data block can be updated *in situ*, as the original soundData table is in ROM and can't be changed.

The sound data block controls the sending of data to the APU during each iteration of the sound effect routine (which is typically every VBlank). The following documentation talks about channel SQ1, but the same logic applies to the SQ2 and NOISE channels.

The list of bytes in the sound effect data block is as follows:

| Byte #0 Length of sound (in iterations) | 
| Ignored if the sound is an infinite loop (i.e. if byte #12 is non-zero)Gets decremented on each iteration
 | 
| Byte #1 How often we send pitch data to the APU | 
| So we send pitch data to the APU every byte #1 iterations
 | 
| Bytes #2 and #3 The first 16-bit pitch data to send to (SQ1_HI SQ1_LO) | 
| Used as 16-bit storage for (soundHiSQ1 soundLoSQ1), which contains the pitch data to send to the APU for this iterationThis gets sent to the APU via (SQ1_HI SQ1_LO) to set the sound effect's pitch as the effect progresses
 | 
| Bytes #4 and #5 A 16-bit value to apply to the pitch every iteration | 
| The pitch is only varied if enabled by byte #8 being non-zero
 | 
| Byte #6 High nibble of the SQ1_VOL byte | 
| This value gets OR'd with the soundVolumeSQ1 variable to send to the APU via SQ1_VOLIt sets the duty, loop and NES envelope settings to send to the APU
 | 
| Byte #7 Add vibrato | 
| Non-zero means add vibrato to the pitch on each iteration using the randomised vibrato value in soundVibrato
 | 
| Byte #8 Enable/disable the pitch variation in byte #4/#5 | 
| Non-zero means:
											Bit 7 clear = subtract byte #4/#5 from the APU pitch on each iteration (so the note frequency goes up)Bit 7 set = add byte #4/#5 to the APU pitch on each iteration (so the note frequency goes down)
Zero disables the pitch variation in byte #4/#5
 | 
| Byte #9 Number of iterations for which we send pitch data to the APU | 
| Ignored if the sound is an infinite loop (i.e. if byte #12 is non-zero)
 | 
| Byte #10 Number of the volume envelope to apply | 
| This is the number of the envelope to apply from the [soundVolume](https://elite.bbcelite.com/nes/bank_6/variable/soundvolume.html)table
 | 
| Byte #11 How often we apply the volume envelope to the sound | 
| We apply the next entry from the volume envelope every byte #11 iterations
 | 
| Byte #12 Enable/disable infinite loop | 
| Non-zero means the sound effect loops and keeps being made, even after the counter in byte #0 runs downZero means the sound only runs for the number of iterations in byte #0
 | 
| Byte #13 How often to apply the pitch variation in byte #4/#5 | 
| If pitch variation is enabled by byte #8 being non-zero, then:
											Non-zero means only apply the pitch variation in byte #4/#5 every byte #13 iterationsZero means apply the pitch variation every iteration
 | 

The above table defines everything about the sound that we need to send to the APU. Vibrato is applied using the randomised byte from the soundVibrato variable, but the only other bit of data that's needed to make each sound is the volume envelope that's configured by bytes #10 and #11, so let's have a look at that.

The volume envelopes can be found in the [soundVolume](https://elite.bbcelite.com/nes/bank_6/variable/soundvolume.html) table. The changes in volume defined in these envelopes are applied to the sound effect by altering the channel's volume register (such as SQ1_VOL for channel SQ1). Entries in the soundEnvelope table only have the low nibble populated (apart from the $FF value that signifies the end of the data), and this is combined with the high nibble from byte #6 in the sound data block, which sets the duty, loop and NES envelope settings to send to the APU. In this way the volume envelope changes the volume of the sound effect as it progresses, according to the data in the specified envelope and the settings in the sound data block.

Of course, the table above just describes David Whittaker's sound player, which takes the sound data and pushes it to the APU. The clever part is creating the sound effects in the first place, and encoding them into a sound data block to make the desired noise. How that part works is David Whittaker's secret, though it's clear that the sound routines (as with the music routines) were generated using macros, as each different channel has its own separate routines and variable blocks that contain almost identical code, with channels like NOISE and TRI only differing slightly from the two square-wave channels. Presumably he had a macro-based build system that allowed him to churn out bespoke sound engines for new games relatively easily; it's no wonder he was able to be so prolific.

The music routines are similarly structured, and are described in the deep dive on [music in NES Elite](https://elite.bbcelite.com/music_in_nes_elite.html).

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Length of sound (in iterations)
```

### Snippet Codice (BASIC)

```basic
How often we send pitch data to the APU
```

### Snippet Codice (BASIC)

```basic
The first 16-bit pitch data to send to (SQ1_HI SQ1_LO)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
A 16-bit value to apply to the pitch every iteration
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
High nibble of the SQ1_VOL byte
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Add vibrato
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Enable/disable the pitch variation in byte #4/#5
```

### Snippet Codice (BASIC)

```basic
Number of iterations for which we send pitch data to the APU
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Number of the volume envelope to apply
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
How often we apply the volume envelope to the sound
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
Enable/disable infinite loop
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
How often to apply the pitch variation in byte #4/#5
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/sound_effects_in_nes_elite.html](https://elite.bbcelite.com/deep_dives/sound_effects_in_nes_elite.html)*
