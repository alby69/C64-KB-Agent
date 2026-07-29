---
title: perform LET
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
- a9a5-basic-befehl-let
- a9c4-wertzuweisung-integer
- a9d6-wertzuweisung-real
- a9d9-wertzuweisung-string
- a9da-install-string-descriptor-address-is-at-fac34
- a9e0-assign-to-ti
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A9A5
  address_end: $AA1A
  symbol: perform-let
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A9A5**: get variable address'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A9A5**: sucht Variable hinter LET'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A9AC**: equals code'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A9A5**: GET <VAR>'
---

# $A9A5 — perform LET

## Disassemblatura
```assembly
.A9A5  20 8B B0 JSR $B08B   ; get variable address
.A9A8  85 49    STA $49   ; save variable address low byte
.A9AA  84 4A    STY $4A   ; save variable address high byte
.A9AC  A9 B2    LDA #$B2   ; $B2 is "=" token
.A9AE  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.A9B1  A5 0E    LDA $0E   ; get data type flag, $80 = integer, $00 = float
.A9B3  48       PHA   ; push data type flag
.A9B4  A5 0D    LDA $0D   ; get data type flag, $FF = string, $00 = numeric
.A9B6  48       PHA   ; push data type flag
.A9B7  20 9E AD JSR $AD9E   ; evaluate expression
.A9BA  68       PLA   ; pop data type flag
.A9BB  2A       ROL   ; string bit into carry
.A9BC  20 90 AD JSR $AD90   ; do type match check
.A9BF  D0 18    BNE $A9D9   ; branch if string
.A9C1  68       PLA   ; pop integer/float data type flag assign value to numeric variable
.A9C2  10 12    BPL $A9D6   ; branch if float expression is numeric integer
.A9C4  20 1B BC JSR $BC1B   ; round FAC1
.A9C7  20 BF B1 JSR $B1BF   ; evaluate integer expression, no sign check
.A9CA  A0 00    LDY #$00   ; clear index
.A9CC  A5 64    LDA $64   ; get FAC1 mantissa 3
.A9CE  91 49    STA ($49),Y   ; save as integer variable low byte
.A9D0  C8       INY   ; increment index
.A9D1  A5 65    LDA $65   ; get FAC1 mantissa 4
.A9D3  91 49    STA ($49),Y   ; save as integer variable high byte
.A9D5  60       RTS
.A9D6  4C D0 BB JMP $BBD0   ; pack FAC1 into variable pointer and return assign value to numeric variable
.A9D9  68       PLA   ; dump integer/float data type flag
.A9DA  A4 4A    LDY $4A   ; get variable pointer high byte
.A9DC  C0 BF    CPY #$BF   ; was it TI$ pointer
.A9DE  D0 4C    BNE $AA2C   ; branch if not else it's TI$ = <expr$>
.A9E0  20 A6 B6 JSR $B6A6   ; pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.A9E3  C9 06    CMP #$06   ; compare length with 6
.A9E5  D0 3D    BNE $AA24   ; if length not 6 do illegal quantity error then warm start
.A9E7  A0 00    LDY #$00   ; clear index
.A9E9  84 61    STY $61   ; clear FAC1 exponent
.A9EB  84 66    STY $66   ; clear FAC1 sign (b7)
.A9ED  84 71    STY $71   ; save index
.A9EF  20 1D AA JSR $AA1D   ; check and evaluate numeric digit
.A9F2  20 E2 BA JSR $BAE2   ; multiply FAC1 by 10
.A9F5  E6 71    INC $71   ; increment index
.A9F7  A4 71    LDY $71   ; restore index
.A9F9  20 1D AA JSR $AA1D   ; check and evaluate numeric digit
.A9FC  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.A9FF  AA       TAX   ; copy FAC1 exponent
.AA00  F0 05    BEQ $AA07   ; branch if FAC1 zero
.AA02  E8       INX   ; increment index, * 2
.AA03  8A       TXA   ; copy back to A
.AA04  20 ED BA JSR $BAED   ; FAC1 = (FAC1 + (FAC2 * 2)) * 2 = FAC1 * 6
.AA07  A4 71    LDY $71   ; get index
.AA09  C8       INY   ; increment index
.AA0A  C0 06    CPY #$06   ; compare index with 6
.AA0C  D0 DF    BNE $A9ED   ; loop if not 6
.AA0E  20 E2 BA JSR $BAE2   ; multiply FAC1 by 10
.AA11  20 9B BC JSR $BC9B   ; convert FAC1 floating to fixed
.AA14  A6 64    LDX $64   ; get FAC1 mantissa 3
.AA16  A4 63    LDY $63   ; get FAC1 mantissa 2
.AA18  A5 65    LDA $65   ; get FAC1 mantissa 4
.AA1A  4C DB FF JMP $FFDB   ; set real time clock and return
```


