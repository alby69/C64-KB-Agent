---
title: The key logger
source_url: https://elite.bbcelite.com/deep_dives/the_key_logger.html
category: deep-dive
topics:
- basic
- assembly
- input handling
difficulty: beginner
language: mixed
hardware:
- CPU
- KERNAL
- CIA
related:
- keyboard-handling
- joystick-reading
- memory-map
- kernal-routines
- cia-registers
scraped_at: '2026-07-14'
---

# The key logger

## Supporting concurrent in-flight key presses using a key logger

There's a lot to do when piloting a spaceship. Pitching and rolling while slamming on the brakes to avoid missing the docking slot; firing lasers while activating the E.C.M. and slamming your foot on the accelerator; targeting a missile while switching between space views, trying to track down your foe... it's all in a day's work for your average Cobra Mk III pilot.

Unfortunately, most 8-bit micros weren't built to handle multiple concurrent key presses. The Machine Operating System (MOS) in the BBC Micro can handle up to two concurrent key presses, on top of the modifier keys; this known as a "two-key rollover", and it's generally fine for typing, as you rarely intend to press more than two letter keys at the same time. However, for a game where you legitimately might want to pitch up, roll right, fire lasers, slow down and launch a missile all at the same time (by pressing "X", ">", "A", "?" and "M" concurrently), a simple two-key rollover just won't do.

Elite therefore implements its own logging system that listens for key presses for all the important flight controls, and stores their details in a keyboard logger for the main loop to process in its own time. There are 15 of these flight controls, which are split up into the seven primary controls (speed, pitch, roll and lasers) and eight secondary controls (energy bomb, escape pod, missile controls, E.C.M., in-system jump and the docking computer). The key logger effectively implements an eight-key rollover for each of the primary controls, plus one secondary control, which is more than enough to make the game responsive to our every whim.

The Commodore 64 version uses a variant of the BBC Micro's key logger, called KEYLOOK (also known as KLO). It does the same job as the KL key logger in the BBC Micro versions, but it has a very different structure, due to the different way in which the Commodore's keyboard works. See the deep dive on [reading the Commodore 64 keyboard matrix](https://elite.bbcelite.com/reading_the_commodore_64_keyboard_matrix.html) for details.

Interestingly, the NES conversion of Elite also uses the key logger, even though it doesn't have a keyboard; for details, see the deep dive on [bolting NES controllers onto the key logger](https://elite.bbcelite.com/bolting_nes_controllers_onto_the_key_logger.html). The following describes the key logger in the BBC Micro version, but the general idea is the same in all the 6502 versions of Elite.

## How the key logger works

													 ------------------------

						The heart of the key logger system is the table at location [KL](https://elite.bbcelite.com/cassette/main/workspace/zp.html#kl). This contains one byte for each of the 15 flight controls listed in the keyboard lookup table at [KYTB](https://elite.bbcelite.com/cassette/main/variable/kytb.html), starting from KL+1 for "?" (slow down) and going through to KL+15 for "C" (which turns on the docking computer). Each key logger location has its own label, so KY1 = KL+1, KY2 = KL+2 up to KY15 = KL+15, where KY1 corresponds to the internal key number in KYTB+1, KY2 to the key number in KYTB+2, and so on.

The various keyboard scanning routines can set the relevant byte in the KL table to &FF to denote that a particular key is being pressed. The logger is cleared to zero (to denote that no keys are being pressed) by the U% routine.

The main routines that populate the key logger in the BBC Micro version are:

- [DKS4](https://elite.bbcelite.com/cassette/main/subroutine/dks4.html), which scans the keyboard for a specific key
- [DKS1](https://elite.bbcelite.com/cassette/main/subroutine/dks1.html), which calls DKS4 and updates the key logger with the result
- [DOKEY](https://elite.bbcelite.com/cassette/main/subroutine/dokey.html), which calls DKS1 for each of the primary flight controls
- [DK4](https://elite.bbcelite.com/cassette/main/subroutine/dk4.html), which scans for the secondary flight controls

If a key is being pressed that is not in the keyboard table at KYTB, then it can be stored in the first location in the key logger, KL, as this isn't mapped to a KYTB key. This is done in routine DK4, for example, so we almost never miss a key press.

In addition, the joystick fire button is checked, and if it is pressed, the key logger entry for laser fire ("A") is set, so there is only one location to check when processing laser fire.

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/the_key_logger.html](https://elite.bbcelite.com/deep_dives/the_key_logger.html)*
