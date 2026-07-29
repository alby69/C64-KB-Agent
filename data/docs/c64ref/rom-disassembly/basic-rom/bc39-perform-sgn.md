---
title: perform SGN()
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bc39-basic-funktion-sgn
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BC39
  address_end: $BC39
  symbol: perform-sgn
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC39**: get FAC1 sign, return A = $FF -ve, A = $01 +ve'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BC39**: Vorzeichen holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC39**: CONVERT FAC TO -1,0,1'
---

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