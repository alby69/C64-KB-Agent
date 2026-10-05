---
id: 00a8-bitci
type: entity
title: Tp Wrt new byte/Rd error/inbit cnt
aliases:
- Tp Wrt new byte/Rd error/inbit cnt
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00a8-bitci.md
  sha256: e0c18aca8dee8f4c8dab71dc59df22314f4905a0fd2e966e967c23351e0d3d34
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00a8-bitci
---

# Tp Wrt new byte/Rd error/inbit cnt



# BITCI — Tp Wrt new byte/Rd error/inbit cnt ($00A8)

## Panoramica
Il registro o area di memoria BITCI è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00A8` (`168` decimale)
- **Range**: `$00A8`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RS-232 rcvr bit count in

### Original Source Comments (Microsoft/Commodore)
Cassette: flags errors (if Z then no error)

### C64 Programmer's Reference Guide (Commodore)
RS-232 Input Bit Count / Cassette Temp

### Memory Map (Jim Butterfield)
Tp Wrt new byte/Rd error/inbit cnt

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to count the number of bits of serial data that
has been received.  This is necessary so that the serial routines will
know when a full word has been received.  It is also used as an error
flag during tape loads.

### Reference (Joe Forster / STA)
Bit counter during RS232 input

### 64'er Magazin (64'er)
Die Speicherzelle 168 wird als Zähler verwendet, der dies mal nicht die Bytes,
sondern die Anzahl der Bits zählt, die sowohl über den User-Port als auch über
den Kassetten-Port geleitet werden. Das dient dem Betriebssystem dazu, zu
wissen, wann ein volles Wort abgearbeitet worden ist.

### 64map (—)
RS232 Input Bit count/Tape temporary

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00a8-bitci]]
