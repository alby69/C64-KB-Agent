---
id: bbca-pack-fac1-into-57
type: entity
title: pack FAC1 into $57
aliases:
- pack FAC1 into $57
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bbca-pack-fac1-into-57.md
  sha256: 0a1a677daee2e529542448283de6015c63c66a40fd49b044bc7763c0394fd2a1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bbca-pack-fac1-into-57
---

# pack FAC1 into $57



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

## References
- Source: [[src-bbca-pack-fac1-into-57]]
