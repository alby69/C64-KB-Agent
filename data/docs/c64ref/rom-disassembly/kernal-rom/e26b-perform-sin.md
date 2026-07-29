---
title: perform SIN()
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
- e26b-basic-funktion-sin
- e284-fac-angle-as-a-fraction-of-a-full-circle
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  - marko_mäkelä.txt
  - bob_sander-cederlof.txt
  - magnus_nyman.txt
  address: $E26B
  address_end: $E2B1
  symbol: perform-sin
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E26B**: round and copy FAC1 to FAC2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E26B**: FAC runden und nach ARG'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E26E**: low  E2E5'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$E26E**: REMOVE MULTIPLES OF 2*PI'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: Nessun commento disponibile.
---

# $E26B — perform SIN()

## Disassemblatura
```assembly
.E26B  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.E26E  A9 E5    LDA #$E5   ; set 2*pi pointer low byte
.E270  A0 E2    LDY #$E2   ; set 2*pi pointer high byte
.E272  A6 6E    LDX $6E   ; get FAC2 sign (b7)
.E274  20 07 BB JSR $BB07   ; divide by (AY) (X=sign)
.E277  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.E27A  20 CC BC JSR $BCCC   ; perform INT()
.E27D  A9 00    LDA #$00   ; clear byte
.E27F  85 6F    STA $6F   ; clear sign compare (FAC1 EOR FAC2)
.E281  20 53 B8 JSR $B853   ; perform subtraction, FAC2 from FAC1
.E284  A9 EA    LDA #$EA   ; set 0.25 pointer low byte
.E286  A0 E2    LDY #$E2   ; set 0.25 pointer high byte
.E288  20 50 B8 JSR $B850   ; perform subtraction, FAC1 from (AY)
.E28B  A5 66    LDA $66   ; get FAC1 sign (b7)
.E28D  48       PHA   ; save FAC1 sign
.E28E  10 0D    BPL $E29D   ; branch if +ve FAC1 sign was -ve
.E290  20 49 B8 JSR $B849   ; add 0.5 to FAC1 (round FAC1)
.E293  A5 66    LDA $66   ; get FAC1 sign (b7)
.E295  30 09    BMI $E2A0   ; branch if -ve
.E297  A5 12    LDA $12   ; get the comparison evaluation flag
.E299  49 FF    EOR #$FF   ; toggle flag
.E29B  85 12    STA $12   ; save the comparison evaluation flag
.E29D  20 B4 BF JSR $BFB4   ; do - FAC1
.E2A0  A9 EA    LDA #$EA   ; set 0.25 pointer low byte
.E2A2  A0 E2    LDY #$E2   ; set 0.25 pointer high byte
.E2A4  20 67 B8 JSR $B867   ; add (AY) to FAC1
.E2A7  68       PLA   ; restore FAC1 sign
.E2A8  10 03    BPL $E2AD   ; branch if was +ve else correct FAC1
.E2AA  20 B4 BF JSR $BFB4   ; do - FAC1
.E2AD  A9 EF    LDA #$EF   ; set pointer low byte to counter
.E2AF  A0 E2    LDY #$E2   ; set pointer high byte to counter
.E2B1  4C 43 E0 JMP $E043   ; ^2 then series evaluation and return
```


## Commenti

### Original Disassembly (—)
- **$E26B**: round and copy FAC1 to FAC2
- **$E26E**: set 2*pi pointer low byte
- **$E270**: set 2*pi pointer high byte
- **$E272**: get FAC2 sign (b7)
- **$E274**: divide by (AY) (X=sign)
- **$E277**: round and copy FAC1 to FAC2
- **$E27A**: perform INT()
- **$E27D**: clear byte
- **$E27F**: clear sign compare (FAC1 EOR FAC2)
- **$E281**: perform subtraction, FAC2 from FAC1
- **$E284**: set 0.25 pointer low byte
- **$E286**: set 0.25 pointer high byte
- **$E288**: perform subtraction, FAC1 from (AY)
- **$E28B**: get FAC1 sign (b7)
- **$E28D**: save FAC1 sign
- **$E28E**: branch if +ve FAC1 sign was -ve
- **$E290**: add 0.5 to FAC1 (round FAC1)
- **$E293**: get FAC1 sign (b7)
- **$E295**: branch if -ve
- **$E297**: get the comparison evaluation flag
- **$E299**: toggle flag
- **$E29B**: save the comparison evaluation flag
- **$E29D**: do - FAC1
- **$E2A0**: set 0.25 pointer low byte
- **$E2A2**: set 0.25 pointer high byte
- **$E2A4**: add (AY) to FAC1
- **$E2A7**: restore FAC1 sign
- **$E2A8**: branch if was +ve else correct FAC1
- **$E2AA**: do - FAC1
- **$E2AD**: set pointer low byte to counter
- **$E2AF**: set pointer high byte to counter
- **$E2B1**: ^2 then series evaluation and return

### Commodore-64-intern-Buch (Commodore)
- **$E26B**: FAC runden und nach ARG
- **$E26E**: Zeiger auf
- **$E270**: Konstante Pi*2
- **$E272**: Vorzeichen von ARG
- **$E274**: FAC durch 2*Pi dividieren
- **$E277**: FAC runden und nach ARG
- **$E27A**: INT - Funktion
- **$E27D**: Vergleichsbyte
- **$E27F**: löschen
- **$E281**: ARG minus FAC
- **$E284**: Zeiger auf
- **$E286**: Konstante 0.25
- **$E288**: 0.25 - FAC
- **$E28B**: Vorzeichen laden
- **$E28D**: Vorzeichen in Stack
- **$E28E**: positiv ?
- **$E290**: FAC + 0.5
- **$E293**: Vorzeichen
- **$E295**: negativ ?
- **$E297**: Vorzeichen laden
- **$E299**: und umdrehen
- **$E29B**: Vorzeichen speichern
- **$E29D**: Vorzeichen wechseln
- **$E2A0**: Zeiger auf
- **$E2A2**: Konstante 0.25
- **$E2A4**: FAC + 0.25
- **$E2A7**: Vorzeichen holen
- **$E2A8**: positiv ?
- **$E2AA**: Vorzeichen wechseln
- **$E2AD**: Zeiger auf
- **$E2AF**: Polynomkoeffizienten
- **$E2B1**: Polynom berechnen

### Marko Mäkelä (Marko Mäkelä)
- **$E26E**: low  E2E5
- **$E270**: high E2E5
- **$E284**: low  E2EA
- **$E286**: high E2EA
- **$E2A0**: low  E2EA
- **$E2A2**: high E2EA

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$E26E**: REMOVE MULTIPLES OF 2*PI
- **$E270**: BY DIVIDING AND SAVING
- **$E272**: THE FRACTIONAL PART
- **$E274**: USE SIGN OF ARGUMENT
- **$E27A**: TAKE INTEGER PART
- **$E27D**: <<< WASTED LINES, BECAUSE FSUBT >>>
- **$E27F**: <<< CHANGES SGNCPR AGAIN        >>>
- **$E281**: SUBTRACT TO GET FRACTIONAL PART

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*