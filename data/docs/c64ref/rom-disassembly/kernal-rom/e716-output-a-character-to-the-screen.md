---
title: output a character to the screen
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
- 00c7-rvs
- cursor
- e716-ausgabe-auf-bildschirm
- e7d4-zeichen-grer-127
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E716
  address_end: $E879
  symbol: output-a-character-to-the-screen
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E716**: save character'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E716**: Zeichen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E72A**: return code'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E716**: store (A), (X) and (Y) on stack'
---

# $E716 — output a character to the screen

## Disassemblatura
```assembly
.E716  48       PHA   ; save character
.E717  85 D7    STA $D7   ; save temporary last character
.E719  8A       TXA   ; copy X
.E71A  48       PHA   ; save X
.E71B  98       TYA   ; copy Y
.E71C  48       PHA   ; save Y
.E71D  A9 00    LDA #$00   ; clear A
.E71F  85 D0    STA $D0   ; clear input from keyboard or screen, $xx = screen, $00 = keyboard
.E721  A4 D3    LDY $D3   ; get cursor column
.E723  A5 D7    LDA $D7   ; restore last character
.E725  10 03    BPL $E72A   ; branch if unshifted
.E727  4C D4 E7 JMP $E7D4   ; do shifted characters and return
.E72A  C9 0D    CMP #$0D   ; compare with [CR]
.E72C  D0 03    BNE $E731   ; branch if not [CR]
.E72E  4C 91 E8 JMP $E891   ; else output [CR] and return
.E731  C9 20    CMP #$20   ; compare with [SPACE]
.E733  90 10    BCC $E745   ; branch if < [SPACE], not a printable character
.E735  C9 60    CMP #$60
.E737  90 04    BCC $E73D   ; branch if $20 to $5F character is $60 or greater
.E739  29 DF    AND #$DF   ; conversion of PETSCII character to screen code
.E73B  D0 02    BNE $E73F   ; branch always character is $20 to $5F
.E73D  29 3F    AND #$3F   ; conversion of PETSCII character to screen code
.E73F  20 84 E6 JSR $E684   ; if open quote toggle cursor direct/programmed flag
.E742  4C 93 E6 JMP $E693   ; character was < [SPACE] so is a control character of some sort
.E745  A6 D8    LDX $D8   ; get the insert count
.E747  F0 03    BEQ $E74C   ; if no characters to insert continue
.E749  4C 97 E6 JMP $E697   ; insert reversed character
.E74C  C9 14    CMP #$14   ; compare the character with [INSERT]/[DELETE]
.E74E  D0 2E    BNE $E77E   ; if not [INSERT]/[DELETE] go ??
.E750  98       TYA
.E751  D0 06    BNE $E759
.E753  20 01 E7 JSR $E701   ; back onto the previous line if possible
.E756  4C 73 E7 JMP $E773
.E759  20 A1 E8 JSR $E8A1   ; test for line decrement now close up the line
.E75C  88       DEY   ; decrement index to previous character
.E75D  84 D3    STY $D3   ; save the cursor column
.E75F  20 24 EA JSR $EA24   ; calculate the pointer to colour RAM
.E762  C8       INY   ; increment index to next character
.E763  B1 D1    LDA ($D1),Y   ; get character from current screen line
.E765  88       DEY   ; decrement index to previous character
.E766  91 D1    STA ($D1),Y   ; save character to current screen line
.E768  C8       INY   ; increment index to next character
.E769  B1 F3    LDA ($F3),Y   ; get colour RAM byte
.E76B  88       DEY   ; decrement index to previous character
.E76C  91 F3    STA ($F3),Y   ; save colour RAM byte
.E76E  C8       INY   ; increment index to next character
.E76F  C4 D5    CPY $D5   ; compare with current screen line length
.E771  D0 EF    BNE $E762   ; loop if not there yet
.E773  A9 20    LDA #$20   ; set [SPACE]
.E775  91 D1    STA ($D1),Y   ; clear last character on current screen line
.E777  AD 86 02 LDA $0286   ; get the current colour code
.E77A  91 F3    STA ($F3),Y   ; save to colour RAM
.E77C  10 4D    BPL $E7CB   ; branch always
.E77E  A6 D4    LDX $D4   ; get cursor quote flag, $xx = quote, $00 = no quote
.E780  F0 03    BEQ $E785   ; branch if not quote mode
.E782  4C 97 E6 JMP $E697   ; insert reversed character
.E785  C9 12    CMP #$12   ; compare with [RVS ON]
.E787  D0 02    BNE $E78B   ; if not [RVS ON] skip setting the reverse flag
.E789  85 C7    STA $C7   ; else set the reverse flag
.E78B  C9 13    CMP #$13   ; compare with [CLR HOME]
.E78D  D0 03    BNE $E792   ; if not [CLR HOME] continue
.E78F  20 66 E5 JSR $E566   ; home the cursor
.E792  C9 1D    CMP #$1D   ; compare with [CURSOR RIGHT]
.E794  D0 17    BNE $E7AD   ; if not [CURSOR RIGHT] go ??
.E796  C8       INY   ; increment the cursor column
.E797  20 B3 E8 JSR $E8B3   ; test for line increment
.E79A  84 D3    STY $D3   ; save the cursor column
.E79C  88       DEY   ; decrement the cursor column
.E79D  C4 D5    CPY $D5   ; compare cursor column with current screen line length
.E79F  90 09    BCC $E7AA   ; exit if less else the cursor column is >= the current screen line length so back onto the current line and do a newline
.E7A1  C6 D6    DEC $D6   ; decrement the cursor row
.E7A3  20 7C E8 JSR $E87C   ; do newline
.E7A6  A0 00    LDY #$00   ; clear cursor column
.E7A8  84 D3    STY $D3   ; save the cursor column
.E7AA  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
.E7AD  C9 11    CMP #$11   ; compare with [CURSOR DOWN]
.E7AF  D0 1D    BNE $E7CE   ; if not [CURSOR DOWN] go ??
.E7B1  18       CLC   ; clear carry for add
.E7B2  98       TYA   ; copy the cursor column
.E7B3  69 28    ADC #$28   ; add one line
.E7B5  A8       TAY   ; copy back to Y
.E7B6  E6 D6    INC $D6   ; increment the cursor row
.E7B8  C5 D5    CMP $D5   ; compare cursor column with current screen line length
.E7BA  90 EC    BCC $E7A8   ; if less go save cursor column and exit
.E7BC  F0 EA    BEQ $E7A8   ; if equal go save cursor column and exit else the cursor has moved beyond the end of this line so back it up until it's on the start of the logical line
.E7BE  C6 D6    DEC $D6   ; decrement the cursor row
.E7C0  E9 28    SBC #$28   ; subtract one line
.E7C2  90 04    BCC $E7C8   ; if on previous line exit the loop
.E7C4  85 D3    STA $D3   ; else save the cursor column
.E7C6  D0 F8    BNE $E7C0   ; loop if not at the start of the line
.E7C8  20 7C E8 JSR $E87C   ; do newline
.E7CB  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
.E7CE  20 CB E8 JSR $E8CB   ; set the colour code
.E7D1  4C 44 EC JMP $EC44   ; go check for special character codes
.E7D4  29 7F    AND #$7F   ; mask 0xxx xxxx, clear b7
.E7D6  C9 7F    CMP #$7F   ; was it $FF before the mask
.E7D8  D0 02    BNE $E7DC   ; branch if not
.E7DA  A9 5E    LDA #$5E   ; else make it $5E
.E7DC  C9 20    CMP #$20   ; compare the character with [SPACE]
.E7DE  90 03    BCC $E7E3   ; if < [SPACE] go ??
.E7E0  4C 91 E6 JMP $E691   ; insert uppercase/graphic character and return character was $80 to $9F and is now $00 to $1F
.E7E3  C9 0D    CMP #$0D   ; compare with [CR]
.E7E5  D0 03    BNE $E7EA   ; if not [CR] continue
.E7E7  4C 91 E8 JMP $E891   ; else output [CR] and return was not [CR]
.E7EA  A6 D4    LDX $D4   ; get the cursor quote flag, $xx = quote, $00 = no quote
.E7EC  D0 3F    BNE $E82D   ; branch if quote mode
.E7EE  C9 14    CMP #$14   ; compare with [INSERT DELETE]
.E7F0  D0 37    BNE $E829   ; if not [INSERT DELETE] go ??
.E7F2  A4 D5    LDY $D5   ; get current screen line length
.E7F4  B1 D1    LDA ($D1),Y   ; get character from current screen line
.E7F6  C9 20    CMP #$20   ; compare the character with [SPACE]
.E7F8  D0 04    BNE $E7FE   ; if not [SPACE] continue
.E7FA  C4 D3    CPY $D3   ; compare the current column with the cursor column
.E7FC  D0 07    BNE $E805   ; if not cursor column go open up space on line
.E7FE  C0 4F    CPY #$4F   ; compare current column with max line length
.E800  F0 24    BEQ $E826   ; if at line end just exit
.E802  20 65 E9 JSR $E965   ; else open up a space on the screen now open up space on the line to insert a character
.E805  A4 D5    LDY $D5   ; get current screen line length
.E807  20 24 EA JSR $EA24   ; calculate the pointer to colour RAM
.E80A  88       DEY   ; decrement the index to previous character
.E80B  B1 D1    LDA ($D1),Y   ; get the character from the current screen line
.E80D  C8       INY   ; increment the index to next character
.E80E  91 D1    STA ($D1),Y   ; save the character to the current screen line
.E810  88       DEY   ; decrement the index to previous character
.E811  B1 F3    LDA ($F3),Y   ; get the current screen line colour RAM byte
.E813  C8       INY   ; increment the index to next character
.E814  91 F3    STA ($F3),Y   ; save the current screen line colour RAM byte
.E816  88       DEY   ; decrement the index to the previous character
.E817  C4 D3    CPY $D3   ; compare the index with the cursor column
.E819  D0 EF    BNE $E80A   ; loop if not there yet
.E81B  A9 20    LDA #$20   ; set [SPACE]
.E81D  91 D1    STA ($D1),Y   ; clear character at cursor position on current screen line
.E81F  AD 86 02 LDA $0286   ; get current colour code
.E822  91 F3    STA ($F3),Y   ; save to cursor position on current screen line colour RAM
.E824  E6 D8    INC $D8   ; increment insert count
.E826  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
.E829  A6 D8    LDX $D8   ; get the insert count
.E82B  F0 05    BEQ $E832   ; branch if no insert space
.E82D  09 40    ORA #$40   ; change to uppercase/graphic
.E82F  4C 97 E6 JMP $E697   ; insert reversed character
.E832  C9 11    CMP #$11   ; compare with [CURSOR UP]
.E834  D0 16    BNE $E84C   ; branch if not [CURSOR UP]
.E836  A6 D6    LDX $D6   ; get the cursor row
.E838  F0 37    BEQ $E871   ; if on the top line go restore the registers, set the quote flag and exit
.E83A  C6 D6    DEC $D6   ; decrement the cursor row
.E83C  A5 D3    LDA $D3   ; get the cursor column
.E83E  38       SEC   ; set carry for subtract
.E83F  E9 28    SBC #$28   ; subtract one line length
.E841  90 04    BCC $E847   ; branch if stepped back to previous line
.E843  85 D3    STA $D3   ; else save the cursor column ..
.E845  10 2A    BPL $E871   ; .. and exit, branch always
.E847  20 6C E5 JSR $E56C   ; set the screen pointers for cursor row, column ..
.E84A  D0 25    BNE $E871   ; .. and exit, branch always
.E84C  C9 12    CMP #$12   ; compare with [RVS OFF]
.E84E  D0 04    BNE $E854   ; if not [RVS OFF] continue
.E850  A9 00    LDA #$00   ; else clear A
.E852  85 C7    STA $C7   ; clear the reverse flag
.E854  C9 1D    CMP #$1D   ; compare with [CURSOR LEFT]
.E856  D0 12    BNE $E86A   ; if not [CURSOR LEFT] go ??
.E858  98       TYA   ; copy the cursor column
.E859  F0 09    BEQ $E864   ; if at start of line go back onto the previous line
.E85B  20 A1 E8 JSR $E8A1   ; test for line decrement
.E85E  88       DEY   ; decrement the cursor column
.E85F  84 D3    STY $D3   ; save the cursor column
.E861  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
.E864  20 01 E7 JSR $E701   ; back onto the previous line if possible
.E867  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
.E86A  C9 13    CMP #$13   ; compare with [CLR]
.E86C  D0 06    BNE $E874   ; if not [CLR] continue
.E86E  20 44 E5 JSR $E544   ; clear the screen
.E871  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
.E874  09 80    ORA #$80   ; restore b7, colour can only be black, cyan, magenta or yellow
.E876  20 CB E8 JSR $E8CB   ; set the colour code
.E879  4C 4F EC JMP $EC4F   ; go check for special character codes except fro switch to lower case
```


