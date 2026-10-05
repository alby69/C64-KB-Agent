---
id: b761-pull-string-data-and-byte-parameter-from-stack
type: entity
title: pull string data and byte parameter from stack
aliases:
- pull string data and byte parameter from stack
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b761-pull-string-data-and-byte-parameter-from-stack.md
  sha256: 128869faa4008fa5f00662a0c16407dcb22b958b8f8e7c2a0cb48371eb1f5d0d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b761-pull-string-data-and-byte-parameter-from-stack
---

# pull string data and byte parameter from stack



# $B761 — pull string data and byte parameter from stack

## Disassemblatura
```assembly
.B761  20 F7 AE JSR $AEF7   ; scan for ")", else do syntax error then warm start
.B764  68       PLA   ; pull return address low byte
.B765  A8       TAY   ; save return address low byte
.B766  68       PLA   ; pull return address high byte
.B767  85 55    STA $55   ; save return address high byte
.B769  68       PLA   ; dump call to function vector low byte
.B76A  68       PLA   ; dump call to function vector high byte
.B76B  68       PLA   ; pull byte parameter
.B76C  AA       TAX   ; copy byte parameter to X
.B76D  68       PLA   ; pull string pointer low byte
.B76E  85 50    STA $50   ; save it
.B770  68       PLA   ; pull string pointer high byte
.B771  85 51    STA $51   ; save it
.B773  A5 55    LDA $55   ; get return address high byte
.B775  48       PHA   ; back on stack
.B776  98       TYA   ; get return address low byte
.B777  48       PHA   ; back on stack
.B778  A0 00    LDY #$00   ; clear index
.B77A  8A       TXA   ; copy byte parameter
.B77B  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B761**: scan for ")", else do syntax error then warm start
- **$B764**: pull return address low byte
- **$B765**: save return address low byte
- **$B766**: pull return address high byte
- **$B767**: save return address high byte
- **$B769**: dump call to function vector low byte
- **$B76A**: dump call to function vector high byte
- **$B76B**: pull byte parameter
- **$B76C**: copy byte parameter to X
- **$B76D**: pull string pointer low byte
- **$B76E**: save it
- **$B770**: pull string pointer high byte
- **$B771**: save it
- **$B773**: get return address high byte
- **$B775**: back on stack
- **$B776**: get return address low byte
- **$B777**: back on stack
- **$B778**: clear index
- **$B77A**: copy byte parameter

### Commodore-64-intern-Buch (Commodore)
- **$B761**: prüft auf Klammer zu
- **$B764**: LOW-Byte der
- **$B765**: Aufrufadresse merken
- **$B766**: HIGH-Byte der
- **$B767**: Aufrufadresse merken
- **$B769**: LOW-und HIGH-Byte der
- **$B76A**: Aufrufadresse merken
- **$B76B**: 1. Parameter holen
- **$B76C**: und ins X-Reg
- **$B76D**: LOW- und HIGH-Byte
- **$B76E**: des
- **$B770**: Stringdescriptors
- **$B771**: nach
- **$B773**: $51 und $52 speichern
- **$B775**: Aufrufadresse
- **$B776**: wieder auf
- **$B777**: Stack
- **$B778**: Zähler auf Null
- **$B77A**: Länge, zweiter Parameter
- **$B77B**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B761**: REQUIRE ")"
- **$B764**: SAVE RETURN ADDRESS
- **$B765**: IN Y-REG AND LENGTH
- **$B769**: POP PREVIOUS RETURN ADDRESS
- **$B76A**: (FROM GOROUT).
- **$B76B**: RETRIEVE 1ST PARAMETER
- **$B76D**: GET ADDRESS OF STRING DESCRIPTOR
- **$B773**: RESTORE RETURN ADDRESS
- **$B77A**: GET 1ST PARAMETER IN A-REG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b761-pull-string-data-and-byte-parameter-from-stack]]
