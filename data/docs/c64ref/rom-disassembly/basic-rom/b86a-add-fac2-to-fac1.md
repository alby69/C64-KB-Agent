---
title: add FAC2 to FAC1
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
- b86a-plus-fac-fac-arg
- bc5b-fac
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B86A
  address_end: $B8D0
  symbol: add-fac2-to-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B86A**: branch if FAC1 is not zero'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B86A**: FAC ungleich null ?'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B86A**: FAC IS NON-ZERO'
---

# $B86A — add FAC2 to FAC1

## Disassemblatura
```assembly
.B86A  D0 03    BNE $B86F   ; branch if FAC1 is not zero
.B86C  4C FC BB JMP $BBFC   ; FAC1 was zero so copy FAC2 to FAC1 and return FAC1 is non zero
.B86F  A6 70    LDX $70   ; get FAC1 rounding byte
.B871  86 56    STX $56   ; save as FAC2 rounding byte
.B873  A2 69    LDX #$69   ; set index to FAC2 exponent address
.B875  A5 69    LDA $69   ; get FAC2 exponent
.B877  A8       TAY   ; copy exponent
.B878  F0 CE    BEQ $B848   ; exit if zero
.B87A  38       SEC   ; set carry for subtract
.B87B  E5 61    SBC $61   ; subtract FAC1 exponent
.B87D  F0 24    BEQ $B8A3   ; if equal go add mantissas
.B87F  90 12    BCC $B893   ; if FAC2 < FAC1 then go shift FAC2 right else FAC2 > FAC1
.B881  84 61    STY $61   ; save FAC1 exponent
.B883  A4 6E    LDY $6E   ; get FAC2 sign (b7)
.B885  84 66    STY $66   ; save FAC1 sign (b7)
.B887  49 FF    EOR #$FF   ; complement A
.B889  69 00    ADC #$00   ; +1, twos complement, carry is set
.B88B  A0 00    LDY #$00   ; clear Y
.B88D  84 56    STY $56   ; clear FAC2 rounding byte
.B88F  A2 61    LDX #$61   ; set index to FAC1 exponent address
.B891  D0 04    BNE $B897   ; branch always FAC2 < FAC1
.B893  A0 00    LDY #$00   ; clear Y
.B895  84 70    STY $70   ; clear FAC1 rounding byte
.B897  C9 F9    CMP #$F9   ; compare exponent diff with $F9
.B899  30 C7    BMI $B862   ; branch if range $79-$F8
.B89B  A8       TAY   ; copy exponent difference to Y
.B89C  A5 70    LDA $70   ; get FAC1 rounding byte
.B89E  56 01    LSR $01,X   ; shift FAC? mantissa 1
.B8A0  20 B0 B9 JSR $B9B0   ; shift FACX Y times right exponents are equal now do mantissa subtract
.B8A3  24 6F    BIT $6F   ; test sign compare (FAC1 EOR FAC2)
.B8A5  10 57    BPL $B8FE   ; if = add FAC2 mantissa to FAC1 mantissa and return
.B8A7  A0 61    LDY #$61   ; set the Y index to FAC1 exponent address
.B8A9  E0 69    CPX #$69   ; compare X to FAC2 exponent address
.B8AB  F0 02    BEQ $B8AF   ; if = continue, Y = FAC1, X = FAC2
.B8AD  A0 69    LDY #$69   ; else set the Y index to FAC2 exponent address subtract the smaller from the bigger (take the sign of the bigger)
.B8AF  38       SEC   ; set carry for subtract
.B8B0  49 FF    EOR #$FF   ; ones complement A
.B8B2  65 56    ADC $56   ; add FAC2 rounding byte
.B8B4  85 70    STA $70   ; save FAC1 rounding byte
.B8B6  B9 04 00 LDA $0004,Y   ; get FACY mantissa 4
.B8B9  F5 04    SBC $04,X   ; subtract FACX mantissa 4
.B8BB  85 65    STA $65   ; save FAC1 mantissa 4
.B8BD  B9 03 00 LDA $0003,Y   ; get FACY mantissa 3
.B8C0  F5 03    SBC $03,X   ; subtract FACX mantissa 3
.B8C2  85 64    STA $64   ; save FAC1 mantissa 3
.B8C4  B9 02 00 LDA $0002,Y   ; get FACY mantissa 2
.B8C7  F5 02    SBC $02,X   ; subtract FACX mantissa 2
.B8C9  85 63    STA $63   ; save FAC1 mantissa 2
.B8CB  B9 01 00 LDA $0001,Y   ; get FACY mantissa 1
.B8CE  F5 01    SBC $01,X   ; subtract FACX mantissa 1
.B8D0  85 62    STA $62   ; save FAC1 mantissa 1
```


## Commenti

