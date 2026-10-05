---
id: b737-perform-mid
type: entity
title: perform MID$()
aliases:
- perform MID$()
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b737-perform-mid.md
  sha256: ff4f16377bfcd7f4d939b7ed00fd386e5efe82db935c33fe5a100e29f4cc80b4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b737-perform-mid
---

# perform MID$()



# $B737 — perform MID$()

## Disassemblatura
```assembly
.B737  A9 FF    LDA #$FF   ; set default length = 255
.B739  85 65    STA $65   ; save default length
.B73B  20 79 00 JSR $0079   ; scan memory
.B73E  C9 29    CMP #$29   ; compare with ")"
.B740  F0 06    BEQ $B748   ; branch if = ")" (skip second byte get)
.B742  20 FD AE JSR $AEFD   ; scan for ",", else do syntax error then warm start
.B745  20 9E B7 JSR $B79E   ; get byte parameter
.B748  20 61 B7 JSR $B761   ; pull string data and byte parameter from stack return pointer in descriptor, byte in A (and X), Y=0
.B74B  F0 4B    BEQ $B798   ; if null do illegal quantity error then warm start
.B74D  CA       DEX   ; decrement start index
.B74E  8A       TXA   ; copy to A
.B74F  48       PHA   ; save string start offset
.B750  18       CLC   ; clear carry for sub-1
.B751  A2 00    LDX #$00   ; clear output string length
.B753  F1 50    SBC ($50),Y   ; subtract string length
.B755  B0 B6    BCS $B70D   ; if start>string length go do null string
.B757  49 FF    EOR #$FF   ; complement -length
.B759  C5 65    CMP $65   ; compare byte parameter
.B75B  90 B1    BCC $B70E   ; if length>remaining string go do RIGHT$
.B75D  A5 65    LDA $65   ; get length byte
.B75F  B0 AD    BCS $B70E   ; go do string copy, branch always
```


## Commenti

### Original Disassembly (—)
- **$B737**: set default length = 255
- **$B739**: save default length
- **$B73B**: scan memory
- **$B73E**: compare with ")"
- **$B740**: branch if = ")" (skip second byte get)
- **$B742**: scan for ",", else do syntax error then warm start
- **$B745**: get byte parameter
- **$B748**: pull string data and byte parameter from stack return pointer in descriptor, byte in A (and X), Y=0
- **$B74B**: if null do illegal quantity error then warm start
- **$B74D**: decrement start index
- **$B74E**: copy to A
- **$B74F**: save string start offset
- **$B750**: clear carry for sub-1
- **$B751**: clear output string length
- **$B753**: subtract string length
- **$B755**: if start>string length go do null string
- **$B757**: complement -length
- **$B759**: compare byte parameter
- **$B75B**: if length>remaining string go do RIGHT$
- **$B75D**: get length byte
- **$B75F**: go do string copy, branch always

### Commodore-64-intern-Buch (Commodore)
- **$B737**: Ersatzwert für den zweiten
- **$B739**: Zahlenparameter
- **$B73B**: CHRGOT letztes Zeichen holen
- **$B73E**: ')' Klammer zu
- **$B740**: wenn ja, dann kein zweiter Parameter, weiter bei $B748
- **$B742**: prüft auf Komma
- **$B745**: holt Byte-Wert des zweiten Parameters
- **$B748**: Stringparameter und Startposition holen
- **$B74B**: 1. Parameter null, 'ILLEGAL QUANTITY'
- **$B74D**: erste Elementposition
- **$B74E**: innerhalb
- **$B74F**: des alten Strings
- **$B750**: im Stack ablegen
- **$B751**: Zähler setzen
- **$B753**: alte Stringlänge kleiner als erster Parameter ?
- **$B755**: wenn ja, dann zu LEFT$
- **$B757**: Berechnen der neuen Länge
- **$B759**: wenn kleiner als zweiter
- **$B75B**: Parameter, dann zu LEFT$
- **$B75D**: Zweitparameter als 'rechte' Stringbegrenzung
- **$B75F**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
- **$B737**: default 3 parameter
- **$B73E**: )

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B737**: FLAG WHETHER 2ND PARAMETER
- **$B73B**: SEE IF ")" YET
- **$B740**: YES, NO 2ND PARAMETER
- **$B742**: NO, MUST HAVE COMMA
- **$B745**: GET 2ND PARAM IN X-REG
- **$B74D**: 1ST PARAMETER - 1
- **$B759**: USE SMALLER OF TWO
- **$B75F**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b737-perform-mid]]
