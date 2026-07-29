---
title: perform TAN()
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e2b4-basic-funktion-tan
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  - marko_mäkelä.txt
  - bob_sander-cederlof.txt
  - magnus_nyman.txt
  address: $E2B4
  address_end: $E2D9
  symbol: perform-tan
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E2B4**: pack FAC1 into $57'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E2B4**: FAC nach Akku#3'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E2BE**: low  004E'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E2B7**: SIGNFLG WILL BE TOGGLED IF 2ND OR 3RD'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: Nessun commento disponibile.
---

# $E2B4 — perform TAN()

## Disassemblatura
```assembly
.E2B4  20 CA BB JSR $BBCA   ; pack FAC1 into $57
.E2B7  A9 00    LDA #$00   ; clear A
.E2B9  85 12    STA $12   ; clear the comparison evaluation flag
.E2BB  20 6B E2 JSR $E26B   ; perform SIN()
.E2BE  A2 4E    LDX #$4E   ; set sin(n) pointer low byte
.E2C0  A0 00    LDY #$00   ; set sin(n) pointer high byte
.E2C2  20 F6 E0 JSR $E0F6   ; pack FAC1 into (XY)
.E2C5  A9 57    LDA #$57   ; set n pointer low byte
.E2C7  A0 00    LDY #$00   ; set n pointer high byte
.E2C9  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
.E2CC  A9 00    LDA #$00   ; clear byte
.E2CE  85 66    STA $66   ; clear FAC1 sign (b7)
.E2D0  A5 12    LDA $12   ; get the comparison evaluation flag
.E2D2  20 DC E2 JSR $E2DC   ; save flag and go do series evaluation
.E2D5  A9 4E    LDA #$4E   ; set sin(n) pointer low byte
.E2D7  A0 00    LDY #$00   ; set sin(n) pointer high byte
.E2D9  4C 0F BB JMP $BB0F   ; convert AY and do (AY)/FAC1
```


## Commenti

### Original Disassembly (—)
- **$E2B4**: pack FAC1 into $57
- **$E2B7**: clear A
- **$E2B9**: clear the comparison evaluation flag
- **$E2BB**: perform SIN()
- **$E2BE**: set sin(n) pointer low byte
- **$E2C0**: set sin(n) pointer high byte
- **$E2C2**: pack FAC1 into (XY)
- **$E2C5**: set n pointer low byte
- **$E2C7**: set n pointer high byte
- **$E2C9**: unpack memory (AY) into FAC1
- **$E2CC**: clear byte
- **$E2CE**: clear FAC1 sign (b7)
- **$E2D0**: get the comparison evaluation flag
- **$E2D2**: save flag and go do series evaluation
- **$E2D5**: set sin(n) pointer low byte
- **$E2D7**: set sin(n) pointer high byte
- **$E2D9**: convert AY and do (AY)/FAC1

### Commodore-64-intern-Buch (Commodore)
- **$E2B4**: FAC nach Akku#3
- **$E2B7**: Flag
- **$E2B9**: setzen
- **$E2BB**: SIN berechnen
- **$E2BE**: Zeiger auf
- **$E2C0**: Hilfsakku
- **$E2C2**: FAC nach Hilfsakku
- **$E2C5**: Zeiger auf
- **$E2C7**: Akku#3
- **$E2C9**: Akku#3 nach FAC
- **$E2CC**: Vorzeichen
- **$E2CE**: löschen
- **$E2D0**: Flag
- **$E2D2**: COS berechnen
- **$E2D5**: Zeiger auf
- **$E2D7**: Hilfsakku (SIN)
- **$E2D9**: durch FAC dividieren
- **$E2DC**: COS
- **$E2DD**: berechnen

### Marko Mäkelä (Marko Mäkelä)
- **$E2BE**: low  004E
- **$E2C0**: high 004E
- **$E2C5**: low  005F
- **$E2C7**: high 005F
- **$E2D5**: low  004E
- **$E2D7**: high 004E

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E2B7**: SIGNFLG WILL BE TOGGLED IF 2ND OR 3RD
- **$E2B9**: QUADRANT
- **$E2BB**: GET SIN(X)
- **$E2BE**: SAVE SIN(X) IN TEMP3
- **$E2C2**: <<<FUNNY WAY TO CALL MOVMF! >>>
- **$E2C5**: RETRIEVE X
- **$E2CC**: AND COMPUTE COS(X)
- **$E2D2**: WEIRD &amp; DANGEROUS WAY TO GET INTO SIN
- **$E2D5**: NOW FORM SIN/COS
- **$E2DC**: SHAME, SHAME!
- **$E2E0**: PI/2
- **$E2E5**: 2*PI
- **$E2EA**: 1/4
- **$E2EF**: POWER OF POLYNOMIAL
- **$E2F0**: (2PI)^11/11!
- **$E2F5**: (2PI)^9/9!
- **$E2FA**: (2PI)^7/7!
- **$E2FF**: (2PI)^5/5!
- **$E304**: (2PI)^3/3!
- **$E309**: 2PI

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*