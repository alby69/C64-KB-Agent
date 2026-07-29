---
title: do string vector
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b475-stringzeiger-berechnen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B475
  address_end: $B47B
  symbol: do-string-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B475**: get descriptor pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B475**: Zeiger in'
---

# $B475 — do string vector

## Disassemblatura
```assembly
.B475  A6 64    LDX $64   ; get descriptor pointer low byte
.B477  A4 65    LDY $65   ; get descriptor pointer high byte
.B479  86 50    STX $50   ; save descriptor pointer low byte
.B47B  84 51    STY $51   ; save descriptor pointer high byte
```


## Commenti

### Original Disassembly (—)
- **$B475**: get descriptor pointer low byte
- **$B477**: get descriptor pointer high byte
- **$B479**: save descriptor pointer low byte
- **$B47B**: save descriptor pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$B475**: Zeiger in
- **$B477**: $64/65 in
- **$B479**: Zeiger auf Stringdescriptor
- **$B47B**: speichern
- **$B47D**: Platz für String, Länge in A
- **$B480**: Adresse LOW
- **$B482**: Adresse HIGH
- **$B484**: Länge

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*