## Commenti

### Original Disassembly (—)
- **$E716**: save character
- **$E717**: save temporary last character
- **$E719**: copy X
- **$E71A**: save X
- **$E71B**: copy Y
- **$E71C**: save Y
- **$E71D**: clear A
- **$E71F**: clear input from keyboard or screen, $xx = screen, $00 = keyboard
- **$E721**: get cursor column
- **$E723**: restore last character
- **$E725**: branch if unshifted
- **$E727**: do shifted characters and return
- **$E72A**: compare with [CR]
- **$E72C**: branch if not [CR]
- **$E72E**: else output [CR] and return
- **$E731**: compare with [SPACE]
- **$E733**: branch if < [SPACE], not a printable character
- **$E737**: branch if $20 to $5F character is $60 or greater
- **$E739**: conversion of PETSCII character to screen code
- **$E73B**: branch always character is $20 to $5F
- **$E73D**: conversion of PETSCII character to screen code
- **$E73F**: if open quote toggle cursor direct/programmed flag
- **$E742**: character was < [SPACE] so is a control character of some sort
- **$E745**: get the insert count
- **$E747**: if no characters to insert continue
- **$E749**: insert reversed character
- **$E74C**: compare the character with [INSERT]/[DELETE]
- **$E74E**: if not [INSERT]/[DELETE] go ??
- **$E753**: back onto the previous line if possible
- **$E759**: test for line decrement now close up the line
- **$E75C**: decrement index to previous character
- **$E75D**: save the cursor column
- **$E75F**: calculate the pointer to colour RAM
- **$E762**: increment index to next character
- **$E763**: get character from current screen line
- **$E765**: decrement index to previous character
- **$E766**: save character to current screen line
- **$E768**: increment index to next character
- **$E769**: get colour RAM byte
- **$E76B**: decrement index to previous character
- **$E76C**: save colour RAM byte
- **$E76E**: increment index to next character
- **$E76F**: compare with current screen line length
- **$E771**: loop if not there yet
- **$E773**: set [SPACE]
- **$E775**: clear last character on current screen line
- **$E777**: get the current colour code
- **$E77A**: save to colour RAM
- **$E77C**: branch always
- **$E77E**: get cursor quote flag, $xx = quote, $00 = no quote
- **$E780**: branch if not quote mode
- **$E782**: insert reversed character
- **$E785**: compare with [RVS ON]
- **$E787**: if not [RVS ON] skip setting the reverse flag
- **$E789**: else set the reverse flag
- **$E78B**: compare with [CLR HOME]
- **$E78D**: if not [CLR HOME] continue
- **$E78F**: home the cursor
- **$E792**: compare with [CURSOR RIGHT]
- **$E794**: if not [CURSOR RIGHT] go ??
- **$E796**: increment the cursor column
- **$E797**: test for line increment
- **$E79A**: save the cursor column
- **$E79C**: decrement the cursor column
- **$E79D**: compare cursor column with current screen line length
- **$E79F**: exit if less else the cursor column is >= the current screen line length so back onto the current line and do a newline
- **$E7A1**: decrement the cursor row
- **$E7A3**: do newline
- **$E7A6**: clear cursor column
- **$E7A8**: save the cursor column
- **$E7AA**: restore the registers, set the quote flag and exit
- **$E7AD**: compare with [CURSOR DOWN]
- **$E7AF**: if not [CURSOR DOWN] go ??
- **$E7B1**: clear carry for add
- **$E7B2**: copy the cursor column
- **$E7B3**: add one line
- **$E7B5**: copy back to Y
- **$E7B6**: increment the cursor row
- **$E7B8**: compare cursor column with current screen line length
- **$E7BA**: if less go save cursor column and exit
- **$E7BC**: if equal go save cursor column and exit else the cursor has moved beyond the end of this line so back it up until it's on the start of the logical line
- **$E7BE**: decrement the cursor row
- **$E7C0**: subtract one line
- **$E7C2**: if on previous line exit the loop
- **$E7C4**: else save the cursor column
- **$E7C6**: loop if not at the start of the line
- **$E7C8**: do newline
- **$E7CB**: restore the registers, set the quote flag and exit
- **$E7CE**: set the colour code
- **$E7D1**: go check for special character codes
- **$E7D4**: mask 0xxx xxxx, clear b7
- **$E7D6**: was it $FF before the mask
- **$E7D8**: branch if not
- **$E7DA**: else make it $5E
- **$E7DC**: compare the character with [SPACE]
- **$E7DE**: if < [SPACE] go ??
- **$E7E0**: insert uppercase/graphic character and return character was $80 to $9F and is now $00 to $1F
- **$E7E3**: compare with [CR]
- **$E7E5**: if not [CR] continue
- **$E7E7**: else output [CR] and return was not [CR]
- **$E7EA**: get the cursor quote flag, $xx = quote, $00 = no quote
- **$E7EC**: branch if quote mode
- **$E7EE**: compare with [INSERT DELETE]
- **$E7F0**: if not [INSERT DELETE] go ??
- **$E7F2**: get current screen line length
- **$E7F4**: get character from current screen line
- **$E7F6**: compare the character with [SPACE]
- **$E7F8**: if not [SPACE] continue
- **$E7FA**: compare the current column with the cursor column
- **$E7FC**: if not cursor column go open up space on line
- **$E7FE**: compare current column with max line length
- **$E800**: if at line end just exit
- **$E802**: else open up a space on the screen now open up space on the line to insert a character
- **$E805**: get current screen line length
- **$E807**: calculate the pointer to colour RAM
- **$E80A**: decrement the index to previous character
- **$E80B**: get the character from the current screen line
- **$E80D**: increment the index to next character
- **$E80E**: save the character to the current screen line
- **$E810**: decrement the index to previous character
- **$E811**: get the current screen line colour RAM byte
- **$E813**: increment the index to next character
- **$E814**: save the current screen line colour RAM byte
- **$E816**: decrement the index to the previous character
- **$E817**: compare the index with the cursor column
- **$E819**: loop if not there yet
- **$E81B**: set [SPACE]
- **$E81D**: clear character at cursor position on current screen line
- **$E81F**: get current colour code
- **$E822**: save to cursor position on current screen line colour RAM
- **$E824**: increment insert count
- **$E826**: restore the registers, set the quote flag and exit
- **$E829**: get the insert count
- **$E82B**: branch if no insert space
- **$E82D**: change to uppercase/graphic
- **$E82F**: insert reversed character
- **$E832**: compare with [CURSOR UP]
- **$E834**: branch if not [CURSOR UP]
- **$E836**: get the cursor row
- **$E838**: if on the top line go restore the registers, set the quote flag and exit
- **$E83A**: decrement the cursor row
- **$E83C**: get the cursor column
- **$E83E**: set carry for subtract
- **$E83F**: subtract one line length
- **$E841**: branch if stepped back to previous line
- **$E843**: else save the cursor column ..
- **$E845**: .. and exit, branch always
- **$E847**: set the screen pointers for cursor row, column ..
- **$E84A**: .. and exit, branch always
- **$E84C**: compare with [RVS OFF]
- **$E84E**: if not [RVS OFF] continue
- **$E850**: else clear A
- **$E852**: clear the reverse flag
- **$E854**: compare with [CURSOR LEFT]
- **$E856**: if not [CURSOR LEFT] go ??
- **$E858**: copy the cursor column
- **$E859**: if at start of line go back onto the previous line
- **$E85B**: test for line decrement
- **$E85E**: decrement the cursor column
- **$E85F**: save the cursor column
- **$E861**: restore the registers, set the quote flag and exit
- **$E864**: back onto the previous line if possible
- **$E867**: restore the registers, set the quote flag and exit
- **$E86A**: compare with [CLR]
- **$E86C**: if not [CLR] continue
- **$E86E**: clear the screen
- **$E871**: restore the registers, set the quote flag and exit
- **$E874**: restore b7, colour can only be black, cyan, magenta or yellow
- **$E876**: set the colour code
- **$E879**: go check for special character codes except fro switch to lower case

