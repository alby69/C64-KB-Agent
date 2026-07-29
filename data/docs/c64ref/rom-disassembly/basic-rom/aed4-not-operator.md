---
title: NOT operator
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $AED4
  address_end: $AEE0
  symbol: not-operator
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AED4**: FAC nach INTEGER wandeln'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

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