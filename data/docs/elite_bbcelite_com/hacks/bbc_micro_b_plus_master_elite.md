---
title: About BBC Master Elite on the BBC Micro B+
source_url: https://elite.bbcelite.com/hacks/bbc_micro_b_plus_master_elite.html
category: manual
topics:
- basic
- assembly
- input handling
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- SID
- CPU
- CIA
related:
- sid-registers
- sound-programming
- joystick-reading
- keyboard-handling
- kernal-routines
- memory-map
- music-player
- cia-registers
scraped_at: '2026-07-20'
---

# About BBC Master Elite on the BBC Micro B+

## Giving the BBC Micro B+ the full colour version of Elite that it deserves

![My signed BBC Micro B+ playing BBC Master Elite](https://elite.bbcelite.com/images/bbc_b_plus/bbc_micro_b_plus_master_elite.jpg) 

						The BBC Micro B+ is perhaps the most overlooked Acorn machine of all. Launched in mid-1985, more than three years after the original BBC Micro's late-1981 debut, the B+ was an attempt to address the main criticism of the original Beeb: the low 32K memory count. But the B+ didn't win people over, partly because the machine was expensive for what it was, but mainly because the excellent BBC Master came along at the start of 1986 and did things properly, leaving the B+ as a textbook example of too little, too late.

This is a shame, as the B+ is a sweet little machine. Outwardly it looks exactly like the BBC Micro; the only clue that it's different is a diminutive "64K" next to the BBC owl logo on the clear function key strip holder. But inside, the motherboard has been completely redesigned, with the sideways ROMs easily accessible and not tucked away under the keyboard, and not only can it handle 32K ROMs as well as the original 16K of the Model B, but it comes with an extra 32K of RAM, with 20K allocated to shadow RAM (for storing the screen) and the spare 12K allocated to so-called "private RAM".

Applications like word processors and languages like BASIC can instantly make use of the shadow RAM, but it comes with limitations that prevent it being useful for games. And the extra 12K is even more bizarre and has limited practical use; see the [technical information](https://elite.bbcelite.com/bbc_micro_b_plus_master_elite_technical_information.html) page for more details. The upshot is that there's no software for the B+ that makes use of all of this extra RAM; all those enhanced BBC Master games that exploit that computer's more flexible shadow RAM system simply won't work on the B+.

In terms of Elite, the B+ can run all of the BBC Micro versions of Elite (cassette, disc and 6502 Second Processor), but they are exactly the same as the originals: there are no extra features for the B+. Even the unofficial sideways RAM version of Elite won't run on the unexpanded B+, as the B+ does not come with sideways RAM built-in (though you can add it).

The even rarer B+128 is a B+ with an extra 64K of sideways RAM fitted by default, so it can at least run sideways RAM Elite, but almost nothing out there appears to use all of the B+'s extra 32K of shadow/private RAM; the only example I've been able to find is the modern [Ozmoo](https://zornslemma.github.io/ozmoo.html) project, where private RAM is used to implement hardware scrolling. It's all a bit sad, really, and I too just glossed over the B+ as little more than an intriguing footnote in Acorn's line-up.

But then, while browsing eBay, I saw a listing for a BBC Micro, signed by none other than David Braben, co-author of Elite:

![David Braben's signature on a BBC Micro B+](https://elite.bbcelite.com/images/bbc_b_plus/signature.jpg) 

						The listing only talked about it being a BBC Micro, but one of the pictures showed a startup banner of "Acorn OS 64K", which I knew made this a B+:

![David Braben's signature on a BBC Micro B+](https://elite.bbcelite.com/images/bbc_b_plus/startup.jpg) 

						That was enough for me to put in a speculative bid, as I already own a BBC Micro, but I didn't own a B+, so there were two good reasons to make this an attractive collector's item.

And as the only bidder, I won!

As expected, the B+ needed a really good clean and some of the keys were dead, but I gave it a proper service and a big hug and it's now working beautifully. Here it is in all its polished glory:

![My cleaned-up signed BBC Micro B+](https://elite.bbcelite.com/images/bbc_b_plus/cleaned.jpg) 

						And here's the icing on the cake, carefully revealed from under all that accumulated space dust:

![The signature on my cleaned-up signed BBC Micro B+](https://elite.bbcelite.com/images/bbc_b_plus/signature_cleaned.jpg) 

						In return for a bit of affection, my new B+ inspired me. I realised that the best tribute to both the signature and the signature-bearer would be to create a souped-up version of Elite that would take advantage of the whole extra 32K - both the 20K of shadow RAM and the 12K of private RAM. A quick calculation shows that the size of the BBC Master Elite binary is pretty similar to the size of the B+ memory map, so I decided to go the whole hog and try porting BBC Master Elite to the B+.

This hack is the result. It works perfectly, and despite the extra colours and features, it still runs at the same speed as BBC Master Elite. I even found room for all the extra features from the [Elite Compendium](https://elite.bbcelite.com/elite_compendium.html):

- Flicker-free ships and planets
- Trumbles mission
- Red enemy lasers
- Docking improvements
- Fuel scoop improvements
- Joystick improvements
- Delta 14B joystick support
- Fixed: file deletion bug, data on system bug, Moray bug
- Title and docking music (B+128 only)

The title and docking music require sideways RAM, which doesn't come as standard on the B+, so I have released two versions of this hack: one for the standard B+ that doesn't have any music, and one for the B+128 that does. The latter also works on the B+ with 16K of sideways RAM.

So, finally, B+ owners have their own unique version of Elite that uses every single bit of the memory map. Nobody puts B+ in the corner...

Find out how to [download the BBC Micro B+ version of Master Elite](https://elite.bbcelite.com/bbc_micro_b_plus_master_elite_downloads.html), or dive into the [technical information](https://elite.bbcelite.com/bbc_micro_b_plus_master_elite_technical_information.html) to discover exactly how the extra memory in the B+ works, and how we can squeeze a fully featured, full-colour version of Elite into this unique addition to the BBC family.

---
*Fonte originale: [https://elite.bbcelite.com/hacks/bbc_micro_b_plus_master_elite.html](https://elite.bbcelite.com/hacks/bbc_micro_b_plus_master_elite.html)*
