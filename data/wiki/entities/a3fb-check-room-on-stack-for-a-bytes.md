---
id: a3fb-check-room-on-stack-for-a-bytes
type: entity
title: check room on stack for A bytes
aliases:
- check room on stack for A bytes
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a3fb-check-room-on-stack-for-a-bytes.md
  sha256: 60316a28b42bc362775c4d5c0c7778e62817d61e90b780ed556ef11bf90ba858
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a3fb-check-room-on-stack-for-a-bytes
---

# check room on stack for A bytes



# $A3FB — check room on stack for A bytes

## Disassemblatura
```assembly
.A3FB  0A       ASL   ; *2
.A3FC  69 3E    ADC #$3E   ; need at least $3E bytes free
.A3FE  B0 35    BCS $A435   ; if overflow go do out of memory error then warm start
.A400  85 22    STA $22   ; save result in temp byte
.A402  BA       TSX   ; copy stack
.A403  E4 22    CPX $22   ; compare new limit with stack
.A405  90 2E    BCC $A435   ; if stack < limit do out of memory error then warm start
.A407  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A3FB**: *2
- **$A3FC**: need at least $3E bytes free
- **$A3FE**: if overflow go do out of memory error then warm start
- **$A400**: save result in temp byte
- **$A402**: copy stack
- **$A403**: compare new limit with stack
- **$A405**: if stack < limit do out of memory error then warm start

### Commodore-64-intern-Buch (Commodore)
- **$A3FB**: Akku muß die halbe Zahl an
- **$A3FC**: erforderlichem Platz haben
- **$A3FE**: gibt 'OUT OF MEMORY'
- **$A400**: Wert merken
- **$A402**: Ist Stapelzeiger kleiner
- **$A403**: (2 * Akku + 62)?
- **$A405**: Wenn ja, dann OUT OF MEMORY
- **$A407**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A3FE**: ...MEM FULL ERR
- **$A405**: ...MEM FULL ERR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a3fb-check-room-on-stack-for-a-bytes]]
