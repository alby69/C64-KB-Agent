---
title: set filename
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
- fdf9-parameter-f-filenamen-setzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FDF9
  address_end: $FDFF
  symbol: set-filename
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FDF9**: set file name length'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FDF9**: Länge speichern'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FDF9**: store length of filename in FNLEN'
---

# $FDF9 — set filename

## Disassemblatura
```assembly
.FDF9  85 B7    STA $B7   ; set file name length
.FDFB  86 BB    STX $BB   ; set file name pointer low byte
.FDFD  84 BC    STY $BC   ; set file name pointer high byte
.FDFF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FDF9**: set file name length
- **$FDFB**: set file name pointer low byte
- **$FDFD**: set file name pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$FDF9**: Länge speichern
- **$FDFB**: Adresse-LOW speichern
- **$FDFD**: Adresse-HIGH speichern
- **$FDFF**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FDF9**: store length of filename in FNLEN
- **$FDFB**: store pointer to filename in FNADDR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*