---
title: perform LIST
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
- a69c-basic-befehl-list
- a6c9-list-lines-from-5f60-to-1415
- a717-umwandlen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A69C
  address_end: $A717
  symbol: perform-list
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A69C**: branch if next character not token (LIST n...)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A69C**: Ziffer ? (Zeilennummer)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A69C**: NO  LINE # SPECIFIED'
---

# $A69C — perform LIST

## Disassemblatura
```assembly
.A69C  90 06    BCC $A6A4   ; branch if next character not token (LIST n...)
.A69E  F0 04    BEQ $A6A4   ; branch if next character [NULL] (LIST)
.A6A0  C9 AB    CMP #$AB   ; compare with token for -
.A6A2  D0 E9    BNE $A68D   ; exit if not - (LIST -m) LIST [[n][-m]] this bit sets the n , if present, as the start and end
.A6A4  20 6B A9 JSR $A96B   ; get fixed-point number into temporary integer
.A6A7  20 13 A6 JSR $A613   ; search BASIC for temporary integer line number
.A6AA  20 79 00 JSR $0079   ; scan memory
.A6AD  F0 0C    BEQ $A6BB   ; branch if no more chrs this bit checks the - is present
.A6AF  C9 AB    CMP #$AB   ; compare with token for -
.A6B1  D0 8E    BNE $A641   ; return if not "-" (will be SN error) LIST [n]-m the - was there so set m as the end value
.A6B3  20 73 00 JSR $0073   ; increment and scan memory
.A6B6  20 6B A9 JSR $A96B   ; get fixed-point number into temporary integer
.A6B9  D0 86    BNE $A641   ; exit if not ok
.A6BB  68       PLA   ; dump return address low byte, exit via warm start
.A6BC  68       PLA   ; dump return address high byte
.A6BD  A5 14    LDA $14   ; get temporary integer low byte
.A6BF  05 15    ORA $15   ; OR temporary integer high byte
.A6C1  D0 06    BNE $A6C9   ; branch if start set
.A6C3  A9 FF    LDA #$FF   ; set for -1
.A6C5  85 14    STA $14   ; set temporary integer low byte
.A6C7  85 15    STA $15   ; set temporary integer high byte
.A6C9  A0 01    LDY #$01   ; set index for line
.A6CB  84 0F    STY $0F   ; clear open quote flag
.A6CD  B1 5F    LDA ($5F),Y   ; get next line pointer high byte
.A6CF  F0 43    BEQ $A714   ; if null all done so exit
.A6D1  20 2C A8 JSR $A82C   ; do CRTL-C check vector
.A6D4  20 D7 AA JSR $AAD7   ; print CR/LF
.A6D7  C8       INY   ; increment index for line
.A6D8  B1 5F    LDA ($5F),Y   ; get line number low byte
.A6DA  AA       TAX   ; copy to X
.A6DB  C8       INY   ; increment index
.A6DC  B1 5F    LDA ($5F),Y   ; get line number high byte
.A6DE  C5 15    CMP $15   ; compare with temporary integer high byte
.A6E0  D0 04    BNE $A6E6   ; branch if no high byte match
.A6E2  E4 14    CPX $14   ; compare with temporary integer low byte
.A6E4  F0 02    BEQ $A6E8   ; branch if = last line to do, < will pass next branch else
.A6E6  B0 2C    BCS $A714   ; if greater all done so exit
.A6E8  84 49    STY $49   ; save index for line
.A6EA  20 CD BD JSR $BDCD   ; print XA as unsigned integer
.A6ED  A9 20    LDA #$20   ; space is the next character
.A6EF  A4 49    LDY $49   ; get index for line
.A6F1  29 7F    AND #$7F   ; mask top out bit of character
.A6F3  20 47 AB JSR $AB47   ; go print the character
.A6F6  C9 22    CMP #$22   ; was it " character
.A6F8  D0 06    BNE $A700   ; if not skip the quote handle we are either entering or leaving a pair of quotes
.A6FA  A5 0F    LDA $0F   ; get open quote flag
.A6FC  49 FF    EOR #$FF   ; toggle it
.A6FE  85 0F    STA $0F   ; save it back
.A700  C8       INY   ; increment index
.A701  F0 11    BEQ $A714   ; line too long so just bail out and do a warm start
.A703  B1 5F    LDA ($5F),Y   ; get next byte
.A705  D0 10    BNE $A717   ; if not [EOL] (go print character) was [EOL]
.A707  A8       TAY   ; else clear index
.A708  B1 5F    LDA ($5F),Y   ; get next line pointer low byte
.A70A  AA       TAX   ; copy to X
.A70B  C8       INY   ; increment index
.A70C  B1 5F    LDA ($5F),Y   ; get next line pointer high byte
.A70E  86 5F    STX $5F   ; set pointer to line low byte
.A710  85 60    STA $60   ; set pointer to line high byte
.A712  D0 B5    BNE $A6C9   ; go do next line if not [EOT] else ...
.A714  4C 86 E3 JMP $E386   ; do warm start
.A717  6C 06 03 JMP ($0306)   ; do uncrunch BASIC tokens
```


