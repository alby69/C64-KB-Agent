---
title: Elite over Econet
source_url: https://elite.bbcelite.com/hacks/elite_over_econet.html
category: reference
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- CPU
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

# Elite over Econet

## Econet support and scoreboards for the BBC Micro, Electron and Archimedes

For those of us who grew up in 1980s Britain, the BBC Micro was synonymous with education. Some schools only had one shared computer that would be wheeled out on a trolley along with the school TV, but there were other, luckier schools that had entire networks of Beebs, connected together by Acorn's proprietary networking technology, Econet.

Econet let entire classrooms load software from a fileserver, while sharing printers, disc drives and other expensive pieces of equipment. You could load the likes of [Granny's Garden](https://en.wikipedia.org/wiki/Granny%27s_Garden) and [L - A Mathemagical Adventure](https://en.wikipedia.org/wiki/L_%E2%80%93_A_Mathemagical_Adventure) over Econet, but disappointingly for an entire generation of school kids, you couldn't load Elite, no matter how hard you tried. It just wouldn't work.

Fast-forward to the modern era, and Econet is still going strong, albeit in the realm of hobbyists and computer museums. The UK's [National Museum of Computing](https://www.tnmoc.org) has a lovingly crafted 1980s classroom with an entire room full of Econet-connected Acorn machines, and it is a thing of rare beauty:

![The classroom at the National Museum of Computing](https://elite.bbcelite.com/images/elite_over_econet/tnmoc.jpg) 

						I have my own rather more modest network at home, connecting together my Archimedes A410/1, BBC Master, BBC Micro and Acorn Electron, and I just had to get Elite loading over it. The challenge is mainly one of memory; like the disc filing system, Econet steals a chunk of memory for its own use, which isn't normally too much of a problem, but when you're talking about a game that famously uses [almost every single available byte](https://elite.bbcelite.com/deep_dives/the_elite_memory_map.html), Econet is the straw that breaks the camel's back.

Luckily both the BBC Master and the 6502 Second Processor have plenty of spare memory even when running Elite, and so do the BBC Micro and Acorn Electron once they've been expanded with 16K of sideways RAM, so all it takes to get Elite working over Econet is to restructure the game so it no longer uses the memory that Econet needs. I say "all" as if it's an easy thing - there's [a bit more to it](https://elite.bbcelite.com/elite_over_econet_technical_information.html), of course - but the result is a version of Elite that loads and runs over Econet, and which you can [download and install](https://elite.bbcelite.com/elite_over_econet_installing.html) on your own network so your users can [play Elite over Econet](https://elite.bbcelite.com/elite_over_econet_downloads.html). And if your BBC Micro doesn't have sideways RAM at all, then there's a cut-down version that drops a couple of minor features to make it fit, so you can still join in the fun.

Not only that, but I've also added support for a [multiplayer scoreboard](https://elite.bbcelite.com/elite_over_econet_scoreboard.html) that can show live scores from everyone playing Elite on the network. And I've crafted an application for RISC OS that lets Archimedes Elite players send their scores to the scoreboard too; ArcElite already loads over Econet, so all you need to do is [run the application](https://elite.bbcelite.com/elite_over_econet_acorn_archimedes.html), fill in a few details and off you go.

So, finally, after all these years, we can all sit down at our networked Acorns and play competitive Elite. Teachers, you might like to look away now.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_over_econet.html](https://elite.bbcelite.com/hacks/elite_over_econet.html)*
