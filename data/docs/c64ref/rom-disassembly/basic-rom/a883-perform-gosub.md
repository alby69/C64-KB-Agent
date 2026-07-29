---
title: perform GOSUB
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
- a883-basic-befehl-gosub
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A883
  address_end: $A89D
  symbol: perform-gosub
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A883**: need 6 bytes for GOSUB'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A883**: Wert für Prüfung'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A883**: BE SURE ENOUGH ROOM ON STACK'
---

# $A883 — perform GOSUB

## Disassemblatura
```assembly
.A883  A9 03    LDA #$03   ; need 6 bytes for GOSUB
.A885  20 FB A3 JSR $A3FB   ; check room on stack for 2*A bytes
.A888  A5 7B    LDA $7B   ; get BASIC execute pointer high byte
.A88A  48       PHA   ; save it
.A88B  A5 7A    LDA $7A   ; get BASIC execute pointer low byte
.A88D  48       PHA   ; save it
.A88E  A5 3A    LDA $3A   ; get current line number high byte
.A890  48       PHA   ; save it
.A891  A5 39    LDA $39   ; get current line number low byte
.A893  48       PHA   ; save it
.A894  A9 8D    LDA #$8D   ; token for GOSUB
.A896  48       PHA   ; save it
.A897  20 79 00 JSR $0079   ; scan memory
.A89A  20 A0 A8 JSR $A8A0   ; perform GOTO
.A89D  4C AE A7 JMP $A7AE   ; go do interpreter inner loop
```


## Commenti

### Original Disassembly (—)
- **$A883**: need 6 bytes for GOSUB
- **$A885**: check room on stack for 2*A bytes
- **$A888**: get BASIC execute pointer high byte
- **$A88A**: save it
- **$A88B**: get BASIC execute pointer low byte
- **$A88D**: save it
- **$A88E**: get current line number high byte
- **$A890**: save it
- **$A891**: get current line number low byte
- **$A893**: save it
- **$A894**: token for GOSUB
- **$A896**: save it
- **$A897**: scan memory
- **$A89A**: perform GOTO
- **$A89D**: go do interpreter inner loop

### Commodore-64-intern-Buch (Commodore)
- **$A883**: Wert für Prüfung
- **$A885**: prüft auf Platz im Stapel
- **$A888**: Programmzeiger (LOW-
- **$A88A**: und HIGH-Byte) laden
- **$A88B**: und auf den
- **$A88D**: Stapel retten
- **$A88E**: Zeilennummer laden (HIGH)
- **$A890**: und auf den Stapel legen
- **$A891**: Zeilennummer LOW laden
- **$A893**: und auf den Stapel legen
- **$A894**: 'GOSUB'-Code laden
- **$A896**: und auf den Stapel legen
- **$A897**: CHRGOT: letztes Zeichen holen
- **$A89A**: GOTO-Befehl
- **$A89D**: zur Interpreterschleife

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A883**: BE SURE ENOUGH ROOM ON STACK

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*