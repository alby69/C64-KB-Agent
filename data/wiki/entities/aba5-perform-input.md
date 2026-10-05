---
id: aba5-perform-input
type: entity
title: perform INPUT#
aliases:
- perform INPUT#
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aba5-perform-input.md
  sha256: 23b2b470aaa37312cb1df42dd04356d93cee2b15b9fb6826f6a3674c2c8ecd14
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-aba5-perform-input
---

# perform INPUT#



# $ABA5 — perform INPUT#

## Disassemblatura
```assembly
.ABA5  20 9E B7 JSR $B79E   ; get byte parameter
.ABA8  A9 2C    LDA #$2C   ; set ","
.ABAA  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.ABAD  86 13    STX $13   ; set current I/O channel
.ABAF  20 1E E1 JSR $E11E   ; open channel for input with error check
.ABB2  20 CE AB JSR $ABCE   ; perform INPUT with no prompt string
```


## Commenti

### Original Disassembly (—)
- **$ABA5**: get byte parameter
- **$ABA8**: set ","
- **$ABAA**: scan for CHR$(A), else do syntax error then warm start
- **$ABAD**: set current I/O channel
- **$ABAF**: open channel for input with error check
- **$ABB2**: perform INPUT with no prompt string

### Commodore-64-intern-Buch (Commodore)
- **$ABA5**: holt Byte-Wert
- **$ABA8**: ',' Code für Komma
- **$ABAA**: prüft auf Komma
- **$ABAD**: Eingabegerät
- **$ABAF**: CHKIN, Eingabe vorbereiten
- **$ABB2**: INPUT ohne Dialogstring
- **$ABB5**: Eingabegerät im Akku
- **$ABB7**: setzt Eingabegerät zurück
- **$ABBA**: Wert laden und
- **$ABBC**: Eingabegerät wieder Tastatur
- **$ABBE**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$ABA8**: comma

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-aba5-perform-input]]
