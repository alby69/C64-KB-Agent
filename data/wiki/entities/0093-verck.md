---
id: 0093-verck
type: entity
title: Load = 0, Verify = l
aliases:
- Load = 0, Verify = l
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0093-verck.md
  sha256: a3b634087b1278b725cf200f67d7d190528aff2723c2f58bb4a1a824517a6252
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0093-verck
---

# Load = 0, Verify = l



# VERCK — Load = 0, Verify = l ($0093)

## Panoramica
Il registro o area di memoria VERCK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0093` (`147` decimale)
- **Range**: `$0093`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: verify or load flag (Z - loading)

### Commodore-64-intern-Buch (Commodore)
Dieses Flag dient dem Betriebssystem
dazu, um zu unterscheiden, ob eine
LOAD oder eine VERIFY Operation
erfolgt.

### C64 Programmer's Reference Guide (Commodore)
Flag: 0 = Load, 1 = Verify

### Memory Map (Jim Butterfield)
Load = 0, Verify = l

### Mapping the Commodore 64 (Sheldon Leemon)
The same Kernal routine can perform either a LOAD or VERIFY, depending
on the value stored in the Accumulator (.A) on entry to the routine.
This location is used to determine which operation to perform.

### Reference (Joe Forster / STA)
Values:

* $00: LOAD.
* $01-$FF: VERIFY.

### 64'er Magazin (64'er)
Diese Flagge dient dem Betriebssystem, um zu unterscheiden, ob eine LOAD-
Operation nur LOADen oder aber VERIFYen soll.

Sie ist identisch mit der Flagge des Basic-Übersetzers in Speicherzelle 10.
Genauere Hinweise bitte ich der Beschreibung von Zelle 10 zu entnehmen.

### 64map (—)
Flag: 0 = Load, 1 = Verify

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0093-verck]]
