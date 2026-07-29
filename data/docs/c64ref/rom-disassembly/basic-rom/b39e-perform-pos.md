---
title: perform POS()
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
- b39e-basic-funktion-pos
- b3a2-float-y-into-fac-giving-value-0-255
- b3a6-test-auf-direkt-modus
- bit
- input
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B39E
  address_end: $B3B0
  symbol: perform-pos
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B39E**: set Cb for read cursor position'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B39E**: C=1 Cursorposition holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B39E — perform POS()

## Disassemblatura
```assembly
.B39E  38       SEC   ; set Cb for read cursor position
.B39F  20 F0 FF JSR $FFF0   ; read/set X,Y cursor position
.B3A2  A9 00    LDA #$00   ; clear high byte
.B3A4  F0 EB    BEQ $B391   ; convert fixed integer AY to float FAC1, branch always check not Direct, used by DEF and INPUT
.B3A6  A6 3A    LDX $3A   ; get current line number high byte
.B3A8  E8       INX   ; increment it
.B3A9  D0 A0    BNE $B34B   ; return if not direct mode else do illegal direct error
.B3AB  A2 15    LDX #$15   ; error $15, illegal direct error
.B3AD  2C       .BYTE $2C   ; makes next line BIT $1BA2
.B3AE  A2 1B    LDX #$1B   ; error $1B, undefined function error
.B3B0  4C 37 A4 JMP $A437   ; do error #X then warm start
```


## Commenti

### Original Disassembly (—)
- **$B39E**: set Cb for read cursor position
- **$B39F**: read/set X,Y cursor position
- **$B3A2**: clear high byte
- **$B3A4**: convert fixed integer AY to float FAC1, branch always check not Direct, used by DEF and INPUT
- **$B3A6**: get current line number high byte
- **$B3A8**: increment it
- **$B3A9**: return if not direct mode else do illegal direct error
- **$B3AB**: error $15, illegal direct error
- **$B3AD**: makes next line BIT $1BA2
- **$B3AE**: error $1B, undefined function error
- **$B3B0**: do error #X then warm start

### Commodore-64-intern-Buch (Commodore)
- **$B39E**: C=1 Cursorposition holen
- **$B39F**: Cursorposition holen
- **$B3A2**: Z=1
- **$B3A4**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*