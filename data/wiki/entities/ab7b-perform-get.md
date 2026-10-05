---
id: ab7b-perform-get
type: entity
title: perform GET
aliases:
- perform GET
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab7b-perform-get.md
  sha256: 0537571df5ed7bc9976a76cca08f1b29a6349cb8052079f8fe06affa68bca73b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ab7b-perform-get
---

# perform GET



# $AB7B — perform GET

## Disassemblatura
```assembly
.AB7B  20 A6 B3 JSR $B3A6   ; check not Direct, back here if ok
.AB7E  C9 23    CMP #$23   ; compare with "#"
.AB80  D0 10    BNE $AB92   ; branch if not GET#
.AB82  20 73 00 JSR $0073   ; increment and scan memory
.AB85  20 9E B7 JSR $B79E   ; get byte parameter
.AB88  A9 2C    LDA #$2C   ; set ","
.AB8A  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.AB8D  86 13    STX $13   ; set current I/O channel
.AB8F  20 1E E1 JSR $E11E   ; open channel for input with error check
.AB92  A2 01    LDX #$01   ; set pointer low byte
.AB94  A0 02    LDY #$02   ; set pointer high byte
.AB96  A9 00    LDA #$00   ; clear A
.AB98  8D 01 02 STA $0201   ; ensure null terminator
.AB9B  A9 40    LDA #$40   ; input mode = GET
.AB9D  20 0F AC JSR $AC0F   ; perform the GET part of READ
.ABA0  A6 13    LDX $13   ; get current I/O channel
.ABA2  D0 13    BNE $ABB7   ; if not default channel go do channel close and return
.ABA4  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$AB7B**: check not Direct, back here if ok
- **$AB7E**: compare with "#"
- **$AB80**: branch if not GET#
- **$AB82**: increment and scan memory
- **$AB85**: get byte parameter
- **$AB88**: set ","
- **$AB8A**: scan for CHR$(A), else do syntax error then warm start
- **$AB8D**: set current I/O channel
- **$AB8F**: open channel for input with error check
- **$AB92**: set pointer low byte
- **$AB94**: set pointer high byte
- **$AB96**: clear A
- **$AB98**: ensure null terminator
- **$AB9B**: input mode = GET
- **$AB9D**: perform the GET part of READ
- **$ABA0**: get current I/O channel
- **$ABA2**: if not default channel go do channel close and return

### Commodore-64-intern-Buch (Commodore)
- **$AB7B**: Testet auf Direkt-Modus
- **$AB7E**: folgt '#’?
- **$AB80**: nein: $AB92
- **$AB82**: CHRGET nächstes Zeichen holen
- **$AB85**: Byte-Wert holen
- **$AB88**: ',' Komma
- **$AB8A**: prüft auf Code
- **$AB8D**: Filenummer
- **$AB8F**: CHKIN, Eingabe vorbereiten
- **$AB92**: Zeiger auf
- **$AB94**: Pufferende = $201 ein Zeichen
- **$AB96**: Wert laden und
- **$AB98**: Puffer mit $0 abschließen
- **$AB9B**: GET-Flag
- **$AB9D**: Wertzuweisung an Variable
- **$ABA0**: Eingabegerät
- **$ABA2**: nicht Tastatur, dann CLRCH
- **$ABA4**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$AB7E**: #
- **$AB88**: comma
- **$AB9B**: GET code

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AB7B**: ILLEGAL IF IN DIRECT MODE
- **$AB92**: SIMULATE INPUT
- **$AB9B**: SET UP INPUTFLG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ab7b-perform-get]]
