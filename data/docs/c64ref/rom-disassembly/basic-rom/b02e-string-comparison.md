---
title: STRING COMPARISON
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
- 0069-arg
- aa2c-string
- b02e-stringvergleich
- bc5b-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - commodore-64-intern-buch.txt
  address: $B02E
  address_end: $B07B
  symbol: string-comparison
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B02E**: Wert laden und damit'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B02E**: SET RESULT TYPE TO NUMERIC'
---

# $B02E — STRING COMPARISON

## Disassemblatura
```assembly
.B02E  A9 00    LDA #$00   ; SET RESULT TYPE TO NUMERIC
.B030  85 0D    STA $0D
.B032  C6 4D    DEC $4D   ; MAKE CPRTYP 0000<=>0
.B034  20 A6 B6 JSR $B6A6
.B037  85 61    STA $61   ; STRING LENGTH
.B039  86 62    STX $62
.B03B  84 63    STY $63
.B03D  A5 6C    LDA $6C
.B03F  A4 6D    LDY $6D
.B041  20 AA B6 JSR $B6AA
.B044  86 6C    STX $6C
.B046  84 6D    STY $6D
.B048  AA       TAX   ; LEN (ARG) STRING
.B049  38       SEC
.B04A  E5 61    SBC $61   ; SET X TO SMALLER LEN
.B04C  F0 08    BEQ $B056
.B04E  A9 01    LDA #$01
.B050  90 04    BCC $B056
.B052  A6 61    LDX $61
.B054  A9 FF    LDA #$FF
.B056  85 66    STA $66   ; FLAG WHICH SHORTER
.B058  A0 FF    LDY #$FF
.B05A  E8       INX
.B05B  C8       INY
.B05C  CA       DEX
.B05D  D0 07    BNE $B066   ; MORE CHARS IN BOTH STRINGS
.B05F  A6 66    LDX $66   ; IF = SO FAR, DECIDE BY LENGTH
.B061  30 0F    BMI $B072
.B063  18       CLC
.B064  90 0C    BCC $B072   ; ...ALWAYS
.B066  B1 6C    LDA ($6C),Y
.B068  D1 62    CMP ($62),Y
.B06A  F0 EF    BEQ $B05B   ; SAME, KEEP COMPARING
.B06C  A2 FF    LDX #$FF   ; IN CASE ARG GREATER
.B06E  B0 02    BCS $B072   ; IT IS
.B070  A2 01    LDX #$01   ; FAC GREATER
.B072  E8       INX   ; CONVERT FF,0,1 TO 0,1,2
.B073  8A       TXA
.B074  2A       ROL   ; AND TO 0,2,4 IF C=0, ELSE 1,2,5
.B075  25 12    AND $12   ; 00000<=>
.B077  F0 02    BEQ $B07B   ; IF NO MATCH: FALSE
.B079  A9 FF    LDA #$FF   ; AT LEAST ONE MATCH: TRUE
.B07B  4C 3C BC JMP $BC3C
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B02E**: Wert laden und damit
- **$B030**: Stringflag löschen
- **$B032**: Operatormaske - 1
- **$B034**: FRLSTR
- **$B037**: Stringlänge holen
- **$B039**: LOW- und HIGH-Byte der
- **$B03B**: Stringadresse speichern
- **$B03D**: LOW- und HIGH-Byte des
- **$B03F**: Zeigers auf zweiten String
- **$B041**: FRESTR
- **$B044**: Adresse des
- **$B046**: 2. Strings
- **$B048**: Länge des 2.Strings merken
- **$B049**: Carry setzen (Subtraktion)
- **$B04A**: Längen vergleichen
- **$B04C**: gleich: $B056
- **$B04E**: Wert für: 1.String länger
- **$B050**: 2.String kürzer
- **$B052**: Länge des 1.Strings
- **$B054**: Wert für: 1.String kürzer
- **$B056**: Flag für gleichen String,
- **$B058**: wenn beide Strings identisch aber
- **$B05A**: ungleich lang sind
- **$B05B**: Zeiger erhöhen
- **$B05C**: Stringende?
- **$B05D**: nein: weiter
- **$B05F**: Vorzeichenbyte holen
- **$B061**: negativ: $B072
- **$B063**: Carry löschen
- **$B064**: unbedingter Sprung
- **$B066**: Vergleich der Strings
- **$B068**: zeichenweise
- **$B06A**: gleiche Zeichen: weiter
- **$B06C**: Wert laden
- **$B06E**: und Vergleich beenden
- **$B070**: Wert laden
- **$B072**: und um 1 erhöhen
- **$B073**: Wert in den Akku
- **$B074**: linksverschieben, Bit 1, 2=$1
- **$B075**: mit Vorzeichen verknüpfen
- **$B077**: =0: $B07B
- **$B07B**: Ergebnis nach FAC holen
- **$B07E**: CHKCOM prüft auf Komma

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B02E**: SET RESULT TYPE TO NUMERIC
- **$B032**: MAKE CPRTYP 0000<=>0
- **$B037**: STRING LENGTH
- **$B048**: LEN (ARG) STRING
- **$B04A**: SET X TO SMALLER LEN
- **$B056**: FLAG WHICH SHORTER
- **$B05D**: MORE CHARS IN BOTH STRINGS
- **$B05F**: IF = SO FAR, DECIDE BY LENGTH
- **$B064**: ...ALWAYS
- **$B06A**: SAME, KEEP COMPARING
- **$B06C**: IN CASE ARG GREATER
- **$B06E**: IT IS
- **$B070**: FAC GREATER
- **$B072**: CONVERT FF,0,1 TO 0,1,2
- **$B074**: AND TO 0,2,4 IF C=0, ELSE 1,2,5
- **$B075**: 00000<=>
- **$B077**: IF NO MATCH: FALSE
- **$B079**: AT LEAST ONE MATCH: TRUE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*