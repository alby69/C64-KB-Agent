---
title: INPUT vector ($F157)
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
related:
- f157-zeichens
- input
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
  address: $0324
  address_end: $0325
  symbol: IBASIN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F157 INPUT-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL CHRIN Routine
  - name: Memory Map
    author: Jim Butterfield
    description: INPUT vector ($F157)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Vector to Kernal CHRIN Routine (Currently at 61783 ($F157))
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F157.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf die Adresse 61783 ($F157) - beim VC 20 auf
      61966
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal CHRIN Routine ($F157)'
---

# IBASIN — INPUT vector ($F157) ($0324)

## Panoramica
Il registro o area di memoria IBASIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0324` (`804` decimale)
- **Range**: `$0324`-`$0325`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F157 INPUT-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CHRIN Routine

### Memory Map (Jim Butterfield)
INPUT vector ($F157)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CHRIN Routine (Currently at 61783 ($F157))

### Reference (Joe Forster / STA)
Default: $F157.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 61783 ($F157) - beim VC 20 auf 61966
($F20E). Die hier beginnende Routine, deren Abkürzung »Character Input«
bedeutet, holt das jeweils nächste Byte vom Eingabepuffer des angewählten
Gerätes, sofern ein solcher eingerichtet ist (zum Beispiel Kassettenpuffer,
RS232-Puffer).

Bei Eingabe von der Tastatur holt diese Routine so lange Bytes aus dem
Tastaturpuffer und zeigt sie auf dem Bildschirm an, bis das Zeichen für ein
ungeSHIFTetes RETURN auftritt. Erst dann gibt die Routine das erste Zeichen der
logischen Zeile auf dem Bildschirm an den Basic-Übersetzer weiter.

### 64map (—)
Vector: Indirect entry to Kernal CHRIN Routine ($F157)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*