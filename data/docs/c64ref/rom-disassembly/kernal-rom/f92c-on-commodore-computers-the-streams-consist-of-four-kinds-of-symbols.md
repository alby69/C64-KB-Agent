---
title: On Commodore computers, the streams consist of four kinds of symbols
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
- bit
- f92c-lesen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F92C
  address_end: $FA5D
  symbol: on-commodore-computers-the-streams-consist-of-four-kinds-of-symbols
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F92C**: read VIA 1 timer B high byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F92C**: Timer B HIGH laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F92C — On Commodore computers, the streams consist of four kinds of symbols

## Disassemblatura
```assembly
.F92C  AE 07 DC LDX $DC07   ; read VIA 1 timer B high byte
.F92F  A0 FF    LDY #$FF   ; set $FF
.F931  98       TYA   ; A = $FF
.F932  ED 06 DC SBC $DC06   ; subtract VIA 1 timer B low byte
.F935  EC 07 DC CPX $DC07   ; compare it with VIA 1 timer B high byte
.F938  D0 F2    BNE $F92C   ; if timer low byte rolled over loop
.F93A  86 B1    STX $B1   ; save tape timing constant max byte
.F93C  AA       TAX   ; copy $FF - T2C_l
.F93D  8C 06 DC STY $DC06   ; save VIA 1 timer B low byte
.F940  8C 07 DC STY $DC07   ; save VIA 1 timer B high byte
.F943  A9 19    LDA #$19   ; load timer B, timer B single shot, start timer B
.F945  8D 0F DC STA $DC0F   ; save VIA 1 CRB
.F948  AD 0D DC LDA $DC0D   ; read VIA 1 ICR
.F94B  8D A3 02 STA $02A3   ; save VIA 1 ICR shadow copy
.F94E  98       TYA   ; y = $FF
.F94F  E5 B1    SBC $B1   ; subtract tape timing constant max byte A = $FF - T2C_h
.F951  86 B1    STX $B1   ; save tape timing constant max byte $B1 = $FF - T2C_l
.F953  4A       LSR   ; A = $FF - T2C_h >> 1
.F954  66 B1    ROR $B1   ; shift tape timing constant max byte $B1 = $FF - T2C_l >> 1
.F956  4A       LSR   ; A = $FF - T2C_h >> 1
.F957  66 B1    ROR $B1   ; shift tape timing constant max byte $B1 = $FF - T2C_l >> 1
.F959  A5 B0    LDA $B0   ; get tape timing constant min byte
.F95B  18       CLC   ; clear carry for add
.F95C  69 3C    ADC #$3C
.F95E  C5 B1    CMP $B1   ; compare with tape timing constant max byte compare with ($FFFF - T2C) >> 2
.F960  B0 4A    BCS $F9AC   ; branch if min + $3C >= ($FFFF - T2C) >> 2 min + $3C < ($FFFF - T2C) >> 2
.F962  A6 9C    LDX $9C   ; get byte received flag
.F964  F0 03    BEQ $F969   ; if not byte received ??
.F966  4C 60 FA JMP $FA60   ; store the tape character
.F969  A6 A3    LDX $A3   ; get EOI flag byte
.F96B  30 1B    BMI $F988
.F96D  A2 00    LDX #$00
.F96F  69 30    ADC #$30
.F971  65 B0    ADC $B0   ; add tape timing constant min byte
.F973  C5 B1    CMP $B1   ; compare with tape timing constant max byte
.F975  B0 1C    BCS $F993
.F977  E8       INX
.F978  69 26    ADC #$26
.F97A  65 B0    ADC $B0   ; add tape timing constant min byte
.F97C  C5 B1    CMP $B1   ; compare with tape timing constant max byte
.F97E  B0 17    BCS $F997
.F980  69 2C    ADC #$2C
.F982  65 B0    ADC $B0   ; add tape timing constant min byte
.F984  C5 B1    CMP $B1   ; compare with tape timing constant max byte
.F986  90 03    BCC $F98B
.F988  4C 10 FA JMP $FA10
.F98B  A5 B4    LDA $B4   ; get the bit count
.F98D  F0 1D    BEQ $F9AC   ; if all done go ??
.F98F  85 A8    STA $A8   ; save receiver bit count in
.F991  D0 19    BNE $F9AC   ; branch always
.F993  E6 A9    INC $A9   ; increment ?? start bit check flag
.F995  B0 02    BCS $F999
.F997  C6 A9    DEC $A9   ; decrement ?? start bit check flag
.F999  38       SEC
.F99A  E9 13    SBC #$13
.F99C  E5 B1    SBC $B1   ; subtract tape timing constant max byte
.F99E  65 92    ADC $92   ; add timing constant for tape
.F9A0  85 92    STA $92   ; save timing constant for tape
.F9A2  A5 A4    LDA $A4   ; get tape bit cycle phase
.F9A4  49 01    EOR #$01
.F9A6  85 A4    STA $A4   ; save tape bit cycle phase
.F9A8  F0 2B    BEQ $F9D5
.F9AA  86 D7    STX $D7
.F9AC  A5 B4    LDA $B4   ; get the bit count
.F9AE  F0 22    BEQ $F9D2   ; if all done go ??
.F9B0  AD A3 02 LDA $02A3   ; read VIA 1 ICR shadow copy
.F9B3  29 01    AND #$01   ; mask 0000 000x, timer A interrupt enabled
.F9B5  D0 05    BNE $F9BC   ; if timer A is enabled go ??
.F9B7  AD A4 02 LDA $02A4   ; read VIA 1 CRA shadow copy
.F9BA  D0 16    BNE $F9D2   ; if ?? just exit
.F9BC  A9 00    LDA #$00   ; clear A
.F9BE  85 A4    STA $A4   ; clear the tape bit cycle phase
.F9C0  8D A4 02 STA $02A4   ; save VIA 1 CRA shadow copy
.F9C3  A5 A3    LDA $A3   ; get EOI flag byte
.F9C5  10 30    BPL $F9F7
.F9C7  30 BF    BMI $F988
.F9C9  A2 A6    LDX #$A6   ; set timing max byte
.F9CB  20 E2 F8 JSR $F8E2   ; set timing
.F9CE  A5 9B    LDA $9B
.F9D0  D0 B9    BNE $F98B
.F9D2  4C BC FE JMP $FEBC   ; restore registers and exit interrupt
.F9D5  A5 92    LDA $92   ; get timing constant for tape
.F9D7  F0 07    BEQ $F9E0
.F9D9  30 03    BMI $F9DE
.F9DB  C6 B0    DEC $B0   ; decrement tape timing constant min byte
.F9DD  2C       .BYTE $2C   ; makes next line BIT $B0E6
.F9DE  E6 B0    INC $B0   ; increment tape timing constant min byte
.F9E0  A9 00    LDA #$00
.F9E2  85 92    STA $92   ; clear timing constant for tape
.F9E4  E4 D7    CPX $D7
.F9E6  D0 0F    BNE $F9F7
.F9E8  8A       TXA
.F9E9  D0 A0    BNE $F98B
.F9EB  A5 A9    LDA $A9   ; get start bit check flag
.F9ED  30 BD    BMI $F9AC
.F9EF  C9 10    CMP #$10
.F9F1  90 B9    BCC $F9AC
.F9F3  85 96    STA $96   ; save cassette block synchronization number
.F9F5  B0 B5    BCS $F9AC
.F9F7  8A       TXA
.F9F8  45 9B    EOR $9B
.F9FA  85 9B    STA $9B
.F9FC  A5 B4    LDA $B4
.F9FE  F0 D2    BEQ $F9D2
.FA00  C6 A3    DEC $A3   ; decrement EOI flag byte
.FA02  30 C5    BMI $F9C9
.FA04  46 D7    LSR $D7
.FA06  66 BF    ROR $BF   ; parity count
.FA08  A2 DA    LDX #$DA   ; set timing max byte
.FA0A  20 E2 F8 JSR $F8E2   ; set timing
.FA0D  4C BC FE JMP $FEBC   ; restore registers and exit interrupt
.FA10  A5 96    LDA $96   ; get cassette block synchronization number
.FA12  F0 04    BEQ $FA18
.FA14  A5 B4    LDA $B4
.FA16  F0 07    BEQ $FA1F
.FA18  A5 A3    LDA $A3   ; get EOI flag byte
.FA1A  30 03    BMI $FA1F
.FA1C  4C 97 F9 JMP $F997
.FA1F  46 B1    LSR $B1   ; shift tape timing constant max byte
.FA21  A9 93    LDA #$93
.FA23  38       SEC
.FA24  E5 B1    SBC $B1   ; subtract tape timing constant max byte
.FA26  65 B0    ADC $B0   ; add tape timing constant min byte
.FA28  0A       ASL
.FA29  AA       TAX   ; copy timing high byte
.FA2A  20 E2 F8 JSR $F8E2   ; set timing
.FA2D  E6 9C    INC $9C
.FA2F  A5 B4    LDA $B4
.FA31  D0 11    BNE $FA44
.FA33  A5 96    LDA $96   ; get cassette block synchronization number
.FA35  F0 26    BEQ $FA5D
.FA37  85 A8    STA $A8   ; save receiver bit count in
.FA39  A9 00    LDA #$00   ; clear A
.FA3B  85 96    STA $96   ; clear cassette block synchronization number
.FA3D  A9 81    LDA #$81   ; enable timer A interrupt
.FA3F  8D 0D DC STA $DC0D   ; save VIA 1 ICR
.FA42  85 B4    STA $B4
.FA44  A5 96    LDA $96   ; get cassette block synchronization number
.FA46  85 B5    STA $B5
.FA48  F0 09    BEQ $FA53
.FA4A  A9 00    LDA #$00
.FA4C  85 B4    STA $B4
.FA4E  A9 01    LDA #$01   ; disable timer A interrupt
.FA50  8D 0D DC STA $DC0D   ; save VIA 1 ICR
.FA53  A5 BF    LDA $BF   ; parity count
.FA55  85 BD    STA $BD   ; save RS232 parity byte
.FA57  A5 A8    LDA $A8   ; get receiver bit count in
.FA59  05 A9    ORA $A9   ; OR with start bit check flag
.FA5B  85 B6    STA $B6
.FA5D  4C BC FE JMP $FEBC   ; restore registers and exit interrupt
```


