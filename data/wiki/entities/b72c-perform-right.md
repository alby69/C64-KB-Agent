---
id: b72c-perform-right
type: entity
title: perform RIGHT$()
aliases:
- perform RIGHT$()
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b72c-perform-right.md
  sha256: c574d54b45daa85b479f3d377a2293a27f80cf128574fc2d8c159a777e8c0f0f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b72c-perform-right
---

# perform RIGHT$()



# $B72C — perform RIGHT$()

## Disassemblatura
```assembly
.B72C  20 61 B7 JSR $B761   ; pull string data and byte parameter from stack return pointer in descriptor, byte in A (and X), Y=0
.B72F  18       CLC   ; clear carry for add-1
.B730  F1 50    SBC ($50),Y   ; subtract string length
.B732  49 FF    EOR #$FF   ; invert it (A=LEN(expression$)-l)
.B734  4C 06 B7 JMP $B706   ; go do rest of LEFT$()
```


## Commenti

### Original Disassembly (—)
- **$B72C**: pull string data and byte parameter from stack return pointer in descriptor, byte in A (and X), Y=0
- **$B72F**: clear carry for add-1
- **$B730**: subtract string length
- **$B732**: invert it (A=LEN(expression$)-l)
- **$B734**: go do rest of LEFT$()

### Commodore-64-intern-Buch (Commodore)
- **$B72C**: Stringparameter und Länge vom Stack holen
- **$B72F**: von Stringlänge
- **$B730**: abziehen
- **$B732**: Nummer des ersten Elements im alten String
- **$B734**: weiter wie LEFT$

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B72F**: COMPUTE LENGTH-WIDTH OF SUBSTRING
- **$B730**: TO GET STARTING POINT IN STRING
- **$B734**: JOIN LEFT$

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b72c-perform-right]]
