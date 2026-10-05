---
id: b113-check-character-in-a
type: entity
title: check character in A
aliases:
- check character in A
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b113-check-character-in-a.md
  sha256: 491c0e7c22bd4797b5a6fc51a9f42782de4bf8536bc4017441a3f8193a7c18fa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b113-check-character-in-a
---

# check character in A



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

## References
- Source: [[src-b113-check-character-in-a]]
