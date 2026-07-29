---
title: open channel for output
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
- e4ad-basic-ckout-routine
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E4AD
  address_end: $E4B6
  symbol: open-channel-for-output
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E4AD**: save the flag byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E4AD**: Akkuinhalt in Stack'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E4AD**: temp store (A)'
---

# $E4AD — open channel for output

## Disassemblatura
```assembly
.E4AD  48       PHA   ; save the flag byte
.E4AE  20 C9 FF JSR $FFC9   ; open channel for output
.E4B1  AA       TAX   ; copy the returned flag byte
.E4B2  68       PLA   ; restore the calling flag byte
.E4B3  90 01    BCC $E4B6   ; if there is no error skip copying the error flag
.E4B5  8A       TXA   ; else copy the error flag
.E4B6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E4AD**: save the flag byte
- **$E4AE**: open channel for output
- **$E4B1**: copy the returned flag byte
- **$E4B2**: restore the calling flag byte
- **$E4B3**: if there is no error skip copying the error flag
- **$E4B5**: else copy the error flag

### Commodore-64-intern-Buch (Commodore)
- **$E4AD**: Akkuinhalt in Stack
- **$E4AE**: CKOUT Ausgabegerät setzen
- **$E4B1**: Fehlernummer nach X
- **$E4B2**: Akkuinhalt zurückholen
- **$E4B3**: kein Fehler ?
- **$E4B5**: Fehlernummer wieder in Akku
- **$E4B6**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E4AD**: temp store (A)
- **$E4AE**: CHKOUT
- **$E4B2**: retrieve (A)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*