## Commenti

### Original Disassembly (—)
- **$A69C**: branch if next character not token (LIST n...)
- **$A69E**: branch if next character [NULL] (LIST)
- **$A6A0**: compare with token for -
- **$A6A2**: exit if not - (LIST -m) LIST [[n][-m]] this bit sets the n , if present, as the start and end
- **$A6A4**: get fixed-point number into temporary integer
- **$A6A7**: search BASIC for temporary integer line number
- **$A6AA**: scan memory
- **$A6AD**: branch if no more chrs this bit checks the - is present
- **$A6AF**: compare with token for -
- **$A6B1**: return if not "-" (will be SN error) LIST [n]-m the - was there so set m as the end value
- **$A6B3**: increment and scan memory
- **$A6B6**: get fixed-point number into temporary integer
- **$A6B9**: exit if not ok
- **$A6BB**: dump return address low byte, exit via warm start
- **$A6BC**: dump return address high byte
- **$A6BD**: get temporary integer low byte
- **$A6BF**: OR temporary integer high byte
- **$A6C1**: branch if start set
- **$A6C3**: set for -1
- **$A6C5**: set temporary integer low byte
- **$A6C7**: set temporary integer high byte
- **$A6C9**: set index for line
- **$A6CB**: clear open quote flag
- **$A6CD**: get next line pointer high byte
- **$A6CF**: if null all done so exit
- **$A6D1**: do CRTL-C check vector
- **$A6D4**: print CR/LF
- **$A6D7**: increment index for line
- **$A6D8**: get line number low byte
- **$A6DA**: copy to X
- **$A6DB**: increment index
- **$A6DC**: get line number high byte
- **$A6DE**: compare with temporary integer high byte
- **$A6E0**: branch if no high byte match
- **$A6E2**: compare with temporary integer low byte
- **$A6E4**: branch if = last line to do, < will pass next branch else
- **$A6E6**: if greater all done so exit
- **$A6E8**: save index for line
- **$A6EA**: print XA as unsigned integer
- **$A6ED**: space is the next character
- **$A6EF**: get index for line
- **$A6F1**: mask top out bit of character
- **$A6F3**: go print the character
- **$A6F6**: was it " character
- **$A6F8**: if not skip the quote handle we are either entering or leaving a pair of quotes
- **$A6FA**: get open quote flag
- **$A6FC**: toggle it
- **$A6FE**: save it back
- **$A700**: increment index
- **$A701**: line too long so just bail out and do a warm start
- **$A703**: get next byte
- **$A705**: if not [EOL] (go print character) was [EOL]
- **$A707**: else clear index
- **$A708**: get next line pointer low byte
- **$A70A**: copy to X
- **$A70B**: increment index
- **$A70C**: get next line pointer high byte
- **$A70E**: set pointer to line low byte
- **$A710**: set pointer to line high byte
- **$A712**: go do next line if not [EOT] else ...
- **$A714**: do warm start
- **$A717**: do uncrunch BASIC tokens

