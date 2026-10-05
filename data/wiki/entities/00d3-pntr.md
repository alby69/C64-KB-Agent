---
id: 00d3-pntr
type: entity
title: Position of cursor on above line
aliases:
- Position of cursor on above line
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00d3-pntr.md
  sha256: 8a302932050ff251b0fcae2995157c3bbc29154c9629aee1ed11fb9c0a2ca9c7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00d3-pntr
---

# Position of cursor on above line



# PNTR — Position of cursor on above line ($00D3)

## Panoramica
Il registro o area di memoria PNTR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D3` (`211` decimale)
- **Range**: `$00D3`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer to column

### Commodore-64-intern-Buch (Commodore)
Hier wird die Spaltenposition des
Cursors festgehalten.

### C64 Programmer's Reference Guide (Commodore)
Cursor Column on Current Line

### Memory Map (Jim Butterfield)
Position of cursor on above line

### Mapping the Commodore 64 (Sheldon Leemon)
The number contained here is the cursor column position within the
logical line pointed to by 209 ($00D1).  Since a logical line can
contain up to two physical lines, this value may be from 0 to 79 (the
number here is the value returned by the POS function).

### Reference (Joe Forster / STA)
Current cursor column. Values: $00-$27, 0-39

### 64'er Magazin (64'er)
Den Inhalt der Speicherzelle 211 könnte man auch die Spaltenposition des
Cursors nennen, wenn es sich nicht um die Position in der logischen Zeile
handelte (siehe Texteinschub Nr. 23). Beim C 64 sind daher die Werte von 0 bis
79, beim VC 20 von 0 bis 87 möglich.

Diese Speicherzelle zusammen mit Zelle 214 wird von den Befehlen POS, TAB, SPC
und vom Komma innerhalb einer PRINT-Anweisung verwendet, um den Cursor zu
positionieren. Das können wir auch. Um den Cursor auf Platz 5 in der
Bildschirmzeile 18 zu bringen, geben wir folgende Programmzeile ein:

    10 POKE 214,17: PRINT: POKE 211,5:PRINT"C64"

Aus innerbetrieblichen Gründen muß der Wert, den wir als Zeile erzielen wollen,
um 1 verringert in die Zelle 214 gePOKEt werden. Mit der Zahl 17 wird also der
Cursor zuerst auf die Zeile 18 gebracht, dann in Spalte 5, ab der dann das Wort
»C 64« gedruckt wird. Auf diese Weise erhalten wir einen Befehl, der in anderen
Basic-Formen unter dem Namen PRINT AT sehr verbreitet ist, der bei den kleinen
Commodore-Computern aber fehlt.

Der Vorgang dabei besteht darin, daß die Inhalte von 211 und 214 in das X-
Register beziehungsweise in das Y-Register des Mikroprozessors gebracht werden.
Von dort können die Werte dann von einer Routine des Betriebssystems abgerufen
werden. Das klingt alles sehr nach Maschinensprache. Aber wir haben Glück, denn
sowohl die beiden Register als auch die besagte Routine sind von Basic aus
ansprechbar. Das X-Register steht in Speicherzelle 781, das Y-Register in
Speicherzelle 782, die Routine beginnt sowohl beim C 64 als auch beim VC 20 ab
der Adresse 68634, wo wir sie mit dem SYS-Befehl starten können.

Für unser Beispiel sieht das dann so aus:

    10 POKE 781,18:POKE 782,5: SYS 58634:PRINT"C 64"

Wir erhalten dasselbe Ergebnis, nur mit dem Unterschied, daß die Zeile jetzt
wirklich die Zeile 18 ist. Mit dieser Methode ist jetzt auch die Zeile 0
erreichbar.

Die Speicherzellen 781 und 782 bieten natürlich noch andere Anwendungen, auf
die wir noch kommen werden.

### 64map (—)
Cursor Column on current Line, including Wrap-round Line, if any

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00d3-pntr]]
