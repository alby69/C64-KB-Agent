---
title: do " IN " line number message
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
- bdc2-bei-fehlermeldung
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BDC2
  address_end: $BDCB
  symbol: do-in-line-number-message
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BDC2**: set " IN " pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BDC2**: Zeiger'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BDC2**: low  A371'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BDC2**: PRINT " IN "'
---

# $BDC2 — do " IN " line number message

## Disassemblatura
```assembly
.BDC2  A9 71    LDA #$71   ; set " IN " pointer low byte
.BDC4  A0 A3    LDY #$A3   ; set " IN " pointer high byte
.BDC6  20 DA BD JSR $BDDA   ; print null terminated string
.BDC9  A5 3A    LDA $3A   ; get the current line number high byte
.BDCB  A6 39    LDX $39   ; get the current line number low byte
```


## Commenti

### Original Disassembly (—)
- **$BDC2**: set " IN " pointer low byte
- **$BDC4**: set " IN " pointer high byte
- **$BDC6**: print null terminated string
- **$BDC9**: get the current line number high byte
- **$BDCB**: get the current line number low byte

### Commodore-64-intern-Buch (Commodore)
- **$BDC2**: Zeiger
- **$BDC4**: auf 'in'
- **$BDC6**: String ausgeben
- **$BDC9**: laufende
- **$BDCB**: Zeilennummer holen

### Marko Mäkelä (Marko Mäkelä)
- **$BDC2**: low  A371
- **$BDC4**: high A371

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BDC2**: PRINT " IN "

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*