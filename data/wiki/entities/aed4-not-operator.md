---
id: aed4-not-operator
type: entity
title: NOT operator
aliases:
- NOT operator
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aed4-not-operator.md
  sha256: 35fe985a492af5a141ca9e88130bdc8d56012aec4f879042cdd2fdc1878a80e3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-aed4-not-operator
---

# NOT operator



# $AED4 — NOT operator

## Disassemblatura
```assembly
.AED4  20 BF B1 JSR $B1BF
.AED7  A5 65    LDA $65
.AED9  49 FF    EOR #$FF
.AEDB  A8       TAY
.AEDC  A5 64    LDA $64
.AEDE  49 FF    EOR #$FF
.AEE0  4C 91 B3 JMP $B391
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AED4**: FAC nach INTEGER wandeln
- **$AED7**: HIGH-Byte holen
- **$AED9**: alle Bits umdrehen
- **$AEDB**: und ins Y-Reg.
- **$AEDC**: LOW-Byte holen
- **$AEDE**: alle Bits invertieren
- **$AEE0**: nach Fließkomma wandeln
- **$AEE3**: 'FN'-Code?
- **$AEE5**: nein: $AEEA
- **$AEE7**: FN ausführen
- **$AEEA**: 'SGN'-Code
- **$AEEC**: kleiner (keine Stringfunkt.)?
- **$AEEE**: holt String ,ersten Parameter

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-aed4-not-operator]]
