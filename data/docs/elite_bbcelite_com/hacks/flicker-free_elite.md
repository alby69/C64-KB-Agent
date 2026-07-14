---
title: About flicker-free Elite
source_url: https://elite.bbcelite.com/hacks/flicker-free_elite.html
category: reference
topics:
- assembly
difficulty: beginner
language: assembly
hardware:
- CPU
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-14'
---

# About flicker-free Elite

## Improved ship drawing on the BBC Micro, Electron, Commodore and Apple

The Apple II and BBC Master versions of Elite include an improved ship-drawing algorithm that noticeably reduces flicker compared to earlier versions of the game. Unfortunately this improvement never made it back to the original BBC Micro and Commodore 64 versions... until now.

Here's a comparison of Elite-A, with the standard version on the left, and the flicker-free version on the right:

And here's a comparison on the Commodore 64, this time with the flicker-free version on the left, and the standard version on the right:

In the original Apple II and BBC Master versions, planets still flicker, as that's a different part of the code. To fix this, I've written a brand new routine to reduce flicker in the planets as well. This does require a fair amount of memory, so it isn't available the BBC Micro cassette version or Elite-A, but for players of the BBC Micro disc version, BBC Master, 6502 Second Processor, Acorn Electron, Commodore 64, Commodore Plus/4 and Apple II, you can enjoy both flicker-free ships *and* planets. See the [technical information](https://elite.bbcelite.com/flicker-free_elite_technical_information.html) for details.

Here's the flicker-free BBC Master version, showing a rock-steady planet:

Here's another clip from the Commodore 64, showing a flicker-free space station:

And it might only have simple circles for planets, but even the Apple II version looks better without the flicker:

See the [downloads page](https://elite.bbcelite.com/flicker-free_elite_downloads.html) to get hold of a copy of flicker-free Elite, or check out the [technical information](https://elite.bbcelite.com/flicker-free_elite_technical_information.html) for details of how it works.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/flicker-free_elite.html](https://elite.bbcelite.com/hacks/flicker-free_elite.html)*