### Commodore-64-intern-Buch (Commodore)
- **$A69C**: Ziffer ? (Zeilennummer)
- **$A69E**: nur LIST ?
- **$A6A0**: Code für '-'?
- **$A6A2**: anderer Code, dann SYNTAX ERR
- **$A6A4**: Zeilennummer holen
- **$A6A7**: Startadresse berechnen
- **$A6AA**: CHRGOT letztes Zeichen holen
- **$A6AD**: keine Zeilennummer
- **$A6AF**: Code für '-'?
- **$A6B1**: nein: SYNTAX ERROR
- **$A6B3**: CHRGET nächstes Zeichen holen
- **$A6B6**: Zeilennummer holen
- **$A6B9**: kein Trennzeichen: SYNTAX ERR
- **$A6BB**: 2 Bytes von Stapel holen
- **$A6BC**: (Rücksprungadresse übergehen)
- **$A6BD**: zweite Zeilennummer laden
- **$A6BF**: gleich null ?
- **$A6C1**: Nein: $A6C9
- **$A6C3**: Wert laden und
- **$A6C5**: zweite Zeilennummer Maximal-
- **$A6C7**: wert $FFFF (65535)
- **$A6C9**: Zeiger setzen
- **$A6CB**: und Quote Modus abschalten
- **$A6CD**: Linkadresse HIGH holen
- **$A6CF**: Ja: dann fertig
- **$A6D1**: prüft auf Stop-Taste
- **$A6D4**: "CR" ausgeben, neue Zeile
- **$A6D7**: Zeiger erhöhen
- **$A6D8**: Zeilenadresse holen (LOW)
- **$A6DA**: und in das X-Reg. schieben
- **$A6DB**: Zeiger erhöhen
- **$A6DC**: Zeilenadresse holen (HIGH)
- **$A6DE**: mit Endnummer vergleichen
- **$A6E0**: Gleich? Nein: $A6E6
- **$A6E2**: LOW-Nummer vergleichen
- **$A6E4**: Gleich? Ja: $A6E8
- **$A6E6**: Größer: dann fertig
- **$A6E8**: Y-Reg. Zwischenspeichern
- **$A6EA**: Zeilennnummer ausgeben
- **$A6ED**: ' ' Leerzeichen
- **$A6EF**: Y-Reg. wiederholen
- **$A6F1**: Bit 7 löschen
- **$A6F3**: Zeichen ausgeben
- **$A6F6**: '"' Hochkomma ?
- **$A6F8**: Nein: $A700
- **$A6FA**: Hochkomma-Flag laden,
- **$A6FC**: umdrehen (NOT)
- **$A6FE**: und wieder abspeichern
- **$A700**: Zeilenende nach 255 Zeichen ?
- **$A701**: Nein: dann aufhören
- **$A703**: Zeichen holen
- **$A705**: kein Zeilenende, dann listen
- **$A707**: Akku als Zeiger nach Y
- **$A708**: Startadresse der nächsten
- **$A70A**: Zeile holen (LOW) und nach X
- **$A70B**: Zeiger erhöhen
- **$A70C**: Adresse der Zeile (HIGH)
- **$A70E**: als Zeiger merken
- **$A710**: (speichern nach $5F/60) und
- **$A712**: weitermachen
- **$A714**: zum BASIC-Warmstart

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A69C**: NO  LINE # SPECIFIED
- **$A69E**: ---DITTO---
- **$A6A0**: IF DASH OR COMMA, START AT LINE 0
- **$A6A2**: NO, ERROR
- **$A6A4**: CONVERT LINE NUMBER IF ANY
- **$A6A7**: POINT LOWTR TO 1ST LINE
- **$A6AA**: RANGE SPECIFIED?
- **$A6AD**: NO
- **$A6B3**: GET NEXT CHAR
- **$A6B6**: CONVERT SECOND LINE #
- **$A6B9**: BRANCH IF SYNTAX ERR
- **$A6BB**: POP RETURN ADRESS
- **$A6BC**: (GET BACK BY "JMP NEWSTT")
- **$A6BD**: IF NO SECOND NUMBER, USE $FFFF
- **$A6C1**: THERE WAS A SECOND NUMBER
- **$A6C3**: MAX END RANGE
- **$A6CD**: HIGH BYTE OF LINK
- **$A6CF**: END OF PROGRAM
- **$A6D1**: CHECK IF CONTROL-C HAS BEEN TYPED
- **$A6D4**: NO, PRINT <RETURN>
- **$A6D8**: GET LINE #, COMPARE WITH END RANGE
- **$A6E4**: ON LAST LINE OF RANGE
- **$A6E6**: FINISHED THE RANGE LIST ONE LINE
- **$A6EA**: PRINT LINE # FROM X,A
- **$A6ED**: PRINT SPACE AFTER LINE #
- **$A705**: NOT END OF LINE YET
- **$A707**: END OF LINE
- **$A708**: GET LINK TO NEXT LINE
- **$A70E**: POINT TO NEXT LINE
- **$A712**: BRANCH IF NOT END OF PROGRAM
- **$A714**: TO NEXT STATEMENT
- **$A71A**: BRANCH IF NOT A TOKEN
- **$A725**: CONVERT TOKEN TO INDEX
- **$A728**: SAVE LINE POINTER
- **$A72C**: SKIP KEYWORDS UNTIL REACH THIS ONE
- **$A733**: NOT AT END OF KEYWORD YET
- **$A735**: END OF KEYWORD, ALWAYS BRANCHES
- **$A73B**: LAST CHAR OF KEYWORD
- **$A740**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*