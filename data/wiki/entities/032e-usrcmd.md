---
id: 032e-usrcmd
type: entity
title: Warm start vector ($FE66)
aliases:
- Warm start vector ($FE66)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/032e-usrcmd.md
  sha256: 82e17dc8a844313bbfa5f9ccf9ea681103ed1a990bbe5d6a4ca5781a531dd053
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-032e-usrcmd
---

# Warm start vector ($FE66)



# USRCMD — Warm start vector ($FE66) ($032E)

## Panoramica
Il registro o area di memoria USRCMD è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$032E` (`814` decimale)
- **Range**: `$032E`-`$032F`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$FE66 Warmstart-Vektor

### C64 Programmer's Reference Guide (Commodore)
User-Defined Vector

### Memory Map (Jim Butterfield)
Warm start vector ($FE66)

### Mapping the Commodore 64 (Sheldon Leemon)
This appears to be a holdover from PET days, when the built-in machine
language monitor would JuMP through the USRCMD vector when it
encountered a command that it did not understand, allowing the user to
add new commands to the monitor.

Although this vector is initialized to point to the routine called by
STOP/ RESTORE and the BRK interrupt, and is updated by the Kernal
VECTOR routine (64794, $FD1A), it does not seem to have the function
of aiding in the addition of new commands.

### Reference (Joe Forster / STA)
Default: $FE66.

### 64'er Magazin (64'er)
Nach dem Einschalten zeigt dieser Vektor auf die BREAK-Routine, genauso wie der
Vektor in Speicherzelle 790 und 791. Er ist ein Überbleibsel aus dem PET-
Betriebssystem, das aber beim VC 20 und C 64 keine Rolle spielt. Hier können
also eigene Vektoren definiert und eingesetzt werden.

### 64map (—)
User Defined Vector ($FE66)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-032e-usrcmd]]
