---
id: memtop
type: entity
title: Execution FE25/FE73-FE33/FE81
aliases:
- Execution FE25/FE73-FE33/FE81
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/memtop.md
  sha256: 602c45fca40d3d5c1f277c8d870d803fe2f26dacca45182020c5b9e68c3a184a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-memtop
---

# Execution FE25/FE73-FE33/FE81



# MEMTOP — Execution FE25/FE73-FE33/FE81 ($FE25)

## Panoramica
La routine KERNAL `MEMTOP` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FE25`
- **Chiamata**: `JSR MEMTOP` o `SYS 65061`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: JMP from Kernal MEMTOP vector at FF99; alternate entry at
E75 by JSR at F2B2/F377 in Close Logical File for RS-
SR at F468/F527 in Open RS-232 Device; alternate entry
D/FE7B by JMP at F480/F53F in Open RS-232 Device,
 FDCF in Initialize Memory Pointers (VIC only).

ering at FE25/FE73, the carry flag determines
r the top of memory is being set or read. If the carry
 clear, or if the routine is entered at FE2D/FE7B, the top
ory pointer (0283) is set from the X and Y register val-
f the carry is set, or if the routine is entered at
E75, the X and Y registers are set from the top of
 pointer (0283).

ation**:

5/FE73: If carry is set, branch to step 3.
7/FE75: Load X and Y registers from pointer to top of
ory (0283), and fall through to step 3.
D/FE7B: Set (0283) from values in X and Y registers.
.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-memtop]]
