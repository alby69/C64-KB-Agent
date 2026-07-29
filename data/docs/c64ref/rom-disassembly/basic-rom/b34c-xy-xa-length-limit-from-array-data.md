---
title: XY = XA = length * limit from array data
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
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
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $B34C
  address_end: $B37C
  symbol: xy-xa-length-limit-from-array-data
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B34C**: Register merken'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B34C**: SAVE Y-REG'
---

# $B34C — XY = XA = length * limit from array data

## Disassemblatura
```assembly
.B34C  84 22    STY $22
.B34E  B1 5F    LDA ($5F),Y
.B350  85 28    STA $28
.B352  88       DEY
.B353  B1 5F    LDA ($5F),Y
.B355  85 29    STA $29
.B357  A9 10    LDA #$10
.B359  85 5D    STA $5D
.B35B  A2 00    LDX #$00
.B35D  A0 00    LDY #$00
.B35F  8A       TXA
.B360  0A       ASL
.B361  AA       TAX
.B362  98       TYA
.B363  2A       ROL
.B364  A8       TAY
.B365  B0 A4    BCS $B30B
.B367  06 71    ASL $71
.B369  26 72    ROL $72
.B36B  90 0B    BCC $B378
.B36D  18       CLC
.B36E  8A       TXA
.B36F  65 28    ADC $28
.B371  AA       TAX
.B372  98       TYA
.B373  65 29    ADC $29
.B375  A8       TAY
.B376  B0 93    BCS $B30B
.B378  C6 5D    DEC $5D
.B37A  D0 E3    BNE $B35F
.B37C  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B34C**: Register merken
- **$B34E**: 1. Wert holen
- **$B350**: und abspeichern
- **$B352**: Zeiger vermindern
- **$B353**: 2. Wert holen
- **$B355**: und abspeichern
- **$B357**: Wert laden und damit
- **$B359**: Verschiebezähler setzen
- **$B35B**: LOW- und HIGH-Byte des Er-
- **$B35D**: gebnisregisters auf 0 setzen
- **$B35F**: LOW-Byte in Akku holen und
- **$B360**: um 1 Bit nach links schieben
- **$B361**: Byte zurück ins X-Reg.
- **$B362**: HIGH-Byte in den Akku holen,
- **$B363**: um 1 Bit nach links rotieren
- **$B364**: und zurückbringen
- **$B365**: Überlauf: 'out of memory'
- **$B367**: nächstes Bit aus
- **$B369**: $71/72 herausholen
- **$B36B**: =0? ja: Addition umgehen
- **$B36D**: Carry setzen (Addition)
- **$B36E**: LOW-Byte holen
- **$B36F**: 1. Wert addieren
- **$B371**: LOW-Byte zurückbringen
- **$B372**: HIGH-Byte holen
- **$B373**: 2. Wert addieren
- **$B375**: HIGH-Byte zurückholen
- **$B376**: Überlauf: 'out of memory'
- **$B378**: nächstes Bit holen
- **$B37A**: alle 16 Bits? nein: weiter
- **$B37C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B34C**: SAVE Y-REG
- **$B34E**: GET MULTIPLIER
- **$B350**: SAVE IN RESULT+2,3
- **$B355**: LOW BYTE OF MULTIPLIER
- **$B357**: MULTIPLY 16 BITS
- **$B35B**: PRODUCT = 0 INITIALLY
- **$B35F**: DOUBLE PRODUCT
- **$B360**: LOW BYTE
- **$B362**: HIGH BYTE
- **$B363**: IF TOO LARGE, SET CARRY
- **$B365**: TOO LARGE, "MEM FULL ERROR"
- **$B367**: NEXT BIT OF MUTLPLICAND
- **$B369**: INTO CARRY
- **$B36B**: BIT=0, DON'T NEED TO ADD
- **$B36D**: BIT=1, ADD INTO PARTIAL PRODUCT
- **$B376**: TOO LARGE, "MEM FULL ERROR"
- **$B378**: 16-BITS YET?
- **$B37A**: NO, KEEP SHUFFLING
- **$B37C**: YES, PRODUCT IN Y,X AND A,X

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*