---
id: a80e-prft-auf-go-to-code
type: entity
title: prüft auf 'GO' 'TO' Code
aliases:
- prüft auf 'GO' 'TO' Code
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a80e-prft-auf-go-to-code.md
  sha256: ecb577a9fa2936d2964c0904845af1ac0478aa221eb35965208aac377e57f24b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a80e-prft-auf-go-to-code
---

# prüft auf 'GO' 'TO' Code



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

## References
- Source: [[src-a80e-prft-auf-go-to-code]]
