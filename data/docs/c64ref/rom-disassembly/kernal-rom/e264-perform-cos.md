---
title: perform COS()
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e264-basic-funktion-cos
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  - marko_mäkelä.txt
  - bob_sander-cederlof.txt
  - magnus_nyman.txt
  address: $E264
  address_end: $E268
  symbol: perform-cos
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E264**: set pi/2 pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E264**: Zeiger auf'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E264**: low  E2E0'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E264**: COS(X)=SIN(X + PI/2)'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E264**: set address to pi/2'
---

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