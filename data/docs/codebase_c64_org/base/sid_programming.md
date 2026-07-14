---
title: SID and Music Programming
source_url: https://codebase.c64.org/doku.php?id=base%3Asid_programming
category: tutorial
topics:
- raster interrupts
- assembly
- sound generation
difficulty: beginner
language: assembly
hardware:
- SID
- VIC-II
- KERNAL
related:
- sprite-programming
- sound-programming
- memory-map
- raster-interrupts
- sid-registers
- music-player
- kernal-routines
- vic-ii-registers
scraped_at: '2026-07-14'
---

# SID and Music Programming

base:sid_programming

                ### Table of Contents

# SID and Music Programming

This is where you find programming examples as well as hardware information about the SID, the soundchip inside the C64. This section also contain information related to music programming on the c64, such as music file formats and other things like that.

## Playing readymade tunes

This section exemplifies how to play a tune in your own demos/games. The tune itself is done elsewhere, in a editor like JCH/DMC/SDI etc, or coded directly in assembler.

- [Simple IRQ Music Player](https://codebase.c64.org/doku.php?id=sid:simple_irq_music_player)- A small IRQ music player, by Richard/TND
- [Playing music $A000-$FFFF](https://codebase.c64.org/doku.php?id=base:playing_music_a000-_ffff)- A quick tip by Richard/TND
- [Avoiding the $D000-$DFFF issue for playing music](https://codebase.c64.org/doku.php?id=base:avoiding_the_d000-_dfff_issue_for_playing_music)- Some quick tips by Conrad/Viruz
- [Playing music on PAL and NTSC](https://codebase.c64.org/doku.php?id=base:playing_music_on_pal_and_ntsc)- by FTC/HT
- [Very short music play routine with fast forward function](https://codebase.c64.org/doku.php?id=base:very_short_sid_playroutine)- by The Typhoon/FTS 2009

## Waveforms

Detailed examinations of the waveforms.

- [Triangle Waveform](https://codebase.c64.org/doku.php?id=base:triangle_waveform)- by Asger Alstrup
- [Noise Waveform](https://codebase.c64.org/doku.php?id=base:noise_waveform)- by Asger Alstrup

## Players and Editors

This section deals with code to generate music. (Not just playback of readymade music.)

- [256 bytes tune+player](https://codebase.c64.org/doku.php?id=base:256_bytes_tune_player)- Compo entry by FTC/HT for the Tiny SID compo #1.
- [Microtracker V1.0](https://codebase.c64.org/doku.php?id=base:microtracker_v1.0)- minimalistic Musicplayer using max 6 Rasterlines, by The Syndrom
- [A SID Player Routine](https://codebase.c64.org/doku.php?id=base:a_sid_player_routine)- pseudocode for a MIDI controlled SID player - by Linus Wallej (King Fisher/Triad).
- [Building a music routine](https://codebase.c64.org/doku.php?id=base:building_a_music_routine)- aka “- [Rant 6](http://cadaver.homeftp.net/rants/music.htm)” - tutorial by Cadaver
- [Modplay 64](https://codebase.c64.org/doku.php?id=base:modplay_64)- Simple Amiga Module player for the C64.
- [Modplay 128](https://codebase.c64.org/doku.php?id=base:modplay_128)- The C128 version of the above player.
- [Element 114 Music editor](https://codebase.c64.org/doku.php?id=base:element_114_music_editor)- Element 114 music editor with sources.
- [Macro Player](https://codebase.c64.org/doku.php?id=base:macro_player)- Macro Player for the C64 by Geir Tjelta. 64tass source code with music (Noisy Pillars tune by Jeroen Tel).
- [Rob Hubbard - Monty on the Run](https://codebase.c64.org/doku.php?id=magazines:chacking5#rob_hubbard_s_musicdisassembled_commented_and_explained)- A commented disassembly of a player by Rob Hubbard (from C=Hacking #5).
- [Matt Gray - Driller](https://codebase.c64.org/doku.php?id=base:matt_gray_-_driller)- A rough disassembly of Matt Gray's classic Driller tune.
- [Sound Fx Player](https://codebase.c64.org/doku.php?id=base:sound_fx_player)- Play sound fx in your code, by Malcolm Bamber.
- [Sound Fx Routine](https://codebase.c64.org/doku.php?id=base:sound_fx_routine)- Full source code on the sound effect routine made exclusively for the C64 conversion of “Prince of Persia”, by Conrad/Samar.
- [Fake music player](https://codebase.c64.org/doku.php?id=base:fake_music_player)- A debug music player that aids in creating code while considering a music you don't have already. By Karoshier / DaCapo
- [Spectrometer](https://codebase.c64.org/doku.php?id=base:spectrometer)- An example on how you can create a spectrometer by Trap/Bonzai.

### File format descriptions

- [JCH 20.G4 Player File Format](https://codebase.c64.org/doku.php?id=base:jch_20.g4_player_file_format)- Brief documentation of the JCH Editor file format, by FTC

## SID model detection

Is it a 6581 (the old one) or a 8580 (the new one) SID in your machine?

- [detecting sid type](https://codebase.c64.org/doku.php?id=base:detecting_sid_type)- from “mathematica” by Reflex (This is the old and not 100% reliable method)
- [detecting sid type - safe method](https://codebase.c64.org/doku.php?id=base:detecting_sid_type_-_safe_method)- by SounDemon, based on a tip from Dag Lem. (Won't work in VICE.)

## Frequency tables/calculation

- [PAL frequency table](https://codebase.c64.org/doku.php?id=base:pal_frequency_table)- A4 = 440 Hz tuning table for PAL C64s.
- [NTSC frequency table](https://codebase.c64.org/doku.php?id=base:ntsc_frequency_table)- A4 = 440 Hz tuning table for NTSC C64s.
- [ACME-Macros for frequency table calculation](https://codebase.c64.org/doku.php?id=base:acme-macros_for_frequency_table_calculation)- by St0fF/NPL^t0M

## Envelope manipulation

- [Classic hard-restart and about ADSR in generally](https://codebase.c64.org/doku.php?id=base:classic_hard-restart_and_about_adsr_in_generally)- by mixer with contributions from many
- [A new kind of hard-restart](https://codebase.c64.org/doku.php?id=base:a_new_kind_of_hard-restart)- by shrydar with contributions from LFT

## Samples aka Digis

- [NMI Sample Player](https://codebase.c64.org/doku.php?id=base:nmi_sample_player)- Simple universal Sampleplayer (using $d418) working on 6581 and 8580 by Groepaz/Hitmen
- [Digis R Eazy](https://codebase.c64.org/doku.php?id=base:digis_r_eazy)- A tutorial from Domination #13 written by Decomp/Style
- [Vicious Sid Demo Routine Explained](https://codebase.c64.org/doku.php?id=base:vicious_sid_demo_routine_explained)- by SounDemon from Vandalism News #50
- [Musik RunStop Technical Details](https://livet.se/mahoney/c64-files/Musik_RunStop_Technical_Details_by_Pex_Mahoney_Tufvesson_v2.pdf)- Mahoneys 44.1kHz 8-bit digi method from- [Musik Run/Stop](https://csdb.dk/release/?id=129090)

- [Hi Tech Trickery: Sample Dither](https://codebase.c64.org/doku.php?id=magazines:chacking11#hi_tech_trickerysample_dither)- by George Taylor (published in C=Hacking #11)
- [Mods and Digital Mixing](https://codebase.c64.org/doku.php?id=magazines:chacking20#mods_and_digital_mixing)- by Jolse Maginnis (published in C=Hacking #20)
- [The C64 Digi](https://codebase.c64.org/doku.php?id=magazines:chacking20#the_c64_digi)- by R. Harbron, L. Harsfalvi, and S. Judd (published in C=Hacking #20)
- [Addendum to C=Hacking #20](https://codebase.c64.org/doku.php?id=magazines:chacking20addendum)- Further notes on sample playback by L. Harsfalvi

- [C64 DTV DMA SID Digi Player](https://codebase.c64.org/doku.php?id=base:dtv_dma_sid_digi_player)- by Gábor Lénárt.

## Speech Synthesis

- [Disassembly](http://hitmen.c02.at/html/tools_sam.html)of the famous speech synth.
- [Python port](https://github.com/mixer-6581/sampy)of the SAM speech synth.

## MIDI on the C64

- [MIDI on the C64](https://codebase.c64.org/doku.php?id=base:midi_on_the_c64)- A number of wiki pages on MIDI and C64 MIDI coding

## Hardware Issues

base/sid_programming.txt · Last modified:  by mixer

---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asid_programming](https://codebase.c64.org/doku.php?id=base%3Asid_programming)*
