---
id: fe18-control-kernal-messages
type: entity
title: control kernal messages
aliases:
- control kernal messages
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe18-control-kernal-messages.md
  sha256: 72105d51a19081e501955c145af6fa45b8f87af8b6b5322f1c8b03ae83340a73
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe18-control-kernal-messages
---

# control kernal messages



# $FE18 — control kernal messages

## Disassemblatura
```assembly
.FE18  85 9D    STA $9D   ; set message mode flag
.FE1A  A5 90    LDA $90   ; read the serial status byte
```


## Commenti

### Original Disassembly (—)
- **$FE18**: set message mode flag
- **$FE1A**: read the serial status byte

### Commodore-64-intern-Buch (Commodore)
- **$FE18**: Ausgabeflag (Direktmodus)
- **$FE1A**: Statusflag holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE18**: store MSGFLG
- **$FE1A**: read STATUS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fe18-control-kernal-messages]]
