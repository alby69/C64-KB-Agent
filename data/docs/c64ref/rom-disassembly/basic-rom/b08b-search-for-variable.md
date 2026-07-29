---
title: search for variable
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
- af28-variable-holen
- b08b-variable-holen
- b113-prft-auf-buchstabe
- b11d-variable-anlegen
- b128-make-a-new-simple-variable
- b185-put-address-of-value-of-variable-in-varpnt-and-ya
- b194-arrayelement
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B08B
  address_end: $B1A4
  symbol: search-for-variable
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B08B**: set DIM flag = $00'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B08B**: Flag für nicht dimensionieren'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B0BA**: $'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B08D**: GET FIRST CHAR OF VARIABLE NAME'
---

# $B08B — search for variable

## Disassemblatura
```assembly
.B08B  A2 00    LDX #$00   ; set DIM flag = $00
.B08D  20 79 00 JSR $0079   ; scan memory, 1st character
.B090  86 0C    STX $0C   ; save DIM flag
.B092  85 45    STA $45   ; save 1st character
.B094  20 79 00 JSR $0079   ; scan memory
.B097  20 13 B1 JSR $B113   ; check byte, return Cb = 0 if<"A" or >"Z"
.B09A  B0 03    BCS $B09F   ; branch if ok
.B09C  4C 08 AF JMP $AF08   ; else syntax error then warm start was variable name so ...
.B09F  A2 00    LDX #$00   ; clear 2nd character temp
.B0A1  86 0D    STX $0D   ; clear data type flag, $FF = string, $00 = numeric
.B0A3  86 0E    STX $0E   ; clear data type flag, $80 = integer, $00 = float
.B0A5  20 73 00 JSR $0073   ; increment and scan memory, 2nd character
.B0A8  90 05    BCC $B0AF   ; if character = "0"-"9" (ok) go save 2nd character 2nd character wasn't "0" to "9" so ...
.B0AA  20 13 B1 JSR $B113   ; check byte, return Cb = 0 if<"A" or >"Z"
.B0AD  90 0B    BCC $B0BA   ; branch if <"A" or >"Z" (go check if string)
.B0AF  AA       TAX   ; copy 2nd character ignore further (valid) characters in the variable name
.B0B0  20 73 00 JSR $0073   ; increment and scan memory, 3rd character
.B0B3  90 FB    BCC $B0B0   ; loop if character = "0"-"9" (ignore)
.B0B5  20 13 B1 JSR $B113   ; check byte, return Cb = 0 if<"A" or >"Z"
.B0B8  B0 F6    BCS $B0B0   ; loop if character = "A"-"Z" (ignore) check if string variable
.B0BA  C9 24    CMP #$24   ; compare with "$"
.B0BC  D0 06    BNE $B0C4   ; branch if not string type is string
.B0BE  A9 FF    LDA #$FF   ; set data type = string
.B0C0  85 0D    STA $0D   ; set data type flag, $FF = string, $00 = numeric
.B0C2  D0 10    BNE $B0D4   ; branch always
.B0C4  C9 25    CMP #$25   ; compare with "%"
.B0C6  D0 13    BNE $B0DB   ; branch if not integer
.B0C8  A5 10    LDA $10   ; get subscript/FNX flag
.B0CA  D0 D0    BNE $B09C   ; if ?? do syntax error then warm start
.B0CC  A9 80    LDA #$80   ; set integer type
.B0CE  85 0E    STA $0E   ; set data type = integer
.B0D0  05 45    ORA $45   ; OR current variable name first byte
.B0D2  85 45    STA $45   ; save current variable name first byte
.B0D4  8A       TXA   ; get 2nd character back
.B0D5  09 80    ORA #$80   ; set top bit, indicate string or integer variable
.B0D7  AA       TAX   ; copy back to 2nd character temp
.B0D8  20 73 00 JSR $0073   ; increment and scan memory
.B0DB  86 46    STX $46   ; save 2nd character
.B0DD  38       SEC   ; set carry for subtract
.B0DE  05 10    ORA $10   ; or with subscript/FNX flag - or FN name
.B0E0  E9 28    SBC #$28   ; subtract "("
.B0E2  D0 03    BNE $B0E7   ; branch if not "("
.B0E4  4C D1 B1 JMP $B1D1   ; go find, or make, array either find or create variable variable name wasn't xx(.... so look for plain variable
.B0E7  A0 00    LDY #$00   ; clear A
.B0E9  84 10    STY $10   ; clear subscript/FNX flag
.B0EB  A5 2D    LDA $2D   ; get start of variables low byte
.B0ED  A6 2E    LDX $2E   ; get start of variables high byte
.B0EF  86 60    STX $60   ; save search address high byte
.B0F1  85 5F    STA $5F   ; save search address low byte
.B0F3  E4 30    CPX $30   ; compare with end of variables high byte
.B0F5  D0 04    BNE $B0FB   ; skip next compare if <> high addresses were = so compare low addresses
.B0F7  C5 2F    CMP $2F   ; compare low address with end of variables low byte
.B0F9  F0 22    BEQ $B11D   ; if not found go make new variable
.B0FB  A5 45    LDA $45   ; get 1st character of variable to find
.B0FD  D1 5F    CMP ($5F),Y   ; compare with variable name 1st character
.B0FF  D0 08    BNE $B109   ; branch if no match 1st characters match so compare 2nd character
.B101  A5 46    LDA $46   ; get 2nd character of variable to find
.B103  C8       INY   ; index to point to variable name 2nd character
.B104  D1 5F    CMP ($5F),Y   ; compare with variable name 2nd character
.B106  F0 7D    BEQ $B185   ; branch if match (found variable)
.B108  88       DEY   ; else decrement index (now = $00)
.B109  18       CLC   ; clear carry for add
.B10A  A5 5F    LDA $5F   ; get search address low byte
.B10C  69 07    ADC #$07   ; +7, offset to next variable name
.B10E  90 E1    BCC $B0F1   ; loop if no overflow to high byte
.B110  E8       INX   ; else increment high byte
.B111  D0 DC    BNE $B0EF   ; loop always, RAM doesn't extend to $FFFF check byte, return Cb = 0 if<"A" or >"Z"
.B113  C9 41    CMP #$41   ; compare with "A"
.B115  90 05    BCC $B11C   ; exit if less carry is set
.B117  E9 5B    SBC #$5B   ; subtract "Z"+1
.B119  38       SEC   ; set carry
.B11A  E9 A5    SBC #$A5   ; subtract $A5 (restore byte) carry clear if byte > $5A
.B11C  60       RTS   ; reached end of variable memory without match ... so create new variable
.B11D  68       PLA   ; pop return address low byte
.B11E  48       PHA   ; push return address low byte
.B11F  C9 2A    CMP #$2A   ; compare with expected calling routine return low byte
.B121  D0 05    BNE $B128   ; if not get variable go create new variable this will only drop through if the call was from $AF28 and is only called from there if it is searching for a variable from the right hand side of a LET a=b statement, it prevents the creation of variables not assigned a value. value returned by this is either numeric zero, exponent byte is $00, or null string, descriptor length byte is $00. in fact a pointer to any $00 byte would have done. else return dummy null value
.B123  A9 13    LDA #$13   ; set result pointer low byte
.B125  A0 BF    LDY #$BF   ; set result pointer high byte
.B127  60       RTS   ; create new numeric variable
.B128  A5 45    LDA $45   ; get variable name first character
.B12A  A4 46    LDY $46   ; get variable name second character
.B12C  C9 54    CMP #$54   ; compare first character with "T"
.B12E  D0 0B    BNE $B13B   ; branch if not "T"
.B130  C0 C9    CPY #$C9   ; compare second character with "I$"
.B132  F0 EF    BEQ $B123   ; if "I$" return null value
.B134  C0 49    CPY #$49   ; compare second character with "I"
.B136  D0 03    BNE $B13B   ; branch if not "I" if name is "TI" do syntax error
.B138  4C 08 AF JMP $AF08   ; do syntax error then warm start
.B13B  C9 53    CMP #$53   ; compare first character with "S"
.B13D  D0 04    BNE $B143   ; branch if not "S"
.B13F  C0 54    CPY #$54   ; compare second character with "T"
.B141  F0 F5    BEQ $B138   ; if name is "ST" do syntax error
.B143  A5 2F    LDA $2F   ; get end of variables low byte
.B145  A4 30    LDY $30   ; get end of variables high byte
.B147  85 5F    STA $5F   ; save old block start low byte
.B149  84 60    STY $60   ; save old block start high byte
.B14B  A5 31    LDA $31   ; get end of arrays low byte
.B14D  A4 32    LDY $32   ; get end of arrays high byte
.B14F  85 5A    STA $5A   ; save old block end low byte
.B151  84 5B    STY $5B   ; save old block end high byte
.B153  18       CLC   ; clear carry for add
.B154  69 07    ADC #$07   ; +7, space for one variable
.B156  90 01    BCC $B159   ; branch if no overflow to high byte
.B158  C8       INY   ; else increment high byte
.B159  85 58    STA $58   ; set new block end low byte
.B15B  84 59    STY $59   ; set new block end high byte
.B15D  20 B8 A3 JSR $A3B8   ; open up space in memory
.B160  A5 58    LDA $58   ; get new start low byte
.B162  A4 59    LDY $59   ; get new start high byte (-$100)
.B164  C8       INY   ; correct high byte
.B165  85 2F    STA $2F   ; set end of variables low byte
.B167  84 30    STY $30   ; set end of variables high byte
.B169  A0 00    LDY #$00   ; clear index
.B16B  A5 45    LDA $45   ; get variable name 1st character
.B16D  91 5F    STA ($5F),Y   ; save variable name 1st character
.B16F  C8       INY   ; increment index
.B170  A5 46    LDA $46   ; get variable name 2nd character
.B172  91 5F    STA ($5F),Y   ; save variable name 2nd character
.B174  A9 00    LDA #$00   ; clear A
.B176  C8       INY   ; increment index
.B177  91 5F    STA ($5F),Y   ; initialise variable byte
.B179  C8       INY   ; increment index
.B17A  91 5F    STA ($5F),Y   ; initialise variable byte
.B17C  C8       INY   ; increment index
.B17D  91 5F    STA ($5F),Y   ; initialise variable byte
.B17F  C8       INY   ; increment index
.B180  91 5F    STA ($5F),Y   ; initialise variable byte
.B182  C8       INY   ; increment index
.B183  91 5F    STA ($5F),Y   ; initialise variable byte found a match for variable
.B185  A5 5F    LDA $5F   ; get variable address low byte
.B187  18       CLC   ; clear carry for add
.B188  69 02    ADC #$02   ; +2, offset past variable name bytes
.B18A  A4 60    LDY $60   ; get variable address high byte
.B18C  90 01    BCC $B18F   ; branch if no overflow from add
.B18E  C8       INY   ; else increment high byte
.B18F  85 47    STA $47   ; save current variable pointer low byte
.B191  84 48    STY $48   ; save current variable pointer high byte
.B193  60       RTS   ; set-up array pointer to first element in array
.B194  A5 0B    LDA $0B   ; get # of dimensions (1, 2 or 3)
.B196  0A       ASL   ; *2 (also clears the carry !)
.B197  69 05    ADC #$05   ; +5 (result is 7, 9 or 11 here)
.B199  65 5F    ADC $5F   ; add array start pointer low byte
.B19B  A4 60    LDY $60   ; get array pointer high byte
.B19D  90 01    BCC $B1A0   ; branch if no overflow
.B19F  C8       INY   ; else increment high byte
.B1A0  85 58    STA $58   ; save array data pointer low byte
.B1A2  84 59    STY $59   ; save array data pointer high byte
.B1A4  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B08B**: set DIM flag = $00
- **$B08D**: scan memory, 1st character
- **$B090**: save DIM flag
- **$B092**: save 1st character
- **$B094**: scan memory
- **$B097**: check byte, return Cb = 0 if<"A" or >"Z"
- **$B09A**: branch if ok
- **$B09C**: else syntax error then warm start was variable name so ...
- **$B09F**: clear 2nd character temp
- **$B0A1**: clear data type flag, $FF = string, $00 = numeric
- **$B0A3**: clear data type flag, $80 = integer, $00 = float
- **$B0A5**: increment and scan memory, 2nd character
- **$B0A8**: if character = "0"-"9" (ok) go save 2nd character 2nd character wasn't "0" to "9" so ...
- **$B0AA**: check byte, return Cb = 0 if<"A" or >"Z"
- **$B0AD**: branch if <"A" or >"Z" (go check if string)
- **$B0AF**: copy 2nd character ignore further (valid) characters in the variable name
- **$B0B0**: increment and scan memory, 3rd character
- **$B0B3**: loop if character = "0"-"9" (ignore)
- **$B0B5**: check byte, return Cb = 0 if<"A" or >"Z"
- **$B0B8**: loop if character = "A"-"Z" (ignore) check if string variable
- **$B0BA**: compare with "$"
- **$B0BC**: branch if not string type is string
- **$B0BE**: set data type = string
- **$B0C0**: set data type flag, $FF = string, $00 = numeric
- **$B0C2**: branch always
- **$B0C4**: compare with "%"
- **$B0C6**: branch if not integer
- **$B0C8**: get subscript/FNX flag
- **$B0CA**: if ?? do syntax error then warm start
- **$B0CC**: set integer type
- **$B0CE**: set data type = integer
- **$B0D0**: OR current variable name first byte
- **$B0D2**: save current variable name first byte
- **$B0D4**: get 2nd character back
- **$B0D5**: set top bit, indicate string or integer variable
- **$B0D7**: copy back to 2nd character temp
- **$B0D8**: increment and scan memory
- **$B0DB**: save 2nd character
- **$B0DD**: set carry for subtract
- **$B0DE**: or with subscript/FNX flag - or FN name
- **$B0E0**: subtract "("
- **$B0E2**: branch if not "("
- **$B0E4**: go find, or make, array either find or create variable variable name wasn't xx(.... so look for plain variable
- **$B0E7**: clear A
- **$B0E9**: clear subscript/FNX flag
- **$B0EB**: get start of variables low byte
- **$B0ED**: get start of variables high byte
- **$B0EF**: save search address high byte
- **$B0F1**: save search address low byte
- **$B0F3**: compare with end of variables high byte
- **$B0F5**: skip next compare if <> high addresses were = so compare low addresses
- **$B0F7**: compare low address with end of variables low byte
- **$B0F9**: if not found go make new variable
- **$B0FB**: get 1st character of variable to find
- **$B0FD**: compare with variable name 1st character
- **$B0FF**: branch if no match 1st characters match so compare 2nd character
- **$B101**: get 2nd character of variable to find
- **$B103**: index to point to variable name 2nd character
- **$B104**: compare with variable name 2nd character
- **$B106**: branch if match (found variable)
- **$B108**: else decrement index (now = $00)
- **$B109**: clear carry for add
- **$B10A**: get search address low byte
- **$B10C**: +7, offset to next variable name
- **$B10E**: loop if no overflow to high byte
- **$B110**: else increment high byte
- **$B111**: loop always, RAM doesn't extend to $FFFF check byte, return Cb = 0 if<"A" or >"Z"
- **$B113**: compare with "A"
- **$B115**: exit if less carry is set
- **$B117**: subtract "Z"+1
- **$B119**: set carry
- **$B11A**: subtract $A5 (restore byte) carry clear if byte > $5A
- **$B11C**: reached end of variable memory without match ... so create new variable
- **$B11D**: pop return address low byte
- **$B11E**: push return address low byte
- **$B11F**: compare with expected calling routine return low byte
- **$B121**: if not get variable go create new variable this will only drop through if the call was from $AF28 and is only called from there if it is searching for a variable from the right hand side of a LET a=b statement, it prevents the creation of variables not assigned a value. value returned by this is either numeric zero, exponent byte is $00, or null string, descriptor length byte is $00. in fact a pointer to any $00 byte would have done. else return dummy null value
- **$B123**: set result pointer low byte
- **$B125**: set result pointer high byte
- **$B127**: create new numeric variable
- **$B128**: get variable name first character
- **$B12A**: get variable name second character
- **$B12C**: compare first character with "T"
- **$B12E**: branch if not "T"
- **$B130**: compare second character with "I$"
- **$B132**: if "I$" return null value
- **$B134**: compare second character with "I"
- **$B136**: branch if not "I" if name is "TI" do syntax error
- **$B138**: do syntax error then warm start
- **$B13B**: compare first character with "S"
- **$B13D**: branch if not "S"
- **$B13F**: compare second character with "T"
- **$B141**: if name is "ST" do syntax error
- **$B143**: get end of variables low byte
- **$B145**: get end of variables high byte
- **$B147**: save old block start low byte
- **$B149**: save old block start high byte
- **$B14B**: get end of arrays low byte
- **$B14D**: get end of arrays high byte
- **$B14F**: save old block end low byte
- **$B151**: save old block end high byte
- **$B153**: clear carry for add
- **$B154**: +7, space for one variable
- **$B156**: branch if no overflow to high byte
- **$B158**: else increment high byte
- **$B159**: set new block end low byte
- **$B15B**: set new block end high byte
- **$B15D**: open up space in memory
- **$B160**: get new start low byte
- **$B162**: get new start high byte (-$100)
- **$B164**: correct high byte
- **$B165**: set end of variables low byte
- **$B167**: set end of variables high byte
- **$B169**: clear index
- **$B16B**: get variable name 1st character
- **$B16D**: save variable name 1st character
- **$B16F**: increment index
- **$B170**: get variable name 2nd character
- **$B172**: save variable name 2nd character
- **$B174**: clear A
- **$B176**: increment index
- **$B177**: initialise variable byte
- **$B179**: increment index
- **$B17A**: initialise variable byte
- **$B17C**: increment index
- **$B17D**: initialise variable byte
- **$B17F**: increment index
- **$B180**: initialise variable byte
- **$B182**: increment index
- **$B183**: initialise variable byte found a match for variable
- **$B185**: get variable address low byte
- **$B187**: clear carry for add
- **$B188**: +2, offset past variable name bytes
- **$B18A**: get variable address high byte
- **$B18C**: branch if no overflow from add
- **$B18E**: else increment high byte
- **$B18F**: save current variable pointer low byte
- **$B191**: save current variable pointer high byte
- **$B193**: set-up array pointer to first element in array
- **$B194**: get # of dimensions (1, 2 or 3)
- **$B196**: *2 (also clears the carry !)
- **$B197**: +5 (result is 7, 9 or 11 here)
- **$B199**: add array start pointer low byte
- **$B19B**: get array pointer high byte
- **$B19D**: branch if no overflow
- **$B19F**: else increment high byte
- **$B1A0**: save array data pointer low byte
- **$B1A2**: save array data pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$B08B**: Flag für nicht dimensionieren
- **$B08D**: CHRGOT letztes Zeichen holen
- **$B090**: DIM-Flag setzen
- **$B092**: Variablenname
- **$B094**: CHRGOT letztes Zeichen holen
- **$B097**: prüft auf Buchstabe
- **$B09A**: ja: $B09F
- **$B09C**: 'SYNTAX ERROR'
- **$B09F**: Wert laden und damit
- **$B0A1**: Stringflag löschen
- **$B0A3**: Integerflag löschen
- **$B0A5**: CHRGET nächstes Zeichen holen
- **$B0A8**: Ziffer?
- **$B0AA**: prüft auf Buchstabe
- **$B0AD**: nein: $B0BA
- **$B0AF**: zweiter Buchstabe des Names
- **$B0B0**: CHRGET nächstes Zeichen holen
- **$B0B3**: Ziffer?
- **$B0B5**: prüft auf Buchstabe
- **$B0B8**: ja: weitere Zeichen überlesen
- **$B0BA**: '$' Code?
- **$B0BC**: nein: $B0C4
- **$B0BE**: Wert laden und
- **$B0C0**: Stringflag setzen
- **$B0C2**: Sprung
- **$B0C4**: '%' Code?
- **$B0C6**: nein: $B0DB
- **$B0C8**: Integer erlaubt?
- **$B0CA**: nein: 'SYNTAX ERROR'
- **$B0CC**: Wert für Integer laden
- **$B0CE**: und Integerflag setzen
- **$B0D0**: Bit 7 im 1.Zeichen setzen und
- **$B0D2**: speichern (Bit7=1: Integer)
- **$B0D4**: X nach Akku speichern
- **$B0D5**: Bit 7 im 2.Buchstaben setzen
- **$B0D7**: X-Reg. zurückholen
- **$B0D8**: CHRGET nächstes Zeichen holen
- **$B0DB**: zweiten Buchstaben speichern
- **$B0DD**: Feldvariablen erlaubt?
- **$B0DE**: wenn nicht, Bit7 setzen
- **$B0E0**: '('-Wert abziehen
- **$B0E2**: nicht Klammer auf?
- **$B0E4**: dimensionierte Variable holen
- **$B0E7**: Wert laden und
- **$B0E9**: FN-Flag = 0 setzen
- **$B0EB**: Zeiger auf Variablenanfang
- **$B0ED**: holen (LOW und HIGH)
- **$B0EF**: und zum
- **$B0F1**: Suchen merken
- **$B0F3**: Suchzeiger = Variablenanfang
- **$B0F5**: nein: $B0FB
- **$B0F7**: Ende der Variablen erreicht?
- **$B0F9**: ja: nicht gefunden, anlegen
- **$B0FB**: ersten Buchstaben des Namens
- **$B0FD**: mit Tabelle vergleichen
- **$B0FF**: nein: weitersuchen
- **$B101**: zweiten Buchstaben
- **$B103**: Zeiger erhöhen
- **$B104**: vergleichen
- **$B106**: gleich: gefunden
- **$B108**: Zeiger vermindern
- **$B109**: Carry setzen (Addition)
- **$B10A**: Zeiger um 7
- **$B10C**: erhöhen (2+5 Byte REAL Var.)
- **$B10E**: (Länge eines V.-Eintrags)
- **$B110**: Übertrag addieren
- **$B111**: weiter suchen

### Marko Mäkelä (Marko Mäkelä)
- **$B0BA**: $
- **$B0C4**: %
- **$B0E0**: (

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B08D**: GET FIRST CHAR OF VARIABLE NAME
- **$B090**: X IS NONZERO IF FROM DIM
- **$B097**: IS IT A LETTER?
- **$B09A**: YES, OKAY SO FAR
- **$B09C**: NO, SYNTAX ERROR
- **$B0A5**: SECOND CHAR OF VARIABLE NAME
- **$B0A8**: NUMERIC
- **$B0AA**: LETTER?
- **$B0AD**: NO, END OF NAME
- **$B0AF**: SAVE SECOND CHAR OF NAME IN X
- **$B0B0**: SCAN TO END OF VARIABLE NAME
- **$B0B3**: NUMERIC
- **$B0B8**: ALPHA
- **$B0BA**: STRING?
- **$B0BC**: NO
- **$B0C2**: ...ALWAYS
- **$B0C4**: INTEGER?
- **$B0C6**: NO
- **$B0C8**: YES; INTEGER VARIABLE ALLOWED?
- **$B0CA**: NO, SYNTAX ERROR
- **$B0CC**: YES
- **$B0CE**: FLAG INTEGER MODE
- **$B0D2**: SET SIGN BIT ON VARNAME
- **$B0D4**: SECOND CHAR OF NAME
- **$B0D5**: SET SIGN
- **$B0D8**: GET TERMINATING CHAR
- **$B0DB**: STORE SECOND CHAR OF NAME
- **$B0DE**: $00 OR $40 IF SUBSCRIPTS OK, ELSE $80
- **$B0E0**: IF SUBFLG=$00 AND CHAR="("...
- **$B0E2**: NOPE
- **$B0E4**: YES
- **$B0EB**: START LOWTR AT SIMPLE VARIABLE TABLE
- **$B0F3**: END OF SIMPLE VARIABLES?
- **$B0F5**: NO, GO ON
- **$B0F7**: YES; END OF ARRAYS?
- **$B0F9**: YES, MAKE ONE
- **$B0FB**: SAME FIRST LETTER?
- **$B0FF**: NOT SAME FIRST LETTER
- **$B101**: SAME SECOND LETTER?
- **$B106**: YES, SAME VARIABLE NAME
- **$B108**: NO, BUMP TO NEXT NAME
- **$B111**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*