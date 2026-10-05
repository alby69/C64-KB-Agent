---
id: membot
type: entity
title: Execution FE34/FE82-FE42/FE90
aliases:
- Execution FE34/FE82-FE42/FE90
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/membot.md
  sha256: f51821898b722e1ad4ab122d40e652fa9e0047e5302ad3d68232d5634930251d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-membot
---

# Execution FE34/FE82-FE42/FE90



# MEMBOT — Execution FE34/FE82-FE42/FE90 ($FE34)

## Panoramica
La routine KERNAL `MEMBOT` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FE34`
- **Chiamata**: `JSR MEMBOT` o `SYS 65076`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal MEMBOT vector at FF9C.

 carry is clear at entry, set (0281), the pointer to the
 of memory, from the X and Y registers. If carry is set at
 load X and Y registers from (0281).

ation**:

 carry is clear, branch to step 3.
ad X and Y registers from pointer to bottom of memory
281), and fall through to step 3.
t (0281) from values in X and Y registers.
S.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-membot]]
