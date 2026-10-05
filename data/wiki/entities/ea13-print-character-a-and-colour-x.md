---
id: ea13-print-character-a-and-colour-x
type: entity
title: print character A and colour X
aliases:
- print character A and colour X
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ea13-print-character-a-and-colour-x.md
  sha256: 1da3cbf12f251804cd0122c2e4aedb62f1469f7bc7023362bb4ba24b281e5466
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ea13-print-character-a-and-colour-x
---

# print character A and colour X



# $EA13 — print character A and colour X

## Disassemblatura
```assembly
.EA13  A8       TAY   ; copy the character
.EA14  A9 02    LDA #$02   ; set the count to $02, usually $14 ??
.EA16  85 CD    STA $CD   ; save the cursor countdown
.EA18  20 24 EA JSR $EA24   ; calculate the pointer to colour RAM
.EA1B  98       TYA   ; get the character back
```


## Commenti

### Original Disassembly (—)
- **$EA13**: copy the character
- **$EA14**: set the count to $02, usually $14 ??
- **$EA16**: save the cursor countdown
- **$EA18**: calculate the pointer to colour RAM
- **$EA1B**: get the character back

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EA13**: put print character in (Y)
- **$EA16**: store initial value in BLNCT, timer to toggle cursor
- **$EA18**: synchronise colour pointer
- **$EA1B**: print character back to (A)
- **$EA1C**: PNTR, cursor column on line
- **$EA1E**: store character on screen
- **$EA21**: store character colour

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ea13-print-character-a-and-colour-x]]
