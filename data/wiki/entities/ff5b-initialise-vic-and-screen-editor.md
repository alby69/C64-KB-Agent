---
id: ff5b-initialise-vic-and-screen-editor
type: entity
title: initialise VIC and screen editor
aliases:
- initialise VIC and screen editor
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff5b-initialise-vic-and-screen-editor.md
  sha256: 6f502f55aeef4b96bf17aac1ad06357f309f6d05199a452583fc8958da7ffeca
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ff5b-initialise-vic-and-screen-editor
---

# initialise VIC and screen editor



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

### Original Disassembly (—)
- **$FF5B**: initialise the screen and keyboard
- **$FF5E**: read the raster compare register
- **$FF61**: loop if not raster line $00
- **$FF63**: read the vic interrupt flag register
- **$FF66**: mask the raster compare flag
- **$FF68**: save the PAL/NTSC flag

### Commodore-64-intern-Buch (Commodore)
- **$FF5B**: Videocontroller initialisie- ren
- **$FF5E**: Rasterzeile
- **$FF61**: wartet auf Ende Videozeile
- **$FF63**: Interrupt durch Rasterzeile?
- **$FF66**: Bit 0 isolieren und als Flag
- **$FF68**: PAL/NTSC-Version merken
- **$FF6B**: Interrupttimer setzen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FF5B**: original I/O init
- **$FF5E**: wait for top of screen
- **$FF61**: at line zero
- **$FF63**: Check IRQ flag register if interrupt occurred
- **$FF66**: only first bit
- **$FF68**: store in PAL/NTSC flag
- **$FF6B**: jump to ENABLE TIMER

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ff5b-initialise-vic-and-screen-editor]]
