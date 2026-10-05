---
id: src-nmi-sample-player
type: source
title: 'Source Summary: NMI Sample player'
aliases:
- NMI Sample player
- nmi_sample_player.md
tags:
- sprite programming
- assembly
- sound generation
- memory management
sources:
- path: data/docs/codebase_c64_org/base/nmi_sample_player.md
  sha256: eca7d8ee5226930520c8353dbbd7301cee4e2a5697d6182dbca8a7f49e292de7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: NMI Sample player

**Raw Source File**: `data/docs/codebase_c64_org/base/nmi_sample_player.md`
**SHA256**: `eca7d8ee5226930520c8353dbbd7301cee4e2a5697d6182dbca8a7f49e292de7`

## Summary




# NMI Sample player

base:nmi_sample_player

                # NMI Sample player

Coded using the CA65 assembler.

use like this:

call NMIDIGI_Init once for init, then call NMIDIGI_Play with a pointer (x=hi,y=lo) to a table with parameters (data start lo/hi, data end lo/hi, samplerate lo/hi). NMIDIGI_Off temporarily disables the player, NMIDIGI_On enables it again.

the various compile-time options should be self-explaining (i hope) :)

```
;--------------------------------------------------...
