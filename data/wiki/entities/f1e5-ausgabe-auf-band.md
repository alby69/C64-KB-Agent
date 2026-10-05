---
id: f1e5-ausgabe-auf-band
type: entity
title: Ausgabe auf Band
aliases:
- Ausgabe auf Band
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f1e5-ausgabe-auf-band.md
  sha256: 71dd18c9b662426fff97fa96914a03a8ffa0080124499b94523259255296085c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f1e5-ausgabe-auf-band
---

# Ausgabe auf Band



# $F1E5 — Ausgabe auf Band

## Disassemblatura
```assembly
.F1E5  20 0D F8 JSR $F80D   ; Bandpuffer Zeiger erhöhen
.F1E8  D0 0E    BNE $F1F8   ; verzweige wenn Puffer nicht voll
.F1EA  20 64 F8 JSR $F864   ; Puffer auf Band schreiben
.F1ED  B0 0E    BCS $F1FD   ; STOP-Taste, dann Abbruch
.F1EF  A9 02    LDA #$02   ; Kontrollbyte für Datenblock
.F1F1  A0 00    LDY #$00   ; Pufferzeiger auf 0
.F1F3  91 B2    STA ($B2),Y   ; Akku in Puffer schreiben
.F1F5  C8       INY   ; Zeiger erhöhen
.F1F6  84 A6    STY $A6   ; und merken
.F1F8  A5 9E    LDA $9E   ; Datenbyte holen
.F1FA  91 B2    STA ($B2),Y   ; Zeichen in Puffer schreiben
.F1FC  18       CLC   ; Carry =0 (ok Kennzeichen)
.F1FD  68       PLA   ; X-Register
.F1FE  A8       TAY   ; und Y-Register
.F1FF  68       PLA   ; aus Stack
.F200  AA       TAX   ; holen
.F201  A5 9E    LDA $9E   ; Datenbyte zurückholen
.F203  90 02    BCC $F207   ; verzweige wenn ok
.F205  A9 00    LDA #$00   ; Flag für 'STOP-Taste gedrückt'
.F207  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F1E5**: Bandpuffer Zeiger erhöhen
- **$F1E8**: verzweige wenn Puffer nicht voll
- **$F1EA**: Puffer auf Band schreiben
- **$F1ED**: STOP-Taste, dann Abbruch
- **$F1EF**: Kontrollbyte für Datenblock
- **$F1F1**: Pufferzeiger auf 0
- **$F1F3**: Akku in Puffer schreiben
- **$F1F5**: Zeiger erhöhen
- **$F1F6**: und merken
- **$F1F8**: Datenbyte holen
- **$F1FA**: Zeichen in Puffer schreiben
- **$F1FC**: Carry =0 (ok Kennzeichen)
- **$F1FD**: X-Register
- **$F1FE**: und Y-Register
- **$F1FF**: aus Stack
- **$F200**: holen
- **$F201**: Datenbyte zurückholen
- **$F203**: verzweige wenn ok
- **$F205**: Flag für 'STOP-Taste gedrückt'
- **$F207**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f1e5-ausgabe-auf-band]]
