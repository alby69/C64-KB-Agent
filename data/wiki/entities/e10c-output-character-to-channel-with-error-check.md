---
id: e10c-output-character-to-channel-with-error-check
type: entity
title: output character to channel with error check
aliases:
- output character to channel with error check
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e10c-output-character-to-channel-with-error-check.md
  sha256: 788f185f7ed82f8f65094577ff967c748b8189a79e79a6d20aad53bb428e7dc6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e10c-output-character-to-channel-with-error-check
---

# output character to channel with error check



# $E10C — output character to channel with error check

## Disassemblatura
```assembly
.E10C  20 D2 FF JSR $FFD2   ; output character to channel
.E10F  B0 E8    BCS $E0F9   ; if error go handle BASIC I/O error
.E111  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E10C**: output character to channel
- **$E10F**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E10C**: ein Zeichen ausgeben
- **$E10F**: Fehler ?
- **$E111**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E10C**: output character in (A)
- **$E10F**: if carry set, handle I/O error
- **$E111**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e10c-output-character-to-channel-with-error-check]]
