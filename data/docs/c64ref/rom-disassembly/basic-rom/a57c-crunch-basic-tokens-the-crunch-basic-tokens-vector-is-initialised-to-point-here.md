---
title: crunch BASIC tokens, the crunch BASIC tokens vector is initialised to point
  here
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
- 00d7-data
- a57c-tokenize-the-input-line
- a5ac-with-current-char-from-input-line
- a5e5-by-copying-chars-up-to-endchr
- a5f5-advance-pointer-to-next-token-name
- ab45-print
- return
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $A57C
  address_end: $A612
  symbol: crunch-basic-tokens-the-crunch-basic-tokens-vector-is-initialised-to-point-here
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A57C**: get BASIC execute pointer low byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A587**: PI'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A57C**: INDEX INTO UNPARSED LINE'
---

# $A57C — crunch BASIC tokens, the crunch BASIC tokens vector is initialised to point here

## Disassemblatura
```assembly
.A57C  A6 7A    LDX $7A   ; get BASIC execute pointer low byte
.A57E  A0 04    LDY #$04   ; set save index
.A580  84 0F    STY $0F   ; clear open quote/DATA flag
.A582  BD 00 02 LDA $0200,X   ; get a byte from the input buffer
.A585  10 07    BPL $A58E   ; if b7 clear go do crunching
.A587  C9 FF    CMP #$FF   ; compare with the token for PI, this toke is input directly from the keyboard as the PI character
.A589  F0 3E    BEQ $A5C9   ; if PI save byte then continue crunching this is the bit of code that stops you being able to enter some keywords as just single shifted characters. If this dropped through you would be able to enter GOTO as just [SHIFT]G
.A58B  E8       INX   ; increment read index
.A58C  D0 F4    BNE $A582   ; loop if more to do, branch always
.A58E  C9 20    CMP #$20   ; compare with [SPACE]
.A590  F0 37    BEQ $A5C9   ; if [SPACE] save byte then continue crunching
.A592  85 08    STA $08   ; save buffer byte as search character
.A594  C9 22    CMP #$22   ; compare with quote character
.A596  F0 56    BEQ $A5EE   ; if quote go copy quoted string
.A598  24 0F    BIT $0F   ; get open quote/DATA token flag
.A59A  70 2D    BVS $A5C9   ; branch if b6 of Oquote set, was DATA go save byte then continue crunching
.A59C  C9 3F    CMP #$3F   ; compare with "?" character
.A59E  D0 04    BNE $A5A4   ; if not "?" continue crunching
.A5A0  A9 99    LDA #$99   ; else the keyword token is $99, PRINT
.A5A2  D0 25    BNE $A5C9   ; go save byte then continue crunching, branch always
.A5A4  C9 30    CMP #$30   ; compare with "0"
.A5A6  90 04    BCC $A5AC   ; branch if <, continue crunching
.A5A8  C9 3C    CMP #$3C   ; compare with "<"
.A5AA  90 1D    BCC $A5C9   ; if <, 0123456789:; go save byte then continue crunching gets here with next character not numeric, ";" or ":"
.A5AC  84 71    STY $71   ; copy save index
.A5AE  A0 00    LDY #$00   ; clear table pointer
.A5B0  84 0B    STY $0B   ; clear word index
.A5B2  88       DEY   ; adjust for pre increment loop
.A5B3  86 7A    STX $7A   ; save BASIC execute pointer low byte, buffer index
.A5B5  CA       DEX   ; adjust for pre increment loop
.A5B6  C8       INY   ; next table byte
.A5B7  E8       INX   ; next buffer byte
.A5B8  BD 00 02 LDA $0200,X   ; get byte from input buffer
.A5BB  38       SEC   ; set carry for subtract
.A5BC  F9 9E A0 SBC $A09E,Y   ; subtract table byte
.A5BF  F0 F5    BEQ $A5B6   ; go compare next if match
.A5C1  C9 80    CMP #$80   ; was it end marker match ?
.A5C3  D0 30    BNE $A5F5   ; branch if not, not found keyword actually this works even if the input buffer byte is the end marker, i.e. a shifted character. As you can't enter any keywords as a single shifted character, see above, you can enter keywords in shorthand by shifting any character after the first. so RETURN can be entered as R[SHIFT]E, RE[SHIFT]T, RET[SHIFT]U or RETU[SHIFT]R. RETUR[SHIFT]N however will not work because the [SHIFT]N will match the RETURN end marker so the routine will try to match the next character. else found keyword
.A5C5  05 0B    ORA $0B   ; OR with word index, +$80 in A makes token
.A5C7  A4 71    LDY $71   ; restore save index save byte then continue crunching
.A5C9  E8       INX   ; increment buffer read index
.A5CA  C8       INY   ; increment save index
.A5CB  99 FB 01 STA $01FB,Y   ; save byte to output
.A5CE  B9 FB 01 LDA $01FB,Y   ; get byte from output, set flags
.A5D1  F0 36    BEQ $A609   ; branch if was null [EOL] A holds the token here
.A5D3  38       SEC   ; set carry for subtract
.A5D4  E9 3A    SBC #$3A   ; subtract ":"
.A5D6  F0 04    BEQ $A5DC   ; branch if it was (is now $00) A now holds token-':'
.A5D8  C9 49    CMP #$49   ; compare with the token for DATA-':'
.A5DA  D0 02    BNE $A5DE   ; if not DATA go try REM token was : or DATA
.A5DC  85 0F    STA $0F   ; save the token-$3A
.A5DE  38       SEC   ; set carry for subtract
.A5DF  E9 55    SBC #$55   ; subtract the token for REM-':'
.A5E1  D0 9F    BNE $A582   ; if wasn't REM crunch next bit of line
.A5E3  85 08    STA $08   ; else was REM so set search for [EOL] loop for "..." etc.
.A5E5  BD 00 02 LDA $0200,X   ; get byte from input buffer
.A5E8  F0 DF    BEQ $A5C9   ; if null [EOL] save byte then continue crunching
.A5EA  C5 08    CMP $08   ; compare with stored character
.A5EC  F0 DB    BEQ $A5C9   ; if match save byte then continue crunching
.A5EE  C8       INY   ; increment save index
.A5EF  99 FB 01 STA $01FB,Y   ; save byte to output
.A5F2  E8       INX   ; increment buffer index
.A5F3  D0 F0    BNE $A5E5   ; loop while <> 0, should never reach 0 not found keyword this go
.A5F5  A6 7A    LDX $7A   ; restore BASIC execute pointer low byte
.A5F7  E6 0B    INC $0B   ; increment word index (next word) now find end of this word in the table
.A5F9  C8       INY   ; increment table index
.A5FA  B9 9D A0 LDA $A09D,Y   ; get table byte
.A5FD  10 FA    BPL $A5F9   ; loop if not end of word yet
.A5FF  B9 9E A0 LDA $A09E,Y   ; get byte from keyword table
.A602  D0 B4    BNE $A5B8   ; go test next word if not zero byte, end of table reached end of table with no match
.A604  BD 00 02 LDA $0200,X   ; restore byte from input buffer
.A607  10 BE    BPL $A5C7   ; branch always, all unmatched bytes in the buffer are $00 to $7F, go save byte in output and continue crunching reached [EOL]
.A609  99 FD 01 STA $01FD,Y   ; save [EOL]
.A60C  C6 7B    DEC $7B   ; decrement BASIC execute pointer high byte
.A60E  A9 FF    LDA #$FF   ; point to start of buffer-1
.A610  85 7A    STA $7A   ; set BASIC execute pointer low byte
.A612  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A57C**: get BASIC execute pointer low byte
- **$A57E**: set save index
- **$A580**: clear open quote/DATA flag
- **$A582**: get a byte from the input buffer
- **$A585**: if b7 clear go do crunching
- **$A587**: compare with the token for PI, this toke is input directly from the keyboard as the PI character
- **$A589**: if PI save byte then continue crunching this is the bit of code that stops you being able to enter some keywords as just single shifted characters. If this dropped through you would be able to enter GOTO as just [SHIFT]G
- **$A58B**: increment read index
- **$A58C**: loop if more to do, branch always
- **$A58E**: compare with [SPACE]
- **$A590**: if [SPACE] save byte then continue crunching
- **$A592**: save buffer byte as search character
- **$A594**: compare with quote character
- **$A596**: if quote go copy quoted string
- **$A598**: get open quote/DATA token flag
- **$A59A**: branch if b6 of Oquote set, was DATA go save byte then continue crunching
- **$A59C**: compare with "?" character
- **$A59E**: if not "?" continue crunching
- **$A5A0**: else the keyword token is $99, PRINT
- **$A5A2**: go save byte then continue crunching, branch always
- **$A5A4**: compare with "0"
- **$A5A6**: branch if <, continue crunching
- **$A5A8**: compare with "<"
- **$A5AA**: if <, 0123456789:; go save byte then continue crunching gets here with next character not numeric, ";" or ":"
- **$A5AC**: copy save index
- **$A5AE**: clear table pointer
- **$A5B0**: clear word index
- **$A5B2**: adjust for pre increment loop
- **$A5B3**: save BASIC execute pointer low byte, buffer index
- **$A5B5**: adjust for pre increment loop
- **$A5B6**: next table byte
- **$A5B7**: next buffer byte
- **$A5B8**: get byte from input buffer
- **$A5BB**: set carry for subtract
- **$A5BC**: subtract table byte
- **$A5BF**: go compare next if match
- **$A5C1**: was it end marker match ?
- **$A5C3**: branch if not, not found keyword actually this works even if the input buffer byte is the end marker, i.e. a shifted character. As you can't enter any keywords as a single shifted character, see above, you can enter keywords in shorthand by shifting any character after the first. so RETURN can be entered as R[SHIFT]E, RE[SHIFT]T, RET[SHIFT]U or RETU[SHIFT]R. RETUR[SHIFT]N however will not work because the [SHIFT]N will match the RETURN end marker so the routine will try to match the next character. else found keyword
- **$A5C5**: OR with word index, +$80 in A makes token
- **$A5C7**: restore save index save byte then continue crunching
- **$A5C9**: increment buffer read index
- **$A5CA**: increment save index
- **$A5CB**: save byte to output
- **$A5CE**: get byte from output, set flags
- **$A5D1**: branch if was null [EOL] A holds the token here
- **$A5D3**: set carry for subtract
- **$A5D4**: subtract ":"
- **$A5D6**: branch if it was (is now $00) A now holds token-':'
- **$A5D8**: compare with the token for DATA-':'
- **$A5DA**: if not DATA go try REM token was : or DATA
- **$A5DC**: save the token-$3A
- **$A5DE**: set carry for subtract
- **$A5DF**: subtract the token for REM-':'
- **$A5E1**: if wasn't REM crunch next bit of line
- **$A5E3**: else was REM so set search for [EOL] loop for "..." etc.
- **$A5E5**: get byte from input buffer
- **$A5E8**: if null [EOL] save byte then continue crunching
- **$A5EA**: compare with stored character
- **$A5EC**: if match save byte then continue crunching
- **$A5EE**: increment save index
- **$A5EF**: save byte to output
- **$A5F2**: increment buffer index
- **$A5F3**: loop while <> 0, should never reach 0 not found keyword this go
- **$A5F5**: restore BASIC execute pointer low byte
- **$A5F7**: increment word index (next word) now find end of this word in the table
- **$A5F9**: increment table index
- **$A5FA**: get table byte
- **$A5FD**: loop if not end of word yet
- **$A5FF**: get byte from keyword table
- **$A602**: go test next word if not zero byte, end of table reached end of table with no match
- **$A604**: restore byte from input buffer
- **$A607**: branch always, all unmatched bytes in the buffer are $00 to $7F, go save byte in output and continue crunching reached [EOL]
- **$A609**: save [EOL]
- **$A60C**: decrement BASIC execute pointer high byte
- **$A60E**: point to start of buffer-1
- **$A610**: set BASIC execute pointer low byte

### Marko Mäkelä (Marko Mäkelä)
- **$A587**: PI
- **$A58E**: space
- **$A594**: quote mark
- **$A59C**: question mark
- **$A5A0**: PRINT code
- **$A5A4**: 0
- **$A5D4**: colon
- **$A5D8**: DATA code
- **$A5DF**: REM code

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A57C**: INDEX INTO UNPARSED LINE
- **$A57E**: INDEX TO PARSED OUTPUT LINE
- **$A580**: CLEAR SIGN-BIT OF DATAFLG
- **$A58E**: IGNORE BLANKS
- **$A594**: START OF QUOTATION?
- **$A59A**: BRANCH IF IN "DATA" STATEMENT
- **$A59C**: SHORTHAND FOR "PRINT"?
- **$A59E**: NO
- **$A5A0**: YES, REPLACE WITH "PRINT" TOKEN
- **$A5A2**: ...ALWAYS
- **$A5A4**: IS IT A DIGIT, COLON, OR SEMI-COLON?
- **$A5A6**: NO, PUNCTUATION !"#$%&amp;'()*+,-./
- **$A5AA**: YES, NOT A TOKEN

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*