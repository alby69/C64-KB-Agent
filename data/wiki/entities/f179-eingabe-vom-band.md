---
id: f179-eingabe-vom-band
type: entity
title: Eingabe vom Band
aliases:
- Eingabe vom Band
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f179-eingabe-vom-band.md
  sha256: 1b551a53cf7a35a2407f69f37e9d7da620bf37ad05fccb135ca05d18525b0331
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f179-eingabe-vom-band
---

# Eingabe vom Band



# $F179 — Eingabe vom Band

## Disassemblatura
```assembly
.F179  86 97    STX $97   ; X-Register merken
.F17B  20 99 F1 JSR $F199   ; ein Zeichen vom Band holen
.F17E  B0 16    BCS $F196   ; verzweige bei Fehler
.F180  48       PHA   ; Akku retten
.F181  20 99 F1 JSR $F199   ; ein Zeichen vom Band holen
.F184  B0 0D    BCS $F193   ; verzweige bei Fehler
.F186  D0 05    BNE $F18D   ; letzes Zeichen ?
.F188  A9 40    LDA #$40   ; Code für 'End of Identify'
.F18A  20 1C FE JSR $FE1C   ; Status setzen
.F18D  C6 A6    DEC $A6   ; Bandpuffer Zeiger erniedrigen
.F18F  A6 97    LDX $97   ; X-Register zurückholen
.F191  68       PLA   ; geholtes Zeichen in Akku
.F192  60       RTS   ; Rücksprung
.F193  AA       TAX   ; Fehlernummer ins X-Register
.F194  68       PLA   ; Stack normalisieren
.F195  8A       TXA   ; Fehlernummer in Akku
.F196  A6 97    LDX $97   ; X-Register zurückholen
.F198  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F179**: X-Register merken
- **$F17B**: ein Zeichen vom Band holen
- **$F17E**: verzweige bei Fehler
- **$F180**: Akku retten
- **$F181**: ein Zeichen vom Band holen
- **$F184**: verzweige bei Fehler
- **$F186**: letzes Zeichen ?
- **$F188**: Code für 'End of Identify'
- **$F18A**: Status setzen
- **$F18D**: Bandpuffer Zeiger erniedrigen
- **$F18F**: X-Register zurückholen
- **$F191**: geholtes Zeichen in Akku
- **$F192**: Rücksprung
- **$F193**: Fehlernummer ins X-Register
- **$F194**: Stack normalisieren
- **$F195**: Fehlernummer in Akku
- **$F196**: X-Register zurückholen
- **$F198**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f179-eingabe-vom-band]]
