---
id: bbc7-pack-fac1-into-5c
type: entity
title: pack FAC1 into $5C
aliases:
- pack FAC1 into $5C
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bbc7-pack-fac1-into-5c.md
  sha256: acd5ca0ee5a07b73abcbb828d446f94c92fda2bc415e9be69cbe5b8cd63ba5d2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bbc7-pack-fac1-into-5c
---

# pack FAC1 into $5C



# $BBC7 — pack FAC1 into $5C

## Disassemblatura
```assembly
.BBC7  A2 5C    LDX #$5C   ; set pointer low byte
.BBC9  2C       .BYTE $2C   ; makes next line BIT $57A2
```


## Commenti

### Original Disassembly (—)
- **$BBC7**: set pointer low byte
- **$BBC9**: makes next line BIT $57A2

### Marko Mäkelä (Marko Mäkelä)
- **$BBC7**: low  005C

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BBC7**: PACK FAC INTO TEMP2
- **$BBC9**: TRICK TO BRANCH

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bbc7-pack-fac1-into-5c]]
