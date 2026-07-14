---
title: Advanced tactics with the NEWB flags
source_url: https://elite.bbcelite.com/deep_dives/advanced_tactics_with_the_newb_flags.html
category: deep-dive
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

# Advanced tactics with the NEWB flags

## How the enhanced versions of Elite give their ships a bit more personality

The enhanced versions of Elite for the BBC Micro disc, 6502 Second Processor, Commodore 64, Apple II, BBC Master and NES have a much more sophisticated tactics routine than the original BBC Micro cassette and Acorn Electron versions. At the core of this advanced routine is the set of NEWB flags, which were added to the cassette version as it grew into the disc version - "NEWB" stands for "New Byte", which presumably got its name because it's tacked onto the end of the existing 36-byte ship data block, as byte #36 (so that's just after bytes #0 through #35, which are described in the deep dive on [ship data blocks](https://elite.bbcelite.com/ship_data_blocks.html)).

If you've ever sat outside a space station and watched as transporters fly out of the slot and head towards the planet, then you've seen the NEWB flags in action (these transporters are traders, with bit #0 set); here's a transporter leaving a station in the BBC Master version:

![A transporter in the BBC Master version of Elite](https://elite.bbcelite.com/images/master/transporter_station.png) 

						It's the same with shuttles, which are also NEWB-powered; here's one leaving a station in the Commodore 64 version:

![A shuttle in the Commodore 64 version of Elite](https://elite.bbcelite.com/images/c64/busy_station.png) 

						Essentially, the NEWB flags give each newly spawned ship a personality, and they determine how it behaves. For example, traders have the trading flag set (bit #0), and they tend to ply their trade between the space station and the planet; the direction of travel, meanwhile, is determined by the docking flag (bit #4). Some traders might moonlight as bounty hunters (bit #1), which means they will break off their trading runs to attack us if we are a fugitive or a serious offender, at which point they become hostile (bit #2). Other flags cover things like pirate behaviour, whether a ship is a cop or an innocent bystander, and whether a ship has an escape pod fitted.

It's a fairly simple system, but it manages to add a convincing layer to the universe simulation; it's surprisingly immersive to park yourself outside a station and watch the traders and shuttles head off to the planet while others fly back up, and it's all down to the NEWB flags.

## The NEWB flags

													 --------------

						In the versions of Elite that support advanced tactics, there is a table at [E%](https://elite.bbcelite.com/6502sp/main/variable/e_per_cent.html) that contains the default NEWB byte for each ship type. When spawning a new ship, bits #0-3 and #5-6 from this byte are applied to the new ship's NEWB flags in byte #36, so a set bit in the default NEWB byte in E% will set that bit in the spawned ship's NEWB flags. This means that if a ship blueprint has one of the following personality types - trader, bounty hunter, hostile, pirate, innocent bystander or cop - then all spawned ships of that type will have that personality too (so all Geckos are pirates, for example).

The other bits in the spawned ship's NEWB flags are set as follows:

- Bit 4 (docking) is set randomly on spawning for traders only, so 50% of traders are trying to dock, while the other 50% fly towards the planet.
- Bit 7 (has been scooped/has docked) is set when the ship docks or is scooped.
- Bit 7 in the blueprint (as opposed to the spawned ship) is looked up during tactics, for when the ship is about to die, to see if that ship type has an escape pod fitted. If it does, then the ship can launch an escape pod before dying.

Here's a breakdown of the NEWB flags:

| Bit | Description | 
|---|---|
| #0 | Trader flag * 0 = not a trader * 1 = trader 80% of traders (61% in the disc version) are peaceful and mind their own business plying their trade between the planet and space station, but 20% of them (39% in the disc version) moonlight as bounty hunters as well (see bit #1) Ships that are traders: Escape pod, Shuttle, Transporter, Anaconda, Rock hermit, Worm | 
| #1 | Bounty hunter flag * 0 = not a bounty hunter * 1 = bounty hunter If we are a fugitive or a serious offender and we bump into a bounty hunter, they will become hostile and attack us (see bit #2) Ships that are bounty hunters: Viper, Fer-de-lance | 
| #2 | Hostile flag * 0 = not hostile * 1 = hostile Hostile ships will attack us on sight; there are quite a few of them Ships that are hostile: Sidewinder, Mamba, Krait, Adder, Gecko, Cobra Mk I, Worm, Cobra Mk III, Asp Mk II, Python (pirate), Moray, Thargoid, Thargon, Constrictor | 
| #3 | Pirate flag * 0 = not a pirate * 1 = pirate Hostile pirates will attack us on sight, but once we get inside the space station safe zone, they will stop Ships that are pirates: Sidewinder, Mamba, Krait, Adder, Gecko, Cobra Mk I, Cobra Mk III, Asp Mk II, Python (pirate), Moray, Thargoid | 
| #4 | Docking flag * 0 = not docking * 1 = docking Traders with their docking flag set fly towards the space station to try to dock, otherwise they aim for the planet This flag is randomly set for traders when they are spawned Ships that can be docking: Escape pod, Shuttle, Transporter, Anaconda, Rock hermit, Worm | 
| #5 | Innocent bystander * 0 = normal * 1 = innocent bystander If we attack an innocent ship within the space station safe zone, then the station will get angry with us and start spawning cops Ships that are innocent bystanders: Shuttle, Transporter, Cobra Mk III, Python, Boa, Anaconda, Rock hermit, Cougar | 
| #6 | Cop flag * 0 = not a cop * 1 = cop If we destroy a cop, then we instantly become a fugitive (the Transporter isn't actually a cop, but it's clearly under police protection) Ships that are cops: Viper, Transporter | 
| #7 | Scooped, docked, escape pod flag For spawned ships, this flag indicates that the ship been scooped or has docked (bit 7 is always clear on spawning) For blueprints, this flag indicates whether the ship type has an escape pod fitted, so it can launch it when in dire straits Ships that have escape pods: Cobra Mk III, Python, Boa, Anaconda, Rock hermit, Viper, Mamba, Krait, Adder, Cobra Mk I, Cobra Mk III (pirate), Asp Mk II, Python (pirate), Fer-de-lance | 

To see the NEWB flags in action, the best place to look is the main [TACTICS](https://elite.bbcelite.com/6502sp/main/subroutine/tactics_part_2_of_7.html) routine.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/advanced_tactics_with_the_newb_flags.html](https://elite.bbcelite.com/deep_dives/advanced_tactics_with_the_newb_flags.html)*
