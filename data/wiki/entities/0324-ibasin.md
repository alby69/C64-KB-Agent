---
id: 0324-ibasin
type: entity
title: INPUT vector ($F157)
aliases:
- INPUT vector ($F157)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0324-ibasin.md
  sha256: ea4a304eb0724b3a889e63040fbb4f1364b54f3ef35c947d21a5db39e7aafe2f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0324-ibasin
---

# INPUT vector ($F157)



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

## References
- Source: [[src-0324-ibasin]]
