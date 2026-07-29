---
title: perform VAL()
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
- b7ad-basic-funktion-val
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B7AD
  address_end: $B7E0
  symbol: perform-val
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B7AD**: evaluate string, get length in A (and Y)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B7AD**: Stringadresse und Länge holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B7AD**: GET POINTER TO STRING IN INDEX'
---

# $B7AD — perform VAL()

## Disassemblatura
```assembly
.B7AD  20 82 B7 JSR $B782   ; evaluate string, get length in A (and Y)
.B7B0  D0 03    BNE $B7B5   ; branch if not null string string was null so set result = $00
.B7B2  4C F7 B8 JMP $B8F7   ; clear FAC1 exponent and sign and return
.B7B5  A6 7A    LDX $7A   ; get BASIC execute pointer low byte
.B7B7  A4 7B    LDY $7B   ; get BASIC execute pointer high byte
.B7B9  86 71    STX $71   ; save BASIC execute pointer low byte
.B7BB  84 72    STY $72   ; save BASIC execute pointer high byte
.B7BD  A6 22    LDX $22   ; get string pointer low byte
.B7BF  86 7A    STX $7A   ; save BASIC execute pointer low byte
.B7C1  18       CLC   ; clear carry for add
.B7C2  65 22    ADC $22   ; add string length
.B7C4  85 24    STA $24   ; save string end low byte
.B7C6  A6 23    LDX $23   ; get string pointer high byte
.B7C8  86 7B    STX $7B   ; save BASIC execute pointer high byte
.B7CA  90 01    BCC $B7CD   ; branch if no high byte increment
.B7CC  E8       INX   ; increment string end high byte
.B7CD  86 25    STX $25   ; save string end high byte
.B7CF  A0 00    LDY #$00   ; set index to $00
.B7D1  B1 24    LDA ($24),Y   ; get string end byte
.B7D3  48       PHA   ; push it
.B7D4  98       TYA   ; clear A
.B7D5  91 24    STA ($24),Y   ; terminate string with $00
.B7D7  20 79 00 JSR $0079   ; scan memory
.B7DA  20 F3 BC JSR $BCF3   ; get FAC1 from string
.B7DD  68       PLA   ; restore string end byte
.B7DE  A0 00    LDY #$00   ; clear index
.B7E0  91 24    STA ($24),Y   ; put string end byte back
```


## Commenti

### Original Disassembly (—)
- **$B7AD**: evaluate string, get length in A (and Y)
- **$B7B0**: branch if not null string string was null so set result = $00
- **$B7B2**: clear FAC1 exponent and sign and return
- **$B7B5**: get BASIC execute pointer low byte
- **$B7B7**: get BASIC execute pointer high byte
- **$B7B9**: save BASIC execute pointer low byte
- **$B7BB**: save BASIC execute pointer high byte
- **$B7BD**: get string pointer low byte
- **$B7BF**: save BASIC execute pointer low byte
- **$B7C1**: clear carry for add
- **$B7C2**: add string length
- **$B7C4**: save string end low byte
- **$B7C6**: get string pointer high byte
- **$B7C8**: save BASIC execute pointer high byte
- **$B7CA**: branch if no high byte increment
- **$B7CC**: increment string end high byte
- **$B7CD**: save string end high byte
- **$B7CF**: set index to $00
- **$B7D1**: get string end byte
- **$B7D3**: push it
- **$B7D4**: clear A
- **$B7D5**: terminate string with $00
- **$B7D7**: scan memory
- **$B7DA**: get FAC1 from string
- **$B7DD**: restore string end byte
- **$B7DE**: clear index
- **$B7E0**: put string end byte back

### Commodore-64-intern-Buch (Commodore)
- **$B7AD**: Stringadresse und Länge holen
- **$B7B0**: Stringlänge ungleich Null ?
- **$B7B2**: Null in FAC
- **$B7B5**: Programmzeiger
- **$B7B7**: holen
- **$B7B9**: und
- **$B7BB**: speichern
- **$B7BD**: Stringanfangsadresse
- **$B7BF**: in Stringzeiger bringen
- **$B7C1**: LOW-Byte des
- **$B7C2**: ersten Zeichens
- **$B7C4**: nach dem String speichern
- **$B7C6**: HIGH-Byte
- **$B7C8**: des ersten
- **$B7CA**: Zeichens
- **$B7CC**: nach dem String
- **$B7CD**: speichern
- **$B7CF**: Zähler auf Null
- **$B7D1**: erstes Byte nach String
- **$B7D3**: auf Stack
- **$B7D4**: speichern
- **$B7D5**: und durch null ersetzen
- **$B7D7**: CHRGOT letztes Zeichen holen
- **$B7DA**: String in Fließkommazahl umwandeln
- **$B7DD**: Zeichen nach String
- **$B7DE**: Zähler auf Null
- **$B7E0**: wieder zurücksetzen
- **$B7E2**: Die
- **$B7E4**: Programmzeiger
- **$B7E6**: wieder
- **$B7E8**: zurückholen
- **$B7EA**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B7AD**: GET POINTER TO STRING IN INDEX
- **$B7B0**: LENGTH NON-ZERO
- **$B7B2**: RETURN 0 IF LENGTH=0
- **$B7B5**: SAVE CURRENT TXTPTR
- **$B7BF**: POINT TXTPTR TO START OF STRING
- **$B7C2**: ADD LENGTH
- **$B7C4**: POINT DEST TO END OF STRING + 1
- **$B7CF**: SAVE BYTE THAT FOLLOWS STRING
- **$B7D1**: ON STACK
- **$B7D4**: AND STORE $00 IN ITS PLACE
- **$B7D5**: <<< THAT CAUSES A BUG IF HIMEM = $BFFF, >>> <<< BECAUSE STORING $00 AT $C000 IS NO  >>> <<< USE; $C000 WILL ALWAYS BE LAST CHAR >>> <<< TYPED, SO FIN WON'T TERMINATE UNTIL >>> <<< IT SEES A ZERO AT $C010!            >>>
- **$B7D7**: PRIME THE PUMP
- **$B7DA**: EVALUATE STRING
- **$B7DD**: GET BYTE THAT SHOULD FOLLOW STRING
- **$B7DE**: AND PUT IT BACK
- **$B7E0**: RESTORE TXTPTR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*