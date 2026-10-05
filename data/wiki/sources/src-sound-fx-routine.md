---
id: src-sound-fx-routine
type: source
title: 'Source Summary: Sound Fx Routine (From Prince of Persia (C64))'
aliases:
- Sound Fx Routine (From Prince of Persia (C64))
- sound_fx_routine.md
tags:
- sprite programming
- input handling
- assembly
- raster interrupts
- sound generation
- memory management
sources:
- path: data/docs/codebase_c64_org/base/sound_fx_routine.md
  sha256: 19d988d2c3c4f379ab553c741f44d834b27dd452c21c8e280413169920808e5b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Sound Fx Routine (From Prince of Persia (C64))

**Raw Source File**: `data/docs/codebase_c64_org/base/sound_fx_routine.md`
**SHA256**: `19d988d2c3c4f379ab553c741f44d834b27dd452c21c8e280413169920808e5b`

## Summary




# Sound Fx Routine (From Prince of Persia (C64))

### Table of Contents

# Sound Fx Routine (From Prince of Persia (C64))

## Preface

Below is the full source code for the sound effect player routine made exclusively for Mr.SID's Commodore 64 EasyFlash conversion of “Prince of Persia”. It consists of reading chunks of data that is written directly to each SID register at every frame, including the filter registers.

This code is capable of using up to two voices each time a sound effect is i...