### Original Disassembly (—)
- **$B86A**: branch if FAC1 is not zero
- **$B86C**: FAC1 was zero so copy FAC2 to FAC1 and return FAC1 is non zero
- **$B86F**: get FAC1 rounding byte
- **$B871**: save as FAC2 rounding byte
- **$B873**: set index to FAC2 exponent address
- **$B875**: get FAC2 exponent
- **$B877**: copy exponent
- **$B878**: exit if zero
- **$B87A**: set carry for subtract
- **$B87B**: subtract FAC1 exponent
- **$B87D**: if equal go add mantissas
- **$B87F**: if FAC2 < FAC1 then go shift FAC2 right else FAC2 > FAC1
- **$B881**: save FAC1 exponent
- **$B883**: get FAC2 sign (b7)
- **$B885**: save FAC1 sign (b7)
- **$B887**: complement A
- **$B889**: +1, twos complement, carry is set
- **$B88B**: clear Y
- **$B88D**: clear FAC2 rounding byte
- **$B88F**: set index to FAC1 exponent address
- **$B891**: branch always FAC2 < FAC1
- **$B893**: clear Y
- **$B895**: clear FAC1 rounding byte
- **$B897**: compare exponent diff with $F9
- **$B899**: branch if range $79-$F8
- **$B89B**: copy exponent difference to Y
- **$B89C**: get FAC1 rounding byte
- **$B89E**: shift FAC? mantissa 1
- **$B8A0**: shift FACX Y times right exponents are equal now do mantissa subtract
- **$B8A3**: test sign compare (FAC1 EOR FAC2)
- **$B8A5**: if = add FAC2 mantissa to FAC1 mantissa and return
- **$B8A7**: set the Y index to FAC1 exponent address
- **$B8A9**: compare X to FAC2 exponent address
- **$B8AB**: if = continue, Y = FAC1, X = FAC2
- **$B8AD**: else set the Y index to FAC2 exponent address subtract the smaller from the bigger (take the sign of the bigger)
- **$B8AF**: set carry for subtract
- **$B8B0**: ones complement A
- **$B8B2**: add FAC2 rounding byte
- **$B8B4**: save FAC1 rounding byte
- **$B8B6**: get FACY mantissa 4
- **$B8B9**: subtract FACX mantissa 4
- **$B8BB**: save FAC1 mantissa 4
- **$B8BD**: get FACY mantissa 3
- **$B8C0**: subtract FACX mantissa 3
- **$B8C2**: save FAC1 mantissa 3
- **$B8C4**: get FACY mantissa 2
- **$B8C7**: subtract FACX mantissa 2
- **$B8C9**: save FAC1 mantissa 2
- **$B8CB**: get FACY mantissa 1
- **$B8CE**: subtract FACX mantissa 1
- **$B8D0**: save FAC1 mantissa 1

