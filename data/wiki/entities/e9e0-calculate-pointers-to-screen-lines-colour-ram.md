---
id: e9e0-calculate-pointers-to-screen-lines-colour-ram
type: entity
title: calculate pointers to screen lines colour RAM
aliases:
- calculate pointers to screen lines colour RAM
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e9e0-calculate-pointers-to-screen-lines-colour-ram.md
  sha256: 767d2f0fb16284eae50dfd88307c3f40a2e4119659bc65e2c33356f068972b52
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e9e0-calculate-pointers-to-screen-lines-colour-ram
---

# calculate pointers to screen lines colour RAM



# $E9E0 — calculate pointers to screen lines colour RAM

## Disassemblatura
```assembly
.E9E0  20 24 EA JSR $EA24   ; calculate the pointer to the current screen line colour RAM
.E9E3  A5 AC    LDA $AC   ; get the next screen line pointer low byte
.E9E5  85 AE    STA $AE   ; save the next screen line colour RAM pointer low byte
.E9E7  A5 AD    LDA $AD   ; get the next screen line pointer high byte
.E9E9  29 03    AND #$03   ; mask 0000 00xx, line memory page
.E9EB  09 D8    ORA #$D8   ; set  1101 01xx, colour memory page
.E9ED  85 AF    STA $AF   ; save the next screen line colour RAM pointer high byte
.E9EF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E9E0**: calculate the pointer to the current screen line colour RAM
- **$E9E3**: get the next screen line pointer low byte
- **$E9E5**: save the next screen line colour RAM pointer low byte
- **$E9E7**: get the next screen line pointer high byte
- **$E9E9**: mask 0000 00xx, line memory page
- **$E9EB**: set  1101 01xx, colour memory page
- **$E9ED**: save the next screen line colour RAM pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$E9E0**: Zeiger auf Farb-RAM berechnen
- **$E9E3**: Zeiger
- **$E9E5**: für Zeile
- **$E9E7**: speichern
- **$E9E9**: Startadresse
- **$E9EB**: des Video-RAM
- **$E9ED**: berechnen
- **$E9EF**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E9E0**: synchronise colour pointer
- **$E9E3**: SAL, pointer for screen scroll
- **$E9E5**: EAL
- **$E9EB**: setup colour ram to $d800

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e9e0-calculate-pointers-to-screen-lines-colour-ram]]
