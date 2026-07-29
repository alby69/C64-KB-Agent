---
title: EVALUATE "(EXPRESSION)"
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
- 007a-txtptr
- aef1-holt-term-in-klammern
- aef7-prft-auf-zeichen-im-b-text
- check
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - commodore-64-intern-buch.txt
  address: $AEF1
  address_end: $AEFD
  symbol: evaluate-expression
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AEF1**: prüft auf Klammer auf'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AEF1**: IS THERE A ''('' AT TXTPTR?'
---

# $AEF1 — EVALUATE "(EXPRESSION)"

## Disassemblatura
```assembly
.AEF1  20 FA AE JSR $AEFA   ; IS THERE A '(' AT TXTPTR?
.AEF4  20 9E AD JSR $AD9E   ; YES, EVALUATE EXPRESSION
.AEF7  A9 29    LDA #$29   ; CHECK FOR ')'
.AEF9  2C       .BYTE $2C   ; TRICK
.AEFA  A9 28    LDA #$28
.AEFC  2C       .BYTE $2C   ; TRICK
.AEFD  A9 2C    LDA #$2C   ; COMMA AT TXTPTR?
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AEF1**: prüft auf Klammer auf
- **$AEF4**: FRMEVL holt Term

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AEF1**: IS THERE A '(' AT TXTPTR?
- **$AEF4**: YES, EVALUATE EXPRESSION
- **$AEF7**: CHECK FOR ')'
- **$AEF9**: TRICK
- **$AEFC**: TRICK
- **$AEFD**: COMMA AT TXTPTR?

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*