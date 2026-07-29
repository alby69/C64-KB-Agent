---
title: pack FAC1 into $57
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
- bbca-fac-nach-akku-3-bertragen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BBCA
  address_end: $BBCE
  symbol: pack-fac1-into-57
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BBCA**: set pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BBCA**: Adresse LOW Akku #3'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BBCA**: low  0057'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BBCA**: PACK FAC INTO TEMP1'
---

# $BBCA — pack FAC1 into $57

## Disassemblatura
```assembly
.BBCA  A2 57    LDX #$57   ; set pointer low byte
.BBCC  A0 00    LDY #$00   ; set pointer high byte
.BBCE  F0 04    BEQ $BBD4   ; pack FAC1 into (XY) and return, branch always
```


## Commenti

### Original Disassembly (—)
- **$BBCA**: set pointer low byte
- **$BBCC**: set pointer high byte
- **$BBCE**: pack FAC1 into (XY) and return, branch always

### Commodore-64-intern-Buch (Commodore)
- **$BBCA**: Adresse LOW Akku #3
- **$BBCC**: Adresse HIGH
- **$BBCE**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
- **$BBCA**: low  0057
- **$BBCC**: high 0057

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BBCA**: PACK FAC INTO TEMP1
- **$BBCC**: HI-BYTE OF TEMP1 SAME AS TEMP2
- **$BBCE**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*