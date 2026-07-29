---
title: perform LEN()
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
- b77c-basic-funktion-len
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B77C
  address_end: $B77F
  symbol: perform-len
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B77C**: evaluate string, get length in A (and Y)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B77C**: FRESTR, Stringlänge holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B77C**: GET LENTGH IN Y-REG, MAKE FAC NUMERIC'
---

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