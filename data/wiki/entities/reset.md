---
id: reset
type: entity
title: to No Open Files F32F/F3EF-F332/F3F2
aliases:
- to No Open Files F32F/F3EF-F332/F3F2
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/reset.md
  sha256: bdc9757bd31b5725cfccad1ee23a242240b42e0df927a288062724f46bd49127
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-reset
---

# to No Open Files F32F/F3EF-F332/F3F2



# Reset — to No Open Files F32F/F3EF-F332/F3F2 ($F32F)

## Panoramica
La routine KERNAL `Reset` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F32F`
- **Chiamata**: `JSR Reset` o `SYS 62255`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (032C) from Kernal CLALL vector at
FFE7.

location 98, the number of open files, to zero and
hrough to F333/F3F3 to reset any open serial channels
set the default device numbers.

ation**:

 98, the number of open files, to 0.
l through to F333/F3F3, Clear Serial Channels and Reset
ault Devices routine.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-reset]]
