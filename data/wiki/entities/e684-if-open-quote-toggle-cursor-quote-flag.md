---
id: e684-if-open-quote-toggle-cursor-quote-flag
type: entity
title: if open quote toggle cursor quote flag
aliases:
- if open quote toggle cursor quote flag
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e684-if-open-quote-toggle-cursor-quote-flag.md
  sha256: 70e3afbbc08520fcec480305d0ac5bcc64a296f2d1e5176936a06394a4654dc4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e684-if-open-quote-toggle-cursor-quote-flag
---

# if open quote toggle cursor quote flag



# $E684 — if open quote toggle cursor quote flag

## Disassemblatura
```assembly
.E684  C9 22    CMP #$22   ; comapre byte with "
.E686  D0 08    BNE $E690   ; exit if not "
.E688  A5 D4    LDA $D4   ; get cursor quote flag, $xx = quote, $00 = no quote
.E68A  49 01    EOR #$01   ; toggle it
.E68C  85 D4    STA $D4   ; save cursor quote flag
.E68E  A9 22    LDA #$22   ; restore the "
.E690  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E684**: comapre byte with "
- **$E686**: exit if not "
- **$E688**: get cursor quote flag, $xx = quote, $00 = no quote
- **$E68A**: toggle it
- **$E68C**: save cursor quote flag
- **$E68E**: restore the "

### Commodore-64-intern-Buch (Commodore)
- **$E684**: '"' ?
- **$E686**: nein ?, dann fertig
- **$E688**: Hochkomma-
- **$E68A**: Flag
- **$E68C**: umdrehen
- **$E68E**: Hochkomma-Code wieder- herstellen
- **$E690**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E684**: quote mark
- **$E68E**: quote mark

### Magnus Nyman (Magnus Nyman)
- **$E684**: ASCII quotes (")
- **$E686**: nope, return
- **$E688**: QTSW, quotes mode flag
- **$E68A**: toggle on/off
- **$E68C**: store
- **$E68E**: restore (A) to #$22

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e684-if-open-quote-toggle-cursor-quote-flag]]
