---
title: check and skip characters
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- aef7-prft-auf-zeichen-im-b-text
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $AEF7
  address_end: $AF0A
  symbol: check-and-skip-characters
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AEF7**: '')'' Klammer zu'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AEF7**: )'
---

# $AEF7 — check and skip characters

## Disassemblatura
```assembly
.AEF7  A9 29    LDA #$29   ; )
.AEF9  2C       .BYTE $2C
.AEFA  A9 28    LDA #$28   ; (
.AEFC  2C       .BYTE $2C
.AEFD  A9 2C    LDA #$2C   ; comma
.AEFF  A0 00    LDY #$00
.AF01  D1 7A    CMP ($7A),Y
.AF03  D0 03    BNE $AF08
.AF05  4C 73 00 JMP $0073
.AF08  A2 0B    LDX #$0B   ; error number
.AF0A  4C 37 A4 JMP $A437
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AEF7**: ')' Klammer zu
- **$AEFA**: '(' Klammer auf
- **$AEFD**: ',' Komma
- **$AEFF**: Zeiger setzen
- **$AF01**: mit laufendem Zeichen vergl.
- **$AF03**: keine Übereinstimmung?
- **$AF05**: CHRGET nächstes Zeichen holen
- **$AF08**: Nummer für 'SYNTAX ERROR'
- **$AF0A**: Fehlermeldung ausgeben
- **$AF0D**: Offset Hierachie-Code für VZW
- **$AF0F**: nächsten 2 Bytes vom
- **$AF10**: Stapel entfernen
- **$AF11**: zur Auswertung

### Marko Mäkelä (Marko Mäkelä)
- **$AEF7**: )
- **$AEFA**: (
- **$AEFD**: comma
- **$AF08**: error number

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*