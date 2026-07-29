---
title: Pointer to screen line
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $00D1
  address_end: $00D2
  symbol: PNT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Pointer to row
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In diesen Speicherzellen wird in LOW-
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Current Screen Line Address'
  - name: Memory Map
    author: Jim Butterfield
    description: Pointer to screen line
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the address in screen RAM of the first column
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to current line in screen memory
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Zeiger in Low-/High-Byte-Darstellung zeigt auf die Adresse
      im
  - name: 64map
    author: —
    description: 'Pointer: Current Screen Line Address'
---

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