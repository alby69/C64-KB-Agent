---
id: b77c-perform-len
type: entity
title: perform LEN()
aliases:
- perform LEN()
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b77c-perform-len.md
  sha256: 8b7bffb0eafd85c609951528d1f273508971739af9fc7db17a31d2a81deba800
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b77c-perform-len
---

# perform LEN()



# $B77C — perform LEN()

## Disassemblatura
```assembly
.B77C  20 82 B7 JSR $B782   ; evaluate string, get length in A (and Y)
.B77F  4C A2 B3 JMP $B3A2   ; convert Y to byte in FAC1 and return
```


## Commenti

### Original Disassembly (—)
- **$B77C**: evaluate string, get length in A (and Y)
- **$B77F**: convert Y to byte in FAC1 and return

### Commodore-64-intern-Buch (Commodore)
- **$B77C**: FRESTR, Stringlänge holen
- **$B77F**: Byte-Wert nach Fließkommaformat wandeln

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B77C**: GET LENTGH IN Y-REG, MAKE FAC NUMERIC
- **$B77F**: FLOAT Y-REG INTO FAC IF LAST RESULT IS A TEMPORARY STRING, FREE IT MAKE VALTYP NUMERIC, RETURN LENGTH IN Y-REG
- **$B782**: IF LAST RESULT IS A STRING, FREE IT
- **$B785**: MAKE VALTYP NUMERIC
- **$B789**: LENGTH OF STRING TO Y-REG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b77c-perform-len]]
