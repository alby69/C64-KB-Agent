---
id: 00d1-pnt
type: entity
title: Pointer to screen line
aliases:
- Pointer to screen line
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00d1-pnt.md
  sha256: 8c5d5eda7b84718d38fb11baabc53d34d763163649ac3a88d9b3f05abf93aef4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00d1-pnt
---

# Pointer to screen line



# PNT — Pointer to screen line ($00D1)

## Panoramica
Il registro o area di memoria PNT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D1` (`209` decimale)
- **Range**: `$00D1`-`$00D2`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer to row

### Commodore-64-intern-Buch (Commodore)
In diesen Speicherzellen wird in LOW-
und HIGH-Byte-Darstellung angezeigt,
wo sich im Video-RAM die Zeile befindet,
auf der der Cursor gerade
steht.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Current Screen Line Address

### Memory Map (Jim Butterfield)
Pointer to screen line

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address in screen RAM of the first column
of the logical line upon which the cursor is currently positioned.

### Reference (Joe Forster / STA)
Pointer to current line in screen memory

### 64'er Magazin (64'er)
Dieser Zeiger in Low-/High-Byte-Darstellung zeigt auf die Adresse im
Bildschirmspeicher, in welcher diejenige Zeile beginnt, auf der der Cursor
gerade steht. Das läßt sich leicht nachprüfen durch folgende Programmzeile:

    10 PRINT CHR$(147) PEEK(209) PEEK(210)

Nach RUN wird erst der Bildschirm gelöscht, der Cursor in die HOME-Position
gebracht und dann der Inhalt der beiden Zellen ausgedruckt. Da dies alles in
der ersten Zeile passiert, sehen wir als Resultat eine 0 und eine 4. Die beiden
Zahlen ergeben zusammen die Adresse, in der die erste Zeile des
Bildschirmspeichers beginnt. Erweitern Sie die Zeile 10 um ein Komma und die
Low-/High-Byte-Berechnung:

    10 PRINT CHR$(147) PEEK(209) PEEK(210), PEEK(209)+256*PEEK(210)

Jetzt sehen wir als Resultat:

    0 4 1024

Beim VC 20 erscheinen die der verwendeten Speichererweiterung entsprechenden
Zahlen. Wir können durch einen TAB-Befehl den zweiten Teil der PRINT-Anweisung
in die nächste Zeile schieben und sehen, was dann herauskommt:

    20 PRINT PEEK(209) PEEK (210),TAB(50) PEEK(209)+ 256*PEEK(210)

Das Resultat ist jetzt:

    0      4       1024
    40     4       1104

Einen entsprechenden Zeiger für die Adresse der dazugehörigen Zeile im
Farbspeicher werden wir in den Speicherzellen 243 und 244 antreffen. Durch
POKEn können wir die Cursorposition leider nicht beeinflussen, aber Abfragen
geht, wenn es uns interessiert.

### 64map (—)
Pointer: Current Screen Line Address

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00d1-pnt]]
