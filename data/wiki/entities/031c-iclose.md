---
id: 031c-iclose
type: entity
title: CLOSE vector ($F291)
aliases:
- CLOSE vector ($F291)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/031c-iclose.md
  sha256: e68f234ba1bc6a718359cf922bba8c9a9a06649ff8dc3b2bb903e9ed0dbf42f4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-031c-iclose
---

# CLOSE vector ($F291)



# ICLOSE — CLOSE vector ($F291) ($031C)

## Panoramica
Il registro o area di memoria ICLOSE è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$031C` (`796` decimale)
- **Range**: `$031C`-`$031D`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F291 CLOSE-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CLOSE Routine Vector

### Memory Map (Jim Butterfield)
CLOSE vector ($F291)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CLOSE Routine (Currently at 62097 ($F291))

### Reference (Joe Forster / STA)
Default: $F291.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf die Adresse 62097 ($F291) - beim VC 20 auf 62282
($F34A). Ab hier beginnt eine Routine, die beim CLOSE-Befehl zuerst prüft, ob
die Datei-Nummer in der Tabelle der eröffneten Datei enthalten ist. Dann holt
sie die dazugehörige Geräte-Nummer und Sekundär-Adresse und schließt den Kanal
und die Datei.

### 64map (—)
Vector: Indirect entry to Kernal CLOSE Routine ($F291)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-031c-iclose]]