## Commenti

### Original Disassembly (—)
- **$A9A5**: get variable address
- **$A9A8**: save variable address low byte
- **$A9AA**: save variable address high byte
- **$A9AC**: $B2 is "=" token
- **$A9AE**: scan for CHR$(A), else do syntax error then warm start
- **$A9B1**: get data type flag, $80 = integer, $00 = float
- **$A9B3**: push data type flag
- **$A9B4**: get data type flag, $FF = string, $00 = numeric
- **$A9B6**: push data type flag
- **$A9B7**: evaluate expression
- **$A9BA**: pop data type flag
- **$A9BB**: string bit into carry
- **$A9BC**: do type match check
- **$A9BF**: branch if string
- **$A9C1**: pop integer/float data type flag assign value to numeric variable
- **$A9C2**: branch if float expression is numeric integer
- **$A9C4**: round FAC1
- **$A9C7**: evaluate integer expression, no sign check
- **$A9CA**: clear index
- **$A9CC**: get FAC1 mantissa 3
- **$A9CE**: save as integer variable low byte
- **$A9D0**: increment index
- **$A9D1**: get FAC1 mantissa 4
- **$A9D3**: save as integer variable high byte
- **$A9D6**: pack FAC1 into variable pointer and return assign value to numeric variable
- **$A9D9**: dump integer/float data type flag
- **$A9DA**: get variable pointer high byte
- **$A9DC**: was it TI$ pointer
- **$A9DE**: branch if not else it's TI$ = <expr$>
- **$A9E0**: pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$A9E3**: compare length with 6
- **$A9E5**: if length not 6 do illegal quantity error then warm start
- **$A9E7**: clear index
- **$A9E9**: clear FAC1 exponent
- **$A9EB**: clear FAC1 sign (b7)
- **$A9ED**: save index
- **$A9EF**: check and evaluate numeric digit
- **$A9F2**: multiply FAC1 by 10
- **$A9F5**: increment index
- **$A9F7**: restore index
- **$A9F9**: check and evaluate numeric digit
- **$A9FC**: round and copy FAC1 to FAC2
- **$A9FF**: copy FAC1 exponent
- **$AA00**: branch if FAC1 zero
- **$AA02**: increment index, * 2
- **$AA03**: copy back to A
- **$AA04**: FAC1 = (FAC1 + (FAC2 * 2)) * 2 = FAC1 * 6
- **$AA07**: get index
- **$AA09**: increment index
- **$AA0A**: compare index with 6
- **$AA0C**: loop if not 6
- **$AA0E**: multiply FAC1 by 10
- **$AA11**: convert FAC1 floating to fixed
- **$AA14**: get FAC1 mantissa 3
- **$AA16**: get FAC1 mantissa 2
- **$AA18**: get FAC1 mantissa 4
- **$AA1A**: set real time clock and return

### Commodore-64-intern-Buch (Commodore)
- **$A9A5**: sucht Variable hinter LET
- **$A9A8**: und Variablenadresse
- **$A9AA**: merken (LOW- und HIGH-Byte)
- **$A9AC**: '=' - Code
- **$A9AE**: prüft auf Code
- **$A9B1**: Integer-Flag
- **$A9B3**: auf Stapel retten
- **$A9B4**: und Typ-Flag
- **$A9B6**: (String/numerisch) retten
- **$A9B7**: FRMEVL: Ausdruck holen
- **$A9BA**: Typ-Flag wiederholen
- **$A9BB**: und Bit 7 ins Carry schieben
- **$A9BC**: auf richtigen Typ prüfen
- **$A9BF**: String? ja: $A9D9
- **$A9C1**: Integer-Flag zurückholen
- **$A9C2**: INTEGER? ja: $A9D6

### Marko Mäkelä (Marko Mäkelä)
- **$A9AC**: equals code

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A9A5**: GET <VAR>
- **$A9B1**: SAVE VARIABLE TYPE
- **$A9B7**: EVALUATE <EXP>
- **$A9C2**: REAL VARIABLE
- **$A9C4**: INTEGER VAR: ROUND TO 32 BITS
- **$A9C7**: TRUNCATE TO 16-BITS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*