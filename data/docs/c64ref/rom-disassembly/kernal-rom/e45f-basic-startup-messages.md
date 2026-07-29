---
title: BASIC startup messages
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e45f-system-meldungen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E45F
  address_end: $E4AB
  symbol: basic-startup-messages
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E45F**: basic bytes free'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E45F**: basic bytes free'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E45F**: basic bytes free'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E45F**: basic bytes free'
---

# $E45F — BASIC startup messages

## Disassemblatura
```assembly
.E45F  00 20 42 41 53 49 43 20   ; basic bytes free
.E467  42 59 54 45 53 20 46 52
.E46F  45 45 0D 00
.E473  93 0D 20 20 20 20 2A 2A   ; (clr) **** commodore 64 basic v2 ****
.E47B  2A 2A 20 43 4F 4D 4D 4F   ; (cr) (cr) 64k ram system
.E483  44 4F 52 45 20 36 34 20
.E48B  42 41 53 49 43 20 56 32
.E493  20 2A 2A 2A 2A 0D 0D 20
.E49B  36 34 4B 20 52 41 4D 20
.E4A3  53 59 53 54 45 4D 20 20
.E4AB  00
```


## Commenti

### Original Disassembly (—)
- **$E45F**: basic bytes free
- **$E473**: (clr) **** commodore 64 basic v2 ****
- **$E47B**: (cr) (cr) 64k ram system

### Commodore-64-intern-Buch (Commodore)
- **$E45F**: basic bytes free
- **$E473**: (clr) **** commodore 64 basic v2 ****
- **$E47B**: (cr) (cr) 64k ram system

### Marko Mäkelä (Marko Mäkelä)
- **$E45F**: basic bytes free
- **$E473**: (clr) **** commodore 64 basic v2 ****
- **$E47B**: (cr) (cr) 64k ram system

### Magnus Nyman (Magnus Nyman)
- **$E45F**: basic bytes free
- **$E473**: (clr) **** commodore 64 basic v2 ****
- **$E47B**: (cr) (cr) 64k ram system

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*