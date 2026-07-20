---
title: Commander save files
source_url: https://elite.bbcelite.com/deep_dives/commander_save_files.html
category: manual
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
related:
- memory-map
- kernal-routines
scraped_at: '2026-07-20'
---

# Commander save files

## A description of each and every byte in the saved commander file

Elite maintains two separate copies of your commander's status in memory. The current commander data block in the [T% workspace](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html) gets updated every time you do something in game, so when you finally destroy that pesky pirate that's been hounding you for ages, your combat rating in [TALLY](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#tally) gets increased, and your bounty gets paid into your cash pot in [CASH](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#cash). If you die, however, you lose all this progress, which is why you should save your game regularly. Saving your game not only writes to cassette or disc, but it also copies all the commander data to [the last saved commander data block at NA%](https://elite.bbcelite.com/cassette/main/variable/na_per_cent.html), so if you die, the game can reload the commander data from this point.

![The disc access menu in BBC Micro disc Elite](https://elite.bbcelite.com/images/disc/disk_access_menu.png) 

						To save a commander file, Elite simply saves the block of memory between NA%+8 and CHK (the first 8 bytes of NA% contain the commander name and a carriage return, which isn't saved as part of the file, but is used as the filename). Before doing the save, it calculates two checksums and puts them in CHK and CHK2, to make it harder to for crackers to manipulate commander files manually, and then it just saves out that clock of memory. In the Commodore 64 and Apple II versions, it also calculates a third checksum and puts it into CHK3. Let's take a look at the format of this saved file.

## The save file format

													 --------------------

						Each commander file is exactly 256 bytes long, though only the first 75 (&4B) bytes contain any data (the rest are zeroed out). Those 75 bytes are shown in the table below, along with links to the relevant variables in the current commander data block, and the corresponding value in the default JAMESON commander from when you start a brand new game.

Note that the NES version of Elite has a slightly different file structure to the following and encrypts its save files differently; see the [NA2%](https://elite.bbcelite.com/nes/bank_6/variable/na2_per_cent.html) variable for the file structure, and the [SaveLoadCommander](https://elite.bbcelite.com/nes/bank_6/subroutine/saveloadcommander.html) routine for the encryption.

| Byte # | In hex | Variable | Description | Default | 
|---|---|---|---|---|
| #1 | &01 | [QQ0](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq0) | Current system X-coordinate (Lave) | 20 | 
| #2 | &02 | [QQ1](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq1) | Current system Y-coordinate (Lave) | 173 | 
| #3-4 | &03-&04 | [QQ21](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq21) | Seed s0 for system 0, galaxy 0 (Tibedied) | &5A4A | 
| #5-6 | &05-&06 | [QQ21+2](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq21) | Seed s1 for system 0, galaxy 0 (Tibedied) | &0248 | 
| #7-8 | &07-&08 | [QQ21+4](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq21) | Seed s2 for system 0, galaxy 0 (Tibedied) | &B753 | 
| #9-12 | &09-&0C | [CASH](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#cash) | Amount of cash (100 Cr) | &E8030000 | 
| #13 | &0D | [QQ14](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq14) | Fuel level | 70 | 
| #14 | &0E | [COK](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#cok) | Competition flags | 0 | 
| #15 | &0F | [GCNT](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#gcnt) | Galaxy number, 0-7 | 0 | 
| #16 | &10 | [LASER](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#laser) | Front laser | POW | 
| #17 | &11 | [LASER+1](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#laser) | Rear laser | 0 | 
| #18 | &12 | [LASER+2](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#laser) | Left laser | 0 | 
| #19 | &13 | [LASER+3](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#laser) | Right laser | 0 | 
| #20-21 | &14-&15 | These two bytes are unused (they were originally used for up/down lasers, but they were dropped) | 0 | |
| #22 | &16 | [CRGO](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#crgo) | Cargo capacity | 22 | 
| #23 | &17 | [QQ20+0](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Food in cargo hold | 0 | 
| #24 | &18 | [QQ20+1](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Textiles in cargo hold | 0 | 
| #25 | &19 | [QQ20+2](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Radioactives in cargo hold | 0 | 
| #26 | &1A | [QQ20+3](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Slaves in cargo hold | 0 | 
| #27 | &1B | [QQ20+4](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Liquor/Wines in cargo hold | 0 | 
| #28 | &1C | [QQ20+5](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Luxuries in cargo hold | 0 | 
| #29 | &1D | [QQ20+6](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Narcotics in cargo hold | 0 | 
| #30 | &1E | [QQ20+7](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Computers in cargo hold | 0 | 
| #31 | &1F | [QQ20+8](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Machinery in cargo hold | 0 | 
| #32 | &20 | [QQ20+9](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Alloys in cargo hold | 0 | 
| #33 | &21 | [QQ20+10](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Firearms in cargo hold | 0 | 
| #34 | &22 | [QQ20+11](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Furs in cargo hold | 0 | 
| #35 | &23 | [QQ20+12](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Minerals in cargo hold | 0 | 
| #36 | &24 | [QQ20+13](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Gold in cargo hold | 0 | 
| #37 | &25 | [QQ20+14](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Platinum in cargo hold | 0 | 
| #38 | &26 | [QQ20+15](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Gem-Stones in cargo hold | 0 | 
| #39 | &27 | [QQ20+16](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq20) | Amount of Alien Items in cargo hold | 0 | 
| #40 | &28 | [ECM](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#ecm) | E.C.M. | 0 | 
| #41 | &29 | [BST](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#bst) | Fuel scoops ("barrel status") | 0 | 
| #42 | &2A | [BOMB](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#bomb) | Energy bomb | 0 | 
| #43 | &2B | [ENGY](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#engy) | Energy/shield level | 0 | 
| #44 | &2C | [DKCMP](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#dkcmp) | Docking computer | 0 | 
| #45 | &2D | [GHYP](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#ghyp) | Galactic hyperdrive | 0 | 
| #46 | &2E | [ESCP](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#escp) | Escape pod | 0 | 
| #47-50 | &2F-&32 | These four bytes are unused | 0 | |
| #51 | &33 | [NOMSL](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#nomsl) | Number of missiles | 3 | 
| #52 | &34 | [FIST](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#fist) | Legal status ("fugitive/innocent status") | 0 | 
| #53 | &35 | [AVL+0](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Food | 16 | 
| #54 | &36 | [AVL+1](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Textiles | 15 | 
| #55 | &37 | [AVL+2](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Radioactives | 17 | 
| #56 | &38 | [AVL+3](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Slaves | 0 | 
| #57 | &39 | [AVL+4](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Liquor/Wines | 3 | 
| #58 | &3A | [AVL+5](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Luxuries | 28 | 
| #59 | &3B | [AVL+6](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Narcotics | 14 | 
| #60 | &3C | [AVL+7](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Computers | 0 | 
| #61 | &3D | [AVL+8](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Machinery | 0 | 
| #62 | &3E | [AVL+9](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Alloys | 10 | 
| #63 | &3F | [AVL+10](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Firearms | 0 | 
| #64 | &40 | [AVL+11](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Furs | 17 | 
| #65 | &41 | [AVL+12](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Minerals | 58 | 
| #66 | &42 | [AVL+13](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Gold | 7 | 
| #67 | &43 | [AVL+14](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Platinum | 9 | 
| #68 | &44 | [AVL+15](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Gem-Stones | 8 | 
| #69 | &45 | [AVL+16](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#avl) | Market availability of Alien Items | 0 | 
| #70 | &46 | [QQ26](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#qq26) | Random byte that changes for each visit to a system, for randomising market prices | 0 | 
| #71-72 | &47-&48 | [TALLY](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#tally) | Number of kills (low byte then high byte) | 0 | 
| #73 | &49 | [SVC](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#svc) | Save count | 128 | 
| #74 | &4A | [CHK2](https://elite.bbcelite.com/cassette/main/variable/chk2.html) | Secondary checksum | &AA | 
| #75 | &4B | [CHK](https://elite.bbcelite.com/cassette/main/variable/chk.html) | Primary checksum | &03 | 

For the Commodore 64 and Apple II versions, the last few bytes are slightly different:

| Byte # | In hex | Variable | Description | Default | 
|---|---|---|---|---|
| #74 | &4A | [CHK2](https://elite.bbcelite.com/c64/main/variable/chk2.html) | Secondary checksum | &AA | 
| #75 | &4B | [CHK3](https://elite.bbcelite.com/c64/main/variable/chk3.html) | Tertiary checksum | &27 | 
| #76 | &4C | [CHK](https://elite.bbcelite.com/c64/main/variable/chk.html) | Primary checksum | &03 | 

There are various programs from back in the day that let you edit your commander save file; the only complicated part is calculating the CHK checksum, which is done by the [CHECK](https://elite.bbcelite.com/cassette/main/subroutine/check.html) routine (and for the Commodore 64 and Apple II versions, there's also the CHK3 checksum, which is done by the [CHECK2](https://elite.bbcelite.com/c64/main/subroutine/check2.html) routine). You can also find this same algorithm implemented in Python in the elite-checksum.py script, as part of the build process (see the page on [building Elite from the source](https://elite.bbcelite.com/about_site/building_elite.html) for more details).

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/commander_save_files.html](https://elite.bbcelite.com/deep_dives/commander_save_files.html)*
