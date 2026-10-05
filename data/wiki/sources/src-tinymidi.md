---
id: src-tinymidi
type: source
title: 'Source Summary: base:tinymidi [Codebase64 wiki]'
aliases:
- base:tinymidi [Codebase64 wiki]
- tinymidi.md
tags:
- raster interrupts
- assembly
- sound generation
- memory management
sources:
- path: data/docs/codebase_c64_org/base/tinymidi.md
  sha256: 94d70187a872c1d1dfba67372e39eea9c28b04f9adf898acd2d140d54d7a1262
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:tinymidi [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/tinymidi.md`
**SHA256**: `94d70187a872c1d1dfba67372e39eea9c28b04f9adf898acd2d140d54d7a1262`

## Summary




# base:tinymidi [Codebase64 wiki]

base:tinymidi

                ## TinyMidi Source Code:

```
;---------------------------------------------
;TinyMIDI (c) GRG/SHAPE 2007
;---------------------------------------------
;This program was made for the Sequential (SCI) Interface.
;It will play the notes you press on your midi keyboard
;with the sid chip. 
_MIDIReset      = %00000011 ;Same for all interfaces
_MIDI16CountDiv = %00010101 ;1mhz interfaces: 16 divider
_MIDI64CountDIv = %00010110 ;2mh...
