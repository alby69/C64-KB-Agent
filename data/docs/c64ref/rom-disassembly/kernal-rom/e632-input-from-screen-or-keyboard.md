---
title: input from screen or keyboard
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
- e632-holen
- e63a-get-character-from-current-screen-line
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E632
  address_end: $E683
  symbol: input-from-screen-or-keyboard
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E632**: copy Y'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E632**: die'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E632**: preserve (X) and (Y) registers'
---

# $E632 — input from screen or keyboard

## Disassemblatura
```assembly
.E632  98       TYA   ; copy Y
.E633  48       PHA   ; save Y
.E634  8A       TXA   ; copy X
.E635  48       PHA   ; save X
.E636  A5 D0    LDA $D0   ; input from keyboard or screen, $xx = screen, $00 = keyboard
.E638  F0 93    BEQ $E5CD   ; if keyboard go wait for key
.E63A  A4 D3    LDY $D3   ; get the cursor column
.E63C  B1 D1    LDA ($D1),Y   ; get character from the current screen line
.E63E  85 D7    STA $D7   ; save temporary last character
.E640  29 3F    AND #$3F   ; mask key bits
.E642  06 D7    ASL $D7   ; << temporary last character
.E644  24 D7    BIT $D7   ; test it
.E646  10 02    BPL $E64A   ; branch if not [NO KEY]
.E648  09 80    ORA #$80
.E64A  90 04    BCC $E650
.E64C  A6 D4    LDX $D4   ; get the cursor quote flag, $xx = quote, $00 = no quote
.E64E  D0 04    BNE $E654   ; if in quote mode go ??
.E650  70 02    BVS $E654
.E652  09 40    ORA #$40
.E654  E6 D3    INC $D3   ; increment the cursor column
.E656  20 84 E6 JSR $E684   ; if open quote toggle the cursor quote flag
.E659  C4 C8    CPY $C8   ; compare ?? with input [EOL] pointer
.E65B  D0 17    BNE $E674   ; if not at line end go ??
.E65D  A9 00    LDA #$00   ; clear A
.E65F  85 D0    STA $D0   ; clear input from keyboard or screen, $xx = screen, $00 = keyboard
.E661  A9 0D    LDA #$0D   ; set character [CR]
.E663  A6 99    LDX $99   ; get the input device number
.E665  E0 03    CPX #$03   ; compare the input device with the screen
.E667  F0 06    BEQ $E66F   ; if screen go ??
.E669  A6 9A    LDX $9A   ; get the output device number
.E66B  E0 03    CPX #$03   ; compare the output device with the screen
.E66D  F0 03    BEQ $E672   ; if screen go ??
.E66F  20 16 E7 JSR $E716   ; output the character
.E672  A9 0D    LDA #$0D   ; set character [CR]
.E674  85 D7    STA $D7   ; save character
.E676  68       PLA   ; pull X
.E677  AA       TAX   ; restore X
.E678  68       PLA   ; pull Y
.E679  A8       TAY   ; restore Y
.E67A  A5 D7    LDA $D7   ; restore character
.E67C  C9 DE    CMP #$DE
.E67E  D0 02    BNE $E682
.E680  A9 FF    LDA #$FF
.E682  18       CLC   ; flag ok
.E683  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E632**: copy Y
- **$E633**: save Y
- **$E634**: copy X
- **$E635**: save X
- **$E636**: input from keyboard or screen, $xx = screen, $00 = keyboard
- **$E638**: if keyboard go wait for key
- **$E63A**: get the cursor column
- **$E63C**: get character from the current screen line
- **$E63E**: save temporary last character
- **$E640**: mask key bits
- **$E642**: << temporary last character
- **$E644**: test it
- **$E646**: branch if not [NO KEY]
- **$E64C**: get the cursor quote flag, $xx = quote, $00 = no quote
- **$E64E**: if in quote mode go ??
- **$E654**: increment the cursor column
- **$E656**: if open quote toggle the cursor quote flag
- **$E659**: compare ?? with input [EOL] pointer
- **$E65B**: if not at line end go ??
- **$E65D**: clear A
- **$E65F**: clear input from keyboard or screen, $xx = screen, $00 = keyboard
- **$E661**: set character [CR]
- **$E663**: get the input device number
- **$E665**: compare the input device with the screen
- **$E667**: if screen go ??
- **$E669**: get the output device number
- **$E66B**: compare the output device with the screen
- **$E66D**: if screen go ??
- **$E66F**: output the character
- **$E672**: set character [CR]
- **$E674**: save character
- **$E676**: pull X
- **$E677**: restore X
- **$E678**: pull Y
- **$E679**: restore Y
- **$E67A**: restore character
- **$E682**: flag ok

### Commodore-64-intern-Buch (Commodore)
- **$E632**: die
- **$E633**: Re-
- **$E634**: gister
- **$E635**: retten
- **$E636**: CR-Flag
- **$E638**: nein, dann zur Warteschleife
- **$E63A**: Spalte
- **$E63C**: Zeichen vom Bildschirm holen
- **$E63E**: und
- **$E640**: nach
- **$E642**: ASCII
- **$E644**: wandeln
- **$E646**: wenn Bit 6 nicht gesetzt, dann zu $E64A
- **$E648**: Bit 7 setzen
- **$E64A**: Zeichen nicht revers ?, dann zu $E650
- **$E64C**: Hochkommaflag nicht
- **$E64E**: gesetzt ?, dann zu $E654
- **$E650**: wenn ja, dann zu $E654
- **$E652**: Bit 6 im Zeichen setzen
- **$E654**: Cursor eins weiter setzen
- **$E656**: auf Hochkomma testen
- **$E659**: Cursor in letzter Spalte ?
- **$E65B**: wenn nicht, dann zu $E674
- **$E65D**: Zeile
- **$E65F**: vollständig gelesen
- **$E661**: 'CR'
- **$E663**: ans Ende der Zeile setzen
- **$E665**: Eingabe vom Bildschirm ?
- **$E667**: ja, dann zu $E66F
- **$E669**: Ausgabe auf Bildschirm
- **$E66B**: ja, dann
- **$E66D**: zu $E672
- **$E66F**: Zeichen auf Bildschirm schreiben
- **$E672**: Wert für
- **$E674**: 'CR'
- **$E676**: die
- **$E677**: Register
- **$E678**: zürück-
- **$E679**: holen
- **$E67A**: Bildschirm-Kode
- **$E67C**: mit Kode für Pi vergleichen
- **$E67E**: nein ?, dann fertig
- **$E680**: ja ?, durch BASIC-Kode für Pi ersetzen
- **$E682**: Carry löschen
- **$E683**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E632**: preserve (X) and (Y) registers
- **$E636**: CRSW, INPUT/GET from keyboard or screen
- **$E638**: input from keyboard
- **$E63A**: PNTR, cursor column
- **$E63C**: read from current screen address
- **$E63E**: temp store
- **$E64C**: QTSW, editor in quotes mode
- **$E64E**: yepp
- **$E654**: PNTR
- **$E656**: do quotes test
- **$E659**: INDX, end of logical line for input
- **$E65F**: CRSW
- **$E663**: DFLTN, default input device
- **$E665**: screen
- **$E667**: yes
- **$E669**: DFLTO, default output device
- **$E66B**: screen
- **$E66D**: yes
- **$E66F**: output to screen
- **$E677**: restore (X) and (Y) registers

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*