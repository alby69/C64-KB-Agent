---
title: Voice 1 Control Register
source_url: https://github.com/mist64/c64ref/blob/main/src/c64io/mapping_the_commodore_64.txt
category: reference
topics:
- io-map
- sid-registers
difficulty: intermediate
language: assembly
hardware:
- SID
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64io
  source_files:
  - mapping_the_commodore_64.txt
  - c64_programmer's_reference_guide.txt
  address: $D404
  symbol: VCREG1
  sources:
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 7    Select Random Noise Waveform, 1 = On
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: '0    Gate Bit:  1=Start attack/decay/sustain, 0=Start release'
---

# VCREG1 — Voice 1 Control Register ($D404)

## Panoramica
Il registro o area di memoria VCREG1 è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D404` (`54276` decimale)
- **Range**: `$D404`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7    Select Random Noise Waveform, 1 = On
6    Select Pulse Waveform, 1 = On
5    Select Sawtooth Waveform, 1 = On
4    Select Triangle Waveform, 1 = On
3    Test Bit: 1 = Disable Oscillator 1
2    Ring Modulate Osc. 1 with Osc. 3 Output,
       1 = On
1    Synchronize Osc.1 with Osc.3 Frequency,
       1 = On
0    Gate Bit: 1 = Start Att/Dec/Sus,
               0 = Start Release

### Mapping the Commodore 64 (Sheldon Leemon)
0    Gate Bit:  1=Start attack/decay/sustain, 0=Start release
1    Sync Bit:  1=Synchronize Oscillator with Oscillator 3 frequency
2    Ring Modulation:  1=Ring modulate Oscillators 1 and 3
3    Test Bit:  1=Disable Oscillator 1
4    Select triangle waveform
5    Select sawtooth waveform
6    Select pulse waveform
7    Select random noise waveform

     Bit 0.  Bit 0 is used to gate the sound.  Setting this bit to a 1
     while selecting one of the four waveforms will start the
     attack/decay/sustain part of the cycle.  Setting this bit back to 0
     (while keeping the same waveform setting) anytime after a note has
     started playing will begin the release cycle of the note.  Of course,
     in order for the gate bit to have an effect, the frequency and
     attack/decay/sustain/release (ADSR) registers must be set, as well as
     the pulse width, if necessary, and the volume control set to a nonzero
     value.

     Bit 1.  This bit is used to synchronize the fundamental frequency of
     Oscillator 1 with the fundamental frequency of Oscillator 3, allowing
     you to create a wide range of complex harmonic structures from voice
     1.  Synchronization occurs when this bit is set to 1.  Oscillator 3
     must be set to some frequency other than zero, but no other voice 3
     parameters will affect the output from voice 1.

     Bit 2.  When Bit 2 is set to 1, the triangle waveform output of voice
     1 is replaced with a ring modulated combination of Oscillators 1 and
     3.  This ring modulation produces nonharmonic overtone structures that
     are useful for creating bell or gong effects.

     Bit 3.  Bit 3 is the test bit.  When set to 1, it disables the output
     of the oscillator.  This can be useful in generating very complex
     waveforms (even speech synthesis) under software control.

     Bit 4.  When set to 1, Bit 4 selects the triangle waveform output of
     Oscillator 1.  Bit 0 must also be set for the note to be sounded.

     Bit 5.  This bit selects the sawtooth waveform when set to 1.  Bit 0
     must also be set for the sound to begin.

     Bit 6.  Bit 6 chooses the pulse waveform when set to 1.  The harmonic
     content of sound produced using this waveform may be varied using the
     Pulse Width Registers.  Bit 0 must be set to begin the sound.

     Bit 7.  When Bit 7 is set to 1, the noise output waveform for
     Oscillator 1 is set.  This creates a random sound output whose
     waveform varies with a frequency proportionate to that of Oscillator
     1.  It can be used to imitate the sound of explosions, drums, and
     other unpitched noises.

     One of the four waveforms must be chosen in order to create a sound.
     Setting more than one of these bits will result in a logical ANDing of
     the waveforms.  Particularly, the combination of the noise waveform
     and another is not recommended.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*