## Commenti

### Original Disassembly (—)
- **$F92C**: read VIA 1 timer B high byte
- **$F92F**: set $FF
- **$F931**: A = $FF
- **$F932**: subtract VIA 1 timer B low byte
- **$F935**: compare it with VIA 1 timer B high byte
- **$F938**: if timer low byte rolled over loop
- **$F93A**: save tape timing constant max byte
- **$F93C**: copy $FF - T2C_l
- **$F93D**: save VIA 1 timer B low byte
- **$F940**: save VIA 1 timer B high byte
- **$F943**: load timer B, timer B single shot, start timer B
- **$F945**: save VIA 1 CRB
- **$F948**: read VIA 1 ICR
- **$F94B**: save VIA 1 ICR shadow copy
- **$F94E**: y = $FF
- **$F94F**: subtract tape timing constant max byte A = $FF - T2C_h
- **$F951**: save tape timing constant max byte $B1 = $FF - T2C_l
- **$F953**: A = $FF - T2C_h >> 1
- **$F954**: shift tape timing constant max byte $B1 = $FF - T2C_l >> 1
- **$F956**: A = $FF - T2C_h >> 1
- **$F957**: shift tape timing constant max byte $B1 = $FF - T2C_l >> 1
- **$F959**: get tape timing constant min byte
- **$F95B**: clear carry for add
- **$F95E**: compare with tape timing constant max byte compare with ($FFFF - T2C) >> 2
- **$F960**: branch if min + $3C >= ($FFFF - T2C) >> 2 min + $3C < ($FFFF - T2C) >> 2
- **$F962**: get byte received flag
- **$F964**: if not byte received ??
- **$F966**: store the tape character
- **$F969**: get EOI flag byte
- **$F971**: add tape timing constant min byte
- **$F973**: compare with tape timing constant max byte
- **$F97A**: add tape timing constant min byte
- **$F97C**: compare with tape timing constant max byte
- **$F982**: add tape timing constant min byte
- **$F984**: compare with tape timing constant max byte
- **$F98B**: get the bit count
- **$F98D**: if all done go ??
- **$F98F**: save receiver bit count in
- **$F991**: branch always
- **$F993**: increment ?? start bit check flag
- **$F997**: decrement ?? start bit check flag
- **$F99C**: subtract tape timing constant max byte
- **$F99E**: add timing constant for tape
- **$F9A0**: save timing constant for tape
- **$F9A2**: get tape bit cycle phase
- **$F9A6**: save tape bit cycle phase
- **$F9AC**: get the bit count
- **$F9AE**: if all done go ??
- **$F9B0**: read VIA 1 ICR shadow copy
- **$F9B3**: mask 0000 000x, timer A interrupt enabled
- **$F9B5**: if timer A is enabled go ??
- **$F9B7**: read VIA 1 CRA shadow copy
- **$F9BA**: if ?? just exit
- **$F9BC**: clear A
- **$F9BE**: clear the tape bit cycle phase
- **$F9C0**: save VIA 1 CRA shadow copy
- **$F9C3**: get EOI flag byte
- **$F9C9**: set timing max byte
- **$F9CB**: set timing
- **$F9D2**: restore registers and exit interrupt
- **$F9D5**: get timing constant for tape
- **$F9DB**: decrement tape timing constant min byte
- **$F9DD**: makes next line BIT $B0E6
- **$F9DE**: increment tape timing constant min byte
- **$F9E2**: clear timing constant for tape
- **$F9EB**: get start bit check flag
- **$F9F3**: save cassette block synchronization number
- **$FA00**: decrement EOI flag byte
- **$FA06**: parity count
- **$FA08**: set timing max byte
- **$FA0A**: set timing
- **$FA0D**: restore registers and exit interrupt
- **$FA10**: get cassette block synchronization number
- **$FA18**: get EOI flag byte
- **$FA1F**: shift tape timing constant max byte
- **$FA24**: subtract tape timing constant max byte
- **$FA26**: add tape timing constant min byte
- **$FA29**: copy timing high byte
- **$FA2A**: set timing
- **$FA33**: get cassette block synchronization number
- **$FA37**: save receiver bit count in
- **$FA39**: clear A
- **$FA3B**: clear cassette block synchronization number
- **$FA3D**: enable timer A interrupt
- **$FA3F**: save VIA 1 ICR
- **$FA44**: get cassette block synchronization number
- **$FA4E**: disable timer A interrupt
- **$FA50**: save VIA 1 ICR
- **$FA53**: parity count
- **$FA55**: save RS232 parity byte
- **$FA57**: get receiver bit count in
- **$FA59**: OR with start bit check flag
- **$FA5D**: restore registers and exit interrupt

