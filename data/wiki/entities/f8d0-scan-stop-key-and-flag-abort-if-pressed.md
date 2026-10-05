---
id: f8d0-scan-stop-key-and-flag-abort-if-pressed
type: entity
title: scan stop key and flag abort if pressed
aliases:
- scan stop key and flag abort if pressed
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f8d0-scan-stop-key-and-flag-abort-if-pressed.md
  sha256: bb352d8b5a991bd22a5e1a396efacae0e5d012d5dad84aa78f04fed3926f3fd4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f8d0-scan-stop-key-and-flag-abort-if-pressed
---

# scan stop key and flag abort if pressed



# $F8D0 — scan stop key and flag abort if pressed

## Disassemblatura
```assembly
.F8D0  20 E1 FF JSR $FFE1   ; scan stop key
.F8D3  18       CLC   ; flag no stop
.F8D4  D0 0B    BNE $F8E1   ; exit if no stop
.F8D6  20 93 FC JSR $FC93   ; restore everything for STOP
.F8D9  38       SEC   ; flag stopped
.F8DA  68       PLA   ; dump return address low byte
.F8DB  68       PLA   ; dump return address high byte
```


## Commenti

### Original Disassembly (—)
- **$F8D0**: scan stop key
- **$F8D3**: flag no stop
- **$F8D4**: exit if no stop
- **$F8D6**: restore everything for STOP
- **$F8D9**: flag stopped
- **$F8DA**: dump return address low byte
- **$F8DB**: dump return address high byte

### Commodore-64-intern-Buch (Commodore)
- **$F8D0**: Stop-Taste abfragen
- **$F8D3**: Carry =0 (ok Kennzeichen)
- **$F8D4**: verzweige wenn Taste nein gedrückt
- **$F8D6**: Band-Motor aus, normalen IRQ wiederherstellen
- **$F8D9**: Kennzeichen für Abbruch
- **$F8DA**: Rücksprung
- **$F8DB**: Adresse löschen
- **$F8DC**: Kennzeichen für normalen
- **$F8DE**: IRQ setzen
- **$F8E1**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f8d0-scan-stop-key-and-flag-abort-if-pressed]]
