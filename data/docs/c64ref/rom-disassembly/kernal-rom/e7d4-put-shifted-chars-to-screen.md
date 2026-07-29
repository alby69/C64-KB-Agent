---
title: put shifted chars to screen
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
- e7d4-zeichen-grer-127
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $E7D4
  address_end: $E879
  symbol: put-shifted-chars-to-screen
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E7D4**: Kode größer 127, Bit 7 löschen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E7D4**: remove shift bit'
---

# $E7D4 — put shifted chars to screen

## Disassemblatura
```assembly
.E7D4  29 7F    AND #$7F   ; remove shift bit
.E7D6  C9 7F    CMP #$7F   ; code for PI
.E7D8  D0 02    BNE $E7DC
.E7DA  A9 5E    LDA #$5E   ; screen PI
.E7DC  C9 20    CMP #$20
.E7DE  90 03    BCC $E7E3
.E7E0  4C 91 E6 JMP $E691
.E7E3  C9 0D    CMP #$0D   ; shift return
.E7E5  D0 03    BNE $E7EA
.E7E7  4C 91 E8 JMP $E891
.E7EA  A6 D4    LDX $D4
.E7EC  D0 3F    BNE $E82D
.E7EE  C9 14    CMP #$14   ; insert
.E7F0  D0 37    BNE $E829
.E7F2  A4 D5    LDY $D5
.E7F4  B1 D1    LDA ($D1),Y
.E7F6  C9 20    CMP #$20
.E7F8  D0 04    BNE $E7FE
.E7FA  C4 D3    CPY $D3
.E7FC  D0 07    BNE $E805
.E7FE  C0 4F    CPY #$4F
.E800  F0 24    BEQ $E826
.E802  20 65 E9 JSR $E965
.E805  A4 D5    LDY $D5
.E807  20 24 EA JSR $EA24
.E80A  88       DEY
.E80B  B1 D1    LDA ($D1),Y
.E80D  C8       INY
.E80E  91 D1    STA ($D1),Y
.E810  88       DEY
.E811  B1 F3    LDA ($F3),Y
.E813  C8       INY
.E814  91 F3    STA ($F3),Y
.E816  88       DEY
.E817  C4 D3    CPY $D3
.E819  D0 EF    BNE $E80A
.E81B  A9 20    LDA #$20
.E81D  91 D1    STA ($D1),Y
.E81F  AD 86 02 LDA $0286
.E822  91 F3    STA ($F3),Y
.E824  E6 D8    INC $D8
.E826  4C A8 E6 JMP $E6A8
.E829  A6 D8    LDX $D8
.E82B  F0 05    BEQ $E832
.E82D  09 40    ORA #$40
.E82F  4C 97 E6 JMP $E697
.E832  C9 11    CMP #$11   ; csr up
.E834  D0 16    BNE $E84C
.E836  A6 D6    LDX $D6
.E838  F0 37    BEQ $E871
.E83A  C6 D6    DEC $D6
.E83C  A5 D3    LDA $D3
.E83E  38       SEC
.E83F  E9 28    SBC #$28
.E841  90 04    BCC $E847
.E843  85 D3    STA $D3
.E845  10 2A    BPL $E871
.E847  20 6C E5 JSR $E56C
.E84A  D0 25    BNE $E871
.E84C  C9 12    CMP #$12   ; reverse off
.E84E  D0 04    BNE $E854
.E850  A9 00    LDA #$00
.E852  85 C7    STA $C7
.E854  C9 1D    CMP #$1D   ; csr left
.E856  D0 12    BNE $E86A
.E858  98       TYA
.E859  F0 09    BEQ $E864
.E85B  20 A1 E8 JSR $E8A1
.E85E  88       DEY
.E85F  84 D3    STY $D3
.E861  4C A8 E6 JMP $E6A8
.E864  20 01 E7 JSR $E701
.E867  4C A8 E6 JMP $E6A8
.E86A  C9 13    CMP #$13   ; clr code
.E86C  D0 06    BNE $E874
.E86E  20 44 E5 JSR $E544
.E871  4C A8 E6 JMP $E6A8
.E874  09 80    ORA #$80
.E876  20 CB E8 JSR $E8CB
.E879  4C 4F EC JMP $EC4F
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$E7D4**: Kode größer 127, Bit 7 löschen
- **$E7D6**: nicht 'Pi' ?
- **$E7D8**: dann zu $E7DC
- **$E7DA**: Bildschirmkode für Pi
- **$E7DC**: Steuerzeichen ?
- **$E7DE**: ja
- **$E7E0**: druckendes Zeichen ausgeben
- **$E7E3**: nicht 'Shift return' ?
- **$E7E5**: dann zu $E7EA
- **$E7E7**: neue Zeile
- **$E7EA**: Hochkomma-Hodus ?
- **$E7EC**: ja, Steuerzeichen revers ausgeben
- **$E7EE**: nicht 'INS' ?,
- **$E7F0**: dann zu $E829
- **$E7F2**: Zeilenlänge
- **$E7F4**: letztes Zeichen in Zeile
- **$E7F6**: gleich Leerzeichen ?
- **$E7F8**: nein, dann zu $E7FE
- **$E7FA**: Cursor in letzter Spalte ?
- **$E7FC**: nein, dann zu $E805
- **$E7FE**: 79 ? maximale Zeilenlänge
- **$E800**: letzte Spalte, dann keine Aktion
- **$E802**: Leerzeile einfügen
- **$E805**: Zeilenlänge
- **$E807**: Zeiger auf Farbram berechnen
- **$E80A**: Zeiger erniedrigen
- **$E80B**: Zeichen vom Bildschirm
- **$E80D**: Zeiger erhöhen
- **$E80E**: eins nach rechts schieben
- **$E810**: Zeiger erniedrigen
- **$E811**: und Farbe
- **$E813**: Zeiger erhöhen
- **$E814**: verschieben
- **$E816**: Zeiger erniedrigen
- **$E817**: bis zur aktuellen Position aufrücken
- **$E819**: nicht ?, dann weiter
- **$E81B**: Leerzeichen
- **$E81D**: an augenblickliche Position schreiben
- **$E81F**: Farbe
- **$E822**: setzen
- **$E824**: Anzahl der Inserts erhöhen
- **$E826**: Ende der Zeichenausgabe
- **$E829**: Zähler Null?
- **$E82B**: dann zu $E832
- **$E82D**: Bit 6 setzen
- **$E82F**: und Zeichen ausgeben
- **$E832**: nicht Cursor up ?,
- **$E834**: dann zu $E84C
- **$E836**: Zeile
- **$E838**: null, dann fertig
- **$E83A**: Zeilennummer um eins erniedrigen
- **$E83C**: Spalte
- **$E83E**: 40
- **$E83F**: abziehen nicht in Doppelzeile ?,
- **$E841**: dann zu $E847
- **$E843**: Cursorspalte
- **$E845**: positiv, ok
- **$E847**: Bildschirmzeiger neu setzen
- **$E84A**: unbedingter Sprung
- **$E84C**: nicht 'RVS OFF' ?,
- **$E84E**: dann zu $E854
- **$E850**: RVS-Flag
- **$E852**: löschen
- **$E854**: nicht ’Cursor left' ?,
- **$E856**: dann zu $E86A
- **$E858**: wenn erste Spalte,
- **$E859**: dann zu $E864
- **$E85B**: Cursorzeile erniedrigen
- **$E85E**: Zähler erniedrigen
- **$E85F**: Cursorspalte
- **$E861**: fertig
- **$E864**: Rückschritt in vorherige Zeile
- **$E867**: fertig
- **$E86A**: nicht 'CLR SCREEN' ?,
- **$E86C**: dann zu $E874
- **$E86E**: Bildschirm löschen
- **$E871**: fertig
- **$E874**: Bit 7 wiederherstellen
- **$E876**: auf Farbcode prüfen
- **$E879**: prüft auf Umschaltung Text/Grafik
- **$E87C**: Flag für Zeilenwechsel
- **$E87E**: Cursorzeilenzeiger
- **$E880**: Zeiger erhöhen
- **$E881**: noch nicht letzte Zeile ?,
- **$E883**: dann zu $E888
- **$E885**: Bildschirm scrollen
- **$E888**: nächste Zeile, dann
- **$E88A**: wieder scrollen
- **$E88C**: neue Zeile
- **$E88E**: Cursorposition berechnen
- **$E891**: Einfüg-
- **$E893**: zähler löschen
- **$E895**: Flag für RVS löschen
- **$E897**: Quote-Modus löschen
- **$E899**: Cursor in erste Spalte
- **$E89B**: Zeile initialisieren
- **$E89E**: fertig
- **$E8A1**: maximale Zeilenanzahl
- **$E8A3**: wenn Cursorspalte
- **$E8A5**: gleich Akku,
- **$E8A7**: dann zu $E8B0
- **$E8A9**: 40 addieren,
- **$E8AA**: eine Zeile
- **$E8AC**: schon zweimal addiert ?,
- **$E8AD**: ja, dann weiter
- **$E8AF**: Rücksprung
- **$E8B0**: Zeiger auf Cursorzeile erniedrigen
- **$E8B2**: Rücksprung
- **$E8B3**: maximale Zeilenanzahl
- **$E8B5**: 39, letzte Spalte
- **$E8B7**: wenn Cursorspalte gleich
- **$E8B9**: akku ?, dann zu $E8C2
- **$E8BB**: 40
- **$E8BC**: addieren
- **$E8BE**: schon zweimal ?,
- **$E8BF**: ja, dann weiter
- **$E8C1**: Rücksprung
- **$E8C2**: wenn Cursorzeile
- **$E8C4**: gleich 25,
- **$E8C6**: dann fertig
- **$E8C8**: Zeiger auf Cursorzeile erhöhen
- **$E8CA**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E7D4**: remove shift bit
- **$E7D6**: code for PI
- **$E7DA**: screen PI
- **$E7E3**: shift return
- **$E7EE**: insert
- **$E832**: csr up
- **$E84C**: reverse off
- **$E854**: csr left
- **$E86A**: clr code

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*