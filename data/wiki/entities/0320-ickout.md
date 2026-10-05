---
id: 0320-ickout
type: entity
title: Set - output vector ($F250)
aliases:
- Set - output vector ($F250)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0320-ickout.md
  sha256: f988f6002e3bc2945ee70758ee1b0ab497c43efbdd7f803267b1805c33ec7cf8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0320-ickout
---

# Set - output vector ($F250)



# ICKOUT — Set - output vector ($F250) ($0320)

## Panoramica
Il registro o area di memoria ICKOUT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0320` (`800` decimale)
- **Range**: `$0320`-`$0321`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F250 CKOUT-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CHKOUT Routine

### Memory Map (Jim Butterfield)
Set - output vector ($F250)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CKOUT Routine (Currently at 62032 ($F250))

### Reference (Joe Forster / STA)
Default: $F250.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 62032 ($F250) - beim VC 20 auf 62217
($F309). Dort beginnt die Routine, welche einen Datenkanal zur Abgabe von Daten
an das im OPEN-Befehl angegebene Gerät aufmacht.

### 64map (—)
Vector: Indirect entry to Kernal CHKOUT Routine ($F250)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0320-ickout]]
