---
id: bc39-perform-sgn
type: entity
title: perform SGN()
aliases:
- perform SGN()
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc39-perform-sgn.md
  sha256: bf7cb277434eebcffa803786ae7224587e549eeb0281b614480f5cb6550db8f5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bc39-perform-sgn
---

# perform SGN()



# $BC39 — perform SGN()

## Disassemblatura
```assembly
.BC39  20 2B BC JSR $BC2B   ; get FAC1 sign, return A = $FF -ve, A = $01 +ve
```


## Commenti

### Original Disassembly (—)
- **$BC39**: get FAC1 sign, return A = $FF -ve, A = $01 +ve

### Commodore-64-intern-Buch (Commodore)
- **$BC39**: Vorzeichen holen
- **$BC3C**: und in FAC speichern
- **$BC3E**: $63
- **$BC40**: löschen
- **$BC42**: Exponent
- **$BC44**: Vorzeichen
- **$BC46**: invertieren
- **$BC48**: und nach links rollen
- **$BC49**: Die Adressen
- **$BC4B**: $65
- **$BC4D**: und $64 löschen
- **$BC4F**: Exponent
- **$BC51**: Rundungsstelle
- **$BC53**: löschen
- **$BC55**: linksbündig machen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC39**: CONVERT FAC TO -1,0,1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bc39-perform-sgn]]
