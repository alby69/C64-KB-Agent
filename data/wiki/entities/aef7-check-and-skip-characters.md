---
id: aef7-check-and-skip-characters
type: entity
title: check and skip characters
aliases:
- check and skip characters
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aef7-check-and-skip-characters.md
  sha256: 49b476b3f7a9e814364867b2e9553d9d11b24df7544191de374290db879f6dba
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-aef7-check-and-skip-characters
---

# check and skip characters



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

## References
- Source: [[src-aef7-check-and-skip-characters]]
