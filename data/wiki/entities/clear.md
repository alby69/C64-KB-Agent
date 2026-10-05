---
id: clear
type: entity
title: Serial Channels and Reset Default Devices F333/F3F3-F349/F409
aliases:
- Serial Channels and Reset Default Devices F333/F3F3-F349/F409
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/clear.md
  sha256: 1c7763737d0d70bc566cebaaf955f849397314b290bd9b97d367bc1a3860997e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-clear
---

# Serial Channels and Reset Default Devices F333/F3F3-F349/F409



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

## References
- Source: [[src-clear]]
