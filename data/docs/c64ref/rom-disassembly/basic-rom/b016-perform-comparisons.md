---
title: perform comparisons
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
- b016-vergleich
- b02e-stringvergleich
- b07e-dim-statement
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B016
  address_end: $B07E
  symbol: perform-comparisons
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B016**: type match check, set C for string'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B016**: prüft auf identischen Typ'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B016**: MAKE SURE FAC IS CORRECT TYPE'
---

# $B016 — perform comparisons

## Disassemblatura
```assembly
.B016  20 90 AD JSR $AD90   ; type match check, set C for string
.B019  B0 13    BCS $B02E   ; branch if string do numeric < compare
.B01B  A5 6E    LDA $6E   ; get FAC2 sign (b7)
.B01D  09 7F    ORA #$7F   ; set all non sign bits
.B01F  25 6A    AND $6A   ; and FAC2 mantissa 1 (AND in sign bit)
.B021  85 6A    STA $6A   ; save FAC2 mantissa 1
.B023  A9 69    LDA #$69   ; set pointer low byte to FAC2
.B025  A0 00    LDY #$00   ; set pointer high byte to FAC2
.B027  20 5B BC JSR $BC5B   ; compare FAC1 with (AY)
.B02A  AA       TAX   ; copy the result
.B02B  4C 61 B0 JMP $B061   ; go evaluate result do string < compare
.B02E  A9 00    LDA #$00   ; clear byte
.B030  85 0D    STA $0D   ; clear data type flag, $FF = string, $00 = numeric
.B032  C6 4D    DEC $4D   ; clear < bit in comparison evaluation flag
.B034  20 A6 B6 JSR $B6A6   ; pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.B037  85 61    STA $61   ; save length
.B039  86 62    STX $62   ; save string pointer low byte
.B03B  84 63    STY $63   ; save string pointer high byte
.B03D  A5 6C    LDA $6C   ; get descriptor pointer low byte
.B03F  A4 6D    LDY $6D   ; get descriptor pointer high byte
.B041  20 AA B6 JSR $B6AA   ; pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.B044  86 6C    STX $6C   ; save string pointer low byte
.B046  84 6D    STY $6D   ; save string pointer high byte
.B048  AA       TAX   ; copy length
.B049  38       SEC   ; set carry for subtract
.B04A  E5 61    SBC $61   ; subtract string 1 length
.B04C  F0 08    BEQ $B056   ; branch if str 1 length = string 2 length
.B04E  A9 01    LDA #$01   ; set str 1 length > string 2 length
.B050  90 04    BCC $B056   ; branch if so
.B052  A6 61    LDX $61   ; get string 1 length
.B054  A9 FF    LDA #$FF   ; set str 1 length < string 2 length
.B056  85 66    STA $66   ; save length compare
.B058  A0 FF    LDY #$FF   ; set index
.B05A  E8       INX   ; adjust for loop
.B05B  C8       INY   ; increment index
.B05C  CA       DEX   ; decrement count
.B05D  D0 07    BNE $B066   ; branch if still bytes to do
.B05F  A6 66    LDX $66   ; get length compare back
.B061  30 0F    BMI $B072   ; branch if str 1 < str 2
.B063  18       CLC   ; flag str 1 <= str 2
.B064  90 0C    BCC $B072   ; go evaluate result
.B066  B1 6C    LDA ($6C),Y   ; get string 2 byte
.B068  D1 62    CMP ($62),Y   ; compare with string 1 byte
.B06A  F0 EF    BEQ $B05B   ; loop if bytes =
.B06C  A2 FF    LDX #$FF   ; set str 1 < string 2
.B06E  B0 02    BCS $B072   ; branch if so
.B070  A2 01    LDX #$01   ; set str 1 > string 2
.B072  E8       INX   ; x = 0, 1 or 2
.B073  8A       TXA   ; copy to A
.B074  2A       ROL   ; * 2 (1, 2 or 4)
.B075  25 12    AND $12   ; AND with the comparison evaluation flag
.B077  F0 02    BEQ $B07B   ; branch if 0 (compare is false)
.B079  A9 FF    LDA #$FF   ; else set result true
.B07B  4C 3C BC JMP $BC3C   ; save A as integer byte and return
.B07E  20 FD AE JSR $AEFD   ; scan for ",", else do syntax error then warm start
```


## Commenti

### Original Disassembly (—)
- **$B016**: type match check, set C for string
- **$B019**: branch if string do numeric < compare
- **$B01B**: get FAC2 sign (b7)
- **$B01D**: set all non sign bits
- **$B01F**: and FAC2 mantissa 1 (AND in sign bit)
- **$B021**: save FAC2 mantissa 1
- **$B023**: set pointer low byte to FAC2
- **$B025**: set pointer high byte to FAC2
- **$B027**: compare FAC1 with (AY)
- **$B02A**: copy the result
- **$B02B**: go evaluate result do string < compare
- **$B02E**: clear byte
- **$B030**: clear data type flag, $FF = string, $00 = numeric
- **$B032**: clear < bit in comparison evaluation flag
- **$B034**: pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$B037**: save length
- **$B039**: save string pointer low byte
- **$B03B**: save string pointer high byte
- **$B03D**: get descriptor pointer low byte
- **$B03F**: get descriptor pointer high byte
- **$B041**: pop (YA) descriptor off stack or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$B044**: save string pointer low byte
- **$B046**: save string pointer high byte
- **$B048**: copy length
- **$B049**: set carry for subtract
- **$B04A**: subtract string 1 length
- **$B04C**: branch if str 1 length = string 2 length
- **$B04E**: set str 1 length > string 2 length
- **$B050**: branch if so
- **$B052**: get string 1 length
- **$B054**: set str 1 length < string 2 length
- **$B056**: save length compare
- **$B058**: set index
- **$B05A**: adjust for loop
- **$B05B**: increment index
- **$B05C**: decrement count
- **$B05D**: branch if still bytes to do
- **$B05F**: get length compare back
- **$B061**: branch if str 1 < str 2
- **$B063**: flag str 1 <= str 2
- **$B064**: go evaluate result
- **$B066**: get string 2 byte
- **$B068**: compare with string 1 byte
- **$B06A**: loop if bytes =
- **$B06C**: set str 1 < string 2
- **$B06E**: branch if so
- **$B070**: set str 1 > string 2
- **$B072**: x = 0, 1 or 2
- **$B073**: copy to A
- **$B074**: * 2 (1, 2 or 4)
- **$B075**: AND with the comparison evaluation flag
- **$B077**: branch if 0 (compare is false)
- **$B079**: else set result true
- **$B07B**: save A as integer byte and return
- **$B07E**: scan for ",", else do syntax error then warm start

### Commodore-64-intern-Buch (Commodore)
- **$B016**: prüft auf identischen Typ
- **$B019**: String: dann weiter
- **$B01B**: Wert holen
- **$B01D**: ARG in Speicherformat
- **$B01F**: wandeln und
- **$B021**: wieder abspeichern
- **$B023**: Adresse von ARG
- **$B025**: (LOW- und HIGH-Byte)
- **$B027**: Vergleich ARG mit FAC
- **$B02B**: Ergebnis in FAC holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B016**: MAKE SURE FAC IS CORRECT TYPE
- **$B019**: TYPE MATCHES, BRANCH IF STRINGS
- **$B01B**: NUMERIC COMPARISON
- **$B01D**: RE-PACK VALUE IN ARG FOR FCOMP
- **$B027**: RETURN A-REG = -1,0,1
- **$B02A**: AS ARG <,=,> FAC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*