---
title: Working with the Apple II keyboard
source_url: https://elite.bbcelite.com/deep_dives/working_with_the_apple_ii_keyboard.html
category: deep-dive
topics:
- basic
- assembly
- input handling
difficulty: beginner
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

# Working with the Apple II keyboard

## Trying to implement a game-ready key logger, one key press at a time

The Apple II is an interesting computer to work with. On one hand, it puts you so closely in touch with the hardware that it can be a bit of a shock: the sound system is a particularly extreme example, giving the programmer nothing more than a single switch to flip the loudspeaker cone in and out (see the deep dive on [sound effects in Apple II Elite](https://elite.bbcelite.com/sound_effects_in_apple_ii_elite.html) for details).

But there are some aspects that feel as if the hardware is overly hidden from the programmer, with no way to access the low-level electronics. The keyboard is probably the most obvious example, and the effect that it has on Elite is quite profound. Let's see why.

## One key at a time

													 -----------------

						The other versions of 6502 Elite contain some pretty sophisticated keyboard routines. The game originated on the BBC Micro, whose keyboard is a thing of beauty, and the authors took full advantage of this sophisticated hardware, building a key logging system that enables multiple flight keys to be read at the same time (see the deep dive on [the key logger](https://elite.bbcelite.com/the_key_logger.html) for details).

This same model is used in all the versions of 6502 Elite, from the Commodore 64's keyboard to the NES version's controllers, as discussed in the deep dives on [reading the Commodore 64 keyboard matrix](https://elite.bbcelite.com/reading_the_commodore_64_keyboard_matrix.html) and [bolting NES controllers onto the key logger](https://elite.bbcelite.com/bolting_nes_controllers_onto_the_key_logger.html). The result is a game in which you can roll and pitch and fire lasers and speed up, all at the same time; all you need are lots of fingers.

The Apple II version also uses the key logger, but only because it was already built into the Commodore 64 codebase from which the Apple version is derived; unplugging the key logger would be a big job, and it isn't necessary, but it does mean the Apple version also has a sophisticated key logger inside the codebase. But this key logger is only ever used to log one key press at time, and this is down to the hardware: the Apple keyboard controller only reads one key at a time, and that's it.

The other versions of Elite all scan their keyboards or controllers for multiple flight keys during each iteration of the main loop, but there simply isn't the hardware support for this approach in the Apple II. Instead, the Apple II exposes the keyboard via two memory-mapped soft switches at $C000 and $C010. If the byte at $C000 has bit 7 set, then bits 0 to 6 contain the ASCII code of the last key to be pressed; and accessing $C010 resets the keyboard strobe so the keyboard controller looks for the next key press, and updates $C000 accordingly when it is pressed. And that's it: only one key press is ever exposed at a time, and it's always the last key to be pressed.

You can see this in action in the [RDKEY](https://elite.bbcelite.com/apple/main/subroutine/rdkey.html) routine, which is the only place in the whole game where the keyboard is read (there is another routine called [DKSANYKEY](https://elite.bbcelite.com/apple/main/subroutine/dksanykey.html) that detects whether any key is being pressed, but this is not used anywhere). The RDKEY routine starts with a call to the [ZEKTRAN](https://elite.bbcelite.com/apple/main/subroutine/zektran.html) routine, which resets the key logger at [KEYLOOK](https://elite.bbcelite.com/apple/main/workspace/zp.html#keylook), and then it checks bit 7 of $C000 to see if a key press has been registered. If it has, then it updates the relevant entry in the key logger... and that's it - that's the entire keyboard scanning routine. We don't even need a translation table to convert internal key numbers into ASCII, as the Apple II already returns ASCII via $C000. It's really easy to use, but it's also pretty restrictive when it comes to seat-of-the-pants gaming.

## Impact on gameplay

													 ------------------

						Not surprisingly, this one-key limitation makes the flight controls feel pretty different. Apple II Elite is perfectly playable on the keyboard, and if you grew up with this as your only version, then you wouldn't know what you were missing. But switch from the BBC Micro to the Apple II version, and the difference in the keyboard controls is quite profound.

For example, one of my favourite moves in Elite is to roll and pitch at the same time - it's an efficient way of getting those pesky pirates into your sights. But you simply can't do this on the Apple version: when you press a key, the game forgets about any other keys that you are holding down, and it only processes the latest key press. So if you press climb ("X") and then roll right (">"), you will only roll right, as that's the last key you pressed. And if you are pitching down ("S") and decide to fire your lasers at your foe ("A"), the game will forget that you are holding down the "S" key, and you will slowly stop pitching down as the damping kicks in, even though you are still holding down "S". To add to the confusion, if you then release the "A" key to stop firing but continue to hold down "S", the game will not take any notice, and you won't start pitching down again unless you release the key and press it again.

The reason is that the Apple II keyboard controller only records when keys are actually pressed down, at which point the ASCII value of the key being pressed is stored in $C000 and bit 7 is set. If a new key is then pressed, then $C000 is updated to the new value and the old key press is discarded, even if that key is still being held down. If the latest key is then held down and no other keys are pressed, then the key being held down will auto-repeat, updating the $C000 soft switch at a repeat rate of roughly ten times a second; but as soon as the current key is released or any other key is pressed, the system forgets about the original key and moves on to the next one.

We can't access the keyboard matrix to scan the keyboard ourselves, so we simply have to live with this limitation. In other words, we can tell when a key is pressed, and the keyboard controller repeats the key press for us if the key is held down, but that's it: we can't tell if a key has been released, and we can't tell if any other keys are being held down, other than the last one to be pressed.

This is perhaps for the best, as the even though the keyboard controller in the Apple II supports n-key rollover (i.e. holding down multiple keys at once), the keyboard itself doesn't contain the diodes needed to make this work, so ghosting on an Apple keyboard would be a major issue if the matrix were exposed. Instead, the controller hides the keyboard from the programmer and exposes just one key - the last one to be pressed.

Luckily, like the BBC Micro, the Apple II supports analogue joysticks, which provide much more fine-tuned control over your ship than the Apple keyboard... though on the Apple II and Apple II+, the joystick port is little more than a 16-pin DIP socket on the motherboard, so even installing this option requires getting involved with the hardware.

Welcome to home computing, 1970s-style...

---
*Fonte originale: [https://elite.bbcelite.com/deep_dives/working_with_the_apple_ii_keyboard.html](https://elite.bbcelite.com/deep_dives/working_with_the_apple_ii_keyboard.html)*