### Commodore-64-intern-Buch (Commodore)
- **$E716**: Zeichen
- **$E717**: merken
- **$E719**: die
- **$E71A**: Re-
- **$E71B**: gister
- **$E71C**: retten
- **$E71D**: Eingabeflag
- **$E71F**: löschen
- **$E721**: Cursorspalte
- **$E723**: Zeichen
- **$E725**: wenn kleiner 128, dann zu $E72A
- **$E727**: Zeichen größer $7F behandeln
- **$E72A**: 'CARRIAGE RETURN' ?
- **$E72C**: wenn nicht, dann zu $E731
- **$E72E**: Return ausgeben
- **$E731**: ' '
- **$E733**: druckendes Zeichen ?
- **$E735**: Zahl kleiner $60,
- **$E737**: dann keine Graphikzeichen
- **$E739**: Umwandlung in BS-Kode
- **$E73B**: unbedingter Sprung
- **$E73D**: Umwandlung in BS-Kode
- **$E73F**: Test auf Hochkomma
- **$E742**: zur Ausgabe, ASCII-Kode in BS-Code
- **$E745**: wenn Einfügzähler =0,
- **$E747**: dann zu $E74C
- **$E749**: ASCII-Kode in BS-Code
- **$E74C**: nicht 'DEL' ?,
- **$E74E**: dann zu $E77E
- **$E750**: erste Spalte =0
- **$E751**: dann zu $E759
- **$E753**: zurück in vorherige Zeile
- **$E756**: Zeichen in Cursorposition eliminieren
- **$E759**: Rückschritt prüfen
- **$E75C**: Zeiger erniedrigen
- **$E75D**: und speichern
- **$E75F**: Zeiger auf Farb-RAM berechnen
- **$E762**: Zeiger erhöhen
- **$E763**: Zeichen vom Bildschirm
- **$E765**: Zeiger erniedrigen
- **$E766**: eins nach links schieben
- **$E768**: Zeiger erhöhen
- **$E769**: Farbe
- **$E76B**: Zeiger erniedrigen
- **$E76C**: eins nach links schieben
- **$E76E**: Zeiger erhöhen
- **$E76F**: Endspalte nicht
- **$E771**: erreicht, dann weiter
- **$E773**: Blank
- **$E775**: einfügen
- **$E777**: Farbcode
- **$E77A**: setzen
- **$E77C**: fertig
- **$E77E**: Hochkomma-Modus ?
- **$E780**: nein
- **$E782**: Zeichen revers ausgeben
- **$E785**: 'RVS ON' ?
- **$E787**: nein, dann
- **$E789**: Flag für RVS setzen
- **$E78B**: 'HOME' ?
- **$E78D**: nein
- **$E78F**: ja, Cursor Home
- **$E792**: 'Cursor right' ?
- **$E794**: nein
- **$E796**: Zeiger erhöhen
- **$E797**: Cursorposition prüfen
- **$E79A**: neuer Zeiger
- **$E79C**: Zeiger erniedrigen
- **$E79D**: keine neue Zeile ?,
- **$E79F**: dann fertig
- **$E7A1**: Zeiger erniedrigen
- **$E7A3**: Zeile initialisieren
- **$E7A6**: Spalte
- **$E7A8**: gleich null
- **$E7AA**: fertig
- **$E7AD**: 'Cursor down' ?
- **$E7AF**: nein
- **$E7B1**: plus
- **$E7B2**: 40,
- **$E7B3**: eine Zeile
- **$E7B5**: tiefer
- **$E7B6**: Zeiger erhöhen
- **$E7B8**: neue Zeile erreicht?
- **$E7BA**: nein, dann zu $E7A8
- **$E7BC**: Ja, dann zu $E7A8
- **$E7BE**: Zeiger erniedrigen
- **$E7C0**: 40 abziehen
- **$E7C2**: genügend abgezogen, dann zu $E7C8
- **$E7C4**: Spalte setzen
- **$E7C6**: noch mal
- **$E7C8**: Zeile initialisieren
- **$E7CB**: fertig
- **$E7CE**: prüft auf Farbcodes
- **$E7D1**: Test auf weitere Sonderzeichen

