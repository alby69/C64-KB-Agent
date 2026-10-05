---
id: 0095-bsour
type: entity
title: Serial deferred character
aliases:
- Serial deferred character
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0095-bsour.md
  sha256: fe78e2eaf4d7647d721a87ee496cc8bada4ca0b6fcdb92279c90a8654bd24ad5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0095-bsour
---

# Serial deferred character



# BSOUR — Serial deferred character ($0095)

## Panoramica
Il registro o area di memoria BSOUR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0095` (`149` decimale)
- **Range**: `$0095`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Char buffer for IEEE

### Commodore-64-intern-Buch (Commodore)
Hier wird das Zeichen abgelegt,
welches über den seriellen Port zur
Floppy oder zum Drucker geschickt
werden soll, sobald die Adresse $0094
Bereitschaft zeigt.

### C64 Programmer's Reference Guide (Commodore)
Buffered Character for Serial Bus

### Memory Map (Jim Butterfield)
Serial deferred character

### Mapping the Commodore 64 (Sheldon Leemon)
This is the character waiting to be sent.  A 255 ($FF) indicates that
no character is waiting for serial output.

### Reference (Joe Forster / STA)
Serial bus output cache, previous byte to be sent to serial bus

### 64'er Magazin (64'er)
In dieser Speicherzelle wird das Zeichen abgelegt, welches als nächstes über
den Serial-Port zum Floppy-Gerät oder zum Drucker transportiert wird, sobald
die Flagge in 148 die Bereitschaft anzeigt.

### 64map (—)
Buffered Character for Serial Bus

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0095-bsour]]
