---
title: Serial Channels and Reset Default Devices F333/F3F3-F349/F409
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/compute!'s_tool_kit:_kernal.txt
category: reference
topics:
- kernal-api
- system-routines
- jumps
difficulty: intermediate
language: assembly
hardware:
- C64
related:
- clrchn
- jmp
- jsr
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - compute!'s_tool_kit:_kernal.txt
  address: $F333
  symbol: Clear
  sources:
  - name: 'COMPUTE!''s Tool Kit: Kernal'
    author: Dan Heeb
    description: 'ed by**: Indirect JMP through (0322) from Kernal CLRCHN vector at'
---

# Clear — Serial Channels and Reset Default Devices F333/F3F3-F349/F409 ($F333)

## Panoramica
La routine KERNAL `Clear` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F333`
- **Chiamata**: `JSR Clear` o `SYS 62259`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (0322) from Kernal CLRCHN vector at
fall through from F331/F3F1 in Reset to No Open Files.

ation**:

the current output device is a serial device, JSR
E/EF04 to command the serial device to unlisten.
the current input device is a serial device, JSR
F/EEF6 to command the serial device to untalk.
et 9A, the current output device, to the screen (3).
et 99, the current input device, to the keyboard (0).

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*