### Commodore-64-intern-Buch (Commodore)
- **$B86A**: FAC ungleich null ?
- **$B86C**: nein, dann FAC = ARG
- **$B86F**: Rundungsbyte für FAC
- **$B871**: in $56 speichern
- **$B873**: Offset-Zeiger für ARG laden
- **$B875**: Exponent von ARG laden
- **$B877**: in Y-Reg schieben
- **$B878**: wenn ARG=0, dann RTS
- **$B87A**: Exponent von
- **$B87B**: FAC subtrahieren
- **$B87D**: wenn Exponent gleich, dann zu $B8A3
- **$B87F**: wenn Exponent von FAC größer, dann zu $B893
- **$B881**: FAC-Exponent durch ARG-Vorzeichen ersetzen
- **$B883**: FAC-Vorzeichen durch
- **$B885**: ARG-Vorzeichen ersetzen
- **$B887**: Vorzeichen wechseln
- **$B889**: Carry ist schon 1
- **$B88B**: Rundungsstelle
- **$B88D**: löschen
- **$B88F**: Offset-Zeiger für FAC laden
- **$B891**: unbedingter Sprung
- **$B893**: FAC-Rundungsstelle
- **$B895**: löschen
- **$B897**: wenn Exponentdifferenz
- **$B899**: größer als 7, dann zu $B862
- **$B89B**: Akku löschen
- **$B89C**: FAC-Rundungsstelle
- **$B89E**: laden
- **$B8A0**: Mantisse verschieben
- **$B8A3**: wenn FAC- und ARG-Vorzeichen
- **$B8A5**: identisch, dann zu $B8FE
- **$B8A7**: Offset-Zeiger für FAC laden
- **$B8A9**: wenn Offset-Zeiger für ARG
- **$B8AB**: initialisiert, dann zu $B8AF
- **$B8AD**: Offset-Zeiger laden
- **$B8AF**: Carryflag für Subtraktion setzen
- **$B8B0**: Alle Bits umdrehen
- **$B8B2**: Rundungsstelle addieren
- **$B8B4**: und speichern
- **$B8B6**: viertes Byte
- **$B8B9**: subtrahieren und in
- **$B8BB**: FAC speichern
- **$B8BD**: drittes Byte
- **$B8C0**: subtrahieren und in
- **$B8C2**: FAC speichern
- **$B8C4**: zweites Byte
- **$B8C7**: subtrahieren und in
- **$B8C9**: FAC speichern
- **$B8CB**: erstes Byte
- **$B8CE**: subtrahieren und in
- **$B8D0**: FAC speichern
- **$B8D2**: wenn Übertrag negativ, dann weiter
- **$B8D4**: Mantisse von FAC invertieren
- **$B8D7**: Y-Reg und
- **$B8D9**: Akku löschen
- **$B8DA**: Carry löschen
- **$B8DB**: wenn $62=0 dann,
- **$B8DD**: zu $B929
- **$B8DF**: Das
- **$B8E1**: gesamte
- **$B8E3**: FAC
- **$B8E5**: wieder
- **$B8E7**: norma-
- **$B8E9**: lisieren
- **$B8EB**: Rundungsstelle
- **$B8ED**: wieder
- **$B8EF**: löschen
- **$B8F1**: Zähler um 8 Bits verschieben
- **$B8F3**: wenn 32 Bits verschoben,
- **$B8F5**: dann weiter
- **$B8F7**: Mantisse =0
- **$B8F9**: FAC =0
- **$B8FB**: Exponent =0
- **$B8FD**: Rücksprung
- **$B8FE**: Rundungsstelle addieren
- **$B900**: und speichern
- **$B902**: FAC
- **$B904**: und ARG
- **$B906**: addieren
- **$B908**: FAC
- **$B90A**: und ARG
- **$B90C**: addieren
- **$B90E**: FAC
- **$B910**: und ARG
- **$B912**: addieren
- **$B914**: FAC
- **$B916**: und ARG
- **$B918**: addieren
- **$B91A**: Überlaufbit in Mantisse zurückshiften
- **$B91D**: Zähler erhöhen
- **$B91F**: FAC solange
- **$B921**: nach links
- **$B923**: verschieben bis das
- **$B925**: Bit 7
- **$B927**: gesetzt ist
- **$B929**: nicht gesetzt ? dann nochmal
- **$B92B**: wenn Binärexponent kleiner
- **$B92C**: als die Anzahl der
- **$B92E**: Verschiebungen, dann wird die Zahl als Null behandelt
- **$B930**: Exponent um
- **$B932**: Verschiebungsanzahl
- **$B934**: vermindern
- **$B936**: Carry gesetzt, nein dann RTS
- **$B938**: Exponent erhöhen
- **$B93A**: wenn Überlauf in Exponent, dann 'OVERFLOW ERROR'
- **$B93C**: Überlaufbit in Carry schieben
- **$B93E**: Das Carry-Flag
- **$B940**: erhält die
- **$B942**: Position des
- **$B944**: höchstwertigen Bits
- **$B946**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B86A**: FAC IS NON-ZERO
- **$B86C**: FAC = 0 + ARG
- **$B873**: SET UP TO SHIFT ARG
- **$B875**: EXPONENT
- **$B878**: IF ARG=0, WE ARE FINISHED
- **$B87B**: GET DIFFNCE OF EXP
- **$B87D**: GO ADD IF SAME EXP
- **$B87F**: ARG HAS SMALLER EXPONENT
- **$B881**: EXP HAS SMALLER EXPONENT
- **$B887**: COMPLEMENT SHIFT COUNT
- **$B889**: CARRY WAS SET
- **$B88F**: SET UP TO SHIFT FAC
- **$B891**: ...ALWAYS
- **$B897**: SHIFT MORE THAN 7 BITS?
- **$B899**: YES
- **$B89B**: INDEX TO # OF SHIFTS
- **$B89E**: START SHIFTING...
- **$B8A0**: ...COMPLETE SHIFTING
- **$B8A3**: DO FAC AND ARG HAVE SAME SIGNS?
- **$B8A5**: YES, ADD THE MANTISSAS
- **$B8A7**: NO, SUBTRACT SMALLER FROM LARGER
- **$B8A9**: WHICH WAS ADJUSTED?
- **$B8AB**: IF ARG, DO FAC-ARG
- **$B8AD**: IF FAC, DO ARG-FAC
- **$B8AF**: SUBTRACT SMALLER FROM LARGER (WE HOPE)
- **$B8B0**: (IF EXPONENTS WERE EQUAL, WE MIGHT BE
- **$B8B2**: SUBTRACTING LARGER FROM SMALLER)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*