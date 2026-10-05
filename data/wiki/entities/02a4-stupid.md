---
id: 02a4-stupid
type: entity
title: CIA 1 Timer A enabled flag
aliases:
- CIA 1 Timer A enabled flag
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/02a4-stupid.md
  sha256: 2c317b7c940bb6955b8f490658a98b5b28b2077ca20619419b8ca1cba7fbb356
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-02a4-stupid
---

# CIA 1 Timer A enabled flag



# STUPID — CIA 1 Timer A enabled flag ($02A4)

## Panoramica
Il registro o area di memoria STUPID è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$02A4` (`676` decimale)
- **Range**: `$02A4`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: hold indicator (NZ - no T1IRQ yet) for T1IRQ

### Commodore-64-intern-Buch (Commodore)
Hier wird bei Bandroutinen angegeben,
ob Timer A läuft oder nicht. Wenn hier
eine $00 steht, ist der Timer
freigegeben, andernfalls ist er
gesperrt.

### C64 Programmer's Reference Guide (Commodore)
Temp D1 IRQ Indicator For Cassette Read

### Memory Map (Jim Butterfield)
CIA 1 Timer A enabled flag

### Mapping the Commodore 64 (Sheldon Leemon)
Save Area for CIA #1 Control Register A During Cassette Read

### 64'er Magazin (64'er)
Derselbe Wert, der bei der Vorbereitung des Lesevorganges von der Kassette in
die Speicherzelle 674 kommt, gelangt auch nach 676, von wo er zu einem späteren
Zeitpunkt beim Lesen zu Vergleichszwecken herangezogen wird.

### 64map (—)
Temporary D1IRQ Indicator during Tape READ

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-02a4-stupid]]