### Marko Mäkelä (Marko Mäkelä)
- **$E72A**: return code
- **$E74C**: delete code
- **$E773**: space
- **$E785**: reverse code
- **$E78B**: home code
- **$E792**: csr right
- **$E7AD**: csr down

### Magnus Nyman (Magnus Nyman)
- **$E716**: store (A), (X) and (Y) on stack
- **$E717**: temp store
- **$E71F**: store in CRSW
- **$E721**: PNTR, cursor positions on line
- **$E723**: retrieve from temp store
- **$E725**: do unshifted characters
- **$E727**: do shifted characters UNSHIFTED CHARACTERS. Ordinary unshifted ASCII characters and PET graphics are output directly to the screen. The following control codes are trapped and precessed: <RETURN>, <DEL>, <CRSR RIGHT>, <CRSR DOWN>. If either insert mode is on or quotes are open (except for <DEL>) then the control characters are not processed, but output as reversed ASCII literals.
- **$E72A**: <RETURN>?
- **$E72C**: nope
- **$E72E**: execute return
- **$E731**: <SPACE>?
- **$E735**: #$60, first PET graphic character?
- **$E739**: %11011111
- **$E73D**: %00111111
- **$E73F**: do quotes test
- **$E742**: setup screen print
- **$E745**: INSRT, insert mode flag
- **$E747**: mode not set
- **$E749**: output reversed character
- **$E74C**: <DEL>?
- **$E74E**: nope
- **$E750**: (Y) holds cursor column
- **$E751**: not start of line
- **$E753**: back on previous line
- **$E759**: check line decrement
- **$E75C**: decrement cursor column
- **$E75D**: and store in PNTR
- **$E75F**: synchronise colour pointer
- **$E762**: copy character at cursor position (Y+1) to (Y)
- **$E763**: read character
- **$E766**: and store it one position back
- **$E769**: read character  colour
- **$E76C**: and store it one position back
- **$E76E**: more characters to move
- **$E76F**: compare with LNMX, length of physical screen line
- **$E771**: if not equal, move more characters
- **$E775**: store <SPACE> at end of line
- **$E777**: COLOR, current character colour
- **$E77A**: store colour at end of line
- **$E77C**: always jump
- **$E77E**: QTSW, editor in quotes mode
- **$E780**: no
- **$E782**: output reversed character
- **$E785**: <RVS>?
- **$E787**: no
- **$E789**: RVS, reversed character output flag
- **$E78B**: <HOME>?
- **$E78D**: no
- **$E78F**: home cursor
- **$E792**: <CRSR RIGHT>?
- **$E794**: nope
- **$E796**: increment (Y), internal counter for column
- **$E797**: check line increment
- **$E79A**: store (Y) in PNTR
- **$E79C**: decrement (Y)
- **$E79D**: and compare to LNMX
- **$E79F**: not exceeded line length
- **$E7A1**: TBLX, current physical line number
- **$E7A3**: goto next line
- **$E7A8**: set PNTR to zero, cursor to the left
- **$E7AA**: finish screen print
- **$E7AD**: <CRSR DOWN>?
- **$E7AF**: no
- **$E7B1**: prepare for add
- **$E7B2**: (Y) holds cursor column
- **$E7B3**: add 40 to next line
- **$E7B5**: to (Y)
- **$E7B6**: increment TBLX, physical line number
- **$E7B8**: compare to LNMX
- **$E7BA**: finish screen print
- **$E7BC**: finish screen print
- **$E7BE**: restore TBLX
- **$E7C4**: store PNTR
- **$E7C8**: go to next line
- **$E7CB**: finish screen print
- **$E7CE**: set colour code
- **$E7D1**: do graphics/text control SHIFTED CHARACTERS. These are dealt with in the following order: Shifted ordinary ASCII and PET graphics characters, <shift RETURN>, <INST>, <CRSR UP>, <RVS OFF>, <CRSR LEFT>, <CLR>. If either insert mode is on, or quotes are open, then the control character is not processed but reversed ASCII literal is printed.
- **$E7D4**: clear bit7
- **$E7D6**: compare to #$7f
- **$E7D8**: not equal
- **$E7DA**: if #$7f, load #$5e
- **$E7DC**: ASCII <SPACE>?
- **$E7E0**: set up screen print
- **$E7E3**: <RETURN>?
- **$E7E5**: nope
- **$E7E7**: do return
- **$E7EA**: read QTSW
- **$E7EC**: if quotes mode, jump
- **$E7EE**: <INST>?
- **$E7F0**: nope
- **$E7F2**: LNMX
- **$E7F4**: get screen character
- **$E7F6**: space?
- **$E7F8**: nope
- **$E7FA**: PNTR equal to LNMX
- **$E7FC**: nope
- **$E7FE**: #$4f=79, last character
- **$E800**: end of logical line, can not insert
- **$E802**: open space on line
- **$E805**: LNMX
- **$E807**: synchronise colour pointer
- **$E80A**: prepare for move
- **$E80B**: read character at pos (Y)
- **$E80E**: and move one step to the right
- **$E811**: read character colour
- **$E814**: move one step to the right
- **$E816**: decrement counter
- **$E817**: compare with PNTR
- **$E819**: till all characters right of cursor are moved
- **$E81B**: <SPACE>, ASCII #$20
- **$E81D**: store at new character position
- **$E81F**: COLOR, current character colour
- **$E822**: store at new colour position
- **$E824**: INSRT FLAG
- **$E826**: finish screen print
- **$E829**: INSRT FLAG
- **$E82B**: insert mode is off
- **$E82F**: set up screen print
- **$E832**: <CRSR UP>?
- **$E834**: nope
- **$E836**: read TBLX
- **$E838**: at topline, do nothing
- **$E83A**: else decrement TBLX
- **$E83C**: PNTR
- **$E83E**: prepare for subtract
- **$E83F**: back 40 columns for double line
- **$E841**: skip
- **$E843**: store PNTR
- **$E845**: finish screen print
- **$E847**: set screen pointer
- **$E84A**: finish screen print
- **$E84C**: <RVS OFF>?
- **$E84E**: nope
- **$E852**: RVS, disable reverse print
- **$E854**: <CRSR LEFT>?
- **$E856**: nope
- **$E858**: (Y) holds cursor column
- **$E859**: at first position
- **$E85B**: check line decrement
- **$E85E**: one position left
- **$E85F**: store in PNTR
- **$E861**: finish screen print
- **$E864**: back to previous line
- **$E867**: finish screen print
- **$E86A**: <CLR>?
- **$E86C**: nope
- **$E86E**: clear screen
- **$E871**: finish screen print
- **$E876**: set colour code
- **$E879**: set graphics/text mode

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*