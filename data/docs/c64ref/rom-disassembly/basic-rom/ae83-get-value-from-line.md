---
title: get value from line
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
- ae83-ausdrucks-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AE83
  address_end: $AE83
  symbol: get-value-from-line
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AE83**: get arithmetic element'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AE83**: JMP $AE86'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AE83**: normally AE86'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AE86**: ASSUME NUMERIC'
---

# $AE83 — get value from line

## Disassemblatura
```assembly
.AE83  6C 0A 03 JMP ($030A)   ; get arithmetic element
```


## Commenti

### Original Disassembly (—)
- **$AE83**: get arithmetic element

### Commodore-64-intern-Buch (Commodore)
- **$AE83**: JMP $AE86
- **$AE86**: Wert laden und damit
- **$AE88**: Typflag auf numerisch setzen
- **$AE8A**: CHRGET nächstes Zeichen holen
- **$AE8D**: Ziffer? nein: $AE92
- **$AE8F**: Variable nach FAC holen
- **$AE92**: Buchstabe?
- **$AE95**: nein: JMP umgehen
- **$AE97**: Variable holen
- **$AE9A**: BASIC-Code für Pi?
- **$AE9C**: nein: $AEAD
- **$AE9E**: Zeiger auf Konstante Pi
- **$AEA0**: (LOW und HIGH-Byte)
- **$AEA2**: Konstante in FAC holen
- **$AEA5**: CHRGET nächstes Zeichen holen
- **$AEA8**: Konstante Pi 3.14159265
- **$AEAD**: '.' Dezimalpunkt?
- **$AEAF**: ja: $AE8F
- **$AEB1**: '-'?
- **$AEB3**: zum Vorzeichenwechsel
- **$AEB5**: '+'?
- **$AEB7**: ja: $Ae8A
- **$AEB9**: '"'?
- **$AEBB**: nein: $AECC
- **$AEBD**: LOW- und HIGH-Byte des
- **$AEBF**: Programmzeigers holen
- **$AEC1**: und Übertrag addieren
- **$AEC3**: C=0: $AEC6
- **$AEC5**: HIGH-Byte erhöhen
- **$AEC6**: String übertragen
- **$AEC9**: Programmz. auf Stringende +1
- **$AECC**: 'NOT'-Code?
- **$AECE**: nein: $AEE3
- **$AED0**: Offset des H.Flags in Tabelle
- **$AED2**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
- **$AE83**: normally AE86

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AE86**: ASSUME NUMERIC
- **$AE8D**: NOT A DIGIT
- **$AE8F**: NUMERIC CONSTANT
- **$AE92**: VARIABLE NAME?
- **$AE97**: YES
- **$AEAD**: DECIMAL POINT
- **$AEAF**: YES, NUMERIC CONSTANT
- **$AEB1**: UNARY MINUS?
- **$AEB3**: YES
- **$AEB5**: UNARY PLUS
- **$AEB7**: YES
- **$AEB9**: STRING CONSTANT?
- **$AEBB**: NO

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*