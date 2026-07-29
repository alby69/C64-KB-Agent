---
title: perform CLR
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
- a65e-basic-befehl-clr
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A65E
  address_end: $A675
  symbol: perform-clr
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A65E**: exit if following byte to allow syntax error'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A65E**: Kein Trennzeichen: SYNTAX ERROR'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A65E**: IGNORE IF NOT AT END OF STATEMENT'
---

# $A65E — perform CLR

## Disassemblatura
```assembly
.A65E  D0 2D    BNE $A68D   ; exit if following byte to allow syntax error
.A660  20 E7 FF JSR $FFE7   ; close all channels and files
.A663  A5 37    LDA $37   ; get end of memory low byte
.A665  A4 38    LDY $38   ; get end of memory high byte
.A667  85 33    STA $33   ; set bottom of string space low byte, clear strings
.A669  84 34    STY $34   ; set bottom of string space high byte
.A66B  A5 2D    LDA $2D   ; get start of variables low byte
.A66D  A4 2E    LDY $2E   ; get start of variables high byte
.A66F  85 2F    STA $2F   ; set end of variables low byte, clear variables
.A671  84 30    STY $30   ; set end of variables high byte
.A673  85 31    STA $31   ; set end of arrays low byte, clear arrays
.A675  84 32    STY $32   ; set end of arrays high byte
```


## Commenti

### Original Disassembly (—)
- **$A65E**: exit if following byte to allow syntax error
- **$A660**: close all channels and files
- **$A663**: get end of memory low byte
- **$A665**: get end of memory high byte
- **$A667**: set bottom of string space low byte, clear strings
- **$A669**: set bottom of string space high byte
- **$A66B**: get start of variables low byte
- **$A66D**: get start of variables high byte
- **$A66F**: set end of variables low byte, clear variables
- **$A671**: set end of variables high byte
- **$A673**: set end of arrays low byte, clear arrays
- **$A675**: set end of arrays high byte

### Commodore-64-intern-Buch (Commodore)
- **$A65E**: Kein Trennzeichen: SYNTAX ERROR
- **$A660**: alle I/O Kanäle zurücksetzen
- **$A663**: Zeiger auf BASIC-RAM-Ende
- **$A665**: (LOW/HIGH) laden
- **$A667**: String-Start auf BASIC-
- **$A669**: RAM-Ende setzen
- **$A66B**: Zeiger auf Variablen-
- **$A66D**: start laden
- **$A66F**: und in Array-Anfangs-
- **$A671**: zeiger setzen
- **$A673**: und in Zeiger auf Array-
- **$A675**: Ende speichern
- **$A677**: RESTORE-Befehl
- **$A67A**: Wert laden und String-
- **$A67C**: Descriptor-Index zurücksetzen
- **$A67E**: 2 Bytes vom Stapel in das
- **$A67F**: Y-Register und den
- **$A680**: Akku holen
- **$A681**: Wert laden und damit
- **$A683**: Stapelzeiger initialisieren
- **$A684**: 2 Bytes aus dem Y-Register
- **$A685**: und dem Akku wieder auf
- **$A686**: den Stapel schieben
- **$A687**: Wert laden und damit
- **$A689**: CONT sperren
- **$A68B**: und in FN-Flag speichern
- **$A68D**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A65E**: IGNORE IF NOT AT END OF STATEMENT
- **$A663**: CLEAR STRING AREA
- **$A66B**: CLEAR ARRAY AREA
- **$A673**: LOW END OF FREE SPACE
- **$A677**: SET "DATA" POINTER TO BEGINNING
- **$A67E**: SAVE RETURN ADDRESS
- **$A681**: START STACK AT $F8,
- **$A683**: LEAVING ROOM FOR PARSING LINES
- **$A684**: RESTORE RETURN ADDRESS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*