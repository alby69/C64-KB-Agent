---
title: save descriptor from $61-$63 on stack
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $B4CA
  address_end: $B4F3
  symbol: save-descriptor-from-61-63-on-stack
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B4CA**: Stringdescriptor-Zeiger'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $B4CA — save descriptor from $61-$63 on stack

## Disassemblatura
```assembly
.B4CA  A6 16    LDX $16
.B4CC  E0 22    CPX #$22
.B4CE  D0 05    BNE $B4D5
.B4D0  A2 19    LDX #$19
.B4D2  4C 37 A4 JMP $A437
.B4D5  A5 61    LDA $61
.B4D7  95 00    STA $00,X
.B4D9  A5 62    LDA $62
.B4DB  95 01    STA $01,X
.B4DD  A5 63    LDA $63
.B4DF  95 02    STA $02,X
.B4E1  A0 00    LDY #$00
.B4E3  86 64    STX $64
.B4E5  84 65    STY $65
.B4E7  84 70    STY $70
.B4E9  88       DEY
.B4EA  84 0D    STY $0D
.B4EC  86 17    STX $17
.B4EE  E8       INX
.B4EF  E8       INX
.B4F0  E8       INX
.B4F1  86 16    STX $16
.B4F3  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B4CA**: Stringdescriptor-Zeiger
- **$B4CC**: Stringstapel voll?
- **$B4CE**: nein: $B4D5
- **$B4D0**: Nr für 'formula too complex'
- **$B4D2**: Fehlermeldung ausgeben
- **$B4D5**: Stringlänge holen und
- **$B4D7**: Stringstapel speichern
- **$B4D9**: LOW- und HIGH-Byte der
- **$B4DB**: Adresse holen
- **$B4DD**: und in
- **$B4DF**: Stringstapel bringen
- **$B4E1**: Nullwert laden
- **$B4E3**: und Zeiger
- **$B4E5**: jetzt auf Descriptor setzen
- **$B4E7**: Zeiger für Polynomauswertung
- **$B4E9**: Register vermindern
- **$B4EA**: Stringflag setzen $FF
- **$B4EC**: Index des letzten
- **$B4EE**: Stringdescriptors
- **$B4EF**: um drei erhöhen
- **$B4F0**: und als
- **$B4F1**: neuen Index merken
- **$B4F3**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*