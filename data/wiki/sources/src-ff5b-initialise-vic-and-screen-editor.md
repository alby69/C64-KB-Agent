---
id: src-ff5b-initialise-vic-and-screen-editor
type: source
title: 'Source Summary: initialise VIC and screen editor'
aliases:
- initialise VIC and screen editor
- ff5b-initialise-vic-and-screen-editor.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff5b-initialise-vic-and-screen-editor.md
  sha256: 6f502f55aeef4b96bf17aac1ad06357f309f6d05199a452583fc8958da7ffeca
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: initialise VIC and screen editor

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ff5b-initialise-vic-and-screen-editor.md`
**SHA256**: `6f502f55aeef4b96bf17aac1ad06357f309f6d05199a452583fc8958da7ffeca`

## Summary



# $FF5B — initialise VIC and screen editor

## Disassemblatura
```assembly
.FF5B  20 18 E5 JSR $E518   ; initialise the screen and keyboard
.FF5E  AD 12 D0 LDA $D012   ; read the raster compare register
.FF61  D0 FB    BNE $FF5E   ; loop if not raster line $00
.FF63  AD 19 D0 LDA $D019   ; read the vic interrupt flag register
.FF66  29 01    AND #$01   ; mask the raster compare flag
.FF68  8D A6 02 STA $02A6   ; save the PAL/NTSC flag
.FF6B  4C DD FD JMP $FDDD
```


## Commenti

### Original D...
