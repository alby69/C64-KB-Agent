---
title: delete old line
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
  address: $A4A9
  address_end: $A4EB
  symbol: delete-old-line
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A4A9**: Zeiger setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $A4A9 — delete old line

## Disassemblatura
```assembly
.A4A9  A0 01    LDY #$01
.A4AB  B1 5F    LDA ($5F),Y
.A4AD  85 23    STA $23
.A4AF  A5 2D    LDA $2D
.A4B1  85 22    STA $22
.A4B3  A5 60    LDA $60
.A4B5  85 25    STA $25
.A4B7  A5 5F    LDA $5F
.A4B9  88       DEY
.A4BA  F1 5F    SBC ($5F),Y
.A4BC  18       CLC
.A4BD  65 2D    ADC $2D
.A4BF  85 2D    STA $2D
.A4C1  85 24    STA $24
.A4C3  A5 2E    LDA $2E
.A4C5  69 FF    ADC #$FF
.A4C7  85 2E    STA $2E
.A4C9  E5 60    SBC $60
.A4CB  AA       TAX
.A4CC  38       SEC
.A4CD  A5 5F    LDA $5F
.A4CF  E5 2D    SBC $2D
.A4D1  A8       TAY
.A4D2  B0 03    BCS $A4D7
.A4D4  E8       INX
.A4D5  C6 25    DEC $25
.A4D7  18       CLC
.A4D8  65 22    ADC $22
.A4DA  90 03    BCC $A4DF
.A4DC  C6 23    DEC $23
.A4DE  18       CLC
.A4DF  B1 22    LDA ($22),Y
.A4E1  91 24    STA ($24),Y
.A4E3  C8       INY
.A4E4  D0 F9    BNE $A4DF
.A4E6  E6 23    INC $23
.A4E8  E6 25    INC $25
.A4EA  CA       DEX
.A4EB  D0 F2    BNE $A4DF
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A4A9**: Zeiger setzen
- **$A4AB**: Startadresse der nächsten
- **$A4AD**: Zeile (HIGH) setzen
- **$A4AF**: Variablenanfangszeiger
- **$A4B1**: (LOW) setzen
- **$A4B3**: Startadresse der zu
- **$A4B5**: löschenden Zeile (HIGH)
- **$A4B7**: Startadresse der zu
- **$A4B9**: löschenden Zeile (LOW)
- **$A4BA**: Startadresse der nächsten
- **$A4BC**: Zeile (LOW)
- **$A4BD**: Variablenanfangszeiger (LOW)
- **$A4BF**: ergibt neuen Variablenan-
- **$A4C1**: fangszeiger (LOW)
- **$A4C3**: Gleiches System für
- **$A4C5**: HIGH-Byte des Variablenan-
- **$A4C7**: fangszeigers
- **$A4C9**: minus Startadresse der zu
- **$A4CB**: löschenden Zeile (LOW) ergibt
- **$A4CC**: die zu verschiebenden Blöcke
- **$A4CD**: Startadresse (LOW) minus
- **$A4CF**: Variablenanfangszeiger (LOW)
- **$A4D1**: ergibt Länge des Restabschn.
- **$A4D2**: Größer als 255? Nein: $A4D7
- **$A4D4**: Zähler für Blöcke erhöhen
- **$A4D5**: Transportzeiger vermindern
- **$A4D7**: Carry löschen
- **$A4D8**: Anfangszeiger (LOW)
- **$A4DA**: Verminderung überspringen
- **$A4DC**: Zeiger um 1 vermindern
- **$A4DE**: Carry löschen
- **$A4DF**: Verschiebeschleife
- **$A4E1**: Wert abspeichern
- **$A4E3**: Zähler um 1 erhöhen
- **$A4E4**: Block fertig? Nein: weiter
- **$A4E6**: 1.Adreßzeiger erhöhen (LOW)
- **$A4E8**: 2.Adreßzeiger erhöhen (LOW)
- **$A4EA**: Blockzähter um 1 vermindern
- **$A4EB**: Alle Blöcke? Nein: weiter

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*