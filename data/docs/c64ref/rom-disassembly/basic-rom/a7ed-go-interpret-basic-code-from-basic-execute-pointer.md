---
title: go interpret BASIC code from BASIC execute pointer
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
- a7ed-basic-statement-ausfhren
- a80e-prft-auf-go-to-code
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A7ED
  address_end: $A81A
  symbol: go-interpret-basic-code-from-basic-execute-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A7ED**: if the first byte is null just exit'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A7ED**: Zeilenende, dann fertig'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A807**: colon'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A7ED**: END OF LINE, NULL STATEMENT'
---

# $A7ED — go interpret BASIC code from BASIC execute pointer

## Disassemblatura
```assembly
.A7ED  F0 3C    BEQ $A82B   ; if the first byte is null just exit
.A7EF  E9 80    SBC #$80   ; normalise the token
.A7F1  90 11    BCC $A804   ; if wasn't token go do LET
.A7F3  C9 23    CMP #$23   ; compare with token for TAB(-$80
.A7F5  B0 17    BCS $A80E   ; branch if >= TAB(
.A7F7  0A       ASL   ; *2 bytes per vector
.A7F8  A8       TAY   ; copy to index
.A7F9  B9 0D A0 LDA $A00D,Y   ; get vector high byte
.A7FC  48       PHA   ; push on stack
.A7FD  B9 0C A0 LDA $A00C,Y   ; get vector low byte
.A800  48       PHA   ; push on stack
.A801  4C 73 00 JMP $0073   ; increment and scan memory and return. the return in this case calls the command code, the return from that will eventually return to the interpreter inner loop above
.A804  4C A5 A9 JMP $A9A5   ; perform LET was not [EOL]
.A807  C9 3A    CMP #$3A   ; comapre with ":"
.A809  F0 D6    BEQ $A7E1   ; if ":" go execute new code else ...
.A80B  4C 08 AF JMP $AF08   ; do syntax error then warm start token was >= TAB(
.A80E  C9 4B    CMP #$4B   ; compare with the token for GO
.A810  D0 F9    BNE $A80B   ; if not "GO" do syntax error then warm start else was "GO"
.A812  20 73 00 JSR $0073   ; increment and scan memory
.A815  A9 A4    LDA #$A4   ; set "TO" token
.A817  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.A81A  4C A0 A8 JMP $A8A0   ; perform GOTO
```


## Commenti

### Original Disassembly (—)
- **$A7ED**: if the first byte is null just exit
- **$A7EF**: normalise the token
- **$A7F1**: if wasn't token go do LET
- **$A7F3**: compare with token for TAB(-$80
- **$A7F5**: branch if >= TAB(
- **$A7F7**: *2 bytes per vector
- **$A7F8**: copy to index
- **$A7F9**: get vector high byte
- **$A7FC**: push on stack
- **$A7FD**: get vector low byte
- **$A800**: push on stack
- **$A801**: increment and scan memory and return. the return in this case calls the command code, the return from that will eventually return to the interpreter inner loop above
- **$A804**: perform LET was not [EOL]
- **$A807**: comapre with ":"
- **$A809**: if ":" go execute new code else ...
- **$A80B**: do syntax error then warm start token was >= TAB(
- **$A80E**: compare with the token for GO
- **$A810**: if not "GO" do syntax error then warm start else was "GO"
- **$A812**: increment and scan memory
- **$A815**: set "TO" token
- **$A817**: scan for CHR$(A), else do syntax error then warm start
- **$A81A**: perform GOTO

### Commodore-64-intern-Buch (Commodore)
- **$A7ED**: Zeilenende, dann fertig
- **$A7EF**: Token?
- **$A7F1**: nein: dann zum LET-Befehl
- **$A7F3**: NEW?
- **$A7F5**: Funktions-Token oder GO TO
- **$A7F7**: BASIC-Befehl, Code mal 2
- **$A7F8**: als Zeiger ins Y-Reg.
- **$A7F9**: Befehlsadresse (LOW und
- **$A7FC**: HIGH) aus Tabelle
- **$A7FD**: holen und als
- **$A800**: Rücksprungadresse auf Stapel
- **$A801**: Zeichen und Befehl ausführen
- **$A804**: zum LET-Befehl
- **$A807**: ':' ist es Doppelpunkt?
- **$A809**: ja: $A7E1
- **$A80B**: sonst 'SYNTAX ERROR'

### Marko Mäkelä (Marko Mäkelä)
- **$A807**: colon
- **$A80E**: GO code
- **$A815**: TO code
- **$A81A**: do GOTO

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A7ED**: END OF LINE, NULL STATEMENT
- **$A7EF**: FIRST CHAR A TOKEN?
- **$A7F1**: NOT TOKEN, MUST BE "LET"
- **$A7F3**: STATEMENT-TYPE TOKEN?
- **$A7F5**: NO, SYNTAX ERROR
- **$A7F7**: DOUBLE TO GET INDEX
- **$A7F8**: INTO ADDRESS TABLE
- **$A7FC**: PUT ADDRESS ON STACK
- **$A801**: GET NEXT CHR &amp; RTS TO ROUTINE
- **$A804**: MUST BE <VAR> = <EXP>

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*