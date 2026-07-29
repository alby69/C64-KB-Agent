---
title: IEC-Load
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ece7-load
- f34a-open
- f4b8-iec-load
- f533
- f5a9-load-end
- stop
- talk
- untalk
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F4B8
  address_end: $F5AE
  symbol: iec-load
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F4B8**: Länge des Filenamens laden'
---

# $F4B8 — IEC-Load

## Disassemblatura
```assembly
.F4B8  A4 B7    LDY $B7   ; Länge des Filenamens laden
.F4BA  D0 03    BNE $F4BF   ; ungleich Null, dann ok
.F4BC  4C 10 F7 JMP $F710   ; 'MISSING FILENAME'
.F4BF  A6 B9    LDX $B9   ; Sekundäradresse laden
.F4C1  20 AF F5 JSR $F5AF   ; 'SEARCHING FOR' (filename)
.F4C4  A9 60    LDA #$60   ; Sekundäradresse Null laden (für OPEN)
.F4C6  85 B9    STA $B9   ; und speichern
.F4C8  20 D5 F3 JSR $F3D5   ; File auf IEC-Bus eröffnen
.F4CB  A5 BA    LDA $BA   ; Gerätenummer laden
.F4CD  20 09 ED JSR $ED09   ; und TALK senden
.F4D0  A5 B9    LDA $B9   ; Sekundäradresse laden
.F4D2  20 C7 ED JSR $EDC7   ; und senden
.F4D5  20 13 EE JSR $EE13   ; Byte vom IEC-Bus holen
.F4D8  85 AE    STA $AE   ; als Startadresse LOW spei chern
.F4DA  A5 90    LDA $90   ; Status laden
.F4DC  4A       LSR   ; Bit 1
.F4DD  4A       LSR   ; ins Carry schieben
.F4DE  B0 50    BCS $F530   ; falls gesetzt, dann Time out (Fehler)
.F4E0  20 13 EE JSR $EE13   ; Startadresse HIGH holen
.F4E3  85 AF    STA $AF   ; und speichern
.F4E5  8A       TXA   ; Sekundäradresse laden
.F4E6  D0 08    BNE $F4F0   ; verzweige falls ungleich Null
.F4E8  A5 C3    LDA $C3   ; Startadresse LOW laden
.F4EA  85 AE    STA $AE   ; und speichern
.F4EC  A5 C4    LDA $C4   ; Startadresse HIGH laden
.F4EE  85 AF    STA $AF   ; und speichern
.F4F0  20 D2 F5 JSR $F5D2   ; 'LOADING'/'VERIFYING' ausgeben
.F4F3  A9 FD    LDA #$FD   ; Time-out
.F4F5  25 90    AND $90   ; Bit
.F4F7  85 90    STA $90   ; löschen
.F4F9  20 E1 FF JSR $FFE1   ; Stop-Taste abfragen
.F4FC  D0 03    BNE $F501   ; nicht gedrückt, dann weiter
.F4FE  4C 33 F6 JMP $F633   ; File schließen
.F501  20 13 EE JSR $EE13   ; Programmbyte vom Bus holen
.F504  AA       TAX   ; Akku in X-REG retten
.F505  A5 90    LDA $90   ; Status testen
.F507  4A       LSR   ; Time-out
.F508  4A       LSR   ; Bit ins Carry schieben
.F509  B0 E8    BCS $F4F3   ; falls Fehler, dann abbrechen
.F50B  8A       TXA   ; ansonsten Akku wiederholen
.F50C  A4 93    LDY $93   ; Load/Verify Flag testen
.F50E  F0 0C    BEQ $F51C   ; gleich Null, dann LOAD
.F510  A0 00    LDY #$00   ; Zähler auf Null setzen
.F512  D1 AE    CMP ($AE),Y   ; Verify, Vergleich
.F514  F0 08    BEQ $F51E   ; verzweige falls gleich
.F516  A9 10    LDA #$10   ; Bit 4 für Status setzen
.F518  20 1C FE JSR $FE1C   ; Status setzen
.F51B  2C       .BYTE $2C   ; Skip nach $F51E
.F51C  91 AE    STA ($AE),Y   ; Byte abspeichern
.F51E  E6 AE    INC $AE   ; LOW-Byte der Adresse erhöhen
.F520  D0 02    BNE $F524   ; verzweige falls kein Übertrag
.F522  E6 AF    INC $AF   ; ansonsten HIGH-Byte erhöhen
.F524  24 90    BIT $90   ; Status prüfen
.F526  50 CB    BVC $F4F3   ; verzweige wenn noch kein EOI
.F528  20 EF ED JSR $EDEF   ; UNTALK senden
.F52B  20 42 F6 JSR $F642   ; File schließen
.F52E  90 79    BCC $F5A9   ; vezweige wenn kein Fehler
.F530  4C 04 F7 JMP $F704   ; 'FILE NOT FOUND'
.F533  4A       LSR   ; Gerätenummer feststellen
.F534  B0 03    BCS $F539   ; eins (Band) , dann weiter
.F536  4C 13 F7 JMP $F713   ; RS 232, 'ILLEGAL DEVICE NUMBER'
.F539  20 D0 F7 JSR $F7D0   ; Bandpuffer Startadresse holen
.F53C  B0 03    BCS $F541   ; verzweige wenn HIGH-Byte der Bandpufferstartadresse größer/ gleich 2
.F53E  4C 13 F7 JMP $F713   ; sonst 'ILLEGAL DEVICE NUMBER'
.F541  20 17 F8 JSR $F817   ; wartet auf Play-Taste
.F544  B0 68    BCS $F5AE   ; STOP-Taste, dann Abbruch
.F546  20 AF F5 JSR $F5AF   ; 'SEARCHING' ('for name') ausgeben
.F549  A5 B7    LDA $B7   ; Länge des Filenamens laden
.F54B  F0 09    BEQ $F556   ; verzweige wenn Null
.F54D  20 EA F7 JSR $F7EA   ; gewünschten Bandheader suchen
.F550  90 0B    BCC $F55D   ; verzweige wenn gefunden
.F552  F0 5A    BEQ $F5AE   ; STOP-Taste, dann Abbruch
.F554  B0 DA    BCS $F530   ; EOT, dann 'FILE NOT FOUND'
.F556  20 2C F7 JSR $F72C   ; nächsten Bandheader suchen
.F559  F0 53    BEQ $F5AE   ; STOP-Taste, dann Abbruch
.F55B  B0 D3    BCS $F530   ; 'EOT', dann 'FILE NOT FOUND'
.F55D  A5 90    LDA $90   ; Status holen
.F55F  29 10    AND #$10   ; EOF-Bit ausblenden
.F561  38       SEC   ; Carry =1 (Fehlerkennzeichen)
.F562  D0 4A    BNE $F5AE   ; verzweige falls Fehler
.F564  E0 01    CPX #$01   ; Header-Typ 1 = BASIC- Programm (verschiebbar)
.F566  F0 11    BEQ $F579   ; verzweige wenn Header-Typ =1
.F568  E0 03    CPX #$03   ; 3 = Maschinen-Programm (absolut)
.F56A  D0 DD    BNE $F549   ; verzweige wenn nicht 3 (falscher Header)
.F56C  A0 01    LDY #$01   ; Zeiger setzen
.F56E  B1 B2    LDA ($B2),Y   ; LOW-Byte Startadresse holen
.F570  85 C3    STA $C3   ; und speichern
.F572  C8       INY   ; Zeiger erhöhen
.F573  B1 B2    LDA ($B2),Y   ; HIGH-Byte Startadresse holen
.F575  85 C4    STA $C4   ; und speichern
.F577  B0 04    BCS $F57D   ; unbedingter Sprung
.F579  A5 B9    LDA $B9   ; Sekundär-Adresse
.F57B  D0 EF    BNE $F56C   ; ungleich Null, dann nicht verschiebbar laden
.F57D  A0 03    LDY #$03   ; Zeiger setzen
.F57F  B1 B2    LDA ($B2),Y   ; LOW-Byte der Endadresse+1 des Programms holen
.F581  A0 01    LDY #$01   ; Zeiger auf LOW-Byte Anfangs adresse setzen
.F583  F1 B2    SBC ($B2),Y   ; von Endadresse subtrahieren
.F585  AA       TAX   ; Ergebnis ins X-REG schieben
.F586  A0 04    LDY #$04   ; Zeiger auf HIGH-Byte der Endadresse setzen
.F588  B1 B2    LDA ($B2),Y   ; Endadresse holen
.F58A  A0 02    LDY #$02   ; Zeiger auf Startadresse setzen
.F58C  F1 B2    SBC ($B2),Y   ; und von Endadresse subtrahie ren
.F58E  A8       TAY   ; Ergebnis ins Y-REG schieben
.F58F  18       CLC   ; Carry für Addition löschen
.F590  8A       TXA   ; LOW-Byte der Programmlänge in Akku schieben
.F591  65 C3    ADC $C3   ; mit LOW-Byte der Anfangs adresse addieren
.F593  85 AE    STA $AE   ; als LOW-Byte der Endadresse speichern
.F595  98       TYA   ; HIGH-Byte der Programmlänge in Akku schieben
.F596  65 C4    ADC $C4   ; mit HIGH-Byte Anfangsadresse addieren
.F598  85 AF    STA $AF   ; als HIGH-Byte Endadresse speichern
.F59A  A5 C3    LDA $C3   ; Startadresse
.F59C  85 C1    STA $C1   ; nach $C1
.F59E  A5 C4    LDA $C4   ; und $C2
.F5A0  85 C2    STA $C2   ; bringen
.F5A2  20 D2 F5 JSR $F5D2   ; 'LOADING' / 'VERIFYING' ausgeben
.F5A5  20 4A F8 JSR $F84A   ; Programm vom Band laden
.F5A8  24       .BYTE $24   ; Skip nach $F5AA
.F5A9  18       CLC   ; Carry =0 (ok Kennzeichen)
.F5AA  A6 AE    LDX $AE   ; Endadresse
.F5AC  A4 AF    LDY $AF   ; nach X/Y
.F5AE  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F4B8**: Länge des Filenamens laden
- **$F4BA**: ungleich Null, dann ok
- **$F4BC**: 'MISSING FILENAME'
- **$F4BF**: Sekundäradresse laden
- **$F4C1**: 'SEARCHING FOR' (filename)
- **$F4C4**: Sekundäradresse Null laden (für OPEN)
- **$F4C6**: und speichern
- **$F4C8**: File auf IEC-Bus eröffnen
- **$F4CB**: Gerätenummer laden
- **$F4CD**: und TALK senden
- **$F4D0**: Sekundäradresse laden
- **$F4D2**: und senden
- **$F4D5**: Byte vom IEC-Bus holen
- **$F4D8**: als Startadresse LOW spei chern
- **$F4DA**: Status laden
- **$F4DC**: Bit 1
- **$F4DD**: ins Carry schieben
- **$F4DE**: falls gesetzt, dann Time out (Fehler)
- **$F4E0**: Startadresse HIGH holen
- **$F4E3**: und speichern
- **$F4E5**: Sekundäradresse laden
- **$F4E6**: verzweige falls ungleich Null
- **$F4E8**: Startadresse LOW laden
- **$F4EA**: und speichern
- **$F4EC**: Startadresse HIGH laden
- **$F4EE**: und speichern
- **$F4F0**: 'LOADING'/'VERIFYING' ausgeben
- **$F4F3**: Time-out
- **$F4F5**: Bit
- **$F4F7**: löschen
- **$F4F9**: Stop-Taste abfragen
- **$F4FC**: nicht gedrückt, dann weiter
- **$F4FE**: File schließen
- **$F501**: Programmbyte vom Bus holen
- **$F504**: Akku in X-REG retten
- **$F505**: Status testen
- **$F507**: Time-out
- **$F508**: Bit ins Carry schieben
- **$F509**: falls Fehler, dann abbrechen
- **$F50B**: ansonsten Akku wiederholen
- **$F50C**: Load/Verify Flag testen
- **$F50E**: gleich Null, dann LOAD
- **$F510**: Zähler auf Null setzen
- **$F512**: Verify, Vergleich
- **$F514**: verzweige falls gleich
- **$F516**: Bit 4 für Status setzen
- **$F518**: Status setzen
- **$F51B**: Skip nach $F51E
- **$F51C**: Byte abspeichern
- **$F51E**: LOW-Byte der Adresse erhöhen
- **$F520**: verzweige falls kein Übertrag
- **$F522**: ansonsten HIGH-Byte erhöhen
- **$F524**: Status prüfen
- **$F526**: verzweige wenn noch kein EOI
- **$F528**: UNTALK senden
- **$F52B**: File schließen
- **$F52E**: vezweige wenn kein Fehler
- **$F530**: 'FILE NOT FOUND'
- **$F533**: Gerätenummer feststellen
- **$F534**: eins (Band) , dann weiter
- **$F536**: RS 232, 'ILLEGAL DEVICE NUMBER'
- **$F539**: Bandpuffer Startadresse holen
- **$F53C**: verzweige wenn HIGH-Byte der Bandpufferstartadresse größer/ gleich 2
- **$F53E**: sonst 'ILLEGAL DEVICE NUMBER'
- **$F541**: wartet auf Play-Taste
- **$F544**: STOP-Taste, dann Abbruch
- **$F546**: 'SEARCHING' ('for name') ausgeben
- **$F549**: Länge des Filenamens laden
- **$F54B**: verzweige wenn Null
- **$F54D**: gewünschten Bandheader suchen
- **$F550**: verzweige wenn gefunden
- **$F552**: STOP-Taste, dann Abbruch
- **$F554**: EOT, dann 'FILE NOT FOUND'
- **$F556**: nächsten Bandheader suchen
- **$F559**: STOP-Taste, dann Abbruch
- **$F55B**: 'EOT', dann 'FILE NOT FOUND'
- **$F55D**: Status holen
- **$F55F**: EOF-Bit ausblenden
- **$F561**: Carry =1 (Fehlerkennzeichen)
- **$F562**: verzweige falls Fehler
- **$F564**: Header-Typ 1 = BASIC- Programm (verschiebbar)
- **$F566**: verzweige wenn Header-Typ =1
- **$F568**: 3 = Maschinen-Programm (absolut)
- **$F56A**: verzweige wenn nicht 3 (falscher Header)
- **$F56C**: Zeiger setzen
- **$F56E**: LOW-Byte Startadresse holen
- **$F570**: und speichern
- **$F572**: Zeiger erhöhen
- **$F573**: HIGH-Byte Startadresse holen
- **$F575**: und speichern
- **$F577**: unbedingter Sprung
- **$F579**: Sekundär-Adresse
- **$F57B**: ungleich Null, dann nicht verschiebbar laden
- **$F57D**: Zeiger setzen
- **$F57F**: LOW-Byte der Endadresse+1 des Programms holen
- **$F581**: Zeiger auf LOW-Byte Anfangs adresse setzen
- **$F583**: von Endadresse subtrahieren
- **$F585**: Ergebnis ins X-REG schieben
- **$F586**: Zeiger auf HIGH-Byte der Endadresse setzen
- **$F588**: Endadresse holen
- **$F58A**: Zeiger auf Startadresse setzen
- **$F58C**: und von Endadresse subtrahie ren
- **$F58E**: Ergebnis ins Y-REG schieben
- **$F58F**: Carry für Addition löschen
- **$F590**: LOW-Byte der Programmlänge in Akku schieben
- **$F591**: mit LOW-Byte der Anfangs adresse addieren
- **$F593**: als LOW-Byte der Endadresse speichern
- **$F595**: HIGH-Byte der Programmlänge in Akku schieben
- **$F596**: mit HIGH-Byte Anfangsadresse addieren
- **$F598**: als HIGH-Byte Endadresse speichern
- **$F59A**: Startadresse
- **$F59C**: nach $C1
- **$F59E**: und $C2
- **$F5A0**: bringen
- **$F5A2**: 'LOADING' / 'VERIFYING' ausgeben
- **$F5A5**: Programm vom Band laden
- **$F5A8**: Skip nach $F5AA
- **$F5A9**: Carry =0 (ok Kennzeichen)
- **$F5AA**: Endadresse
- **$F5AC**: nach X/Y
- **$F5AE**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*