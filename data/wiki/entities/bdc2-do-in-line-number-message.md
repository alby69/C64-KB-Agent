---
id: bdc2-do-in-line-number-message
type: entity
title: do " IN " line number message
aliases:
- do " IN " line number message
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bdc2-do-in-line-number-message.md
  sha256: e7f4b68025d2392c9bb519da44e09cac102033717838f803a072cdd071efa31a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bdc2-do-in-line-number-message
---

# do " IN " line number message



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

## References
- Source: [[src-bdc2-do-in-line-number-message]]
