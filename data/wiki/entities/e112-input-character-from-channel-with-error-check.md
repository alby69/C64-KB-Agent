---
id: e112-input-character-from-channel-with-error-check
type: entity
title: input character from channel with error check
aliases:
- input character from channel with error check
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e112-input-character-from-channel-with-error-check.md
  sha256: a5e8ccb37e4235a29dcdbad84ee085af0295c21017fbdacc9d44939917ac69f7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e112-input-character-from-channel-with-error-check
---

# input character from channel with error check



# $E112 — input character from channel with error check

## Disassemblatura
```assembly
.E112  20 CF FF JSR $FFCF   ; input character from channel
.E115  B0 E2    BCS $E0F9   ; if error go handle BASIC I/O error
.E117  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E112**: input character from channel
- **$E115**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E112**: ein Zeichen holen
- **$E115**: Fehler ?
- **$E117**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E112**: input character from CHRIN
- **$E115**: if carry set, handle I/O error
- **$E117**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e112-input-character-from-channel-with-error-check]]
