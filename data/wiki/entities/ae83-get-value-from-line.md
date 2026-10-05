---
id: ae83-get-value-from-line
type: entity
title: get value from line
aliases:
- get value from line
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae83-get-value-from-line.md
  sha256: d45d0ca977215d23c07c5d1cac71aaf4dbe041990df557f7dcae9a290fe1b283
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ae83-get-value-from-line
---

# get value from line



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

## References
- Source: [[src-ae83-get-value-from-line]]
