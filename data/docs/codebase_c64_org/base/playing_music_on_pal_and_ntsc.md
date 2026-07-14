---
title: Playing music on PAL and NTSC
source_url: https://codebase.c64.org/doku.php?id=base%3Aplaying_music_on_pal_and_ntsc
category: reference
topics:
- basic
- sound generation
difficulty: advanced
language: basic
hardware:
- SID
- CPU
- CIA
- KERNAL
related:
- keyboard-handling
- sound-programming
- cia-registers
- memory-map
- sid-registers
- music-player
- kernal-routines
- joystick-reading
scraped_at: '2026-07-14'
---

# Playing music on PAL and NTSC

### Table of Contents

# Playing music on PAL and NTSC

By FTC/HT

This article deals (briefly) with the question of how to play PAL tunes on a NTSC system, and vice versa. Most music players are called once a frame in order to update the music which is playing. One PAL frame is 312*63=19656 ($4CC8) cycles and one NTSC frame is 263*65=17095 ($42C7) cycles. In addition, a cycle is in itself taking a different amount of time on a PAL system compared to on a NTSC system because the system clocks run at different speeds. A PAL processor executes 985248 cycles each second and a NTSC system executes 1022727 cycles. The question we are asking now is:

What timer values do we need to use for our timer interrupts in order to play our PAL and NTSC tunes correctly on the opposite kind of system?

PAL/NTSC speed ratio:

985248 / 1022727 = 0.963353857

So… In order to play a PAL tune on a NTSC system, in “PAL” speed, you should use the following timer value in your timer interrupt:

```
19656 / 0.963353857 = 20403.717551 ($4FB3) ...or rather $4FB2, since the timer 
                                      counts from 0, and not from 1.
```
Let's do the opposite calculation too:

```
1022727 / 985248 = 1.038040169  ...NTSC/PAL speed ratio
1.038040169 * 17095 = 17745.3 ($4551) ...or rather $4550, since the timer 
                                      counts from 0, and not from 1.
```
This means, playing a NTSC tune on a PAL machine requires the timer to be set to $4550.

Note that there are still other differences regarding music playback on PAL and NTSC machines. For example, the differing system clock speeds make the pitch come out slightly different on these two systems. This can't be compensated for in a self-evident manner, since the pitch is not a linear function on the SID, so you can't just add an “offset” to the frequencies to correct them, since the offset would (at least in theory) have to have different size (logaritmic) at different pitch heights, and (as pointed out by Devia in the CSDb forum thread below) this affects how portamentos and vibratos and that kind of effects will sound.

Also see [this related thread](http://noname.c64.org/csdb/forums/) on CSDb.

Good luck!

/FTC

## Addendum: Playing PAL music on PAL-N (drean)

Ratio between PAL and PAL-N:

98524/102344 = 0.9626749003

So… In order to play a PAL tune on a PAL-N system, in “PAL” speed, you should use the following timer value in your timer interrupt:

```
19656 / 0.9626749003 = 20418.107914 ($4FC2) ...or rather $4FC1, since the timer 
                                      counts from 0, and not from 1.
```
/riq

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
985248 / 1022727 = 0.963353857
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
19656 / 0.963353857 = 20403.717551 ($4FB3) ...or rather $4FB2, since the timer 
                                      counts from 0, and not from 1.
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
1022727 / 985248 = 1.038040169  ...NTSC/PAL speed ratio

1.038040169 * 17095 = 17745.3 ($4551) ...or rather $4550, since the timer 
                                      counts from 0, and not from 1.
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
98524/102344 = 0.9626749003
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
19656 / 0.9626749003 = 20418.107914 ($4FC2) ...or rather $4FC1, since the timer 
                                      counts from 0, and not from 1.
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Aplaying_music_on_pal_and_ntsc](https://codebase.c64.org/doku.php?id=base%3Aplaying_music_on_pal_and_ntsc)*
