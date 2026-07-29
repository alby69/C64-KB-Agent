---
title: check and evaluate numeric digit
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- aa1d-zeichen-auf-ziffer-prfen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AA1D
  address_end: $AA29
  symbol: check-and-evaluate-numeric-digit
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AA1D**: get byte from string'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AA1D**: Zeichen holen (aus String)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $AA1D — check and evaluate numeric digit

## Disassemblatura
```assembly
.AA1D  B1 22    LDA ($22),Y   ; get byte from string
.AA1F  20 80 00 JSR $0080   ; clear Cb if numeric. this call should be to $84 as the code from $80 first compares the byte with [SPACE] and does a BASIC increment and get if it is
.AA22  90 03    BCC $AA27   ; branch if numeric
.AA24  4C 48 B2 JMP $B248   ; do illegal quantity error then warm start
.AA27  E9 2F    SBC #$2F   ; subtract $2F + carry to convert ASCII to binary
.AA29  4C 7E BD JMP $BD7E   ; evaluate new ASCII digit and return
```


## Commenti

### Original Disassembly (—)
- **$AA1D**: get byte from string
- **$AA1F**: clear Cb if numeric. this call should be to $84 as the code from $80 first compares the byte with [SPACE] and does a BASIC increment and get if it is
- **$AA22**: branch if numeric
- **$AA24**: do illegal quantity error then warm start
- **$AA27**: subtract $2F + carry to convert ASCII to binary
- **$AA29**: evaluate new ASCII digit and return

### Commodore-64-intern-Buch (Commodore)
- **$AA1D**: Zeichen holen (aus String)
- **$AA1F**: auf Ziffer prüfen
- **$AA22**: Ziffer: $AA27
- **$AA24**: sonst: 'illegal quantity'
- **$AA27**: von ASCII nach HEX umwandeln
- **$AA29**: in FAC und ARG übertragen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*