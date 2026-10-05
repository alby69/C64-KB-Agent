---
id: fdf9-set-filename
type: entity
title: set filename
aliases:
- set filename
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fdf9-set-filename.md
  sha256: d8b86ddb6d06394154fb62981098549c905da8715c08d3e1f774a341d505ef59
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fdf9-set-filename
---

# set filename



# $FDF9 — set filename

## Disassemblatura
```assembly
.FDF9  85 B7    STA $B7   ; set file name length
.FDFB  86 BB    STX $BB   ; set file name pointer low byte
.FDFD  84 BC    STY $BC   ; set file name pointer high byte
.FDFF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FDF9**: set file name length
- **$FDFB**: set file name pointer low byte
- **$FDFD**: set file name pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$FDF9**: Länge speichern
- **$FDFB**: Adresse-LOW speichern
- **$FDFD**: Adresse-HIGH speichern
- **$FDFF**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FDF9**: store length of filename in FNLEN
- **$FDFB**: store pointer to filename in FNADDR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fdf9-set-filename]]
