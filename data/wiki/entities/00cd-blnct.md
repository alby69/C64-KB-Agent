---
id: 00cd-blnct
type: entity
title: Cursor timing countdown
aliases:
- Cursor timing countdown
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00cd-blnct.md
  sha256: d497c3139dd197f9d2be75cfe3375c7dbee517fba4a5993d884665407b641733
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00cd-blnct
---

# Cursor timing countdown



# BLNCT — Cursor timing countdown ($00CD)

## Panoramica
Il registro o area di memoria BLNCT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00CD` (`205` decimale)
- **Range**: `$00CD`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Count to toggle cur

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle dient als Zähler
für die Cursor-Blinkphase. Wenn der
Wert 20 in dieser Speicherzelle
abgezählt ist, wird der Cursor eingeschaltet.

### C64 Programmer's Reference Guide (Commodore)
Timer: Countdown to Toggle Cursor

### Memory Map (Jim Butterfield)
Cursor timing countdown

### Mapping the Commodore 64 (Sheldon Leemon)
The interrupt routine that blinks the cursor uses this location to
tell when it's time for a blink.  First the number 20 is put here, and
every jiffy (1/60 second) the value here is decreased by one, until it
reaches zero.  Then the cursor is blinked, the number 20 is put back
here, and the cycle starts all over again.  Thus, under normal
circumstances, the cursor blinks three times per second.

### Reference (Joe Forster / STA)
Values:

* $00, 0: Must change cursor phase.
* $01-$14, 1-20: Delay.

### 64'er Magazin (64'er)
Das Blinken des Cursors besorgt die Interrupt-Routine. 60mal in jeder Sekunde
unterbricht sie den normalen Programmablauf. Während dieser Zeit führt sie
mehrere »Haushalt«-Arbeiten durch. So wird hier die Tastatur abgefragt und das
Cursorblinken gesteuert.

Dazu wird die Zahl 20 in die Speicherzelle 205 geschrieben und bei jeder
Unterbrechung dann um 1 reduziert. Wenn die Zahl in 205 den Wert 0 erreicht
hat, wird der Cursor eingeschaltet. Nach Adam Riese erfolgt das also 60/20 =
3mal pro Sekunde. Im Texteinschub Nr. 22 »Cursor-Spiele oder der INPUT-Befehl
einmal etwas anders« wird mit diesem Zähler für die Blinkfrequenz
experimentiert.

### 64map (—)
Timer: Count down for Cursor blink toggle

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00cd-blnct]]
