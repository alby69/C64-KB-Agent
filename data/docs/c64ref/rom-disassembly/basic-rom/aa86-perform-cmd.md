---
title: perform CMD
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
- aa86-basic-befehl-cmd
- ab45-print
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AA86
  address_end: $AA9D
  symbol: perform-cmd
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AA86**: get byte parameter'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AA86**: holt Byte-Ausdruck'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AA8B**: comma'
---

# $AA86 — perform CMD

## Disassemblatura
```assembly
.AA86  20 9E B7 JSR $B79E   ; get byte parameter
.AA89  F0 05    BEQ $AA90   ; branch if following byte is ":" or [EOT]
.AA8B  A9 2C    LDA #$2C   ; set ","
.AA8D  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.AA90  08       PHP   ; save status
.AA91  86 13    STX $13   ; set current I/O channel
.AA93  20 18 E1 JSR $E118   ; open channel for output with error check
.AA96  28       PLP   ; restore status
.AA97  4C A0 AA JMP $AAA0   ; perform PRINT
.AA9A  20 21 AB JSR $AB21   ; print string from utility pointer
.AA9D  20 79 00 JSR $0079   ; scan memory
```


## Commenti

### Original Disassembly (—)
- **$AA86**: get byte parameter
- **$AA89**: branch if following byte is ":" or [EOT]
- **$AA8B**: set ","
- **$AA8D**: scan for CHR$(A), else do syntax error then warm start
- **$AA90**: save status
- **$AA91**: set current I/O channel
- **$AA93**: open channel for output with error check
- **$AA96**: restore status
- **$AA97**: perform PRINT
- **$AA9A**: print string from utility pointer
- **$AA9D**: scan memory

### Commodore-64-intern-Buch (Commodore)
- **$AA86**: holt Byte-Ausdruck
- **$AA89**: Trennzeichen: $AA90
- **$AA8B**: ',', Wert laden
- **$AA8D**: prüft auf Komma
- **$AA90**: Statusregister merken
- **$AA91**: Nr. des Ausgabegeräts merken
- **$AA93**: CKOUT, Ausgabegerät setzen
- **$AA96**: Statusregister wiederholen
- **$AA97**: zum PRINT-Befehl
- **$AA9A**: String drucken
- **$AA9D**: CHRGOT letztes Zeichen

### Marko Mäkelä (Marko Mäkelä)
- **$AA8B**: comma
- **$AA97**: do PRINT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*