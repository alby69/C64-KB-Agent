---
id: b824-perform-poke
type: entity
title: perform POKE
aliases:
- perform POKE
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b824-perform-poke.md
  sha256: a29fb3b044dfa0ed68880d97f4d681b558bd50fc3cade2af384ecf208bba4689
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b824-perform-poke
---

# perform POKE



# $B824 — perform POKE

## Disassemblatura
```assembly
.B824  20 EB B7 JSR $B7EB   ; get parameters for POKE/WAIT
.B827  8A       TXA   ; copy byte to A
.B828  A0 00    LDY #$00   ; clear index
.B82A  91 14    STA ($14),Y   ; write byte
.B82C  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B824**: get parameters for POKE/WAIT
- **$B827**: copy byte to A
- **$B828**: clear index
- **$B82A**: write byte

### Commodore-64-intern-Buch (Commodore)
- **$B824**: Poke-Adrefcse und Wert holen
- **$B827**: Poke-Wert in Akku
- **$B828**: Zähler auf Null
- **$B82A**: und in Speicher schreiben
- **$B82C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B824**: GET THE ADDRESS AND VALUE
- **$B827**: VALUE IN A,
- **$B82A**: STORE IT AWAY,
- **$B82C**: AND THAT'S ALL FOR TODAY

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b824-perform-poke]]
