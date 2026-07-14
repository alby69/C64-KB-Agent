---
title: C64 MIDI Data
source_url: https://codebase.c64.org/doku.php?id=base%3Ac64_midi_data
category: reference
topics:
- basic
- assembly
difficulty: intermediate
language: mixed
hardware:
- KERNAL
- CIA
related:
- keyboard-handling
- cia-registers
- memory-map
- kernal-routines
- joystick-reading
scraped_at: '2026-07-14'
---

# C64 MIDI Data

### Table of Contents

# C64 MIDI Data

A Midi keyboard will output Status bytes and data bytes (if any). Status bytes have bit 7 set, while all data bytes have bit 7 cleared.

Status Byte: 80-EF (Midi & Channel messages) Status Byte: F0-F7 (System Common Messages) Status Byte: F8-FF (System Realtime Messages) Data Byte: 00-7F (note, value of pitch bend, value of volume slider, etc..)

Status Bytes between 80-EF controls Midi message and channel number. Midi messages uses the high nybble of the Status Byte. There are 16 midi channels and these can be read from the low nybble of the Status byte. For instance, Midi channel 16 would be hexmal 'F' and Midi Channel 1 would be heximal '0'. If we add the status byte for Pitch wheel to these two examples you will get 'EF' and 'E0'

I will use X as midi channel when describing each Midi message:

## $8x NOTE OFF

This is the note off message and it is followed by 2 data bytes.

data 1: Note number (0-127) data 2: Velocity (0-127)

The velocity inidcates how quickly the note should be released. Note that on some midi keyboards the Status byte $9x will provide the Note Off message.

## $9x NOTE ON

This is the note on message and it is followed by 2 data bytes.

data 1: Note Number (0-127) data 2: Velocity (0-127) (0 = note off)

The velocity indicates how hard you press the note on the keyboard. If the Velocity is zero, the note should be treated as a Note Off message.

## $Ax AFTERTOUCH

This is the aftertouch message and it is followed by 2 data bytes.

data 1: Note Number (0-127) data 2: Pressure amount (0-127) (0 = note off)

Some keyboards allows you to add extra pressure on the keys you already have pressed down. The pressure amount indicates how hard you press the note when using this.

## $Bx CONTROL CHANGE

This is the control change message and it is followed by 2 data bytes.

data 1: Controller number (0-127) data 2: Value (0-127)

Controller number is usally 1 (modulation wheel) but can also be set to 7 (volume wheel), infact there's 127 different controler numbers. Value is just what it says 0-127.

## $Cx PROGRAM CHANGE

This is the program change message and it is followed by 1 data byte.

data 1: program number (0-127)

## $Dx CHANNEL PRESSURE

This is the channel pressure message and it is followed by 1 data byte.

data 1: channel pressure number (0-127, where 127 is the the most pressure).

While notes are playing, pressure can be applied to all of them.

## $Ex PITCH WHEEL

This is the pitch wheel message and it is followed by 2 data bytes.

data 1: bits 0-6 of the 14 bit value (0-127) data 2: bits 7-13 of the 14 bit value (0-127)

The two data bytes should be combined together to form a 14-bit value. The value can be used to decrease or increase the pitch.

## Codice Estratto

### Snippet Codice (BASIC)

```basic
Status Byte: 80-EF  (Midi & Channel messages)
Status Byte: F0-F7  (System Common Messages)
Status Byte: F8-FF  (System Realtime Messages)
Data Byte:   00-7F  (note, value of pitch bend, value of volume slider, etc..)
```

### Snippet Codice (BASIC)

```basic
data 1: Note number (0-127)
data 2: Velocity (0-127)
```

### Snippet Codice (BASIC)

```basic
data 1: Note Number (0-127)
  data 2: Velocity (0-127)     (0 = note off)
```

### Snippet Codice (BASIC)

```basic
data 1: Note Number (0-127)
  data 2: Pressure amount (0-127)     (0 = note off)
```

### Snippet Codice (BASIC)

```basic
data 1: Controller number (0-127)
  data 2: Value (0-127)
```

### Snippet Codice (BASIC)

```basic
data 1: program number (0-127)
```

### Snippet Codice (BASIC)

```basic
data 1: channel pressure number (0-127, where 127 is the the most pressure).
```

### Snippet Codice (BASIC)

```basic
data 1: bits 0-6 of the 14 bit value (0-127)
  data 2: bits 7-13 of the 14 bit value (0-127)
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Ac64_midi_data](https://codebase.c64.org/doku.php?id=base%3Ac64_midi_data)*
