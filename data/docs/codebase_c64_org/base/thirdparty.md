---
title: Third party hardware programming
source_url: https://codebase.c64.org/doku.php?id=base%3Athirdparty
category: manual
topics:
- basic
- assembly
difficulty: beginner
language: assembly
hardware:
- CPU
- KERNAL
- CIA
- SID
related:
- sid-registers
- keyboard-handling
- memory-map
- joystick-reading
- music-player
- sound-programming
- kernal-routines
- cia-registers
scraped_at: '2026-07-20'
---

# Third party hardware programming

### Table of Contents

# Third party hardware programming

Information about programming REU's, cartridges such as Action Replay/Final Cartridge/Retro Replay, RR-net/SilverSurfer, and so on.

## Cartridges

### General cartridge info

- [Cartridge bugs](https://codebase.c64.org/doku.php?id=base:cartridge_bugs)- A collection of bugs in common cartridges like Action Replay, Retro Replay and Final Cartridge. Original version of this text was by GRG.
- [Cartridge detection](https://codebase.c64.org/doku.php?id=base:cartridge_detection)- Article by AlexC.
- [Assembling your own cart ROM image](https://codebase.c64.org/doku.php?id=base:assembling_your_own_cart_rom_image)- info collected by FTC.
- [Code frame for 16 KB crt-images](https://codebase.c64.org/doku.php?id=base:code_frame_for_16_kb_crt-images)- by enthusi.
- [Code frame for 64 KB crt-images, i.e. for RGCD](https://codebase.c64.org/doku.php?id=base:code_frame_for_64_kb_crt-images_i.e._for_rgcd)- by enthusi.
- ["crt.txt"](https://codebase.c64.org/doku.php?id=base:crt_file_format)- Emu cart file format. By Peter Schepers (and Per Hakan Sundell, Markus Brenner, Marco Van Den Heuvel)
- ["io_stnd.txt" - IO addresses](https://codebase.c64.org/doku.php?id=base:io_addresses)- Swiftlink, MIDI interfaces, IDE64, ETH64, REUc etc.. by T. Pribyl
- [Hardware Expansions Info at AAY64](http://www.unusedino.de/ec64/technical/aay/c64/cartmain.htm)- by Ninja
- [C64GS detection](https://codebase.c64.org/doku.php?id=base:c64gs_detection)- by encore.

### Retro Replay

- [Inside Retro Replay](https://codebase.c64.org/doku.php?id=base:inside_retro_replay)- Jens Schoenfeld
- [RR detect](https://codebase.c64.org/doku.php?id=base:rr_detect)- detecting the presence of a Retro Replay by FMan
- [RR chip data](https://codebase.c64.org/doku.php?id=base:rr_chip_data)- obtaining chip type and manufacturer by FMan
- [RR flashing](https://codebase.c64.org/doku.php?id=base:rr_flashing)- programming the FlashROM and Block & Chip Erase by FMan

### 1541U

- [Safely freezing the C64 on an asynchronous event](https://codebase.c64.org/lib/exe/fetch.php?media=base:safely_freezing_the_c64.pdf)- Gideon Zweijtzer - How the 1541U freezer works

- [Official website](http://www.1541ultimate.net)- some useful info is hidden among the forum posts

### 1541U-II

- [1541 Ultimate-II Technical Documentation v0.3](https://codebase.c64.org/lib/exe/fetch.php?media=base:1541u2doc_v0.3.pdf)- Gideon Zweijtzer

### EasyFlash

EasyFlash is a 1 MByte Flash memory card for the expansion port.

- [About Easyflash](https://codebase.c64.org/doku.php?id=base:about_easyflash)- Some basic info on this cart by enthusi
- [Code Sample](https://codebase.c64.org/doku.php?id=base:code_sample)- Minimal framework for an EasyFlash cart by skoe/enthusi

- [Official website](http://skoe.de/easyflash/)- Specs, schematics
- [Development website](http://hg.berlios.de/repos/easyflash)- Tool chain, SDK

### REU

This is about the 17xx “RAM Expansion Unit” and compatible clones such as the CMD REU and the 1541U. (Note that not all C64 PSU's can handle the extra current consumed by the REU, in case you experience problems.)

- [REU detect](https://codebase.c64.org/doku.php?id=base:reu_detect)- by M. Sachse
- [REU registers](https://codebase.c64.org/doku.php?id=base:reu_registers)- by Marko Mäkelä
- [REU read and write](https://codebase.c64.org/doku.php?id=base:reu_read_and_write)- using the RAM Expansion by FMan
- [REU programming](https://codebase.c64.org/doku.php?id=base:reu_programming)- by Richard Hable

- [Technical Reference](https://zimmers.net/anonftp/pub/cbm/documents/chipdata/CSG8726TechRefDoc-1.0.zip)(- [local copy](https://codebase.c64.org/lib/exe/fetch.php?media=base:csg8726techrefdoc-1.0.zip)) - most complete REU reference manual by Wolfgang Moser
- [1750/1764 REU Service Schematics](https://codebase.c64.org/lib/exe/fetch.php?media=base:1750-1764-reu-serviceschematics.pdf)- by Commodore

### geoRAM

Not Similar to REUs. Memory banked in between $de00-$deff.

- [geoRAM registers](https://codebase.c64.org/doku.php?id=base:georam_registers)- The simple spec for how to use it - White Flame
- [Tiny screenselection](https://codebase.c64.org/doku.php?id=base:tiny_screenselection)- example on how to code for it by enthusi

### SuperCPU

- [SuperCPU & Kickassembler](https://codebase.c64.org/doku.php?id=base:supercpu_kickassembler)- SuperCPU Kickassembler Library by TWW

### Swiftlink

RS-232 interface cartridge by CMD.

- ["io_stnd.txt" - IO addresses](https://codebase.c64.org/doku.php?id=base:io_addresses)- Brief info on Swiftlink, among other things. By T. Pribyl

### MIDI cartridges

See the [ MIDI section](https://codebase.c64.org/doku.php?id=base:midi_on_the_c64) for information on MIDI cart programming.

### Stereo SID carts

- [FB-SSID](https://codebase.c64.org/doku.php?id=base:fb-ssid)- Hardware created by Fotios

### Wersiboard Music 64

- [Wersiboard Music 64](https://codebase.c64.org/doku.php?id=base:wersiboard_music_64)- by FTC

## Other third party hardware

### CMD HD

- [HD-Park-Switch - How to Patch a CMD-HD to your own needs](https://codebase.c64.org/doku.php?id=base:hd-park-switch_-_how_to_patch_a_cmd-hd_to_your_own_needs)- in Domination #17 by Ninja/The Dreams.

### RR-Net

This hardware is an add-on to be used with the Retro Replay or the MMC64 interface.

- [RR-Net memory map & docs](https://codebase.c64.org/doku.php?id=base:rr-net_memory_map_docs)- by Jens Schoenfeld

### Silversurfer

This hardware is an add-on to be used with the Retro Replay or the MMC64 interface.

- [Inside_RetroSurfer](https://codebase.c64.org/doku.php?id=base:inside_retrosurfer)- how to code it on the C64 with Retro Replay, by Groepaz
- [Inside_Surfer](https://codebase.c64.org/doku.php?id=base:inside_surfer)- how to code it on Amiga, by Jens Schoenfeld

- [silversurfer.inc](https://codebase.c64.org/doku.php?id=base:silversurfer_hardware-defines)- Silversurfer Hardware-defines, by Groepaz
- [silversurfer_polling.s](https://codebase.c64.org/doku.php?id=base:silversurfer_polling)- simple and small polling-mode driver for the SilverSurfer, by Groepaz

Below is a quick hack of a serial driver for use with the [CC65](http://www.cc65.org/) c-compiler.
WARNING: this *really* is a hack, not even implementing half of what it should!

- [rs232silversurfer.h](https://codebase.c64.org/doku.php?id=base:rs232silversurfer.h)- by Groepaz
- [rs232silversurfer.s](https://codebase.c64.org/doku.php?id=base:rs232silversurfer.s)- by Groepaz

### DTV

- [Detect DTV Type](https://codebase.c64.org/doku.php?id=base:dtv_detect)- by TLR, also detects c64/c128 and pal/ntsc

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Athirdparty](https://codebase.c64.org/doku.php?id=base%3Athirdparty)*
