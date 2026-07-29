---
title: copy I/O start address to buffer address
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
- fb8e-programmstart
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FB8E
  address_end: $FB96
  symbol: copy-io-start-address-to-buffer-address
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FB8E**: get I/O start address high byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FB8E**: Startadresse'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FB8E — copy I/O start address to buffer address

## Disassemblatura
```assembly
.FB8E  A5 C2    LDA $C2   ; get I/O start address high byte
.FB90  85 AD    STA $AD   ; set buffer address high byte
.FB92  A5 C1    LDA $C1   ; get I/O start address low byte
.FB94  85 AC    STA $AC   ; set buffer address low byte
.FB96  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FB8E**: get I/O start address high byte
- **$FB90**: set buffer address high byte
- **$FB92**: get I/O start address low byte
- **$FB94**: set buffer address low byte

### Commodore-64-intern-Buch (Commodore)
- **$FB8E**: Startadresse
- **$FB90**: $C1/$C2
- **$FB92**: nach $AC/$AD
- **$FB94**: speichern
- **$FB96**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*