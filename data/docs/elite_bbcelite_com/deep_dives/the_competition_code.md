---
title: The competition code
source_url: https://elite.bbcelite.com/deep_dives/the_competition_code.html
category: manual
topics:
- basic
- assembly
difficulty: beginner
language: assembly
hardware:
- KERNAL
- SID
- CPU
related:
- sid-registers
- sound-programming
- memory-map
- kernal-routines
- music-player
scraped_at: '2026-07-20'
---

# The competition code

## All the information that's hidden in the Elite competition code

Bundled with Elite, and easy to miss amongst the razzmatazz of the manual, novel, function key strip and control summary card, was the competition entry form. Unfortunately the entry deadline of March 1985 has long since passed, but back in the day, budding players could fill out the postcard in hope of joining the Order of Elite, with the six best players standing a chance of being invited to the "national Elite tournament" in April 1985. Accordingly, piles of postcards poured into Acornsoft's offices and sat in tottering stacks around the office, waiting for some lucky soul to process them all.

My postcard was in there somewhere.

Apart from your name and address, the postcard asked for two things: your credit balance, and the competition code that the game displayed on-screen during the saving process, like this:

![The competition code in the BBC Micro disc version of Elite](https://elite.bbcelite.com/images/disc/competition_code.png) 

						These two bits of information enabled Acornsoft to work out who was a legitimately amazing pilot, and who had cheated, using a decoding algorithm that was a closely guarded secret.

This algorithm can be seen in the BBC BASIC program called UNPACK that's included on the Elite source disc. Some lucky Acornsoft employee presumably had to sit there and enter these two bits of information into UNPACK, which would then tell them whether the cash levels on the postcard were correct, and most importantly, what the player's combat rank was. UNPACK could also tell them whether that person had tampered with their save file, and it also revealed which version of the game this code was from, which could then be cross-checked against the colour of the postcard (blue for the BBC Micro cassette version, brown for the BBC Micro disc version, and green for the Electron version).

And then... onto the next postcard. I bet that was a fun job.

People would have sold their grandmothers to get hold of UNPACK, so let's see how it all works, starting with the competition flags.

## The competition flags

													 ---------------------

						The competition flags in variable [COK](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#cok) track three vital bits of information that get encoded into the final competition code. They are as follows:

- Bit 0 is set in routine ptg if we hold CTRL during hyperspace to force a mis-jump into witchspace (having first paused the game and toggled on the author credits with X). UNPACK does not report the status of this bit, so presumably manually mis-jumping was not regarded as cheating by Acornsoft, but perhaps it was recorded to see if anyone found this way of hunting Thargoids.
- Bit 1 is set if this commander file has ever been saved by the BBC Micro cassette version of Elite. Note that commander files can be loaded into and saved from any BBC Micro or Electron version of the game, so this flag indicates that it was, at some point, saved from the cassette version, and it can be set alongside the other platform bits, if applicable.
- Bit 2 is set if this commander file has ever been saved by the first release of the disc version of BBC Micro Elite. This is the version with the famous refund bug, where trying to buy a laser that you already owned would affect your credit balance; the same version also has a bug where asteroids never spawn. This bit is also set by the 6502 Second Processor version, but this version was launched after the competition expired, so presumably the authors just reused the disc version's save routine code.
- Bit 3 is set if this commander file has ever been saved by the Acorn Electron version of Elite. The same is true of the BBC Master and Apple II versions.
- Bit 4 is not set by any of the 6502 versions of Elite. If it is set in the commander file, the platform is reported as "Something else??" by UNPACK.
- Bit 5 is set if this commander file has ever been saved by the bug-fixed disc version of BBC Micro Elite (where the refund and asteroid bugs have been squashed). Having a different code for the two versions enabled Acornsoft to know whether the player could have taken advantage of the refund bug, though it doesn't prove that the player actually exploited the bug.
- Bit 6 is set if this commander file has ever been saved by the Commodore 64 version of Elite. If this bit is set then the BBC Micro version of UNPACK will report this as "Something else??".
- Bit 7 is set if the [CHK](https://elite.bbcelite.com/cassette/main/variable/chk.html)and[CHK2](https://elite.bbcelite.com/cassette/main/variable/chk2.html)checksums in the commander file do not match, which indicates that the commander data has been tampered with. CHK2 is set to CHK EOR &A9 when the file is saved, so anyone tampering with the file would not only need to update the CHK checksum accordingly, they would also need to update CHK2 as well. The game hangs if you try to load a commander file with an incorrect CHK value, but it lets an incorrect CHK2 through, so the chances are a hacker wouldn't know that CHK2 needed to be correct for a valid competition entry.

Note that the NES version doesn't use the competition flags in this way, though the same variable is still used to keep track of cheats. In this version, COK is set to 1 if you use the built-in cheat mode, but that's all; see the deep dive on [comparing NES Elite with the other versions](https://elite.bbcelite.com/comparing_nes_elite_with_the_other_versions.html) for details.

The competition flag is buried within the competition code that players had to copy onto the competition postcard, so now let's look at the competition code.

## The competition code

													 --------------------

						The competition code is calculated and shown on screen in the [SVE](https://elite.bbcelite.com/cassette/main/subroutine/sve.html) routine when the commander file is saved. It's a four-byte number with a maximum value of 4,294,967,295, which fits nicely into the ten-box slot on the competition postcard.

It is calculated into K(0 1 2 3), which is a big-endian number with the most significant byte in K and the least significant in K+3 (so it's stored in the same way that the player's cash is stored in location CASH, and it's printed out by the same BPRNT routine that displays the credit balance). The calculation is done in this order:

K = CHK OR %10000000 K+2 = K EOR COK K+1 = K+2 EOR CASH+2 K+3 = K+1 EOR &5A EOR TALLY+1

The result is then printed on-screen using BPRNT, and the file is saved.

## Extracting data from the competition code

													 -----------------------------------------

						So to extract the various bits of information encoded in the competition code, we can apply the algorithm in UNPACK, described here using the same variable names as used UNPACK, so you can follow along if you want. The following makes use of the following facts about EOR:

- EOR is commutative:

A EOR B = B EOR A

(A EOR B) EOR C = A EOR (B EOR C)

A EOR A = 0

A EOR 0 = 0 EOR A = A

Given this, let's see how UNPACK extracts the data from the competition code.

- Split the code into the four bytes by AND'ing as follows (UNPACK has to do some division to avoid BBC BASIC overflow errors, but this is effectively what it does):

B1% = code AND &000000FF (i.e. K+3) B2% = code AND &0000FF00 (i.e. K+2) B3% = code AND &00FF0000 (i.e. K+1) B4% = code AND &FF000000 (i.e. K)

```
  B% = B4% EOR B2%
     = K EOR K+2
     = K EOR (K EOR COK)
     = (K EOR K) EOR COK
     = COK
```
							```
  B% = B2% EOR B3%
     = K+2 EOR K+1
     = (K EOR COK) EOR (K+2 EOR CASH+2)
     = (K EOR COK) EOR ((K EOR COK) EOR CASH+2)
     = ((K EOR COK) EOR (K EOR COK)) EOR CASH+2
     = CASH+2
```
							```
  B% = B3% EOR B1% EOR &5A
     = K+1 EOR K+3 EOR &5A
     = (K+2 EOR CASH+2) EOR (K+1 EOR &5A EOR TALLY+1) EOR &5A
     = (K+2 EOR CASH+2) EOR ((K+2 EOR CASH+2) EOR &5A EOR TALLY+1) EOR &5A
     = ((K+2 EOR CASH+2) EOR (K+2 EOR CASH+2)) EOR &5A EOR TALLY+1 EOR &5A
     = &5A EOR TALLY+1 EOR &5A
     = (&5A EOR &5A) EOR TALLY+1
     = TALLY+1
```
						
						So in this way we can extract the competition flags (COK), one byte of the cash amount (CASH+2) and the high byte of the combat rank (TALLY+1). We can check the extracted cash byte against the cash amount entered on the postcard, as follows:

CASH+2 = (cash total from postcard * 10) AND &FF00

and we can work out the combat rank from TALLY+1 using the same algorithm as the [STATUS](https://elite.bbcelite.com/cassette/main/subroutine/status.html) routine:

| Rank | TALLY+1 | 
|---|---|
| Competent | 0 to 2 | 
| Dangerous | 2 to 9 | 
| Deadly | 10 to 24 | 
| Elite | 25 and up | 

and from the value COK we know whether the file has been tampered with, which platforms the game has been played on, and whether the player has done any manual mis-jumps.

That's pretty clever stuff for a few digits on a postcard...

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
K   = CHK OR %10000000

  K+2 = K EOR COK

  K+1 = K+2 EOR CASH+2

  K+3 = K+1 EOR &5A EOR TALLY+1
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`A`** (unknown): No description available

```assembly
A EOR B = B EOR A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
(A EOR B) EOR C = A EOR (B EOR C)
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`A`** (unknown): No description available

```assembly
A EOR A = 0
```

### Snippet Codice (Dialetto: Generic Assembly)

#### Routine Identificate:
- **`A`** (unknown): No description available

```assembly
A EOR 0 = 0 EOR A = A
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
B1% = code AND &000000FF (i.e. K+3)

  B2% = code AND &0000FF00 (i.e. K+2)

  B3% = code AND &00FF0000 (i.e. K+1)

  B4% = code AND &FF000000 (i.e. K)
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
B% = B4% EOR B2%
     = K EOR K+2
     = K EOR (K EOR COK)
     = (K EOR K) EOR COK
     = COK
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
B% = B2% EOR B3%
     = K+2 EOR K+1
     = (K EOR COK) EOR (K+2 EOR CASH+2)
     = (K EOR COK) EOR ((K EOR COK) EOR CASH+2)
     = ((K EOR COK) EOR (K EOR COK)) EOR CASH+2
     = CASH+2
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
B% = B3% EOR B1% EOR &5A
     = K+1 EOR K+3 EOR &5A
     = (K+2 EOR CASH+2) EOR (K+1 EOR &5A EOR TALLY+1) EOR &5A
     = (K+2 EOR CASH+2) EOR ((K+2 EOR CASH+2) EOR &5A EOR TALLY+1) EOR &5A
     = ((K+2 EOR CASH+2) EOR (K+2 EOR CASH+2)) EOR &5A EOR TALLY+1 EOR &5A
     = &5A EOR TALLY+1 EOR &5A
     = (&5A EOR &5A) EOR TALLY+1
     = TALLY+1
```

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
CASH+2 = (cash total from postcard * 10) AND &FF00
```



---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_competition_code.html](https://elite.bbcelite.com/deep_dives/the_competition_code.html)*
