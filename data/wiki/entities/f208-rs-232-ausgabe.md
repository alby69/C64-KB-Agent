---
id: f208-rs-232-ausgabe
type: entity
title: RS-232 Ausgabe
aliases:
- RS-232 Ausgabe
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f208-rs-232-ausgabe.md
  sha256: b59e60a8be6c62e252ab40c76438996cbed8ac9c3efb7598c968e10e9b2f5d9b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f208-rs-232-ausgabe
---

# RS-232 Ausgabe



# $F208 — RS-232 Ausgabe

## Disassemblatura
```assembly
.F208  20 17 F0 JSR $F017   ; ein Zeichen in RS-232 Puffer schreiben
.F20B  4C FC F1 JMP $F1FC   ; CHROUT
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F208**: ein Zeichen in RS-232 Puffer schreiben
- **$F20B**: CHROUT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f208-rs-232-ausgabe]]
