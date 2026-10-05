---
id: b3b3-perform-def
type: entity
title: perform DEF
aliases:
- perform DEF
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b3b3-perform-def.md
  sha256: 0016d642eaaa6987ed7b556f29c23a781bb76aa6f3f4c77c4d52a6b8c188f630
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b3b3-perform-def
---

# perform DEF



# $B3B3 — perform DEF

## Disassemblatura
```assembly
.B3B3  20 E1 B3 JSR $B3E1   ; check FNx syntax
.B3B6  20 A6 B3 JSR $B3A6   ; check not direct, back here if ok
.B3B9  20 FA AE JSR $AEFA   ; scan for "(", else do syntax error then warm start
.B3BC  A9 80    LDA #$80   ; set flag for FNx
.B3BE  85 10    STA $10   ; save subscript/FNx flag
.B3C0  20 8B B0 JSR $B08B   ; get variable address
.B3C3  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.B3C6  20 F7 AE JSR $AEF7   ; scan for ")", else do syntax error then warm start
.B3C9  A9 B2    LDA #$B2   ; get = token
.B3CB  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.B3CE  48       PHA   ; push next character
.B3CF  A5 48    LDA $48   ; get current variable pointer high byte
.B3D1  48       PHA   ; push it
.B3D2  A5 47    LDA $47   ; get current variable pointer low byte
.B3D4  48       PHA   ; push it
.B3D5  A5 7B    LDA $7B   ; get BASIC execute pointer high byte
.B3D7  48       PHA   ; push it
.B3D8  A5 7A    LDA $7A   ; get BASIC execute pointer low byte
.B3DA  48       PHA   ; push it
.B3DB  20 F8 A8 JSR $A8F8   ; perform DATA
.B3DE  4C 4F B4 JMP $B44F   ; put execute pointer and variable pointer into function and return
```


## Commenti

### Original Disassembly (—)
- **$B3B3**: check FNx syntax
- **$B3B6**: check not direct, back here if ok
- **$B3B9**: scan for "(", else do syntax error then warm start
- **$B3BC**: set flag for FNx
- **$B3BE**: save subscript/FNx flag
- **$B3C0**: get variable address
- **$B3C3**: check if source is numeric, else do type mismatch
- **$B3C6**: scan for ")", else do syntax error then warm start
- **$B3C9**: get = token
- **$B3CB**: scan for CHR$(A), else do syntax error then warm start
- **$B3CE**: push next character
- **$B3CF**: get current variable pointer high byte
- **$B3D1**: push it
- **$B3D2**: get current variable pointer low byte
- **$B3D4**: push it
- **$B3D5**: get BASIC execute pointer high byte
- **$B3D7**: push it
- **$B3D8**: get BASIC execute pointer low byte
- **$B3DA**: push it
- **$B3DB**: perform DATA
- **$B3DE**: put execute pointer and variable pointer into function and return

### Commodore-64-intern-Buch (Commodore)
- **$B3B3**: prüft FN-Syntax
- **$B3B6**: testet auf Direkt-Modus
- **$B3B9**: prüft auf 'Klammer auf
- **$B3BC**: Wert laden
- **$B3BE**: sperrt INTEGER-Variable
- **$B3C0**: sucht Variable
- **$B3C3**: prüft auf numerisch
- **$B3C6**: prüft auf 'Klammer zu'
- **$B3C9**: '=' BASIC-Code
- **$B3CB**: prüft auf '='
- **$B3CE**: erstes Zeichen auf Stapel
- **$B3CF**: LOW- und HIGH-Byte der
- **$B3D1**: FN-Variablen-Adresse
- **$B3D2**: auf den Stapel
- **$B3D4**: legen
- **$B3D5**: LOW- und HIGH-Byte
- **$B3D7**: des Programmzeigers
- **$B3D8**: auf den Stapel
- **$B3DA**: legen
- **$B3DB**: Programmzeiger auf Statement
- **$B3DE**: FN-Variable vom Stapel holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B3B3**: PARSE "FN", FUNCTION NAME
- **$B3B6**: ERROR IF IN DIRECT MODE
- **$B3B9**: NEED "("
- **$B3BC**: FLAG PTRGET THAT CALLED FROM "DEF FN"
- **$B3BE**: ALLOW ONLY SIMPLE FP VARIABLE FOR ARG
- **$B3C0**: GET PNTR TO ARGUMENT
- **$B3C3**: MUST BE NUMERIC
- **$B3C6**: MUST HAVE ")" NOW
- **$B3C9**: NOW NEED "="
- **$B3CB**: OR ELSE SYNTAX ERROR
- **$B3CE**: SAVE CHAR AFTER "="
- **$B3CF**: SAVE PNTR TO ARGUMENT
- **$B3D5**: SAVE TXTPTR
- **$B3DB**: SCAN TO NEXT STATEMENT
- **$B3DE**: STORE ABOVE 5 BYTES IN "VALUE"

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b3b3-perform-def]]
