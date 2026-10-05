---
id: src-c64-midi-data
type: source
title: 'Source Summary: C64 MIDI Data'
aliases:
- C64 MIDI Data
- c64_midi_data.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/c64_midi_data.md
  sha256: a6a2f76c1e8ce64073fb89aa388c70ae33f939f23238b0279a27f693b63ceed5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: C64 MIDI Data

**Raw Source File**: `data/docs/codebase_c64_org/base/c64_midi_data.md`
**SHA256**: `a6a2f76c1e8ce64073fb89aa388c70ae33f939f23238b0279a27f693b63ceed5`

## Summary



# C64 MIDI Data

### Table of Contents

# C64 MIDI Data

A Midi keyboard will output Status bytes and data bytes (if any). Status bytes have bit 7 set, while all data bytes have bit 7 cleared.

Status Byte: 80-EF  (Midi & Channel messages)
Status Byte: F0-F7  (System Common Messages)
Status Byte: F8-FF  (System Realtime Messages)
Data Byte:   00-7F  (note, value of pitch bend, value of volume slider, etc..)

Status Bytes between 80-EF controls Midi message and channel number. Midi messages use...
