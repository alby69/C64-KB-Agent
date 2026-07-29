---
title: pack FAC1 into variable pointer
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bbd0-fac-nach-variable-bertragen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BBD0
  address_end: $BBD2
  symbol: pack-fac1-into-variable-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BBD0**: get destination pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BBD0**: Variablenadresse'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $BBD0 — pack FAC1 into variable pointer

## Disassemblatura
```assembly
.BBD0  A6 49    LDX $49   ; get destination pointer low byte
.BBD2  A4 4A    LDY $4A   ; get destination pointer high byte
```


## Commenti

### Original Disassembly (—)
- **$BBD0**: get destination pointer low byte
- **$BBD2**: get destination pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$BBD0**: Variablenadresse
- **$BBD2**: holen
- **$BBD4**: FAC runden
- **$BBD7**: Zeiger auf
- **$BBD9**: Zieladresse
- **$BBDB**: Zähler setzen
- **$BBDD**: LOW-Byte der Mantisse
- **$BBDF**: Den
- **$BBE1**: FAC
- **$BBE2**: in
- **$BBE4**: den
- **$BBE6**: Ziel-
- **$BBE7**: bereich
- **$BBE9**: über-
- **$BBEB**: tragen
- **$BBEC**: FAC-Vorzeichen
- **$BBEE**: Die Bits 0 bis 6 setzen
- **$BBF0**: Vorzeichen auf
- **$BBF2**: Speicherformat
- **$BBF4**: bringen
- **$BBF5**: FAC-Exponent
- **$BBF7**: übertragen
- **$BBF9**: FAC-Rundungsstelle löschen
- **$BBFB**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*