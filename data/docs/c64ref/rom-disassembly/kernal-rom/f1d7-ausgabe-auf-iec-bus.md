---
title: Ausgabe auf IEC-Bus
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f1d7-ausgabe-auf-iec-bus
- f1dd-output-the-character-to-the-cassette-or-rs232-device
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F1D7
  address_end: $F1E3
  symbol: ausgabe-auf-iec-bus
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F1D7**: Datenbyte retten'
---

# $F1D7 — Ausgabe auf IEC-Bus

## Disassemblatura
```assembly
.F1D7  68       PLA   ; Datenbyte retten
.F1D8  4C DD ED JMP $EDDD   ; ein Byte auf IEC-Bus ausgeben
.F1DB  4A       LSR   ; Bit 0 der Ausgabekanal- Nummer ins Carry
.F1DC  68       PLA   ; Datenbyte wiederholen
.F1DD  85 9E    STA $9E   ; auszugebendes Zeichen merken
.F1DF  8A       TXA   ; X-Register
.F1E0  48       PHA   ; und Y-Register
.F1E1  98       TYA   ; auf Stack
.F1E2  48       PHA   ; retten
.F1E3  90 23    BCC $F208   ; RS-232 Ausgabe
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F1D7**: Datenbyte retten
- **$F1D8**: ein Byte auf IEC-Bus ausgeben
- **$F1DB**: Bit 0 der Ausgabekanal- Nummer ins Carry
- **$F1DC**: Datenbyte wiederholen
- **$F1DD**: auszugebendes Zeichen merken
- **$F1DF**: X-Register
- **$F1E0**: und Y-Register
- **$F1E1**: auf Stack
- **$F1E2**: retten
- **$F1E3**: RS-232 Ausgabe

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*