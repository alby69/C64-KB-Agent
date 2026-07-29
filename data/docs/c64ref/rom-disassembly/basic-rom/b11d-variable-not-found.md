---
title: variable not found
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
  address: $B11D
  address_end: $B183
  symbol: variable-not-found
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B11E**: Aufrufadresse prüfen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B12C**: T'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B11D**: LOOK AT RETURN ADDRESS ON STACK TO'
---

# $B11D — variable not found

## Disassemblatura
```assembly
.B11D  68       PLA
.B11E  48       PHA
.B11F  C9 2A    CMP #$2A
.B121  D0 05    BNE $B128
.B123  A9 13    LDA #$13
.B125  A0 BF    LDY #$BF
.B127  60       RTS
.B128  A5 45    LDA $45
.B12A  A4 46    LDY $46
.B12C  C9 54    CMP #$54   ; T
.B12E  D0 0B    BNE $B13B
.B130  C0 C9    CPY #$C9   ; I$
.B132  F0 EF    BEQ $B123
.B134  C0 49    CPY #$49   ; I
.B136  D0 03    BNE $B13B
.B138  4C 08 AF JMP $AF08
.B13B  C9 53    CMP #$53   ; S
.B13D  D0 04    BNE $B143
.B13F  C0 54    CPY #$54   ; T
.B141  F0 F5    BEQ $B138
.B143  A5 2F    LDA $2F
.B145  A4 30    LDY $30
.B147  85 5F    STA $5F
.B149  84 60    STY $60
.B14B  A5 31    LDA $31
.B14D  A4 32    LDY $32
.B14F  85 5A    STA $5A
.B151  84 5B    STY $5B
.B153  18       CLC
.B154  69 07    ADC #$07
.B156  90 01    BCC $B159
.B158  C8       INY
.B159  85 58    STA $58
.B15B  84 59    STY $59
.B15D  20 B8 A3 JSR $A3B8
.B160  A5 58    LDA $58
.B162  A4 59    LDY $59
.B164  C8       INY
.B165  85 2F    STA $2F
.B167  84 30    STY $30
.B169  A0 00    LDY #$00
.B16B  A5 45    LDA $45
.B16D  91 5F    STA ($5F),Y
.B16F  C8       INY
.B170  A5 46    LDA $46
.B172  91 5F    STA ($5F),Y
.B174  A9 00    LDA #$00
.B176  C8       INY
.B177  91 5F    STA ($5F),Y
.B179  C8       INY
.B17A  91 5F    STA ($5F),Y
.B17C  C8       INY
.B17D  91 5F    STA ($5F),Y
.B17F  C8       INY
.B180  91 5F    STA ($5F),Y
.B182  C8       INY
.B183  91 5F    STA ($5F),Y
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B11E**: Aufrufadresse prüfen
- **$B11F**: Aufruf von FRMEVL?
- **$B121**: nein: dann neu anlegen
- **$B123**: Zeiger auf Konstante 0
- **$B125**: (LOW und HIGH)
- **$B127**: Rücksprung
- **$B128**: LOW- und HIGH-Byte
- **$B12A**: des Variablennames
- **$B12C**: 'T'-Code?
- **$B12E**: nein: $B13B
- **$B130**: 'I$'-Code?
- **$B132**: ja: TI$
- **$B134**: 'I'-Code?
- **$B136**: nein: $B13B
- **$B138**: 'SYNTAX ERROR'
- **$B13B**: 'S'-Code?
- **$B13D**: nein: $B143
- **$B13F**: 'T'-Code?
- **$B141**: ST, dann 'SYNTAX ERROR'
- **$B143**: LOW- und HIGH-Byte des
- **$B145**: Zeigers auf Arraytabelle
- **$B147**: laden und
- **$B149**: merken
- **$B14B**: LOW- und HIGH-Byte des
- **$B14D**: Zeigers auf Ende der
- **$B14F**: Arraytabelle
- **$B151**: merken
- **$B153**: Carry für Addition setzen
- **$B154**: um 7 verschieben für Anlage
- **$B156**: einer neuen Variablen
- **$B158**: Übertrag addieren
- **$B159**: LOW- und HIGH-Byte des
- **$B15B**: neuen Blockendes speichern
- **$B15D**: Block verschieben
- **$B160**: Werte
- **$B162**: wiederholen
- **$B164**: und damit
- **$B165**: Zeiger auf Arraytabelle
- **$B167**: neu setzen
- **$B169**: Zeiger setzen
- **$B16B**: erster Buchstabe des Namens
- **$B16D**: und speichern
- **$B16F**: Zeiger erhöhen,
- **$B170**: zweiten Buchstaben holen
- **$B172**: und abspeichern
- **$B174**: Nullwert laden
- **$B176**: Zeiger erhöhen
- **$B177**: nächsten 5 Werte
- **$B179**: der Variable auf 0 setzen
- **$B17A**: 2. Byte speichern
- **$B17C**: Zeiger erhöhen
- **$B17D**: 3. Byte speichern
- **$B17F**: Zeiger erhöhen
- **$B180**: 4. Byte speichern
- **$B182**: Zeiger erhöhen
- **$B183**: 5. Byte speichern
- **$B185**: Zeiger auf Variablenwert
- **$B187**: Carry löschen (Addition)
- **$B188**: zwei für Namen addieren
- **$B18A**: in Zeiger auf Variable
- **$B18C**: Zeiger auf erstes Byte
- **$B18E**: High-Byte $48 erhöhen
- **$B18F**: als Variablenzeiger
- **$B191**: nach $47/48 speichern
- **$B193**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$B12C**: T
- **$B130**: I$
- **$B134**: I
- **$B13B**: S
- **$B13F**: T

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B11D**: LOOK AT RETURN ADDRESS ON STACK TO
- **$B11E**: SEE IF CALLED FROM FRM.VARIABLE
- **$B121**: NO
- **$B123**: YES, CALLED FROM FRM.VARIABLE
- **$B125**: POINT TO A CONSTANT ZERO
- **$B127**: NEW VARIABLE USED IN EXPRESSION = 0

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*