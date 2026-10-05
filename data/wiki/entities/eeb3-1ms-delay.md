---
id: eeb3-1ms-delay
type: entity
title: 1ms delay
aliases:
- 1ms delay
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eeb3-1ms-delay.md
  sha256: 621a847bef771a5c2293e99719c9c9aed5c071cfea9b6530935015f860636f9b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-eeb3-1ms-delay
---

# 1ms delay



# $EEB3 — 1ms delay

## Disassemblatura
```assembly
.EEB3  8A       TXA   ; save X
.EEB4  A2 B8    LDX #$B8   ; set the loop count
.EEB6  CA       DEX   ; decrement the loop count
.EEB7  D0 FD    BNE $EEB6   ; loop if more to do
.EEB9  AA       TAX   ; restore X
.EEBA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEB3**: save X
- **$EEB4**: set the loop count
- **$EEB6**: decrement the loop count
- **$EEB7**: loop if more to do
- **$EEB9**: restore X

### Commodore-64-intern-Buch (Commodore)
- **$EEB3**: X-Register retten
- **$EEB4**: X-Register mit $B8 laden
- **$EEB6**: herunterzählen
- **$EEB7**: verzweige wenn nicht fertig
- **$EEB9**: X-Register wiederherstellen
- **$EEBA**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EEB3**: move (X) to (A)
- **$EEB4**: start value
- **$EEB6**: decrement
- **$EEB7**: until zero
- **$EEB9**: (A) to (X)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-eeb3-1ms-delay]]
