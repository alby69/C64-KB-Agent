---
id: 00aa-ridata
type: entity
title: Tp Scan; Cnt; Ld; End/byte assy
aliases:
- Tp Scan; Cnt; Ld; End/byte assy
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00aa-ridata.md
  sha256: bafa1d2998a6adb42e3ab725479e2f65ed3b97ad0067ae42598fe7fa71769e3c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00aa-ridata
---

# Tp Scan; Cnt; Ld; End/byte assy



# RIDATA — Tp Scan; Cnt; Ld; End/byte assy ($00AA)

## Panoramica
Il registro o area di memoria RIDATA è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00AA` (`170` decimale)
- **Range**: `$00AA`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr byte buffer

### Original Source Comments (Microsoft/Commodore)
MI - waiting for block SYNC
VS - in data block reading data
NE - waiting for byte SYNC

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Byte Buffer/Cassette Temp

### Memory Map (Jim Butterfield)
Tp Scan; Cnt; Ld; End/byte assy

### Mapping the Commodore 64 (Sheldon Leemon)
Serial routines use this area to reassemble the bits received into a
byte that will be stored in the receiving buffer pointed to by 247
($00F7).  Tape routines use this as a flag to help determine whether a
received character should be treated as data or as a synchronization
character.

### Reference (Joe Forster / STA)
Byte buffer during RS232 input

### 64'er Magazin (64'er)
Bei der Speicherzelle 165 haben wir gesehen, daß ein Band Synchronisationsbits
enthält. Die Speicherzelle 170 wird dabei als Flagge benutzt, die angibt, ob
ein gelesenes Zeichen Synchronisierungs-Bits oder ein Datenwort darstellt.

Die RS232-Routinen verwenden Zelle 17 0 dagegen als Speicher, in welchem die
eingelesenen Bits zu einem Byte zusammengefaßt werden, bevor sie im
Eingabepuffer am oberen Ende des Programmspeichers abgelegt werden (siehe auch
Speicherzellen 55/56).

### 64map (—)
RS232 Input Byte Buffer/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00aa-ridata]]
