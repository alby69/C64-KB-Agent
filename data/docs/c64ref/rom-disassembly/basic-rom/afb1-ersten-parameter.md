---
title: ersten Parameter
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- afb1-ersten-parameter
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AFB1
  address_end: $AFCE
  symbol: ersten-parameter
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AFB1**: prüft auf Klammer auf'
---

# $AFB1 — ersten Parameter

## Disassemblatura
```assembly
.AFB1  20 FA AE JSR $AEFA   ; prüft auf Klammer auf
.AFB4  20 9E AD JSR $AD9E   ; FRMEVL holen beliebigen Term
.AFB7  20 FD AE JSR $AEFD   ; prüft auf Komma
.AFBA  20 8F AD JSR $AD8F   ; prüft auf String
.AFBD  68       PLA   ; Funktionstoken left$, r$, m$
.AFBE  AA       TAX   ; Akku nach X holen
.AFBF  A5 65    LDA $65   ; Adresse des
.AFC1  48       PHA   ; Stringdescriptors
.AFC2  A5 64    LDA $64   ; holen und auf den Stapel
.AFC4  48       PHA   ; retten (LOW und HIGH)
.AFC5  8A       TXA   ; Akku wiederholen
.AFC6  48       PHA   ; Token auf den Stapel retten
.AFC7  20 9E B7 JSR $B79E   ; holt Byte-Wert (2. Parameter)
.AFCA  68       PLA   ; Token zurückholen
.AFCB  A8       TAY   ; und ins Y-Reg.
.AFCC  8A       TXA   ; 2. Bytewert in den Akku laden
.AFCD  48       PHA   ; und auf den Stapel retten
.AFCE  4C D6 AF JMP $AFD6   ; Routine ausführen
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AFB1**: prüft auf Klammer auf
- **$AFB4**: FRMEVL holen beliebigen Term
- **$AFB7**: prüft auf Komma
- **$AFBA**: prüft auf String
- **$AFBD**: Funktionstoken left$, r$, m$
- **$AFBE**: Akku nach X holen
- **$AFBF**: Adresse des
- **$AFC1**: Stringdescriptors
- **$AFC2**: holen und auf den Stapel
- **$AFC4**: retten (LOW und HIGH)
- **$AFC5**: Akku wiederholen
- **$AFC6**: Token auf den Stapel retten
- **$AFC7**: holt Byte-Wert (2. Parameter)
- **$AFCA**: Token zurückholen
- **$AFCB**: und ins Y-Reg.
- **$AFCC**: 2. Bytewert in den Akku laden
- **$AFCD**: und auf den Stapel retten
- **$AFCE**: Routine ausführen

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*