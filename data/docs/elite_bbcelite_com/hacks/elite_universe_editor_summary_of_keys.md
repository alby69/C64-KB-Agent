---
title: Summary of keys for the Elite Universe Editor
source_url: https://elite.bbcelite.com/hacks/elite_universe_editor_summary_of_keys.html
category: tool
topics:
- basic
- assembly
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

# Summary of keys for the Elite Universe Editor

## All the keys used in all the different versions of the Elite Universe Editor

The Universe Editor is described in full detail in the instructions for the [BBC version](https://elite.bbcelite.com/elite_universe_editor_instructions_bbc.html) and [Commodore 64 version](https://elite.bbcelite.com/elite_universe_editor_instructions_commodore_64.html), but here's a summary of all supported key presses for reference. Click on the following to jump down to the relevant section:

A lot of these key presses will be familiar from the original game, which is great if you're running the Universe Editor on real hardware. If you're using an emulator, however, note that modern keyboards don't have the same range of keys as the BBC Micro or Commodore 64, or even the same layout. In particular, BBC keys like f0 and COPY don't tend to exist anymore, and neither do Commodore 64 keys like RUN/STOP or C=, so if you are using an emulator, you may have to check the documentation to see which keys you should press instead.

For example, in JSBeeb, BeebEm and b2, you should press f10 instead of f0 to launch the editor, while in B-em you should press f1 to f7 instead of f0 to f6. In all these emulators you should press End instead of COPY to duplicate a ship, and while some emulators will emulate the BBC Micro's DELETE key using both Delete and backspace, others may only recognise backspace. And as for the @ key, it may be mapped to backtick, it may be mapped to backslash, or it may even be mapped to the @ key on your keyboard; experimentation pays off here.

It's a similar story on the Commodore. For example, the VICE emulator maps RUN/STOP to Escape, C= to TAB, left arrow to End, CLR/HOME to Home and INST/DEL to backspace. For details, consult your emulator's documentation.


													 -----------------------------

						Let's start with the keys you can use for opening and closing the editor, and bringing up the menu and various space views:

| BBC key | Function | 
|---|---|
| f0 | Launch the Universe Editor from the first title screen | 
| ESCAPE | Quit the Universe Editor and return to the game | 
| @ | Open the menu for saving, loading and playing universe files | 
| f0 | Switch to the front space view | 
| f1 | Switch to the rear space view | 
| f2 | Switch to the left space view | 
| f3 | Switch to the right space view | 

Next up are the keys for [adding, selecting, duplicating and deleting objects](https://elite.bbcelite.com/elite_universe_editor_instructions_bbc.html#adding):

| BBC key | Function | 
|---|---|
| RETURN | Add a new ship into the first empty slot | 
| Q, W | Select the ship in the previous/next slot | 
| H | Highlight the currently selected ship on the scanner | 
| DELETE | Delete the currently selected ship | 
| COPY | Duplicate the currently selected ship | 

To add a new ship to the universe, press RETURN, followed by the relevant key for the type of ship you want to add:

| Key | Ship | 
|---|---|
| 1 | Missile | 
| 2 | Escape pod | 
| 3 | Alloy plate | 
| 4 | Cargo canister | 
| 5 | Boulder | 
| 6 | Asteroid | 
| 7 | Splinter | 
| 8 | Shuttle | 
| 9 | Transporter | 
| A | Cobra Mk III | 
| B | Python | 
| C | Boa | 
| D | Anaconda | 
| E | Rock hermit (asteroid) | 
| F | Viper | 
| G | Sidewinder | 
| H | Mamba | 
| I | Krait | 
| J | Adder | 
| K | Gecko | 
| L | Cobra Mk I | 
| M | Worm | 
| N | Cobra Mk III (pirate) | 
| O | Asp Mk II | 
| P | Python (pirate) | 
| Q | Fer-de-lance | 
| R | Moray | 
| S | Thargoid | 
| T | Thargon | 
| U | Constrictor | 
| V | Cougar | 
| W | The Elite logo (6502 Second Processor version only) | 

These are the keys for [moving objects in space](https://elite.bbcelite.com/elite_universe_editor_instructions_bbc.html#moving):

| BBC key | Function | 
|---|---|
| Cursor keys | Move the currently selected object up/down/left/right (hold SHIFT for faster movement, CTRL for much faster movement) | 
| ?, SPACE | Move the currently selected object closer/further away (hold SHIFT for faster movement, CTRL for much faster movement) | 
| S, X | Pitch the currently selected object forwards/backwards | 
| <, > | Roll the currently selected object left/right | 
| K, L | Yaw the currently selected object left/right | 
| R | Reset the position of the currently selected object | 

These are the keys for [editing ship attributes](https://elite.bbcelite.com/elite_universe_editor_instructions_bbc.html#attributes):

| BBC key | Function | 
|---|---|
| 1 | Acceleration (1 = increase, SHIFT-1 = decrease) | 
| 2 | Toggle AI tactics on/off | 
| 3 | Toggle innocent bystander flag on/off | 
| 4 | Toggle cop flag on/off | 
| 5 | Toggle hostile flag on/off | 
| 6 | Aggression level (6 = increase, SHIFT-6 = decrease) | 
| 7 | Speed (7 = increase, SHIFT-7 = decrease) | 
| 8 | Roll counter (8 = increase, SHIFT-8 = decrease) | 
| 9 | Pitch counter (9 = increase, SHIFT-9 = decrease) | 
| 0 | Energy level (0 = increase, SHIFT-0 = decrease) | 
| M | Number of missiles (M = increase, SHIFT-M = decrease) | 
| T | Select missile target (press T then the target's slot number, with SHIFT-0 to SHIFT-9 for slots 10 to 19) | 
| C | Toggle docking computer on/off ("S" bulb) | 
| E | Toggle E.C.M. on/off ("E" bulb) | 
| A | Toggle lasers (so they fire at us) | 
| P | Toggle "personality" (trader, pirate, sun/station, etc.) | 
| D | Destroy the currently selected ship (so it explodes) | 

And finally, these are the keys for [editing the galaxy seeds](https://elite.bbcelite.com/elite_universe_editor_instructions_bbc.html#seeds):

| BBC key | Function | 
|---|---|
| G | Edit the galaxy seeds to generate an entirely new set of galaxies | 
| f4 | Long-range Chart | 
| f5 | Short-range Chart | 
| f6 | Data on System | 
| Cursor keys | Move the crosshairs (hold SHIFT for faster movement) | 
| D | Show the distance to the current system | 
| O | Reset crosshairs to the current system | 
| F | Search for a system | 
| H | Set the system under the crosshairs as the current system | 
| CTRL-H | Jump to the next galaxy | 


													 -----------------

						Note that on the Commodore 64, there are only two cursor keys (down and right). To move up or left, hold down SHIFT to move in the opposite direction; most emulators will automatically support the four cursor keys on modern keyboards. As a result of this, we can't use SHIFT for things like faster movement or decreasing a value instead of increasing it, so instead we use the Commodore C= key to modify our actions instead.

Let's start with the keys you can use for opening and closing the editor, and bringing up the menu and various space views:

| C64 key | Function | 
|---|---|
| f1 | Launch the Universe Editor from the first title screen | 
| RUN/STOP | Quit the Universe Editor and return to the game | 
| @ | Open the menu for saving, loading and playing universe files | 
| f1 | Switch to the front space view | 
| f3 | Switch to the rear space view | 
| f5 | Switch to the left space view | 
| f7 | Switch to the right space view | 

Next up are the keys for [adding, selecting, duplicating and deleting objects](https://elite.bbcelite.com/elite_universe_editor_instructions_commodore_64.html#adding):

| C64 key | Function | 
|---|---|
| RETURN | Add a new ship into the first empty slot | 
| Q, W | Select the ship in the previous/next slot | 
| H | Highlight the currently selected ship on the scanner | 
| INST/DEL | Delete the currently selected ship | 
| CLR/HOME | Duplicate the currently selected ship | 

To add a new ship to the universe, press RETURN, followed by the relevant key for the type of ship you want to add:

| Key | Ship | 
|---|---|
| 1 | Missile | 
| 2 | Escape pod | 
| 3 | Alloy plate | 
| 4 | Cargo canister | 
| 5 | Boulder | 
| 6 | Asteroid | 
| 7 | Splinter | 
| 8 | Shuttle | 
| 9 | Transporter | 
| A | Cobra Mk III | 
| B | Python | 
| C | Boa | 
| D | Anaconda | 
| E | Rock hermit (asteroid) | 
| F | Viper | 
| G | Sidewinder | 
| H | Mamba | 
| I | Krait | 
| J | Adder | 
| K | Gecko | 
| L | Cobra Mk I | 
| M | Worm | 
| N | Cobra Mk III (pirate) | 
| O | Asp Mk II | 
| P | Python (pirate) | 
| Q | Fer-de-lance | 
| R | Moray | 
| S | Thargoid | 
| T | Thargon | 
| U | Constrictor | 
| V | Cougar | 

These are the keys for [moving objects in space](https://elite.bbcelite.com/elite_universe_editor_instructions_commodore_64.html#moving):

| C64 key | Function | 
|---|---|
| Cursor keys | Move the currently selected object up/down/left/right (hold SHIFT for opposite direction, C= for faster movement, CTRL for much faster movement) | 
| ?, SPACE | Move the currently selected object closer/further away (hold C= for faster movement, CTRL for much faster movement) | 
| S, X | Pitch the currently selected object forwards/backwards | 
| <, > | Roll the currently selected object left/right | 
| K, L | Yaw the currently selected object left/right | 
| R | Reset the position of the currently selected object | 

These are the keys for [editing ship attributes](https://elite.bbcelite.com/elite_universe_editor_instructions_commodore_64.html#attributes):

| C64 key | Function | 
|---|---|
| 1 | Acceleration (1 = increase, C=1 = decrease) | 
| 2 | Toggle AI tactics on/off | 
| 3 | Toggle innocent bystander flag on/off | 
| 4 | Toggle cop flag on/off | 
| 5 | Toggle hostile flag on/off | 
| 6 | Aggression level (6 = increase, C=6 = decrease) | 
| 7 | Speed (7 = increase, C=7 = decrease) | 
| 8 | Roll counter (8 = increase, C=8 = decrease) | 
| 9 | Pitch counter (9 = increase, C=9 = decrease) | 
| 0 | Energy level (0 = increase, C=0 = decrease) | 
| M | Number of missiles (M = increase, C=M = decrease) | 
| T | Select missile target (press T then the target's slot number, with C=0 to C=9 for slots 10 to 19) | 
| C | Toggle docking computer on/off ("S" bulb) | 
| E | Toggle E.C.M. on/off ("E" bulb) | 
| A | Toggle lasers (so they fire at us) | 
| P | Toggle "personality" (trader, pirate, sun/station, etc.) | 
| D | Destroy the currently selected ship (so it explodes) | 

And finally, these are the keys for [editing the galaxy seeds](https://elite.bbcelite.com/elite_universe_editor_instructions_commodore_64.html#seeds):

| C64 key | Function | 
|---|---|
| G | Edit the galaxy seeds to generate an entirely new set of galaxies | 
| Left arrow | Switch to chart mode so the following keys access the charts rather than changing ship attributes | 
| 4 | Long-range Chart | 
| 5 | Short-range Chart | 
| 6 | Data on System | 
| Cursor keys | Move the crosshairs (hold SHIFT for opposite direction, RETURN for faster movement) | 
| D | Show the distance to the current system | 
| O | Reset crosshairs to the current system | 
| F | Search for a system | 
| H | Set the system under the crosshairs as the current system | 
| CTRL-H | Jump to the next galaxy |

---
*Fonte originale: [https://elite.bbcelite.com/hacks/elite_universe_editor_summary_of_keys.html](https://elite.bbcelite.com/hacks/elite_universe_editor_summary_of_keys.html)*
