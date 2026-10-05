---
id: e264-perform-cos
type: entity
title: perform COS()
aliases:
- perform COS()
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e264-perform-cos.md
  sha256: 4662386667c2309c537e95ac9126929a38516702534adf83712938dc4b25357e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e264-perform-cos
---

# perform COS()



# $E264 — perform COS()

## Disassemblatura
```assembly
.E264  A9 E0    LDA #$E0   ; set pi/2 pointer low byte
.E266  A0 E2    LDY #$E2   ; set pi/2 pointer high byte
.E268  20 67 B8 JSR $B867   ; add (AY) to FAC1
```


## Commenti

### Original Disassembly (—)
- **$E264**: set pi/2 pointer low byte
- **$E266**: set pi/2 pointer high byte
- **$E268**: add (AY) to FAC1

### Commodore-64-intern-Buch (Commodore)
- **$E264**: Zeiger auf
- **$E266**: Konstante Pi/2
- **$E268**: zu FAC addieren

### Marko Mäkelä (Marko Mäkelä)
- **$E264**: low  E2E0
- **$E266**: high E2E0

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E264**: COS(X)=SIN(X + PI/2)

### Magnus Nyman (Magnus Nyman)
- **$E264**: set address to pi/2
- **$E266**: at $e2e0
- **$E268**: add fltp at (A/Y) to fac#1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e264-perform-cos]]
