---
id: src-c64-midi-interfaces
type: source
title: 'Source Summary: MIDI Interfaces'
aliases:
- MIDI Interfaces
- c64_midi_interfaces.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/c64_midi_interfaces.md
  sha256: f7b2fbcee34b94f7dad903917421b4ee8e066c1ba7961d143b9955e94e8fe12a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: MIDI Interfaces

**Raw Source File**: `data/docs/codebase_c64_org/base/c64_midi_interfaces.md`
**SHA256**: `f7b2fbcee34b94f7dad903917421b4ee8e066c1ba7961d143b9955e94e8fe12a`

## Summary



# MIDI Interfaces

base:c64_midi_interfaces

                ### Table of Contents

# MIDI Interfaces

Here is a list of Interfaces, 6850 UART registers and the most important values you will be feeding the Control Register with.

| SEQUENTIAL CIRCUITS INC. |  |  | 
|---|---|---|
| Mode | 1 MHZ IRQ |  | 
| Control Register | $DE00 | Write only | 
| Status Register | $DE02 | Read only | 
| Transmit Data (Tx) | $DE01 | Write only | 
| Receive Data (Rx) | $DE03 | Read only | 
| Midi Reset | $03 |...
