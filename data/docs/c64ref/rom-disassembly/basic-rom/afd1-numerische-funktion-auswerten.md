---
title: numerische Funktion auswerten
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
- afd1-numerische-funktion-auswerten
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AFD1
  address_end: $AFE3
  symbol: numerische-funktion-auswerten
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AFD1**: holt Term in Klammern'
---

# $AFD1 — numerische Funktion auswerten

## Disassemblatura
```assembly
.AFD1  20 F1 AE JSR $AEF1   ; holt Term in Klammern
.AFD4  68       PLA   ; BASIC-Code für Funktion holen
.AFD5  A8       TAY   ; und als Zeiger ins Y-Reg.
.AFD6  B9 EA 9F LDA $9FEA,Y   ; Vektor für Funktionsbe-
.AFD9  85 55    STA $55   ; rechnung holen und speichern
.AFDB  B9 EB 9F LDA $9FEB,Y   ; 2.Byte holen
.AFDE  85 56    STA $56   ; und speichern
.AFE0  20 54 00 JSR $0054   ; Funktion ausführen
.AFE3  4C 8D AD JMP $AD8D   ; prüft auf numerisch
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AFD1**: holt Term in Klammern
- **$AFD4**: BASIC-Code für Funktion holen
- **$AFD5**: und als Zeiger ins Y-Reg.
- **$AFD6**: Vektor für Funktionsbe-
- **$AFD9**: rechnung holen und speichern
- **$AFDB**: 2.Byte holen
- **$AFDE**: und speichern
- **$AFE0**: Funktion ausführen
- **$AFE3**: prüft auf numerisch

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*