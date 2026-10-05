---
id: e4ad-open-channel-for-output
type: entity
title: open channel for output
aliases:
- open channel for output
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e4ad-open-channel-for-output.md
  sha256: 7f261316100a449ef7657ed2de32942129231e7bd25f8cab200aff92b471747d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e4ad-open-channel-for-output
---

# open channel for output



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

## References
- Source: [[src-e4ad-open-channel-for-output]]
