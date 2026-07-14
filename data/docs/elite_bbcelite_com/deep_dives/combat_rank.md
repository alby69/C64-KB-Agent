---
title: Combat rank
source_url: https://elite.bbcelite.com/deep_dives/combat_rank.html
category: deep-dive
topics:
- memory management
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

# Combat rank

## The long, long road from Harmless to Elite

Elite is famous for being one of the first open-world games. It doesn't hold your hand or tell you what to do. You can fly wherever you like and take on a role of your own choosing, from humble trader or isolated asteroid miner, to tenacious bounty hunter or vicious pirate. Elite is whatever you want it to be, and it's all part of its charm.

There is, however, an overarching "point" to the game, and that's to increase your combat rank from Harmless to Elite by destroying other ships. It's part of the lure that makes players keep coming back to the game, and part of the reason that people play this game for months on end. That gradual creep towards the ultimate accolade is key to Elite's appeal; there's a reason that it's literally the name of the game, and a prominent part of the Status Mode screen:

![The Status Mode screen in the BBC Micro disc version of Elite](https://elite.bbcelite.com/images/disc/status_mode.png) 

						These are the ranks that are burned into the memories of anyone who's played this game seriously:

- Harmless
- Mostly Harmless
- Poor
- Average
- Above Average
- Competent
- Dangerous
- Deadly
- Elite

Let's take a deeper look at what's involved in progressing from Harmless to the heady heights of Elite.

## Keeping track of the combat rank

													 --------------------------------

						The current combat rank is stored as the number of kills, in a 16-bit variable at [TALLY(1 0)](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html#tally) in the [T% workspace](https://elite.bbcelite.com/cassette/main/workspace/t_per_cent.html) - so the high byte is in TALLY+1 and the low byte in TALLY.

If the high byte in TALLY+1 is 0 then we have between 0 and 255 kills, so our rank is Harmless, Mostly Harmless, Poor, Average, Above Average or Competent, according to the value of the low byte in TALLY. This is how the lower ranks pan out:

| Rank | Number of kills | From | To | NES kills | 
|---|---|---|---|---|
| Harmless | 0 to 7 | %00000000 | %00000111 | 0 to 1 | 
| Mostly Harmless | 8 to 15 | %00001000 | %00001111 | 2 to 7 | 
| Poor | 16 to 31 | %00010000 | %00011111 | 8 to 23 | 
| Average | 32 to 63 | %00100000 | %00111111 | 24 to 43 | 
| Above Average | 64 to 127 | %01000000 | %01111111 | 44 to 129 | 
| Competent | 128 to 511 | %10000000 | %11111111 | 130 to 511 | 

For the NES version, the ranks were tweaked slightly to make it easier to rise through the lower ranks.

For the other 6502 versions, if you look at the binary equivalents to these ranks, you can see that if we are Harmless then bits 3-7 are clear, if we are Mostly Harmless or below then bits 4-7 are clear, if we are Poor or below then bits 5-7 are clear, if we are Average or below then bits 6-7 are clear, if we are Above Average or below then bit 7 is clear, and if we are Competent then bit 7 is set. This is no coincidence, as it allows the [STATUS](https://elite.bbcelite.com/cassette/main/subroutine/status.html) routine to calculate the lower ranks with a simple loop that shifts the low byte of TALLY to the right until the result is zero, after which the number of shifts gives us the rank.

It isn't quite so convenient with the higher ranks, which are given in the high byte of the kill count in TALLY+1. If the high byte is non-zero then we are Competent, Dangerous, Deadly or Elite, according to the following values of the high byte, though as Competent crosses the boundary, we have to check for that:

| Rank | High byte | Number of kills | 
|---|---|---|
| Competent | 1 | 128 to 511 kills (130 to 511 in NES) | 
| Dangerous | 2 to 9 | 512 to 2559 kills | 
| Deadly | 10 to 24 | 2560 to 6399 kills | 
| Elite | 25 and up | 6400 kills and up | 

These ranges don't have shift-friendly binary values, so the [STATUS](https://elite.bbcelite.com/cassette/main/subroutine/status.html) routine calculates the higher ranks with a sequence of CMP instructions.

## Right On Commander!

													 -------------------

						The lower ranks come and go fairly quickly, once you've got the hang of combat, but although reaching Competent with 128 kills feels like an achievement - and it is! - it's still only 2% of the way to Elite, despite being the sixth rank of ten. To encourage players to keep on grinding through the ranks, the game flashes up the encouraging message "Right On Commander!" on-screen every 256 kills - in other words, every time the high byte of TALLY gets incremented. The checks for this are done in the [EXNO2](https://elite.bbcelite.com/cassette/main/subroutine/exno2.html) routine, which is called after every kill to increment the tally.

The first "Right On Commander!" shows when you have achieved Competent rank and then earned a further 128 kill points, at which point the high byte in TALLY+1 gets updated to 1 to indicate a grand total of 256 kills. It then happens every 256 kills until you reach Elite, and it keeps on going beyond that. When you become Elite in Elite Dangerous, the message from the Pilots Federation starts off with "Right on Commander!", and although the phrase isn't quite so important in the later games, it's still a popular sign-off amongst Elite veterans, along with "See you in the black" and "o7" (the latter representing a commander saluting).

## Combat rank on the BBC Master and NES

													 -------------------------------------

						In the BBC Micro, 6502 Second Processor and Electron versions of Elite, you get one kill for each ship you destroy. It doesn't actually matter what you kill, you still get one point towards your combat rank. Asteroids: one kill point. Harmless traders: one kill point. Cargo canisters: one kill point. This led to people sitting outside space stations, armed to the teeth with military lasers, where they would simply point their sights at the docking slot and wipe out the police as they launched; after all, even for mass murderers, your legal status eventually cools down, and you're still left with one kill point per Viper. It's easy pickings.

This all changed with the Commodore 64 version, which the authors started work on once the BBC versions had proven such a success. Instead of one point per kill, the authors implemented different kill points for each ship type, along with support for fractional kills. This same approach was carried over into the BBC Master, Apple II and NES versions of Elite, where the kill points are as follows (with the most lucrative shown first):

| Ship | Points awarded | 
|---|---|
| Constrictor | 5.33203125 | 
| Cougar | 5.33203125 | 
| Thargoid | 2.6640625 | 
| Fer-de-lance | 1.25 | 
| Cobra Mk III (pirate) | 1.1640625 | 
| Python (pirate) | 1.1640625 | 
| Asp Mk II | 1.08203125 | 
| Anaconda | 1.0 | 
| Cobra Mk III | 0.9140625 | 
| Boa | 0.83203125 | 
| Moray | 0.75 | 
| Python | 0.6640625 | 
| Cobra Mk I | 0.6640625 | 
| Missile | 0.58203125 | 
| Mamba | 0.5 | 
| Adder | 0.3515625 | 
| Rock hermit (asteroid) | 0.33203125 | 
| Sidewinder | 0.33203125 | 
| Krait | 0.33203125 | 
| Gecko | 0.33203125 | 
| Worm | 0.1953125 | 
| Thargon | 0.12890625 | 
| Viper | 0.1015625 | 
| Transporter | 0.06640625 | 
| Escape pod | 0.0625 | 
| Shuttle | 0.0625 | 
| Alloy plate | 0.0390625 | 
| Cargo canister | 0.0390625 | 
| Splinter | 0.0390625 | 
| Asteroid | 0.03125 | 
| Boulder | 0.0234375 | 

In this more sophisticated system, it's worth tracking down Thargoids, Fer-de-lances and pirates, but it's far less profitable to incinerate police Vipers, cargo canisters or more harmless ships like shuttles and transporters. Sure, you can still sit outside a space station, vaporising Vipers until your lasers are raw, but it's probably easier just to learn how to fight.

Also, on the NES version only, the commander image changes with rank. See the deep dive on [displaying two-layer images](https://elite.bbcelite.com/displaying_two-layer_images.html) for details.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/combat_rank.html](https://elite.bbcelite.com/deep_dives/combat_rank.html)*
