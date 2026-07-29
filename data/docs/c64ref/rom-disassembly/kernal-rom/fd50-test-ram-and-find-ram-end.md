---
title: test RAM and find RAM end
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- '0000'
- '0001'
- fd50-arbeitsspei-initialisieren
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FD50
  address_end: $FD9A
  symbol: test-ram-and-find-ram-end
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FD50**: clear A'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FD50**: Wert zum Löschen laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FD53**: Fill pages 0,2,3 with zeros'
---

# $FD50 — test RAM and find RAM end

## Disassemblatura
```assembly
.FD50  A9 00    LDA #$00   ; clear A
.FD52  A8       TAY   ; clear index
.FD53  99 02 00 STA $0002,Y   ; clear page 0, don't do $0000 or $0001
.FD56  99 00 02 STA $0200,Y   ; clear page 2
.FD59  99 00 03 STA $0300,Y   ; clear page 3
.FD5C  C8       INY   ; increment index
.FD5D  D0 F4    BNE $FD53   ; loop if more to do
.FD5F  A2 3C    LDX #$3C   ; set cassette buffer pointer low byte
.FD61  A0 03    LDY #$03   ; set cassette buffer pointer high byte
.FD63  86 B2    STX $B2   ; save tape buffer start pointer low byte
.FD65  84 B3    STY $B3   ; save tape buffer start pointer high byte
.FD67  A8       TAY   ; clear Y
.FD68  A9 03    LDA #$03   ; set RAM test pointer high byte
.FD6A  85 C2    STA $C2   ; save RAM test pointer high byte
.FD6C  E6 C2    INC $C2   ; increment RAM test pointer high byte
.FD6E  B1 C1    LDA ($C1),Y
.FD70  AA       TAX
.FD71  A9 55    LDA #$55
.FD73  91 C1    STA ($C1),Y
.FD75  D1 C1    CMP ($C1),Y
.FD77  D0 0F    BNE $FD88
.FD79  2A       ROL
.FD7A  91 C1    STA ($C1),Y
.FD7C  D1 C1    CMP ($C1),Y
.FD7E  D0 08    BNE $FD88
.FD80  8A       TXA
.FD81  91 C1    STA ($C1),Y
.FD83  C8       INY
.FD84  D0 E8    BNE $FD6E
.FD86  F0 E4    BEQ $FD6C
.FD88  98       TYA
.FD89  AA       TAX
.FD8A  A4 C2    LDY $C2
.FD8C  18       CLC
.FD8D  20 2D FE JSR $FE2D   ; set the top of memory
.FD90  A9 08    LDA #$08
.FD92  8D 82 02 STA $0282   ; save the OS start of memory high byte
.FD95  A9 04    LDA #$04
.FD97  8D 88 02 STA $0288   ; save the screen memory page
.FD9A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FD50**: clear A
- **$FD52**: clear index
- **$FD53**: clear page 0, don't do $0000 or $0001
- **$FD56**: clear page 2
- **$FD59**: clear page 3
- **$FD5C**: increment index
- **$FD5D**: loop if more to do
- **$FD5F**: set cassette buffer pointer low byte
- **$FD61**: set cassette buffer pointer high byte
- **$FD63**: save tape buffer start pointer low byte
- **$FD65**: save tape buffer start pointer high byte
- **$FD67**: clear Y
- **$FD68**: set RAM test pointer high byte
- **$FD6A**: save RAM test pointer high byte
- **$FD6C**: increment RAM test pointer high byte
- **$FD8D**: set the top of memory
- **$FD92**: save the OS start of memory high byte
- **$FD97**: save the screen memory page

### Commodore-64-intern-Buch (Commodore)
- **$FD50**: Wert zum Löschen laden
- **$FD52**: als Zähler nach Y
- **$FD53**: Zeropage,
- **$FD56**: Page 2 und
- **$FD59**: Page 3 löschen
- **$FD5C**: Zähler vermindern
- **$FD5D**: weiter wenn nicht fertig
- **$FD5F**: Werte für Startadresse
- **$FD61**: des Bandpuffers laden
- **$FD63**: Bandpuffer Zeiger
- **$FD65**: auf $033C setzen
- **$FD67**: Zeiger in Y auf 0 setzen
- **$FD68**: Wert für RAM testen ($04-1)
- **$FD6A**: Startadresse (HIGH) des RAM
- **$FD6C**: setzen und auf $0400 erhöhen
- **$FD6E**: Wert holen
- **$FD70**: Wert merken
- **$FD71**: %01010101 ($55)
- **$FD73**: abspeichern und über-
- **$FD75**: prüfen, ob Wert drin ist
- **$FD77**: ungleich dann kein RAM
- **$FD79**: %10101010
- **$FD7A**: Wert abspeichern und
- **$FD7C**: überprüfen, ob Wert drin ist
- **$FD7E**: ungleich dann kein RAM
- **$FD80**: Wert wieder zurückholen
- **$FD81**: und wieder zurückschreiben
- **$FD83**: Zeiger erhöhen
- **$FD84**: Pageende? nein: weiter
- **$FD86**: sonst Zeiger-HIGH erhöhen
- **$FD88**: Zeiger-LOW ins
- **$FD89**: X-Register bringen
- **$FD8A**: Zeiger-HIGH holen
- **$FD8C**: C=0 (Flag für setzen)
- **$FD8D**: Memory (RAM) Top setzen
- **$FD90**: HIGH-Byte der Startadresse
- **$FD92**: Memory (RAM) Start auf $800
- **$FD95**: HIGH-Byte der Startadresse
- **$FD97**: Video-RAM auf $400
- **$FD9A**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FD53**: Fill pages 0,2,3 with zeros
- **$FD5D**: all 256 bytes
- **$FD61**: Set tapebuffer to $033c
- **$FD63**: Variables TAPE1 is used.
- **$FD6E**: Perform memorytest. Starting at $0400 and upwards.
- **$FD70**: Store temporary in X-reg
- **$FD73**: Write #$55 into memory
- **$FD75**: and compare.
- **$FD77**: if not equal... ROM
- **$FD7A**: Write #$AA into same memory
- **$FD7C**: and compare again.
- **$FD7E**: if not equal... ROM
- **$FD81**: Restore stored value
- **$FD84**: Next memorypos
- **$FD86**: New page in memory
- **$FD88**: The memorytest always exits when reaching a ROM
- **$FD8D**: Set top of memory. X and Y holds address.
- **$FD92**: Set pointer to bottom of memory ($0800)
- **$FD97**: Set pointer to bottom of screen ($0400)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*