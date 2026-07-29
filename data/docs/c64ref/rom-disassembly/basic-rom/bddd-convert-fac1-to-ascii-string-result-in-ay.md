---
title: convert FAC1 to ASCII string result in (AY)
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
- bddd-wandeln-und-nach-100
- bde7-str-function-enters-here-with-y0
- be0b-adjust-until-1e8-fac-1e9
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BDDD
  address_end: $BF10
  symbol: convert-fac1-to-ascii-string-result-in-ay
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BDDD**: set index = 1'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BDDD**: Stringzeiger'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BDE5**: minus'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BDDD**: NORMAL ENTRY PUTS STRING AT STACK...'
---

# $BDDD — convert FAC1 to ASCII string result in (AY)

## Disassemblatura
```assembly
.BDDD  A0 01    LDY #$01   ; set index = 1
.BDDF  A9 20    LDA #$20   ; character = " " (assume +ve)
.BDE1  24 66    BIT $66   ; test FAC1 sign (b7)
.BDE3  10 02    BPL $BDE7   ; branch if +ve
.BDE5  A9 2D    LDA #$2D   ; else character = "-"
.BDE7  99 FF 00 STA $00FF,Y   ; save leading character (" " or "-")
.BDEA  85 66    STA $66   ; save FAC1 sign (b7)
.BDEC  84 71    STY $71   ; save index
.BDEE  C8       INY   ; increment index
.BDEF  A9 30    LDA #$30   ; set character = "0"
.BDF1  A6 61    LDX $61   ; get FAC1 exponent
.BDF3  D0 03    BNE $BDF8   ; branch if FAC1<>0 exponent was $00 so FAC1 is 0
.BDF5  4C 04 BF JMP $BF04   ; save last character, [EOT] and exit FAC1 is some non zero value
.BDF8  A9 00    LDA #$00   ; clear (number exponent count)
.BDFA  E0 80    CPX #$80   ; compare FAC1 exponent with $80 (<1.00000)
.BDFC  F0 02    BEQ $BE00   ; branch if 0.5 <= FAC1 < 1.0
.BDFE  B0 09    BCS $BE09   ; branch if FAC1=>1
.BE00  A9 BD    LDA #$BD   ; set 1000000000 pointer low byte
.BE02  A0 BD    LDY #$BD   ; set 1000000000 pointer high byte
.BE04  20 28 BA JSR $BA28   ; do convert AY, FCA1*(AY)
.BE07  A9 F7    LDA #$F7   ; set number exponent count
.BE09  85 5D    STA $5D   ; save number exponent count
.BE0B  A9 B8    LDA #$B8   ; set 999999999.25 pointer low byte (max before sci note)
.BE0D  A0 BD    LDY #$BD   ; set 999999999.25 pointer high byte
.BE0F  20 5B BC JSR $BC5B   ; compare FAC1 with (AY)
.BE12  F0 1E    BEQ $BE32   ; exit if FAC1 = (AY)
.BE14  10 12    BPL $BE28   ; go do /10 if FAC1 > (AY) FAC1 < (AY)
.BE16  A9 B3    LDA #$B3   ; set 99999999.90625 pointer low byte
.BE18  A0 BD    LDY #$BD   ; set 99999999.90625 pointer high byte
.BE1A  20 5B BC JSR $BC5B   ; compare FAC1 with (AY)
.BE1D  F0 02    BEQ $BE21   ; branch if FAC1 = (AY) (allow decimal places)
.BE1F  10 0E    BPL $BE2F   ; branch if FAC1 > (AY) (no decimal places) FAC1 <= (AY)
.BE21  20 E2 BA JSR $BAE2   ; multiply FAC1 by 10
.BE24  C6 5D    DEC $5D   ; decrement number exponent count
.BE26  D0 EE    BNE $BE16   ; go test again, branch always
.BE28  20 FE BA JSR $BAFE   ; divide FAC1 by 10
.BE2B  E6 5D    INC $5D   ; increment number exponent count
.BE2D  D0 DC    BNE $BE0B   ; go test again, branch always now we have just the digits to do
.BE2F  20 49 B8 JSR $B849   ; add 0.5 to FAC1 (round FAC1)
.BE32  20 9B BC JSR $BC9B   ; convert FAC1 floating to fixed
.BE35  A2 01    LDX #$01   ; set default digits before dp = 1
.BE37  A5 5D    LDA $5D   ; get number exponent count
.BE39  18       CLC   ; clear carry for add
.BE3A  69 0A    ADC #$0A   ; up to 9 digits before point
.BE3C  30 09    BMI $BE47   ; if -ve then 1 digit before dp
.BE3E  C9 0B    CMP #$0B   ; A>=$0B if n>=1E9
.BE40  B0 06    BCS $BE48   ; branch if >= $0B carry is clear
.BE42  69 FF    ADC #$FF   ; take 1 from digit count
.BE44  AA       TAX   ; copy to X
.BE45  A9 02    LDA #$02   ; set exponent adjust
.BE47  38       SEC   ; set carry for subtract
.BE48  E9 02    SBC #$02   ; -2
.BE4A  85 5E    STA $5E   ; save exponent adjust
.BE4C  86 5D    STX $5D   ; save digits before dp count
.BE4E  8A       TXA   ; copy to A
.BE4F  F0 02    BEQ $BE53   ; branch if no digits before dp
.BE51  10 13    BPL $BE66   ; branch if digits before dp
.BE53  A4 71    LDY $71   ; get output string index
.BE55  A9 2E    LDA #$2E   ; character "."
.BE57  C8       INY   ; increment index
.BE58  99 FF 00 STA $00FF,Y   ; save to output string
.BE5B  8A       TXA
.BE5C  F0 06    BEQ $BE64
.BE5E  A9 30    LDA #$30   ; character "0"
.BE60  C8       INY   ; increment index
.BE61  99 FF 00 STA $00FF,Y   ; save to output string
.BE64  84 71    STY $71   ; save output string index
.BE66  A0 00    LDY #$00   ; clear index (point to 100,000)
.BE68  A2 80    LDX #$80
.BE6A  A5 65    LDA $65   ; get FAC1 mantissa 4
.BE6C  18       CLC   ; clear carry for add
.BE6D  79 19 BF ADC $BF19,Y   ; add byte 4, least significant
.BE70  85 65    STA $65   ; save FAC1 mantissa4
.BE72  A5 64    LDA $64   ; get FAC1 mantissa 3
.BE74  79 18 BF ADC $BF18,Y   ; add byte 3
.BE77  85 64    STA $64   ; save FAC1 mantissa3
.BE79  A5 63    LDA $63   ; get FAC1 mantissa 2
.BE7B  79 17 BF ADC $BF17,Y   ; add byte 2
.BE7E  85 63    STA $63   ; save FAC1 mantissa2
.BE80  A5 62    LDA $62   ; get FAC1 mantissa 1
.BE82  79 16 BF ADC $BF16,Y   ; add byte 1, most significant
.BE85  85 62    STA $62   ; save FAC1 mantissa1
.BE87  E8       INX   ; increment the digit, set the sign on the test sense bit
.BE88  B0 04    BCS $BE8E   ; if the carry is set go test if the result was positive else the result needs to be negative
.BE8A  10 DE    BPL $BE6A   ; not -ve so try again
.BE8C  30 02    BMI $BE90   ; else done so return the digit
.BE8E  30 DA    BMI $BE6A   ; not +ve so try again else done so return the digit
.BE90  8A       TXA   ; copy the digit
.BE91  90 04    BCC $BE97   ; if Cb=0 just use it
.BE93  49 FF    EOR #$FF   ; else make the 2's complement ..
.BE95  69 0A    ADC #$0A   ; .. and subtract it from 10
.BE97  69 2F    ADC #$2F   ; add "0"-1 to result
.BE99  C8       INY   ; increment ..
.BE9A  C8       INY   ; .. index to..
.BE9B  C8       INY   ; .. next less ..
.BE9C  C8       INY   ; .. power of ten
.BE9D  84 47    STY $47   ; save current variable pointer low byte
.BE9F  A4 71    LDY $71   ; get output string index
.BEA1  C8       INY   ; increment output string index
.BEA2  AA       TAX   ; copy character to X
.BEA3  29 7F    AND #$7F   ; mask out top bit
.BEA5  99 FF 00 STA $00FF,Y   ; save to output string
.BEA8  C6 5D    DEC $5D   ; decrement # of characters before the dp
.BEAA  D0 06    BNE $BEB2   ; branch if still characters to do else output the point
.BEAC  A9 2E    LDA #$2E   ; character "."
.BEAE  C8       INY   ; increment output string index
.BEAF  99 FF 00 STA $00FF,Y   ; save to output string
.BEB2  84 71    STY $71   ; save output string index
.BEB4  A4 47    LDY $47   ; get current variable pointer low byte
.BEB6  8A       TXA   ; get character back
.BEB7  49 FF    EOR #$FF   ; toggle the test sense bit
.BEB9  29 80    AND #$80   ; clear the digit
.BEBB  AA       TAX   ; copy it to the new digit
.BEBC  C0 24    CPY #$24   ; compare the table index with the max for decimal numbers
.BEBE  F0 04    BEQ $BEC4   ; if at the max exit the digit loop
.BEC0  C0 3C    CPY #$3C   ; compare the table index with the max for time
.BEC2  D0 A6    BNE $BE6A   ; loop if not at the max now remove trailing zeroes
.BEC4  A4 71    LDY $71   ; restore the output string index
.BEC6  B9 FF 00 LDA $00FF,Y   ; get character from output string
.BEC9  88       DEY   ; decrement output string index
.BECA  C9 30    CMP #$30   ; compare with "0"
.BECC  F0 F8    BEQ $BEC6   ; loop until non "0" character found
.BECE  C9 2E    CMP #$2E   ; compare with "."
.BED0  F0 01    BEQ $BED3   ; branch if was dp restore last character
.BED2  C8       INY   ; increment output string index
.BED3  A9 2B    LDA #$2B   ; character "+"
.BED5  A6 5E    LDX $5E   ; get exponent count
.BED7  F0 2E    BEQ $BF07   ; if zero go set null terminator and exit exponent isn't zero so write exponent
.BED9  10 08    BPL $BEE3   ; branch if exponent count +ve
.BEDB  A9 00    LDA #$00   ; clear A
.BEDD  38       SEC   ; set carry for subtract
.BEDE  E5 5E    SBC $5E   ; subtract exponent count adjust (convert -ve to +ve)
.BEE0  AA       TAX   ; copy exponent count to X
.BEE1  A9 2D    LDA #$2D   ; character "-"
.BEE3  99 01 01 STA $0101,Y   ; save to output string
.BEE6  A9 45    LDA #$45   ; character "E"
.BEE8  99 00 01 STA $0100,Y   ; save exponent sign to output string
.BEEB  8A       TXA   ; get exponent count back
.BEEC  A2 2F    LDX #$2F   ; one less than "0" character
.BEEE  38       SEC   ; set carry for subtract
.BEEF  E8       INX   ; increment 10's character
.BEF0  E9 0A    SBC #$0A   ; subtract 10 from exponent count
.BEF2  B0 FB    BCS $BEEF   ; loop while still >= 0
.BEF4  69 3A    ADC #$3A   ; add character ":" ($30+$0A, result is 10 less that value)
.BEF6  99 03 01 STA $0103,Y   ; save to output string
.BEF9  8A       TXA   ; copy 10's character
.BEFA  99 02 01 STA $0102,Y   ; save to output string
.BEFD  A9 00    LDA #$00   ; set null terminator
.BEFF  99 04 01 STA $0104,Y   ; save to output string
.BF02  F0 08    BEQ $BF0C   ; go set string pointer (AY) and exit, branch always save last character, [EOT] and exit
.BF04  99 FF 00 STA $00FF,Y   ; save last character to output string set null terminator and exit
.BF07  A9 00    LDA #$00   ; set null terminator
.BF09  99 00 01 STA $0100,Y   ; save after last character set string pointer (AY) and exit
.BF0C  A9 00    LDA #$00   ; set result string pointer low byte
.BF0E  A0 01    LDY #$01   ; set result string pointer high byte
.BF10  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BDDD**: set index = 1
- **$BDDF**: character = " " (assume +ve)
- **$BDE1**: test FAC1 sign (b7)
- **$BDE3**: branch if +ve
- **$BDE5**: else character = "-"
- **$BDE7**: save leading character (" " or "-")
- **$BDEA**: save FAC1 sign (b7)
- **$BDEC**: save index
- **$BDEE**: increment index
- **$BDEF**: set character = "0"
- **$BDF1**: get FAC1 exponent
- **$BDF3**: branch if FAC1<>0 exponent was $00 so FAC1 is 0
- **$BDF5**: save last character, [EOT] and exit FAC1 is some non zero value
- **$BDF8**: clear (number exponent count)
- **$BDFA**: compare FAC1 exponent with $80 (<1.00000)
- **$BDFC**: branch if 0.5 <= FAC1 < 1.0
- **$BDFE**: branch if FAC1=>1
- **$BE00**: set 1000000000 pointer low byte
- **$BE02**: set 1000000000 pointer high byte
- **$BE04**: do convert AY, FCA1*(AY)
- **$BE07**: set number exponent count
- **$BE09**: save number exponent count
- **$BE0B**: set 999999999.25 pointer low byte (max before sci note)
- **$BE0D**: set 999999999.25 pointer high byte
- **$BE0F**: compare FAC1 with (AY)
- **$BE12**: exit if FAC1 = (AY)
- **$BE14**: go do /10 if FAC1 > (AY) FAC1 < (AY)
- **$BE16**: set 99999999.90625 pointer low byte
- **$BE18**: set 99999999.90625 pointer high byte
- **$BE1A**: compare FAC1 with (AY)
- **$BE1D**: branch if FAC1 = (AY) (allow decimal places)
- **$BE1F**: branch if FAC1 > (AY) (no decimal places) FAC1 <= (AY)
- **$BE21**: multiply FAC1 by 10
- **$BE24**: decrement number exponent count
- **$BE26**: go test again, branch always
- **$BE28**: divide FAC1 by 10
- **$BE2B**: increment number exponent count
- **$BE2D**: go test again, branch always now we have just the digits to do
- **$BE2F**: add 0.5 to FAC1 (round FAC1)
- **$BE32**: convert FAC1 floating to fixed
- **$BE35**: set default digits before dp = 1
- **$BE37**: get number exponent count
- **$BE39**: clear carry for add
- **$BE3A**: up to 9 digits before point
- **$BE3C**: if -ve then 1 digit before dp
- **$BE3E**: A>=$0B if n>=1E9
- **$BE40**: branch if >= $0B carry is clear
- **$BE42**: take 1 from digit count
- **$BE44**: copy to X
- **$BE45**: set exponent adjust
- **$BE47**: set carry for subtract
- **$BE48**: -2
- **$BE4A**: save exponent adjust
- **$BE4C**: save digits before dp count
- **$BE4E**: copy to A
- **$BE4F**: branch if no digits before dp
- **$BE51**: branch if digits before dp
- **$BE53**: get output string index
- **$BE55**: character "."
- **$BE57**: increment index
- **$BE58**: save to output string
- **$BE5E**: character "0"
- **$BE60**: increment index
- **$BE61**: save to output string
- **$BE64**: save output string index
- **$BE66**: clear index (point to 100,000)
- **$BE6A**: get FAC1 mantissa 4
- **$BE6C**: clear carry for add
- **$BE6D**: add byte 4, least significant
- **$BE70**: save FAC1 mantissa4
- **$BE72**: get FAC1 mantissa 3
- **$BE74**: add byte 3
- **$BE77**: save FAC1 mantissa3
- **$BE79**: get FAC1 mantissa 2
- **$BE7B**: add byte 2
- **$BE7E**: save FAC1 mantissa2
- **$BE80**: get FAC1 mantissa 1
- **$BE82**: add byte 1, most significant
- **$BE85**: save FAC1 mantissa1
- **$BE87**: increment the digit, set the sign on the test sense bit
- **$BE88**: if the carry is set go test if the result was positive else the result needs to be negative
- **$BE8A**: not -ve so try again
- **$BE8C**: else done so return the digit
- **$BE8E**: not +ve so try again else done so return the digit
- **$BE90**: copy the digit
- **$BE91**: if Cb=0 just use it
- **$BE93**: else make the 2's complement ..
- **$BE95**: .. and subtract it from 10
- **$BE97**: add "0"-1 to result
- **$BE99**: increment ..
- **$BE9A**: .. index to..
- **$BE9B**: .. next less ..
- **$BE9C**: .. power of ten
- **$BE9D**: save current variable pointer low byte
- **$BE9F**: get output string index
- **$BEA1**: increment output string index
- **$BEA2**: copy character to X
- **$BEA3**: mask out top bit
- **$BEA5**: save to output string
- **$BEA8**: decrement # of characters before the dp
- **$BEAA**: branch if still characters to do else output the point
- **$BEAC**: character "."
- **$BEAE**: increment output string index
- **$BEAF**: save to output string
- **$BEB2**: save output string index
- **$BEB4**: get current variable pointer low byte
- **$BEB6**: get character back
- **$BEB7**: toggle the test sense bit
- **$BEB9**: clear the digit
- **$BEBB**: copy it to the new digit
- **$BEBC**: compare the table index with the max for decimal numbers
- **$BEBE**: if at the max exit the digit loop
- **$BEC0**: compare the table index with the max for time
- **$BEC2**: loop if not at the max now remove trailing zeroes
- **$BEC4**: restore the output string index
- **$BEC6**: get character from output string
- **$BEC9**: decrement output string index
- **$BECA**: compare with "0"
- **$BECC**: loop until non "0" character found
- **$BECE**: compare with "."
- **$BED0**: branch if was dp restore last character
- **$BED2**: increment output string index
- **$BED3**: character "+"
- **$BED5**: get exponent count
- **$BED7**: if zero go set null terminator and exit exponent isn't zero so write exponent
- **$BED9**: branch if exponent count +ve
- **$BEDB**: clear A
- **$BEDD**: set carry for subtract
- **$BEDE**: subtract exponent count adjust (convert -ve to +ve)
- **$BEE0**: copy exponent count to X
- **$BEE1**: character "-"
- **$BEE3**: save to output string
- **$BEE6**: character "E"
- **$BEE8**: save exponent sign to output string
- **$BEEB**: get exponent count back
- **$BEEC**: one less than "0" character
- **$BEEE**: set carry for subtract
- **$BEEF**: increment 10's character
- **$BEF0**: subtract 10 from exponent count
- **$BEF2**: loop while still >= 0
- **$BEF4**: add character ":" ($30+$0A, result is 10 less that value)
- **$BEF6**: save to output string
- **$BEF9**: copy 10's character
- **$BEFA**: save to output string
- **$BEFD**: set null terminator
- **$BEFF**: save to output string
- **$BF02**: go set string pointer (AY) and exit, branch always save last character, [EOT] and exit
- **$BF04**: save last character to output string set null terminator and exit
- **$BF07**: set null terminator
- **$BF09**: save after last character set string pointer (AY) and exit
- **$BF0C**: set result string pointer low byte
- **$BF0E**: set result string pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$BDDD**: Stringzeiger
- **$BDDF**: ' ' Leerzeichen für positive Zahl
- **$BDE1**: wenn Vorzeichen
- **$BDE3**: positiv ?, dann zu $BDE7
- **$BDE5**: '-' Minuszeichen für
- **$BDE7**: negative Zahl in
- **$BDEA**: Pufferbereich
- **$BDEC**: schreiben
- **$BDEE**: Zähler erhöhen
- **$BDEF**: '0’
- **$BDF1**: Exponent
- **$BDF3**: wenn Zahl nicht null ?
- **$BDF5**: dann fertig
- **$BDF8**: FAC
- **$BDFA**: mit 1 vergleichen
- **$BDFC**: wenn ja ,dann zu $BE00
- **$BDFE**: FAC größer 1
- **$BE00**: Zeiger auf
- **$BE02**: Konstante 1E9
- **$BE04**: Konstante (Zeiger A/Y) * FAC
- **$BE07**: = -9
- **$BE09**: $ 5D = -9
- **$BE0B**: Zeiger auf
- **$BE0D**: Konstante 999999999
- **$BE0F**: Vergleich Konstante (Zeiger A/Y) mit FAC
- **$BE12**: gleich
- **$BE14**: kleiner
- **$BE16**: Zeiger auf
- **$BE18**: Konstante 99999999.9
- **$BE1A**: Vergleich Konstante (Zeiger A/Y) mit FAC
- **$BE1D**: gleich
- **$BE1F**: kleiner
- **$BE21**: FAC = FAC * 10
- **$BE24**: Dezimalexponent erniedrigen
- **$BE26**: schon 0?
- **$BE28**: FAC = FAC / 10
- **$BE2B**: Dezimalexponent erhöhen
- **$BE2D**: Überlauf ?
- **$BE2F**: FAC = FAC + .5 , runden
- **$BE32**: FAC nach Integer
- **$BE35**: FAC ist nun im Bereich von
- **$BE37**: 1E8 bis 1E9, $5D hat Wert
- **$BE39**: von Zehnerpotenz
- **$BE3A**: Zahl =0.01
- **$BE3C**: Betrag kleiner 0.1 ?
- **$BE3E**: wenn ja, dann
- **$BE40**: Betrag größer 1E9 ?
- **$BE42**: die
- **$BE44**: Be-
- **$BE45**: rechnung
- **$BE47**: des
- **$BE48**: Exponenten-
- **$BE4A**: flags
- **$BE4C**: Negative Darstellung des
- **$BE4E**: Exponenten
- **$BE4F**: wenn 0.1, dann zu $BE53
- **$BE51**: wenn nicht 0.01, dann zu $BE66
- **$BE53**: Zeiger für Polynomauswertung
- **$BE55**: Nummer für '.'
- **$BE57**: Zeiger erhöhen
- **$BE58**: in Stringbereich
- **$BE5B**: schreiben
- **$BE5C**: wenn 0.1, dann zu $BE64
- **$BE5E**: Nummer für '0'
- **$BE60**: Zeiger erhöhen
- **$BE61**: in Stringbereich
- **$BE64**: schreiben
- **$BE66**: Zeiger
- **$BE68**: stellen
- **$BE6A**: Durch
- **$BE6C**: Addition
- **$BE6D**: und
- **$BE70**: Subtraktion
- **$BE72**: der
- **$BE74**: Werte
- **$BE77**: aus
- **$BE79**: der
- **$BE7B**: Tabelle
- **$BE7E**: werden
- **$BE80**: die
- **$BE82**: einzelnen
- **$BE85**: Ziffern
- **$BE87**: des
- **$BE88**: Zahlen-
- **$BE8A**: Strings
- **$BE8C**: be-
- **$BE8E**: rech-
- **$BE90**: net
- **$BE91**: alles addiert?, wenn nicht, dann zu $BE97
- **$BE93**: Ergebnis mit 10
- **$BE95**: komplementieren
- **$BE97**: '0' - 1
- **$BE99**: Zähler
- **$BE9A**: ent-
- **$BE9B**: sprechend
- **$BE9C**: erhöhen
- **$BE9D**: Zähler sichern
- **$BE9F**: Zeiger auf Stringbereich laden
- **$BEA1**: und erhöhen
- **$BEA2**: Ziffer
- **$BEA3**: in
- **$BEA5**: Stringbereich
- **$BEA8**: bringen
- **$BEAA**: wenn Einerstelle nicht erreicht, dann zu $BEB2
- **$BEAC**: Nummer für '.'
- **$BEAE**: Zähler erhöhen
- **$BEAF**: in Stringbereich schreiben
- **$BEB2**: Zähler speichern
- **$BEB4**: Neuen Zähler holen
- **$BEB6**: FAC-
- **$BEB7**: Um-
- **$BEB9**: wand-
- **$BEBB**: lung
- **$BEBC**: Tabellenende ereicht,
- **$BEBE**: dann zu $BEC4
- **$BEC0**: Tabellenende bei TI$-Berechnung
- **$BEC2**: nicht erreicht, dann zu $BE6A
- **$BEC4**: Zähler wieder holen
- **$BEC6**: letzte Stelle suchen
- **$BEC9**: Zähler erniedrigen
- **$BECA**: Nummer für '0'
- **$BECC**: wenn ja, dann zu $BEC6
- **$BECE**: Nummer für '.'
- **$BED0**: wenn ja, dann zu $BED3
- **$BED2**: Zähler erhöhen
- **$BED3**: Nummer für '+'
- **$BED5**: wenn Flag nicht gesetzt,
- **$BED7**: dann zu $BF07
- **$BED9**: wenn Exponent positiv, dann zu $BEE3
- **$BEDB**: Den
- **$BEDD**: Exponenten
- **$BEDE**: be-
- **$BEE0**: rechnen
- **$BEE1**: Nummer für '-'
- **$BEE3**: in Stringbereich schreiben
- **$BEE6**: Nummer für 'E'
- **$BEE8**: in Stringbereich schreiben
- **$BEEB**: Zehner-
- **$BEEC**: stelle
- **$BEEE**: für
- **$BEEF**: den
- **$BEF0**: Exponenten
- **$BEF2**: berechnen
- **$BEF4**: '9' + 1
- **$BEF6**: in Stringbereich schreiben
- **$BEF9**: Zehnerstelle
- **$BEFA**: in Stringbereich schreiben
- **$BEFD**: Puffer mit $0
- **$BEFF**: abschließen
- **$BF02**: unbedingter Sprung
- **$BF04**: Puffer
- **$BF07**: mit $0
- **$BF09**: abschließen
- **$BF0C**: Zeiger auf
- **$BF0E**: Puffer $100
- **$BF10**: Rücksprung
- **$BF11**: Konstante 0.5 für SQR-Funktion

### Marko Mäkelä (Marko Mäkelä)
- **$BDE5**: minus
- **$BDEF**: 0
- **$BE00**: low  BDBD
- **$BE02**: high BDBD
- **$BE0B**: low  BDB8
- **$BE0D**: high BDB8
- **$BE16**: low  BDB3
- **$BE18**: high BDB3
- **$BE55**: decimal point
- **$BE5E**: 0
- **$BECA**: 0
- **$BECE**: decimal point
- **$BED3**: plus
- **$BEE1**: minus
- **$BF0C**: low  0100
- **$BF0E**: high 0100

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BDDD**: NORMAL ENTRY PUTS STRING AT STACK...

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*