---
id: e124-get-character-from-input-device-with-error-check
type: entity
title: get character from input device with error check
aliases:
- get character from input device with error check
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e124-get-character-from-input-device-with-error-check.md
  sha256: 140b403cb1067139b0224d652c5efb4d50869489c138935a0659df4b562af62a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e124-get-character-from-input-device-with-error-check
---

# get character from input device with error check



# $E124 — get character from input device with error check

## Disassemblatura
```assembly
.E124  20 E4 FF JSR $FFE4   ; get character from input device
.E127  B0 D0    BCS $E0F9   ; if error go handle BASIC I/O error
.E129  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E124**: get character from input device
- **$E127**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E124**: ein Zeichen holen
- **$E127**: Fehler ?
- **$E129**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E124**: GETIN, get character from keyboard buffer
- **$E127**: if carry set, handle I/O error
- **$E129**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e124-get-character-from-input-device-with-error-check]]
