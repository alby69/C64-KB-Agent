---
title: perform LOG()
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
- b9ea-basic-funktion-log
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B9EA
  address_end: $BA26
  symbol: perform-log
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B9EA**: test sign and zero'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B9EA**: Vorzeichen holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B9FD**: low  B9D6'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B9EA**: GET -1,0,+1 IN A-REG FOR FAC'
---

# $B9EA — perform LOG()

## Disassemblatura
```assembly
.B9EA  20 2B BC JSR $BC2B   ; test sign and zero
.B9ED  F0 02    BEQ $B9F1   ; if zero do illegal quantity error then warm start
.B9EF  10 03    BPL $B9F4   ; skip error if +ve
.B9F1  4C 48 B2 JMP $B248   ; do illegal quantity error then warm start
.B9F4  A5 61    LDA $61   ; get FAC1 exponent
.B9F6  E9 7F    SBC #$7F   ; normalise it
.B9F8  48       PHA   ; save it
.B9F9  A9 80    LDA #$80   ; set exponent to zero
.B9FB  85 61    STA $61   ; save FAC1 exponent
.B9FD  A9 D6    LDA #$D6   ; pointer to 1/root 2 low byte
.B9FF  A0 B9    LDY #$B9   ; pointer to 1/root 2 high byte
.BA01  20 67 B8 JSR $B867   ; add (AY) to FAC1 (1/root2)
.BA04  A9 DB    LDA #$DB   ; pointer to root 2 low byte
.BA06  A0 B9    LDY #$B9   ; pointer to root 2 high byte
.BA08  20 0F BB JSR $BB0F   ; convert AY and do (AY)/FAC1 (root2/(x+(1/root2)))
.BA0B  A9 BC    LDA #$BC   ; pointer to 1 low byte
.BA0D  A0 B9    LDY #$B9   ; pointer to 1 high byte
.BA0F  20 50 B8 JSR $B850   ; subtract FAC1 ((root2/(x+(1/root2)))-1) from (AY)
.BA12  A9 C1    LDA #$C1   ; pointer to series for LOG(n) low byte
.BA14  A0 B9    LDY #$B9   ; pointer to series for LOG(n) high byte
.BA16  20 43 E0 JSR $E043   ; ^2 then series evaluation
.BA19  A9 E0    LDA #$E0   ; pointer to -0.5 low byte
.BA1B  A0 B9    LDY #$B9   ; pointer to -0.5 high byte
.BA1D  20 67 B8 JSR $B867   ; add (AY) to FAC1
.BA20  68       PLA   ; restore FAC1 exponent
.BA21  20 7E BD JSR $BD7E   ; evaluate new ASCII digit
.BA24  A9 E5    LDA #$E5   ; pointer to LOG(2) low byte
.BA26  A0 B9    LDY #$B9   ; pointer to LOG(2) high byte
```


## Commenti

### Original Disassembly (—)
- **$B9EA**: test sign and zero
- **$B9ED**: if zero do illegal quantity error then warm start
- **$B9EF**: skip error if +ve
- **$B9F1**: do illegal quantity error then warm start
- **$B9F4**: get FAC1 exponent
- **$B9F6**: normalise it
- **$B9F8**: save it
- **$B9F9**: set exponent to zero
- **$B9FB**: save FAC1 exponent
- **$B9FD**: pointer to 1/root 2 low byte
- **$B9FF**: pointer to 1/root 2 high byte
- **$BA01**: add (AY) to FAC1 (1/root2)
- **$BA04**: pointer to root 2 low byte
- **$BA06**: pointer to root 2 high byte
- **$BA08**: convert AY and do (AY)/FAC1 (root2/(x+(1/root2)))
- **$BA0B**: pointer to 1 low byte
- **$BA0D**: pointer to 1 high byte
- **$BA0F**: subtract FAC1 ((root2/(x+(1/root2)))-1) from (AY)
- **$BA12**: pointer to series for LOG(n) low byte
- **$BA14**: pointer to series for LOG(n) high byte
- **$BA16**: ^2 then series evaluation
- **$BA19**: pointer to -0.5 low byte
- **$BA1B**: pointer to -0.5 high byte
- **$BA1D**: add (AY) to FAC1
- **$BA20**: restore FAC1 exponent
- **$BA21**: evaluate new ASCII digit
- **$BA24**: pointer to LOG(2) low byte
- **$BA26**: pointer to LOG(2) high byte

### Commodore-64-intern-Buch (Commodore)
- **$B9EA**: Vorzeichen holen
- **$B9ED**: null ?, dann fertig
- **$B9EF**: positiv ?, dann ok
- **$B9F1**: 'ILLEGAL QUANTITY'
- **$B9F4**: Exponent
- **$B9F6**: normalisieren
- **$B9F8**: und merken
- **$B9F9**: Zahl in Bereich 0.5 bis 1
- **$B9FB**: bringen
- **$B9FD**: Zeiger auf
- **$B9FF**: Konstante 1/SQR(2)
- **$BA01**: zu FAC addieren
- **$BA04**: Zeiger auf
- **$BA06**: Konstante SQR(2)
- **$BA08**: SQR(2) durch FAC dividieren
- **$BA0B**: Zeiger
- **$BA0D**: auf Konstante 1
- **$BA0F**: 1 minus FAC
- **$BA12**: Zeiger auf
- **$BA14**: Polynomkoeffizienten
- **$BA16**: Polynomberechnung
- **$BA19**: Zeiger auf
- **$BA1B**: Konstante -0.5
- **$BA1D**: zu FAC addieren
- **$BA20**: Exponent zurückholen
- **$BA21**: FAC = FAC + FAC
- **$BA24**: Zeiger auf
- **$BA26**: Konstante LOG(2)

### Marko Mäkelä (Marko Mäkelä)
- **$B9FD**: low  B9D6
- **$B9FF**: high B9D6
- **$BA04**: low  B9DB
- **$BA06**: high B9DB
- **$BA0B**: low  B9BC
- **$BA0D**: high B9BC
- **$BA12**: low  B9C1
- **$BA14**: high B9C1
- **$BA19**: low  B9E0
- **$BA1B**: high B9E0
- **$BA24**: low  B9E5
- **$BA26**: high B9E5

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B9EA**: GET -1,0,+1 IN A-REG FOR FAC
- **$B9ED**: LOG (0) IS ILLEGAL
- **$B9EF**: >0 IS OK
- **$B9F1**: <= 0 IS NO GOOD
- **$B9F4**: FIRST GET LOG BASE 2
- **$B9F6**: SAVE UNBIASED EXPONENT
- **$B9F9**: NORMALIZE BETWEEN .5 AND 1
- **$BA01**: COMPUTE VIA SERIES OF ODD
- **$BA04**: POWERS OF
- **$BA06**: (SQR(2)X-1)/(SQR(2)X+1)
- **$BA21**: ADD ORIGINAL EXPONENT
- **$BA24**: MULTIPLY BY LOG(2) TO FORM
- **$BA26**: NATURAL LOG OF X

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*