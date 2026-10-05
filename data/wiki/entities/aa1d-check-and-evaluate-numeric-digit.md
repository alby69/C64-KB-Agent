---
id: aa1d-check-and-evaluate-numeric-digit
type: entity
title: check and evaluate numeric digit
aliases:
- check and evaluate numeric digit
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aa1d-check-and-evaluate-numeric-digit.md
  sha256: 9a1fe3ad72ffd4f071a09c198fb5822e3b4ab20dfeb5253bf0fae4f34d879660
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-aa1d-check-and-evaluate-numeric-digit
---

# check and evaluate numeric digit



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

## References
- Source: [[src-aa1d-check-and-evaluate-numeric-digit]]
