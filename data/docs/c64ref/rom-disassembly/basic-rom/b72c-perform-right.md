---
title: perform RIGHT$()
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
- b72c-basic-funktion-right
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B72C
  address_end: $B734
  symbol: perform-right
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B72C**: pull string data and byte parameter from stack return
      pointer in...'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B72C**: Stringparameter und Länge vom Stack holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B72F**: COMPUTE LENGTH-WIDTH OF SUBSTRING'
---

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