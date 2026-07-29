---
title: perform INPUT#
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
- aba5-basic-befehl-input
- input
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $ABA5
  address_end: $ABB2
  symbol: perform-input
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ABA5**: get byte parameter'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$ABA5**: holt Byte-Wert'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$ABA8**: comma'
---

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