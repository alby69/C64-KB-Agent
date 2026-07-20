---
title: Technical information for BBC Micro disc Elite on the BBC Master
source_url: https://elite.bbcelite.com/hacks/bbc_master_disc_elite_technical_information.html
category: source-code
topics:
- basic
- graphics
difficulty: intermediate
language: basic
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Technical information for BBC Micro disc Elite on the BBC Master

## Details of how disc Elite was converted from the BBC Micro to the BBC Master

![BBC Micro disc Elite breaking on a BBC Master](https://elite.bbcelite.com/images/bbc_master_disc_elite/broken.png) 

						The main problem when running the BBC Micro version on the BBC Master is that all the on-screen text is corrupted (see the screenshot above). This is because the text-printing routine in [TT26](https://elite.bbcelite.com/disc/flight/subroutine/tt26.html) prints text on-screen by poking the individual pixels of characters directly into screen memory, and it fetches the pixel shapes of these characters from the definitions in the BBC Micro MOS (Machine Operating System) ROM at address &C000.

In the BBC Master, however, these character definitions are not only at a different address in the MOS, but the MOS ROM is not paged into accessible memory when TT26 is called. This means that when the text-printing routine from the original Elite tries to fetch the character shapes, it grabs whatever happens to be in location &C000 at the time and displays that instead, resulting in the mess you see above. &C000 actually contains a copy of the disc catalogue from sectors 0 and 1, as this is the address of the HAZEL file system workspace, so what you're seeing is the result of poking the disc catalogue text directly into screen memory as pixels.

To fix this, all it takes is a small change to the text-printing routine to fetch the character definitions from address &8900 rather than &C000. We also need to add some ROM-switching code to ensure that the MOS ROM is switched into memory before we copy out the character data, which we can do pretty easily by setting bit 7 of ROMSEL at SHEILA &30 (and in the RAM copy at &F4), accessing the character definitions from the MOS, and clearing bit 7 of ROMSEL and &F4 when we're done.

![BBC Micro disc Elite working on a BBC Master](https://elite.bbcelite.com/images/bbc_master_disc_elite/fixed.png) 

						If you want to see the code changes that implement the fix, then they're all in the GitHub repository for the BBC Micro disc version. You'll need to switch to the [bbc-master branch](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/tree/bbc-master), and you can then search the [elite-source-docked.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/blob/bbc-master/1-source-files/main-sources/elite-source-docked.asm) and [elite-source-flight.asm](https://github.com/markmoxon/elite-source-code-bbc-micro-disc/blob/bbc-master/1-source-files/main-sources/elite-source-flight.asm) files for "Mod:". This will reveal all of the changes required to make the original version work on the BBC Master; there aren't many.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/bbc_master_disc_elite_technical_information.html](https://elite.bbcelite.com/hacks/bbc_master_disc_elite_technical_information.html)*
