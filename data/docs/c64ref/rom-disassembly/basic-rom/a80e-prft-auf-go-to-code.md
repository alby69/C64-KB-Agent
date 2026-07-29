---
title: prüft auf 'GO' 'TO' Code
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
- a80e-prft-auf-go-to-code
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $A80E
  address_end: $A81A
  symbol: prft-auf-go-to-code
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A80E**: ''GO'' (minus $80)'
---

# $A80E — prüft auf 'GO' 'TO' Code

## Disassemblatura
```assembly
.A80E  C9 4B    CMP #$4B   ; 'GO' (minus $80)
.A810  D0 F9    BNE $A80B   ; nein: 'SYNTAX ERROR'
.A812  20 73 00 JSR $0073   ; nächstes Zeichen holen
.A815  A9 A4    LDA #$A4   ; 'TO'
.A817  20 FF AE JSR $AEFF   ; prüft auf Code
.A81A  4C A0 A8 JMP $A8A0   ; zum GOTO-Befehl
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A80E**: 'GO' (minus $80)
- **$A810**: nein: 'SYNTAX ERROR'
- **$A812**: nächstes Zeichen holen
- **$A815**: 'TO'
- **$A817**: prüft auf Code
- **$A81A**: zum GOTO-Befehl

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*