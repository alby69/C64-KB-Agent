---
id: bafe-divide-fac1-by-10
type: entity
title: divide FAC1 by 10
aliases:
- divide FAC1 by 10
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bafe-divide-fac1-by-10.md
  sha256: ca17d237624124e3a0004ac8c2a6a409504c310cb086f884db8156a99251419d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bafe-divide-fac1-by-10
---

# divide FAC1 by 10



# $BAFE — divide FAC1 by 10

## Disassemblatura
```assembly
.BAFE  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.BB01  A9 F9    LDA #$F9   ; set 10 pointer low byte
.BB03  A0 BA    LDY #$BA   ; set 10 pointer high byte
.BB05  A2 00    LDX #$00   ; clear sign
```


## Commenti

### Original Disassembly (—)
- **$BAFE**: round and copy FAC1 to FAC2
- **$BB01**: set 10 pointer low byte
- **$BB03**: set 10 pointer high byte
- **$BB05**: clear sign

### Commodore-64-intern-Buch (Commodore)
- **$BAFE**: FAC runden und nach ARG
- **$BB01**: Zeiger
- **$BB03**: auf
- **$BB05**: Konstante 10
- **$BB07**: Vergleichsbyte löschen
- **$BB09**: Konstante 10 nach FAC
- **$BB0C**: FAC = ARG / FAC

### Marko Mäkelä (Marko Mäkelä)
- **$BB01**: low  BAF9
- **$BB03**: high BAF9

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BB01**: SET UP TO PUT
- **$BB03**: 10 IN FAC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bafe-divide-fac1-by-10]]
