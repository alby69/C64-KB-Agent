---
title: RS-232 File schließen
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
- f2ab-rs-232-file-schlieen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F2AB
  address_end: $F2C5
  symbol: rs-232-file-schlieen
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F2AB**: Zeiger auf Parametereintrag'
---

# $F2AB — RS-232 File schließen

## Disassemblatura
```assembly
.F2AB  68       PLA   ; Zeiger auf Parametereintrag
.F2AC  20 F2 F2 JSR $F2F2   ; Fileeintrag in Tabelle löschen
.F2AF  20 83 F4 JSR $F483   ; CIAs für I/O rücksetzen
.F2B2  20 27 FE JSR $FE27   ; Memory-Top holen
.F2B5  A5 F8    LDA $F8   ; RS-232 Eingabepuffer HIGH-Byte laden
.F2B7  F0 01    BEQ $F2BA   ; verzweige wenn 0
.F2B9  C8       INY   ; HIGH-Byte von Memory-Top erhöhen
.F2BA  A5 FA    LDA $FA   ; RS-232 Ausgabepuffer HIGH-Byte laden
.F2BC  F0 01    BEQ $F2BF   ; verzweige wenn 0
.F2BE  C8       INY   ; sonst HIGH-Byte von Memory- Top erhöhen
.F2BF  A9 00    LDA #$00   ; 0 laden
.F2C1  85 F8    STA $F8   ; und Puffer
.F2C3  85 FA    STA $FA   ; freigeben
.F2C5  4C 7D F4 JMP $F47D   ; Memory Top neu setzen
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F2AB**: Zeiger auf Parametereintrag
- **$F2AC**: Fileeintrag in Tabelle löschen
- **$F2AF**: CIAs für I/O rücksetzen
- **$F2B2**: Memory-Top holen
- **$F2B5**: RS-232 Eingabepuffer HIGH-Byte laden
- **$F2B7**: verzweige wenn 0
- **$F2B9**: HIGH-Byte von Memory-Top erhöhen
- **$F2BA**: RS-232 Ausgabepuffer HIGH-Byte laden
- **$F2BC**: verzweige wenn 0
- **$F2BE**: sonst HIGH-Byte von Memory- Top erhöhen
- **$F2BF**: 0 laden
- **$F2C1**: und Puffer
- **$F2C3**: freigeben
- **$F2C5**: Memory Top neu setzen

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*