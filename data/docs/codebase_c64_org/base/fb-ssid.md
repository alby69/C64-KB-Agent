---
title: FB-SSID (Stereophonic-SID)
source_url: https://codebase.c64.org/doku.php?id=base%3Afb-ssid
category: manual
topics:
- assembly
difficulty: intermediate
language: assembly
hardware:
- SID
related:
- music-player
- sound-programming
- sid-registers
scraped_at: '2026-07-14'
---

# FB-SSID (Stereophonic-SID)

# FB-SSID (Stereophonic-SID)

This page contains the most essential parts of the [FB-SSID manual](https://codebase.c64.org/lib/exe/fetch.php?media=base:fb-ssid-rev1a1.pdf) for revision 1A1 of the hardware.

The FB-SSID is compatible with both Commodore 64 and Commodore 128 computers and is available in two versions. One is designed to support a 12Volt 6581 SID while the other is designed for a 9Volt 8580 SID. A pass-through cartridge slot is also included intended for use with the Prophet64 cartridge. However, other cartridges like the Epyx Fastloader may also function when plugged into this slot.

The FB-SSID includes an 8-way DIP switch and IO1/IO2 jumper used to configure the memory address of the FBSSID. The default memory address is $DE00.

Pin 8 of the DIP switch is the one closest to the edge of the circuit board. Pin 1 of the DIP switch is the one closest to the SID chip.

| Jumper (JP1) | 8-way DIP Switch | FB-SSID Address | 
|---|---|---|
| Pins 1-2 | Pin 1 down, other pins up | $DEE0 | 
| Pins 1-2 | Pin 2 down, other pins up | $DEC0 | 
| Pins 1-2 | Pin 3 down, other pins up | $DEA0 | 
| Pins 1-2 | Pin 4 down, other pins up | $DE80 | 
| Pins 1-2 | Pin 5 down, other pins up | $DE60 | 
| Pins 1-2 | Pin 6 down, other pins up | $DE40 | 
| Pins 1-2 | Pin 7 down, other pins up | $DE20 | 
| Pins 1-2 | Pin 8 down, other pins up | $DE00 | 
| Pins 2-3 | Pin 1 down, other pins up | $DFE0 | 
| Pins 2-3 | Pin 2 down, other pins up | $DFC0 | 
| Pins 2-3 | Pin 3 down, other pins up | $DFA0 | 
| Pins 2-3 | Pin 4 down, other pins up | $DF80 | 
| Pins 2-3 | Pin 5 down, other pins up | $DF60 | 
| Pins 2-3 | Pin 6 down, other pins up | $DF40 | 
| Pins 2-3 | Pin 7 down, other pins up | $DF20 | 
| Pins 2-3 | Pin 8 down, other pins up | $DF00 | 

DO NOT change the DIP switch settings when the Commodore computer is powered on. Always turn the computer OFF before selecting the required configuration.

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Afb-ssid](https://codebase.c64.org/doku.php?id=base%3Afb-ssid)*
