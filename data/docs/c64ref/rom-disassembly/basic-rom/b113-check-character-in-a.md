---
title: check character in A
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
- b113-prft-auf-buchstabe
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $B113
  address_end: $B11C
  symbol: check-character-in-a
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B113**: ''A''-Code? (Buchstabencode)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B113**: A'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B113**: COMPARE LO END'
---

# $B113 — check character in A

## Disassemblatura
```assembly
.B113  C9 41    CMP #$41   ; A
.B115  90 05    BCC $B11C
.B117  E9 5B    SBC #$5B   ; Z
.B119  38       SEC
.B11A  E9 A5    SBC #$A5
.B11C  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B113**: 'A'-Code? (Buchstabencode)
- **$B115**: wenn kleiner: RTS mit C = 0
- **$B117**: 'Z' + 1
- **$B119**: wenn größer 'Z': C = 0
- **$B11A**: sonst: C = 1 = Buchstabe
- **$B11C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$B113**: A
- **$B117**: Z

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B113**: COMPARE LO END
- **$B115**: C=0 IF LOW
- **$B117**: PREPARE HI END TEST
- **$B119**: TEST HI END, RESTORING (A)
- **$B11A**: C=0 IF LO, C=1 IF A-Z

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*