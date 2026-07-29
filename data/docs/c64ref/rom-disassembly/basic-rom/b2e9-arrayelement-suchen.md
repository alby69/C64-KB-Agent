---
title: Arrayelement suchen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b2e9-arrayelement-suchen
- b2ea-find-specified-array-element
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $B2E9
  address_end: $B30B
  symbol: arrayelement-suchen
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B2E9**: Zeiger erhöhen'
---

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