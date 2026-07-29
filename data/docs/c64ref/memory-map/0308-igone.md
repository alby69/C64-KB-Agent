---
title: Start new Basic code link
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
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
  address: $0308
  address_end: $0309
  symbol: IGONE
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: indirect GONE (char dispatch)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $A7E4 Vektor für BASIC-Befehlsadresse holen
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: BASIC Char. Dispatch'
  - name: Memory Map
    author: Jim Butterfield
    description: Start new Basic code link
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the GONE routine at 42980 ($A7E4)
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $A7E4.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf die Adresse 42980 ($A7E4), beim VC 20 auf
      51172
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to BASIC Character dispatch Routine ($A7E4)'
---

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