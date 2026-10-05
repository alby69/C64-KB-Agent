---
id: 00cf-blnon
type: entity
title: Cursor in blink phase
aliases:
- Cursor in blink phase
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00cf-blnon.md
  sha256: ad209020b15164fab2d6ad7c83596f2c261a2afaf09f8ec2f8e1b0a019aa6f79
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00cf-blnon
---

# Cursor in blink phase



# BLNON — Cursor in blink phase ($00CF)

## Panoramica
Il registro o area di memoria BLNON è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00CF` (`207` decimale)
- **Range**: `$00CF`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
On/off blink flag

### Commodore-64-intern-Buch (Commodore)
In diesem Register wird festgehalten,
in welcher Blink-Phase sich der Cursor
gerade befindet.

### C64 Programmer's Reference Guide (Commodore)
Flag: Last Cursor Blink On/Off

### Memory Map (Jim Butterfield)
Cursor in blink phase

### Mapping the Commodore 64 (Sheldon Leemon)
This location keeps track of whether, during the current cursor blink,
the character under the cursor was reversed, or was restored to
normal.  This location will contain a 0 if the character is reversed,
and a 1 if the character is restored to its nonreversed status.

### Reference (Joe Forster / STA)
Values:

* $00: Cursor off phase, original character visible.
* $01: Cursor on phase, reverse character visible.

### 64'er Magazin (64'er)
In dieser Speicherzelle wird festgehalten, in welcher der beiden Blink-Phasen -
normal oder revers - der Cursor sich gerade befindet. Eine 0 bedeutet reverses
Zeichen, eine 1 bedeutet ein normales Zeichen.

Die Abfrage innerhalb eines Basic-Programms funktioniert nicht. Denn die
Interrupt-Routine steuert den Phasenwechsel.

### 64map (—)
Flag: Cursor Status; $00 = Off, $01 = On

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00cf-blnon]]