### Commodore-64-intern-Buch (Commodore)
- **$F92C**: Timer B HIGH laden
- **$F92F**: Y-Register mit $FF laden (für Timer)
- **$F931**: in Akku schieben
- **$F932**: Timer B von $FF abziehen
- **$F935**: Timer B mit altem Wert vergleichen
- **$F938**: verzweige, falls vermindert
- **$F93A**: Timer B HIGH ablegen
- **$F93C**: und in Akku schieben
- **$F93D**: Timer B LOW und
- **$F940**: Timer B HIGH auf $FF setzen
- **$F943**: Arbeitsmodus für Timer B
- **$F945**: festlegen und starten
- **$F948**: Interrupt Control Register
- **$F94B**: laden und nach $02A3
- **$F94E**: Y-REG in Akku ($FF)
- **$F94F**: Errechnung von vergangener Zeit seit letzter Flanke
- **$F951**: vergangene Zeit LOW nach $B1
- **$F953**: vergangene Zeit
- **$F954**: HIGH
- **$F956**: geteilt
- **$F957**: durch vier
- **$F959**: Timingkonstante laden
- **$F95B**: und mit
- **$F95C**: $3C addiert
- **$F95E**: errechnete Zeit größer als die Zeit bei letzten Flanken
- **$F960**: verzweige, wenn größer
- **$F962**: Flag für empfangenes Byte laden
- **$F964**: verzweige, falls Null (Byte nicht geladen)
- **$F966**: ansonsten nach $FA60
- **$F969**: Byte vollständig gelesen
- **$F96B**: verzweige, falls ja
- **$F96D**: Code für kurzer Impuls (X=0)
- **$F96F**: zu errechneter Zeit mit $30
- **$F971**: und mit Zeitkonstante addieren
- **$F973**: größer als Zeit beim letztem Flanken ?
- **$F975**: verzweige wenn größer
- **$F977**: sonst langer Impuls (X=1)
- **$F978**: und wieder $26 und
- **$F97A**: Zeitkonstanten addieren
- **$F97C**: jetzt größer ?
- **$F97E**: verzweige, falls ja
- **$F980**: sonst wieder $2C und
- **$F982**: Zeitkonstante addieren
- **$F984**: vergangene Zeit noch länger ?
- **$F986**: verzweige, wenn jetzt kürzer
- **$F988**: zu empfangenes Byte verarbeiten
- **$F98B**: Flag für Timer A laden
- **$F98D**: verzweige, wenn Timer A nicht freigegeben
- **$F98F**: Zeiger auf 'READ ERROR' setzen
- **$F991**: unbedingter Sprung
- **$F993**: Zeiger auf Impulswechsel +1
- **$F995**: unbedingter Sprung
- **$F997**: Zeiger auf Impulswechsel -1
- **$F999**: Carry für Subtraktion setzen
- **$F99A**: Anfangswert ($13) und
- **$F99C**: vergangene Zeit subtrahieren
- **$F99E**: und mit Flag für Timing Korrektur addieren
- **$F9A0**: Ergebnis dort speichern
- **$F9A2**: Flag für Empfang beider
- **$F9A4**: Impulse invertieren
- **$F9A6**: und abspeichern
- **$F9A8**: verzweige wenn beide Impulse empfangen
- **$F9AA**: empfangenes Signal speichern
- **$F9AC**: Flag für Timer A laden
- **$F9AE**: verzweige wenn Timer gesperrt
- **$F9B0**: ICR in Akku
- **$F9B3**: Bit 0 isolieren
- **$F9B5**: verzweige wenn Interrupt von Timer A
- **$F9B7**: Timer A abgelaufen
- **$F9BA**: nein, dann zum Interruptende
- **$F9BC**: Impulszähler
- **$F9BE**: löschen und
- **$F9C0**: Zeiger auf Timeout setzen
- **$F9C3**: prüfe ob Byte vollständig gelesen
- **$F9C5**: verzweige falls nein
- **$F9C7**: unbedingter Sprung
- **$F9C9**: Initialisierungswert für Timer A
- **$F9CB**: Band zum Lesen vorbereiten
- **$F9CE**: Paritätsbyte in Akku
- **$F9D0**: verzweige falls parit. Fehler
- **$F9D2**: Rückkehr vom Interrupt
- **$F9D5**: Timing Korrekturzeiger laden
- **$F9D7**: verzweige wenn Flag gelöscht
- **$F9D9**: verzweige wenn kleiner Null
- **$F9DB**: Timing Konstante -1
- **$F9DD**: Skip zu $F9E0
- **$F9DE**: Timing Konstante +1
- **$F9E0**: Timing
- **$F9E2**: Korrekturzeiger löschen
- **$F9E4**: Vergleiche empfangenen Impuls mit vorherigem
- **$F9E6**: verzweige falls ungleich
- **$F9E8**: Prüfe ob kurzer Impuls empfangen
- **$F9E9**: falls nein, verzweige
- **$F9EB**: Impulswechselzeiger laden
- **$F9ED**: verzweige wenn negativ
- **$F9EF**: vergleiche mit $10
- **$F9F1**: verzweige wenn kleiner $10
- **$F9F3**: sonst EOB Flag empfangen
- **$F9F5**: unbedingter Sprung
- **$F9F7**: Empfangenes Bit in Akku
- **$F9F8**: mit Band-Parität verknüpfen
- **$F9FA**: in Band-Parität speichern
- **$F9FC**: Flag für Timer A laden
- **$F9FE**: verzweige wenn nicht frei ge- geben
- **$FA00**: Speicher für Bitzähler -1
- **$FA02**: verzweige wenn Paritätsbit empfangen
- **$FA04**: gelesenes Bit ins Carry und
- **$FA06**: dann in $BF rollen
- **$FA08**: Initialisierungswert für Timer A ins X-Register
- **$FA0A**: zur Kassettensynchronisation
- **$FA0D**: Rückkehr vom Interrupt
- **$FA10**: Prüfe ob EOB empfangen
- **$FA12**: falls nein, verzweige
- **$FA14**: Prüfe ob Timer A freige.
- **$FA16**: wenn nein, überspringe Bit Zähler Test
- **$FA18**: Bitzähler laden
- **$FA1A**: verzweige falls negatv
- **$FA1C**: langen Impuls verarbeiten
- **$FA1F**: vergangene Zeit seit letztem Flangen halbieren
- **$FA21**: und diesen Wert
- **$FA23**: von $93
- **$FA24**: abziehen
- **$FA26**: dazu dann Timing-Konstante addieren
- **$FA28**: und Ergebnis verdoppeln
- **$FA29**: Ergebnis ins X-Register
- **$FA2A**: Timing initialisieren
- **$FA2D**: Flag für Byte empfangen setzen
- **$FA2F**: Flag für Timer A laden
- **$FA31**: verzweige falls freigegeben
- **$FA33**: wurde EOB emfangen ?
- **$FA35**: verzweige wenn nicht empfangen
- **$FA37**: Flag für Lesefehler setzen
- **$FA39**: Flag für
- **$FA3B**: EOB rücksetzen
- **$FA3D**: Interrupt für
- **$FA3F**: Timer A freigeben
- **$FA42**: und Flag für Timer A setzen
- **$FA44**: Flag für EOB laden
- **$FA46**: und nach $B5 kopieren
- **$FA48**: verzweige wenn kein EOB
- **$FA4A**: Flag für Timer A
- **$FA4C**: löschen und auch
- **$FA4E**: Interruptflag
- **$FA50**: wieder löschen
- **$FA53**: Shift Register für Read laden
- **$FA55**: und nach $BD bringen
- **$FA57**: Flag für Lesefehler laden
- **$FA59**: mit Impulswechselzeiger
- **$FA5B**: verknüpfen und in Fehlercode des Bytes ablegen
- **$FA5D**: Rückkehr vom Interrupt
- **$FA60**: Bitzähler für serielle Ausgabe setzen
- **$FA63**: Zeiger auf Byte empfangen rücksetzen
- **$FA65**: Initialisierungswert Timer A
- **$FA67**: Kassettensynchronisation
- **$FA6A**: Anzahl der verbliebenen Blöcke laden
- **$FA6C**: verzweige wenn Null
- **$FA6E**: Blockanzahl neu setzen
- **$FA70**: Maskenwert für Zählung vor dem Lesen
- **$FA72**: Prüfe Zeiger für Lesen von Band
- **$FA74**: verzweige wenn alle Zeichen empfangen (Ende)
- **$FA76**: Flag für EOB laden
- **$FA78**: verzweige wenn gültiges EOB empfangen
- **$FA7A**: Anzahl der verbliebenen Blöcke laden
- **$FA7C**: Anzahl -1
- **$FA7D**: verzweige wenn nicht Null
- **$FA7F**: 'LONG BLOCK' error
- **$FA81**: Status setzen
- **$FA84**: unbedingter Sprung zum normalen IRQ
- **$FA86**: Flag für Lesen vom Band auf
- **$FA88**: Abtastung setzen
- **$FA8A**: Rückkehr vom Interrupt
- **$FA8D**: verzweige wenn Bandzeiger auf lesen
- **$FA8F**: verzweige wenn Bandzeiger auf Zählen
- **$FA91**: Flag für EOB laden
- **$FA93**: verzweige wenn EOB empfangen
- **$FA95**: Flag für Lesefehler laden
- **$FA97**: verzweige falls Fehler aufgetreten
- **$FA99**: Anzahl der noch zu lesenden Blöcke holen
- **$FA9B**: Bit 0 ins Carry schieben
- **$FA9C**: hole gelesenes Byte
- **$FA9E**: verzweige wenn es Zählbyte ist
- **$FAA0**: verzweige wenn mehr als ein Block zu lesen
- **$FAA2**: lösche Carry um nicht zu verzweigen
- **$FAA3**: verzweige falls nur ein Block zu lesen
- **$FAA5**: Bits 0 bis 3 isolieren
- **$FAA7**: und für Zählung speichern
- **$FAA9**: alle Synchrrnisationsbytes empfangen
- **$FAAB**: wenn nein verzweige
- **$FAAD**: Bandzeiger auf
- **$FAAF**: lesen stellen
- **$FAB1**: Ein/Ausgabe Adresse kopieren
- **$FAB4**: Flag für
- **$FAB6**: Leseprüfsumme löschen
- **$FAB8**: unbedingter Sprung
- **$FABA**: Bandzeiger
- **$FABC**: auf Ende stellen
- **$FABE**: unbedingter Sprung
- **$FAC0**: Flag für EOB laden
- **$FAC2**: verzweige wenn nicht gesetzt
- **$FAC4**: 'SHORT BLOCK’ error
- **$FAC6**: Status setzen
- **$FAC9**: Code für Lesezeiger auf "Abtasten"
- **$FACB**: setzen, unbedingter Sprung
- **$FACE**: Endadresse schon erreicht ?
- **$FAD1**: nein dann verzweige
- **$FAD3**: zu Read Ende für Block
- **$FAD6**: nur noch
- **$FAD8**: ein Block zu lesen
- **$FAD9**: verzweige wenn ja (Pass 2)
- **$FADB**: Load/Verify-Flag
- **$FADD**: verzweige wenn Load
- **$FADF**: Zähler auf Null setzen
- **$FAE1**: gelesenes Byte
- **$FAE3**: vergleichen
- **$FAE5**: verzweige wenn Übereinstim- mung
- **$FAE7**: Fehlerflag
- **$FAE9**: setzen
- **$FAEB**: Fehlerflag laden
- **$FAED**: verzweige wenn kein Fehler aufgetreten
- **$FAEF**: bereits 31 Fehler
- **$FAF1**: aufgetreten
- **$FAF3**: verzweige wenn weniger Fehler
- **$FAF5**: Index für Lesefehler
- **$FAF7**: laufender Adressbyte HIGH
- **$FAF9**: im Stack speichern
- **$FAFC**: Adressbyte LOW
- **$FAFE**: für spätere Korrektur ebenfalls im Stack speichern
- **$FB01**: Zeiger auf nachfolgende
- **$FB02**: freie Stelle setzen
- **$FB03**: und abspeichern
- **$FB05**: weitermachen
- **$FB08**: bereits alle Lesefehler
- **$FB0A**: korrigiert ?
- **$FB0C**: verzweige falls ja
- **$FB0E**: Adressbyte LOW laden
- **$FB10**: mit fehlerhaftem Adressbyte LOW vergleichen
- **$FB13**: verzweige falls nicht gefunden
- **$FB15**: Adressbyte HIGH laden
- **$FB17**: mit fehlerhaftem Adressbyte HIGH vergleichen
- **$FB1A**: verzweige wenn nicht gefunden
- **$FB1C**: Korrekturzähler
- **$FB1E**: Pass 2 um zwei erhöhen
- **$FB20**: Verify-Flag gesetzt
- **$FB22**: verzweige wenn nicht gesetzt
- **$FB24**: gelesenes Byte laden
- **$FB26**: Zähler auf Null setzen
- **$FB28**: mit Speicherinhalt verglei- chen
- **$FB2A**: verzweige wenn gleich, dann nächstes Byte
- **$FB2C**: Flag für
- **$FB2D**: Fehler setzen
- **$FB2F**: Fehlerflag testen
- **$FB31**: verzweige wenn kein Fehler
- **$FB33**: 'SECOND PASS' error
- **$FB35**: Status setzen
- **$FB38**: und nächstes Byte verarbeiten
- **$FB3A**: Verify-Flag laden
- **$FB3C**: verzweige wenn gesetzt
- **$FB3E**: Zeiger löschen
- **$FB3F**: gelesenes Byte
- **$FB41**: speichern
- **$FB43**: Adresszeiger erhöhen
- **$FB46**: Rückkehr vom Interrupt
- **$FB48**: Flag für Lesen
- **$FB4A**: auf Ende
- **$FB4C**: Interrupt verhindern
- **$FB4D**: IRQ vom
- **$FB4F**: Timer A verhindern
- **$FB52**: IRQ-Flag löschen
- **$FB55**: Pass-Zähler
- **$FB57**: erniedrigen
- **$FB58**: verzweige wenn Null gewesen
- **$FB5A**: Passzähler merken
- **$FB5C**: Blockzähler vermindern
- **$FB5E**: verzweige wenn Null
- **$FB60**: Fehler in Pass 1 aufgetre- ten ?
- **$FB62**: ja, Rückkehr vom Interrupt
- **$FB64**: kein Block mehr zu verarbei- ten
- **$FB66**: Rückkehr vom Interrupt
- **$FB68**: ein Pass beendet
- **$FB6B**: Adresse wieder auf Programm- anfang
- **$FB6E**: Zähler auf Null setzen
- **$FB70**: Checksumme löschen
- **$FB72**: Programm
- **$FB74**: Checksumme berechnen
- **$FB76**: und speichern
- **$FB78**: Adresszeiger erhöhen
- **$FB7B**: Endadresse schon erreicht ?
- **$FB7E**: nein, weiter vergleichen
- **$FB80**: berechnete Checksumme
- **$FB82**: mit Checksumme vom Band vergleichen
- **$FB84**: Checksumme gleich , dann ok
- **$FB86**: 'CHECKSUM' error
- **$FB88**: Status setzen
- **$FB8B**: Rückkehr vom Interrupt

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*