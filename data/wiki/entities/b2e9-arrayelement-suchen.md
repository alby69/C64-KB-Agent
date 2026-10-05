---
id: b2e9-arrayelement-suchen
type: entity
title: Arrayelement suchen
aliases:
- Arrayelement suchen
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b2e9-arrayelement-suchen.md
  sha256: 285e113dfd697a0ad86a5b542339e92eaa532649d2e7eca36cfa96f5c73f2f3a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b2e9-arrayelement-suchen
---

# Arrayelement suchen



# $B2E9 — Arrayelement suchen

## Disassemblatura
```assembly
.B2E9  C8       INY   ; Zeiger erhöhen
.B2EA  B1 5F    LDA ($5F),Y   ; Zahl der Dimensionen
.B2EC  85 0B    STA $0B   ; speichern
.B2EE  A9 00    LDA #$00   ; Nullwert laden und
.B2F0  85 71    STA $71   ; Zeiger auf Polynom-
.B2F2  85 72    STA $72   ; auswertung löschen
.B2F4  C8       INY   ; Zeiger erhöhen
.B2F5  68       PLA   ; 1. Indexwert vom Stapel
.B2F6  AA       TAX   ; holen und ins X-Reg. bringen
.B2F7  85 64    STA $64   ; Wert speichern
.B2F9  68       PLA   ; 2. Indexwert holen
.B2FA  85 65    STA $65   ; und speichern
.B2FC  D1 5F    CMP ($5F),Y   ; mit Wert im Array vergleichen
.B2FE  90 0E    BCC $B30E   ; kleiner?
.B300  D0 06    BNE $B308   ; größer: 'bad subscript'
.B302  C8       INY   ; Zeiger erhöhen
.B303  8A       TXA   ; 1.Wert zurückholen
.B304  D1 5F    CMP ($5F),Y   ; LOW-Byte vergleichen
.B306  90 07    BCC $B30F   ; kleiner: dann weiter
.B308  4C 45 B2 JMP $B245   ; 'bad subscript'
.B30B  4C 35 A4 JMP $A435   ; 'out of memory'
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B2E9**: Zeiger erhöhen
- **$B2EA**: Zahl der Dimensionen
- **$B2EC**: speichern
- **$B2EE**: Nullwert laden und
- **$B2F0**: Zeiger auf Polynom-
- **$B2F2**: auswertung löschen
- **$B2F4**: Zeiger erhöhen
- **$B2F5**: 1. Indexwert vom Stapel
- **$B2F6**: holen und ins X-Reg. bringen
- **$B2F7**: Wert speichern
- **$B2F9**: 2. Indexwert holen
- **$B2FA**: und speichern
- **$B2FC**: mit Wert im Array vergleichen
- **$B2FE**: kleiner?
- **$B300**: größer: 'bad subscript'
- **$B302**: Zeiger erhöhen
- **$B303**: 1.Wert zurückholen
- **$B304**: LOW-Byte vergleichen
- **$B306**: kleiner: dann weiter
- **$B308**: 'bad subscript'
- **$B30B**: 'out of memory'

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b2e9-arrayelement-suchen]]
