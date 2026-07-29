---
title: scan stop key and flag abort if pressed
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f8d0-testet-auf-stop-taste
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F8D0
  address_end: $F8DB
  symbol: scan-stop-key-and-flag-abort-if-pressed
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F8D0**: scan stop key'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F8D0**: Stop-Taste abfragen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

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