---
title: scan and get byte parameter
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
- b79b-holt-byte-wert-nach-x
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B79B
  address_end: $B79B
  symbol: scan-and-get-byte-parameter
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B79B**: increment and scan memory'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B79B**: CHRGET nächstes Zeichen holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B79B — scan and get byte parameter

## Disassemblatura
```assembly
.B79B  20 73 00 JSR $0073   ; increment and scan memory
```


## Commenti

### Original Disassembly (—)
- **$B79B**: increment and scan memory

### Commodore-64-intern-Buch (Commodore)
- **$B79B**: CHRGET nächstes Zeichen holen
- **$B79E**: FRMNUM numerischen Wert nach FAC holen
- **$B7A1**: prüft auf Bereich und wandelt nach Integer
- **$B7A4**: HIGH-Byte
- **$B7A6**: ungleich null, dann 'ILLEGAL QUANTITY'
- **$B7A8**: LOW-Byte des geholten Ausdrucks ins X-Reg
- **$B7AA**: CHRGOT letztes Zeichen holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*