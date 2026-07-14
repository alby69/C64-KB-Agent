---
title: The dashboard indicators
source_url: https://elite.bbcelite.com/deep_dives/the_dashboard_indicators.html
category: deep-dive
topics:
- assembly
difficulty: intermediate
language: mixed
hardware:
- SID
- KERNAL
related:
- music-player
- sound-programming
- memory-map
- kernal-routines
- sid-registers
scraped_at: '2026-07-14'
---

# The dashboard indicators

## How the bar-based dashboard indicators display their data

The dashboard shows an awful lot of information, and the vast majority of the indicators are bar-based (there are 11 bar indicators in all). These indicators appear on either side of the 3D scanner, like this:

![The dashboard in the BBC Micro version of Elite](https://elite.bbcelite.com/images/cassette/dashboard.png) 

						The game uses one routine to display all 11 of these indicators - routine [DILX](https://elite.bbcelite.com/cassette/main/subroutine/dilx.html), which is called repeatedly by the main dashboard routine at [DIALS](https://elite.bbcelite.com/cassette/main/subroutine/dials_part_1_of_4.html) - and that can lead to some interesting behaviour.

Each bar indicator is 16 pixels long, and the default entry point at DILX can show values from 0-255, with each pixel in the bar representing 16 units (so in the default mode, the last pixel, the 16th, is not used). For comparison, if the routine is called via the entry point at DIL, then the bar's range is 0-16, with each pixel representing 1 unit (and in this case, the 16th pixel can be used).

The dashboard's bar-based indicators are as follows, along with the range of values shown by the bar, plus the range of that particular measurement in the game, if it's different:

| Indicator | Bar range | Range in game | 
|---|---|---|
| Forward and aft shields | 0 to 255 | - | 
| Fuel | 0 to 64 | Fuel is actually 0 to 70 | 
| Cabin temperature | 0 to 255 | - | 
| Laser temperature | 0 to 255 | - | 
| Altitude | 0 to 255 | - | 
| Speed | 0 to 32 | Speed is actually 0 to 40 | 
| Energy banks | 0 to 16 | The first bank is actually 0 to 15 | 

Most of the indicators have internal values of 0-255 and use the standard DILX bar (so, as noted above, they only use pixels 0-15 in the bar, and don't use the last one).

The energy banks are the same, as the maximum value for the ship's energy levels is 255, which is divided into four banks to give a range of 0-15 for the first bank, and a range of 0-16 for the other banks. This means that when the energy banks are fully charged, the top indicator doesn't use the last pixel, while the other energy banks do.

As a result of the above, most of the indicators have a comfortable fit within the dashboard, with an empty pixel at the end of the bar that gives a nice, black gap between the left-hand indicators and the left edge of the scanner. However, the maximum values for fuel and speed don't fit nicely into the space available in their bar-based indicators. Here's why:

- The maximum value for fuel is 70 (for 7.0 light years), so when this routine is called via DILX+2 to show the fuel reserves, the fuel level in A is reduced down to a maximum of 17 (70 >> 2), which is one bigger than the maximum of 16 that each bar can show. You never really notice this as it's only the first 0.6 light years that fall off the end of the bar, and jumps that small aren't that common, but the fuel level does start off using all 16 pixels in its bar, which is one greater than the other indicators in that column (all of which slot into the 0-15 pixel range), so it's clear that this indicator is slightly different.
- The speed indicator is at another level, though. The maximum speed of our ship in Elite is a DELTA value of 40, which reduces down to an indicator value of 20, four greater than the maximum value shown on the bar. The bar simply cuts off any values greater than 16 and doesn't display the four pixels that fall off the end. You can test this in-flight by tapping Space until the speed indicator is just full, and then tapping it again four times (during which your speed will still increase). If you then tap the "?" key to slow down, you have to tap it five times before the speed indicator starts to drop again. I guess there just wasn't room to let this particular control knob go up to 11...

Note that the NES version doesn't have these issues, as it uses fixed patterns to display the bars at the correct size:

![The dashboard in the NES version of Elite](https://elite.bbcelite.com/images/nes/general/dashboard.png) 

						The only other dashboard indicators are the missile indicators, the pitch and roll bars, the compass, the 3D scanner, and the space station and E.C.M. bulbs, all of which have their own individual routines.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_dashboard_indicators.html](https://elite.bbcelite.com/deep_dives/the_dashboard_indicators.html)*
