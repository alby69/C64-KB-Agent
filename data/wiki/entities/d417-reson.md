---
id: d417-reson
type: entity
title: Filter Resonance Control Register
aliases:
- Filter Resonance Control Register
tags:
- io-map
- sid-registers
sources:
- path: data/docs/c64ref/io-map/sid/d417-reson.md
  sha256: 404c180665ec763f31622bdad80ef05554f81fdbfb0dd91d070500baa5c4ebcf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-d417-reson
---

# Filter Resonance Control Register



# RESON — Filter Resonance Control Register ($D417)

## Panoramica
Il registro o area di memoria RESON è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$D417` (`54295` decimale)
- **Range**: `$D417`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### C64 Programmer's Reference Guide (Commodore)
7-4  Select Filter Resonance: 0-15
3    Filter External Input: 1 = Yes, 0 = No
2    Filter Voice 3 Output: 1 = Yes, 0 = No
     Filter Voice 2 Output: 1 = Yes, 0 = No
0    Filter Voice 1 Output: 1 = Yes, 0 = No

### Mapping the Commodore 64 (Sheldon Leemon)
0    Filter the output of voice 1?  1=yes
1    Filter the output of voice 2?  1=yes
2    Filter the output of voice 3?  1=yes
3    Filter the output from the external input?  1=yes
4-7  Select filter resonance 0-15

     Bits 0-3 are used to control which of the voices will be altered by
     the filters.  If one of these bits is set to 1, the corresponding
     voice will be processed through the filter, and its harmonic content
     will be changed accordingly.  If the bit is set to 0, the voice will
     pass directly to the audio output.  Note that there is also a
     provision for processing an external audio signal which is brought
     through pin 5 of the Audio/Video Port.

     Bits 4-7 control the resonance of the filter.  By placing a number
     from 0 to 15 in these four bits, you may peak the volume of those
     frequencies nearest the cutoff.  This creates an even sharper
     filtering effect.  A setting of 0 causes no resonance, while a setting
     of 15 gives maximum resonance.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-d417-reson]]
