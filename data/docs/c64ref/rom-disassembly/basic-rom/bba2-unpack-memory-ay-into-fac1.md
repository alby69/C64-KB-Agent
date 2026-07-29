---
title: unpack memory (AY) into FAC1
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
- bba2-bertragen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BBA2
  address_end: $BBC6
  symbol: unpack-memory-ay-into-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BBA2**: save pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BBA2**: Zeiger'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BBA2**: USE INDEX FOR PNTR'
---

# $BBA2 — unpack memory (AY) into FAC1

## Disassemblatura
```assembly
.BBA2  85 22    STA $22   ; save pointer low byte
.BBA4  84 23    STY $23   ; save pointer high byte
.BBA6  A0 04    LDY #$04   ; 5 bytes to do
.BBA8  B1 22    LDA ($22),Y   ; get fifth byte
.BBAA  85 65    STA $65   ; save FAC1 mantissa 4
.BBAC  88       DEY   ; decrement index
.BBAD  B1 22    LDA ($22),Y   ; get fourth byte
.BBAF  85 64    STA $64   ; save FAC1 mantissa 3
.BBB1  88       DEY   ; decrement index
.BBB2  B1 22    LDA ($22),Y   ; get third byte
.BBB4  85 63    STA $63   ; save FAC1 mantissa 2
.BBB6  88       DEY   ; decrement index
.BBB7  B1 22    LDA ($22),Y   ; get second byte
.BBB9  85 66    STA $66   ; save FAC1 sign (b7)
.BBBB  09 80    ORA #$80   ; set 1xxx xxxx (add normal bit)
.BBBD  85 62    STA $62   ; save FAC1 mantissa 1
.BBBF  88       DEY   ; decrement index
.BBC0  B1 22    LDA ($22),Y   ; get first byte (exponent)
.BBC2  85 61    STA $61   ; save FAC1 exponent
.BBC4  84 70    STY $70   ; clear FAC1 rounding byte
.BBC6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BBA2**: save pointer low byte
- **$BBA4**: save pointer high byte
- **$BBA6**: 5 bytes to do
- **$BBA8**: get fifth byte
- **$BBAA**: save FAC1 mantissa 4
- **$BBAC**: decrement index
- **$BBAD**: get fourth byte
- **$BBAF**: save FAC1 mantissa 3
- **$BBB1**: decrement index
- **$BBB2**: get third byte
- **$BBB4**: save FAC1 mantissa 2
- **$BBB6**: decrement index
- **$BBB7**: get second byte
- **$BBB9**: save FAC1 sign (b7)
- **$BBBB**: set 1xxx xxxx (add normal bit)
- **$BBBD**: save FAC1 mantissa 1
- **$BBBF**: decrement index
- **$BBC0**: get first byte (exponent)
- **$BBC2**: save FAC1 exponent
- **$BBC4**: clear FAC1 rounding byte

### Commodore-64-intern-Buch (Commodore)
- **$BBA2**: Zeiger
- **$BBA4**: setzen
- **$BBA6**: Zähler setzen
- **$BBA8**: LOW-Byte
- **$BBAA**: der
- **$BBAC**: Mantisse
- **$BBAD**: und
- **$BBAF**: HIGH-
- **$BBB1**: Byte
- **$BBB2**: der
- **$BBB4**: Mantisse
- **$BBB6**: in
- **$BBB7**: FAC
- **$BBB9**: holen
- **$BBBB**: Vorzeichen
- **$BBBD**: der
- **$BBBF**: Man-
- **$BBC0**: tisse
- **$BBC2**: Exponent
- **$BBC4**: Rundungsstelle
- **$BBC6**: Rücksprung
- **$BBC7**: Adresse LOW
- **$BBC9**: Akku #4

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BBA2**: USE INDEX FOR PNTR
- **$BBA6**: PICK UP 5 BYTES
- **$BBB9**: FIRST BIT IS SIGN
- **$BBBB**: SET NORMALIZED INVISIBLE BIT
- **$BBC2**: EXPONENT
- **$BBC4**: Y=0

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*