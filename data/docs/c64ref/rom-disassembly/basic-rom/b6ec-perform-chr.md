---
title: perform CHR$()
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
- b6ec-basic-funktion-chr
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B6EC
  address_end: $B6FD
  symbol: perform-chr
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B6EC**: evaluate byte expression, result in X'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B6EC**: holt Byte-Wert (0 bis 255)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B6EC**: CONVERT ARGUMENT TO BYTE IN X'
---

# $B6EC — perform CHR$()

## Disassemblatura
```assembly
.B6EC  20 A1 B7 JSR $B7A1   ; evaluate byte expression, result in X
.B6EF  8A       TXA   ; copy to A
.B6F0  48       PHA   ; save character
.B6F1  A9 01    LDA #$01   ; string is single byte
.B6F3  20 7D B4 JSR $B47D   ; make string space A bytes long
.B6F6  68       PLA   ; get character back
.B6F7  A0 00    LDY #$00   ; clear index
.B6F9  91 62    STA ($62),Y   ; save byte in string - byte IS string!
.B6FB  68       PLA   ; dump return address (skip type check)
.B6FC  68       PLA   ; dump return address (skip type check)
.B6FD  4C CA B4 JMP $B4CA   ; check space on descriptor stack then put string address and length on descriptor stack and update stack pointers
```


## Commenti

### Original Disassembly (—)
- **$B6EC**: evaluate byte expression, result in X
- **$B6EF**: copy to A
- **$B6F0**: save character
- **$B6F1**: string is single byte
- **$B6F3**: make string space A bytes long
- **$B6F6**: get character back
- **$B6F7**: clear index
- **$B6F9**: save byte in string - byte IS string!
- **$B6FB**: dump return address (skip type check)
- **$B6FC**: dump return address (skip type check)
- **$B6FD**: check space on descriptor stack then put string address and length on descriptor stack and update stack pointers

### Commodore-64-intern-Buch (Commodore)
- **$B6EC**: holt Byte-Wert (0 bis 255)
- **$B6EF**: Kode in Akku
- **$B6F0**: Akkuinhalt in Stack
- **$B6F1**: Länge des Strings gleich 1
- **$B6F3**: Platz für String freimachen
- **$B6F6**: ASCII-Kode zurückholen
- **$B6F7**: Zähler auf Null
- **$B6F9**: als Stringzeichen speichern
- **$B6FB**: Rücksprungadresse aus
- **$B6FC**: Stack entfernen
- **$B6FD**: Descriptor in Stringstack

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B6EC**: CONVERT ARGUMENT TO BYTE IN X
- **$B6F0**: SAVE IT
- **$B6F1**: GET SPACE FOR STRING OF LENGTH 1
- **$B6F6**: RECALL THE CHARACTER
- **$B6F7**: PUT IN STRING
- **$B6FB**: POP RETURN ADDRESS
- **$B6FD**: MAKE IT A TEMPORARY STRING

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*