---
id: 0308-igone
type: entity
title: Start new Basic code link
aliases:
- Start new Basic code link
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0308-igone.md
  sha256: 32330a047f8d7cfa9aabeadb7d772677ffba521f576eef20817a96891e50497b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0308-igone
---

# Start new Basic code link



# IGONE — Start new Basic code link ($0308)

## Panoramica
Il registro o area di memoria IGONE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0308` (`776` decimale)
- **Range**: `$0308`-`$0309`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
indirect GONE (char dispatch)

### Commodore-64-intern-Buch (Commodore)
$A7E4 Vektor für BASIC-Befehlsadresse holen

### C64 Programmer's Reference Guide (Commodore)
Vector: BASIC Char. Dispatch

### Memory Map (Jim Butterfield)
Start new Basic code link

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the GONE routine at 42980 ($A7E4)
that executes the next program token.

### Reference (Joe Forster / STA)
Default: $A7E4.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 42980 ($A7E4), beim VC 20 auf 51172
($C7E4). Diese Routine prüft das nächste Token, ob es gültig ist. Wenn der
ASCII-Wert des Token kleiner als 128 ist, wird er als Zeichen einerVariablen
angesehen, und das System springt auf die LET-Routine. Das erklärt, warum zur
Definition einer Variablen der LET-Befehl auch weggelassen werden kann.

Durch Verbiegen dieses Vektors kann zum Beispiel eine Trace-Routine gebaut
werden, welche zuerst die Nummer der Zeile ausdruckt, die gerade ausgeführt
wird, bevor sie auf die ursprüngliche Zieladresse des Vektors zurückkehrt.

### 64map (—)
Vector: Indirect entry to BASIC Character dispatch Routine ($A7E4)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0308-igone]]
