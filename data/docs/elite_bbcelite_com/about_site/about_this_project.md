---
title: About this project
source_url: https://elite.bbcelite.com/about_site/about_this_project.html
category: source-code
topics:
- basic
- assembly
difficulty: beginner
language: mixed
hardware:
- CIA
- SID
- CPU
- KERNAL
- BASIC ROM
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

# About this project

It's no exaggeration to say that I've been dreaming about this project for decades - since 1984, in fact, when the seminal space game Elite was first released on the BBC Micro. From the moment I first strapped myself into a Cobra Mk III and sat there open-mouthed as the planet Lave shot into view at the end of the launch tunnel, I knew it was love at first sight.

![The launch view of Lave in the BBC Micro cassette version of Elitee](https://elite.bbcelite.com/images/ellipses/lave.png) 

						Sure, I spent the next few days crashing into space stations and watching my ship disappear in clouds of stardust, while pirates swooped in to steal my precious cargo from amongst the ashes... but I was hooked.

I was also utterly intrigued. I knew a bit of assembly language and spent most of my spare time programming my trusty BBC Micro for fun, but Elite was so far beyond my rookie coding skills that it might as well have been real rocket science. I knew I just had to know how this thing of beauty worked, but I also knew it was far too advanced for me. But a kid can dream, so that's what I did for the next 35 years, until a global pandemic and a lucky break meant that as a still-dreaming adult, I could finally begin to peel back the curtains on the inner workings of Elite (more of which below).

This project, then, is a decades-old dream of mine. The fully documented Elite source code on this site is based on the original source files for the game, which can be found on [Ian Bell's personal website](http://www.elitehomepage.org/). The code itself is totally unchanged from the original source, apart from being reformatted to be easier to read. I've left all the original label names and file structures intact, as this site is all about software archaeology and appreciating the authors' original handiwork. This is important to me; I feel like I'm following in the footsteps of greatness here, and keeping the original handiwork intact is all part of the curation of this masterpiece.

Here's a bit more on how this project came to be.

## Ian Bell's original sources

						                             ---------------------------

						When I first saw that the sources to Elite had been released on Ian Bell's website, I couldn't believe it. It was like stumbling across the Holy Grail - I had to pinch myself when I saw someone link to them in an otherwise unremarkable thread on an otherwise unremarkable forum. "What, *the* original sources?" I thought as a clicked on the link and downloaded the text file version of the cassette source.

I excitedly opened [one of the source files](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette/blob/main/1-source-files/original-sources/%24.ELITEG.txt) at random... and was greeted by page after page of this kind of thing:

9300.LL145 \CLIP 9305LDA#0:STASWAP 9310LDAXX15+5:.LL147 LDX#Y*2-1:ORAXX12+1:BNELL107:CPXXX12 9315BCCLL107:LDX#0:.LL107 STXXX13:LDAXX15+1:ORAXX15+3:BNELL83 9320LDA#Y*2-1:CMPXX15+2:BCCLL83 9325LDAXX13:BNELL108:.LL146 LDAXX15+2 9330STAXX15+1:LDAXX15+4:STAXX15+2:LDAXX12:STAXX15+3:CLC:RTS 9335.LL109 SEC:RTS:.LL108 LSRXX13:.LL83 9340LDAXX13:BPLLL115 9345LDAXX15+1:ANDXX15+5:BMILL109:LDAXX15+3:ANDXX12+1:BMILL109 9350LDXXX15+1:DEX:TXA:LDXXX15+5:DEX:STXXX12+2:ORAXX12+2 9355BPLLL109:LDAXX15+2:CMP#Y*2:LDAXX15+3:SBC#0:STAXX12+2 9360LDAXX12:CMP#Y*2:LDAXX12+1:SBC#0:ORAXX12+2:BPLLL109 9365.LL115 TYA:PHA:LDAXX15+4:SEC:SBCXX15:STAXX12+2:LDAXX15+5 9370SBCXX15+1:STAXX12+3:LDAXX12:SEC:SBCXX15+2:STAXX12+4 9375LDAXX12+1:SBCXX15+3:STAXX12+5:EORXX12+3:STAS

I suppose I should have expected it, but the original source files are *incredibly* terse. Because the game was compiled on a BBC Micro using BBC BASIC's built-in assembler, the source code had to be squashed into a number of extremely cramped BASIC files, with all the spaces removed and almost no comments to speak of. The source files are not particularly human-friendly; they aren't supposed to be.

Not only that, but parts of the game started life on an Acorn Atom, where labels in assembly language are restricted to two letters plus digits, so the source is full of memorable names like XX16, QQ17 and LL9. I mean, look at this bit:

8501.LL42 \DO nodeX-Ycoords 8506\TrnspMat:LDYXX16+2:LDXXX16+3:LDAXX16+6:STAXX16+2: LDAXX16+7:STAXX16+3:STYXX16+6:STXXX16+7 8508LDYXX16+4:LDXXX16+5:LDAXX16+12:STAXX16+4:LDAXX16+13 8509STAXX16+5:STYXX16+12:STXXX16+13 8510LDYXX16+10:LDXXX16+11:LDAXX16+14:STAXX16+10:LDAXX16+15 8511STAXX16+11:STYXX16+14:STXXX16+15

All those XXXs are enough to make your eyes boggle, but at least this excerpt has some comments, so do they help? "TrnspMat" - is that "transponder materials"? Or "transport maths"? I guess it's something to do with "DO nodeX-Ycoords", which clearly involves nodes and coordinates, but it's not exactly readable. (I now know that this is part of the LL42 routine that transposes the rotation matrix, but knowing that doesn't make it any easier to follow; it possibly makes it even scarier.)

This terseness is not remotely surprising given the space constraints of compiling code on a 32K micro, but I was still flummoxed. The fact that any kind of source code had been released at all was a kind of Holy Grail experience for me, but it ended up generating more questions than answers.

So I put it to one side and figured I'd probably never understand how this game worked.

## Paul Brink's annotated disc disassembly

						                             ---------------------------------------

						The next breakthrough was when I stumbled across the commentary by Paul Brink, whose annotated disassembly of the disc version of BBC Elite appeared on Ian Bell's site in 2014, covering both the [docked code](http://www.elitehomepage.org/archive/a/d4090010.txt) and the [flight code](http://www.elitehomepage.org/archive/a/d4090012.txt). This was a *big* improvement over the original source files, and like many others, I eagerly grabbed them and settled down with a cup of tea for some interesting reading.

Unfortunately, I still couldn't really work out what was going on; it was like stumbling across a trail of breadcrumbs in the forest, but after heavy monsoonal rain. Every now and then something would seem to make some vague kind of sense, but then I'd come across this kind of thing:

\XX16 got INWK 9..21..26 up at LL15. The ROTMAT has 18 bytes, for 3x3 matrix \XX16_lsb[ 0 2 4 highest XX16 done below is 5, then X taken up by 6, \ 6 8 10 Y taken up by 2. \ 12 14 16=0 ?]

This refers to the same code as above, and is one of the more verbose explanations in the commentary. It's definitely a step up from "DO nodeX-Ycoords" and "TrnspMat", but what are XX16 and INWK? And ROTMAT - that's a rotation matrix, right? OK, so there *are* matrices in there somewhere, which is no surprise given the 3D nature of the game. But it's still really hard to work out what's going on, and the code that this comment explains doesn't really make things any clearer than before:

```
      .LL42  \ ->  &4B04 \ DO nodeX-Ycoords their comment  \  TrnspMat 
  A4 0B                  LDY &0B     \ XX16+2          \ Transpose Matrix
  A6 0C                  LDX &0C     \ XX16+3
  A5 0F                  LDA &0F     \ XX16+6
  85 0B                  STA &0B     \ XX16+2
  A5 10                  LDA &10     \ XX16+7
```
						We're still left with XX16+2 and its friends, so this is essentially the source code, laid out differently, with cryptic hints scattered throughout, hints that seem to be aimed at someone who already understands the basics... which I certainly didn't as I sat there, just as confused as ever.

By this time my tea had gone cold, so once again I put my dreams on hold and forgot about trying to unlock the secrets of Elite.

## Kieran Connell's elite-beebasm

						                             ------------------------------

						In 2020, lockdown boredom led me to stumble across a [2018 post on the Stardot forums](https://stardot.org.uk/forums/viewtopic.php?t=15375) by Kieran Connell of the [Bitshifters Collective](https://bitshifters.github.io/). These guys do some incredibly clever things with BBC computers, and that's exactly what Kieran had done - he'd created [elite-beebasm](https://github.com/kieranhj/elite-beebasm), a port of the original BBC Elite source code from the super-terse BASIC files into the [BeebAsm assembler](https://github.com/stardot/beebasm).

Not only had he managed to drag the source code into some kind of human-compatible shape, but he'd also managed to pull apart the encryption process that hides Elite's code from prying eyes. He'd then created an equivalent system in Python, enabling modern computers to build an exact replica of the released version of Elite from the original source. This meant I could not only build a local version of Elite, but I could tweak the code to help work out what it did, which I figured would be a really useful way of working out how Elite weaves its magic.

That said, the source code still looked worryingly familiar:

```
  .LL42
  \DO nodeX-Ycoords
  \TrnspMat
    LDY XX16+2
    LDX XX16+3
    LDA XX16+6
    STA XX16+2
    LDA XX16+7
    STA XX16+3
    STY XX16+6
    STX XX16+7
```
						But at least I now had a buildable codebase I could work with, and that was real progress.

## A fully documented version

						                             --------------------------

						Kieran's version gave me the leg-up that I needed to crack the problem. I started by running a [script by Martin Ling](https://github.com/martinling/elite-beebasm/commits/apply-brink-commentary) that copied some of Paul Brink's comments into Kieran's version, hoping that this would give me some clues to analysing the code. The results needed a fair amount of massaging to get the right comments in the right place (as Paul documented the disc version while Kieran used the cassette version), but going through and matching Paul's comments with Kieran's code was very instructive, and some small, early glimmers of understanding gave me enough confidence to start poking my way through the bits of the game that had always fascinated me.

I started with the [text token system](https://elite.bbcelite.com/deep_dives/printing_text_tokens.html), then worked out the [split-screen mode](https://elite.bbcelite.com/deep_dives/the_split-screen_mode.html), and then moved on to the [universe generation](https://elite.bbcelite.com/deep_dives/galaxy_and_system_seeds.html)... and by then I was completely hooked. Every little step forward, I felt like I was unpicking a bit more of the story of two young developers creating a modern-day masterpiece; if you squint carefully, you can almost sense where the whole starts to become greater than the sum of the parts. Elite is the coding equivalent of *A Day in the Life*, a mash-up between the Acorn world's very own Lennon and McCartney, with results that are just as seminal in their field. They say you should never meet your heroes, but grokking their source code... well, that's another matter altogether.

This site and its accompanying repositories are the result. The aim is that anyone with a basic knowledge of 6502 assembly language and simple trigonometry will be able to read through the source code and not only understand what's going on, but will also be able appreciate the beauty and elegance of this exceptional piece of 1980s programming.

For comparison, this is what the [LL145 code block above now looks like](https://elite.bbcelite.com/cassette/main/subroutine/ll145_part_1_of_4.html), and this is the [fully annotated LL42 rotation matrix code](https://elite.bbcelite.com/cassette/main/subroutine/ll9_part_6_of_12.html). I think it's a bit easier to understand now.

It has been a privilege to unravel the intricacies of Elite. I hope you enjoy the ride.

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
9300.LL145 \CLIP
  9305LDA#0:STASWAP
  9310LDAXX15+5:.LL147 LDX#Y*2-1:ORAXX12+1:BNELL107:CPXXX12
  9315BCCLL107:LDX#0:.LL107 STXXX13:LDAXX15+1:ORAXX15+3:BNELL83
  9320LDA#Y*2-1:CMPXX15+2:BCCLL83
  9325LDAXX13:BNELL108:.LL146 LDAXX15+2
  9330STAXX15+1:LDAXX15+4:STAXX15+2:LDAXX12:STAXX15+3:CLC:RTS
  9335.LL109 SEC:RTS:.LL108 LSRXX13:.LL83
  9340LDAXX13:BPLLL115
  9345LDAXX15+1:ANDXX15+5:BMILL109:LDAXX15+3:ANDXX12+1:BMILL109
  9350LDXXX15+1:DEX:TXA:LDXXX15+5:DEX:STXXX12+2:ORAXX12+2
  9355BPLLL109:LDAXX15+2:CMP#Y*2:LDAXX15+3:SBC#0:STAXX12+2
  9360LDAXX12:CMP#Y*2:LDAXX12+1:SBC#0:ORAXX12+2:BPLLL109
  9365.LL115 TYA:PHA:LDAXX15+4:SEC:SBCXX15:STAXX12+2:LDAXX15+5
  9370SBCXX15+1:STAXX12+3:LDAXX12:SEC:SBCXX15+2:STAXX12+4
  9375LDAXX12+1:SBCXX15+3:STAXX12+5:EORXX12+3:STAS
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
8501.LL42 \DO nodeX-Ycoords
  8506\TrnspMat:LDYXX16+2:LDXXX16+3:LDAXX16+6:STAXX16+2:
  LDAXX16+7:STAXX16+3:STYXX16+6:STXXX16+7
  8508LDYXX16+4:LDXXX16+5:LDAXX16+12:STAXX16+4:LDAXX16+13
  8509STAXX16+5:STYXX16+12:STXXX16+13
  8510LDYXX16+10:LDXXX16+11:LDAXX16+14:STAXX16+10:LDAXX16+15
  8511STAXX16+11:STYXX16+14:STXXX16+15
```

### Snippet Codice (BASIC)

```basic
\XX16 got INWK 9..21..26 up at LL15. The ROTMAT has 18 bytes, for 3x3 matrix
  \XX16_lsb[   0  2  4     highest XX16 done below is 5, then X taken up by 6,
  \            6  8 10                                        Y taken up by 2.
  \       12 14 16=0 ?]
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.LL42  \ ->  &4B04 \ DO nodeX-Ycoords their comment  \  TrnspMat 
  A4 0B                  LDY &0B     \ XX16+2          \ Transpose Matrix
  A6 0C                  LDX &0C     \ XX16+3
  A5 0F                  LDA &0F     \ XX16+6
  85 0B                  STA &0B     \ XX16+2
  A5 10                  LDA &10     \ XX16+7
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
.LL42
  \DO nodeX-Ycoords
  \TrnspMat
    LDY XX16+2
    LDX XX16+3
    LDA XX16+6
    STA XX16+2
    LDA XX16+7
    STA XX16+3
    STY XX16+6
    STX XX16+7
```



---
*Fonte originale: [https://elite.bbcelite.com/about_site/about_this_project.html](https://elite.bbcelite.com/about_site/about_this_project.html)*
