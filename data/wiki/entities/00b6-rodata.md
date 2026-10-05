---
id: 00b6-rodata
type: entity
title: Read character error/outbyte buf
aliases:
- Read character error/outbyte buf
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00b6-rodata.md
  sha256: 826575c1db49c34bc1159887aafff1678db978de19a911fc60fb3a35a4ef256a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00b6-rodata
---

# Read character error/outbyte buf



# RODATA — Read character error/outbyte buf ($00B6)

## Panoramica
Il registro o area di memoria RODATA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00B6` (`182` decimale)
- **Range**: `$00B6`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 trns byte buffer

### Original Source Comments (Microsoft/Commodore)
Cassette: has combined error values from bit routines

### Commodore-64-intern-Buch (Commodore)
Dieses Register wird als Ausgabezwischenspeicher
benutzt.

### C64 Programmer's Reference Guide (Commodore)
RS-232 Out Byte Buffer

### Memory Map (Jim Butterfield)
Read character error/outbyte buf

### Mapping the Commodore 64 (Sheldon Leemon)
RS-232 routines use this area to disassemble each byte to be sent from
the transmission buffer pointed to by 249 ($00F9).

### Reference (Joe Forster / STA)
Byte buffer during RS232 output

### 64'er Magazin (64'er)
Bei Ausgabe von Daten über die RS232-Schnittstelle wird jedes Byte in seine
Einzelteile zerlegt, bevor es über den Ausgabepuffer seriell übertragen wird.
DerAusgabepufferwird im obersten Teil des Programmspeichers angelegt (siehe
auch Speicherzellen 55 und 56); die genaue Anfangsadresse steht in
Speicherzelle 248. Auch die Ausgabe von Daten auf die Kassette verwendet Zelle
182 als Ausgabe-Zwischenspeicher.

### 64map (—)
RS232 Output Byte Buffer/Tape Read Error Flag

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00b6-rodata]]
