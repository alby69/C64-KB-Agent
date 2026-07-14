---
title: Wersiboard Music 64
source_url: https://codebase.c64.org/doku.php?id=base%3Awersiboard_music_64
category: reference
topics: []
difficulty: intermediate
language: none
hardware:
- SID
- KERNAL
- CIA
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

# Wersiboard Music 64

base:wersiboard_music_64

                # Wersiboard Music 64

This is a claviature for the C64, connected through the cartridge port. It is mapped to $df00-$df06, and every key corresponds to one bit each in those seven bytes respectively, except for $df06, where only bit 0 is used. This is because the keyboard consists of (6*8)+1 keys, and therefore 6 bytes is not enough to cover all of the keys. A bit weird, but that is how we like it.

![](https://codebase.c64.org/lib/exe/fetch.php?media=base:wersiboard64_01.gif)


Picture borrowed from [here](http://www.richard-aicher.de/html/wersiboard64.html).

base/wersiboard_music_64.txt · Last modified:  by 127.0.0.1

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Awersiboard_music_64](https://codebase.c64.org/doku.php?id=base%3Awersiboard_music_64)*
