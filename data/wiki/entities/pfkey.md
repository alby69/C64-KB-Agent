---
id: pfkey
type: entity
title: PFKEY
aliases:
- PFKEY
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/pfkey.md
  sha256: 66aedd22a3764d01cbb1bea21522ee655a6635c11631a75ba1a6890df98d4f7d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-pfkey
---

# PFKEY




# PFKEY —  ($FF65)

## Panoramica
La routine KERNAL `PFKEY` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF65`
- **Chiamata**: `JSR PFKEY` o `SYS 65381`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
ou turn on the 128, its function keys are predefined.
ng F3 prints DIRECTORY, F7 holds the LIST command,
 on. The PFKEY Kernal routine assigns a new definition
 of the 10 programmable function keys (F1-F8, SHIFT-
OP, and HELP).

he routine with the accumulator holding the address
hree-byte zero-page string descriptor, .X holding the key
 (1-10), and .Y holding the length of the new defi-
 string. The first two bytes of the descriptor in zero page
 contain the address of the definition string (in the
low-byte/high-byte order); the final byte should hold
nk number where the definition string is located. PFKEY
t check the key number for validity; a value outside the
able range may garble existing definitions. Upon return,
rry bit will be clear if the new definition was success-
added, or set if there was insufficient room in the defi-
 table for the new definition.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-pfkey]]
