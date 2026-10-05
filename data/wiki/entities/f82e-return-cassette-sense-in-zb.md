---
id: f82e-return-cassette-sense-in-zb
type: entity
title: return cassette sense in Zb
aliases:
- return cassette sense in Zb
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f82e-return-cassette-sense-in-zb.md
  sha256: 27ea403da9cd892e6daa30ca8f02b43bbf1ab0ff2923c35547371c9d0c62c1f8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f82e-return-cassette-sense-in-zb
---

# return cassette sense in Zb



# $F82E — return cassette sense in Zb

## Disassemblatura
```assembly
.F82E  A9 10    LDA #$10   ; set the mask for the cassette switch
.F830  24 01    BIT $01   ; test the 6510 I/O port
.F832  D0 02    BNE $F836   ; branch if cassette sense high
.F834  24 01    BIT $01   ; test the 6510 I/O port
.F836  18       CLC
.F837  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F82E**: set the mask for the cassette switch
- **$F830**: test the 6510 I/O port
- **$F832**: branch if cassette sense high
- **$F834**: test the 6510 I/O port

### Commodore-64-intern-Buch (Commodore)
- **$F82E**: Bit 4 testen
- **$F830**: mit Port vergleichen
- **$F832**: verzweige wenn Bandtaste nicht gedrückt
- **$F834**: nochmal abfragen (Entprellen)
- **$F836**: Carry =0 (ok Kennzeichen)
- **$F837**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f82e-return-cassette-sense-in-zb]]
