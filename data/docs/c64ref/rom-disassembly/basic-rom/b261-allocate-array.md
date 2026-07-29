---
title: allocate array
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $B261
  address_end: $B2E9
  symbol: allocate-array
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B261**: Länge des Arraykopfs'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B261**: PUT ADDR OF 1ST ELEMENT IN ARYPNT'
---

# $B261 — allocate array

## Disassemblatura
```assembly
.B261  20 94 B1 JSR $B194
.B264  20 08 A4 JSR $A408
.B267  A0 00    LDY #$00
.B269  84 72    STY $72
.B26B  A2 05    LDX #$05
.B26D  A5 45    LDA $45
.B26F  91 5F    STA ($5F),Y
.B271  10 01    BPL $B274
.B273  CA       DEX
.B274  C8       INY
.B275  A5 46    LDA $46
.B277  91 5F    STA ($5F),Y
.B279  10 02    BPL $B27D
.B27B  CA       DEX
.B27C  CA       DEX
.B27D  86 71    STX $71
.B27F  A5 0B    LDA $0B
.B281  C8       INY
.B282  C8       INY
.B283  C8       INY
.B284  91 5F    STA ($5F),Y
.B286  A2 0B    LDX #$0B
.B288  A9 00    LDA #$00
.B28A  24 0C    BIT $0C
.B28C  50 08    BVC $B296
.B28E  68       PLA
.B28F  18       CLC
.B290  69 01    ADC #$01
.B292  AA       TAX
.B293  68       PLA
.B294  69 00    ADC #$00
.B296  C8       INY
.B297  91 5F    STA ($5F),Y
.B299  C8       INY
.B29A  8A       TXA
.B29B  91 5F    STA ($5F),Y
.B29D  20 4C B3 JSR $B34C
.B2A0  86 71    STX $71
.B2A2  85 72    STA $72
.B2A4  A4 22    LDY $22
.B2A6  C6 0B    DEC $0B
.B2A8  D0 DC    BNE $B286
.B2AA  65 59    ADC $59
.B2AC  B0 5D    BCS $B30B
.B2AE  85 59    STA $59
.B2B0  A8       TAY
.B2B1  8A       TXA
.B2B2  65 58    ADC $58
.B2B4  90 03    BCC $B2B9
.B2B6  C8       INY
.B2B7  F0 52    BEQ $B30B
.B2B9  20 08 A4 JSR $A408
.B2BC  85 31    STA $31
.B2BE  84 32    STY $32
.B2C0  A9 00    LDA #$00
.B2C2  E6 72    INC $72
.B2C4  A4 71    LDY $71
.B2C6  F0 05    BEQ $B2CD
.B2C8  88       DEY
.B2C9  91 58    STA ($58),Y
.B2CB  D0 FB    BNE $B2C8
.B2CD  C6 59    DEC $59
.B2CF  C6 72    DEC $72
.B2D1  D0 F5    BNE $B2C8
.B2D3  E6 59    INC $59
.B2D5  38       SEC
.B2D6  A5 31    LDA $31
.B2D8  E5 5F    SBC $5F
.B2DA  A0 02    LDY #$02
.B2DC  91 5F    STA ($5F),Y
.B2DE  A5 32    LDA $32
.B2E0  C8       INY
.B2E1  E5 60    SBC $60
.B2E3  91 5F    STA ($5F),Y
.B2E5  A5 0C    LDA $0C
.B2E7  D0 62    BNE $B34B
.B2E9  C8       INY
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B261**: Länge des Arraykopfs
- **$B264**: prüft auf genügend Platz
- **$B267**: Zeiger für Polynom-
- **$B269**: auswertung neu setzen
- **$B26B**: Wert für Variablenlänge(REAL)
- **$B26D**: erster Buchstabe des Namens
- **$B26F**: in Arraytabelle
- **$B271**: kein Integer?
- **$B273**: bei Integerzahl
- **$B274**: Bytes vermindern
- **$B275**: zweiter Buchstabe
- **$B277**: in Tabelle schreiben
- **$B279**: kein String oder Integer?
- **$B27B**: entgültige
- **$B27C**: Variablenlänge herstellen
- **$B27D**: und speichern (2, 3 oder 5)
- **$B27F**: Anzahl der Dimensionen holen
- **$B281**: Zeiger
- **$B282**: um 3
- **$B283**: erhöhen
- **$B284**: im Arrayheader speichern
- **$B286**: 11, Defaultwert für
- **$B288**: Dimensionierung
- **$B28A**: Aufruf durch DIM-Befehl?
- **$B28C**: nein: $B296
- **$B28E**: Dimension vom Stapel holen
- **$B28F**: Carry löschen (Addition)
- **$B290**: eins addieren
- **$B292**: und ins X-Reg.
- **$B293**: 2.Wert holen
- **$B294**: Übertrag addieren
- **$B296**: Zeiger erhöhen
- **$B297**: und speichern
- **$B299**: Zeiger erhöhen
- **$B29A**: 1.Wert wieder in den Akku
- **$B29B**: und ebenfalls speichern
- **$B29D**: Platz für Dimensionen berech.
- **$B2A0**: LOW- und HIGH-Byte des
- **$B2A2**: Variablenende-Zeigers merken
- **$B2A4**: Zeiger auf Arrayheader
- **$B2A6**: weitere Dimensionen?
- **$B2A8**: ja: $B286 (Schleifenbeginn)
- **$B2AA**: Feldlänge plus Startadresse
- **$B2AC**: Überlauf: 'OUT OF MEMORY'
- **$B2AE**: Wert wieder speichern
- **$B2B0**: und ins Y-Reg. bringen
- **$B2B1**: Variablenendzeiger in Akku
- **$B2B2**: 2.Zeichen addieren
- **$B2B4**: Überlauf: Platz prüfen
- **$B2B6**: Endadresse erhöhen
- **$B2B7**: Überlauf: 'OUT OF MEMORY'
- **$B2B9**: prüft auf Speicherplatz
- **$B2BC**: Zeiger auf Ende
- **$B2BE**: der Arraytabelle setzen
- **$B2C0**: Array mit Nullen füllen
- **$B2C2**: Schleifenzähler high um 1 erhöhen
- **$B2C4**: Schleifenzähler low
- **$B2C6**: wenn null: $B2CD
- **$B2C8**: Zeiger vermindern
- **$B2C9**: Nullwert setzen
- **$B2CB**: solang Y <>0: $B2C8
- **$B2CD**: High-Byte STA-Ziel verringern
- **$B2CF**: Schleifenzähler high verringern
- **$B2D1**: solang <>0: $B2C8
- **$B2D3**: High-Byte STA-Ziel erhöhen
- **$B2D5**: Carry setzen (Subtr.)
- **$B2D6**: Zeiger auf Feldende
- **$B2D8**: - Zeiger auf Arrayheader
- **$B2DA**: Zeiger setzen
- **$B2DC**: Arraylänge LOW
- **$B2DE**: Zeiger auf Feldende
- **$B2E0**: Zeiger erhöhen
- **$B2E1**: - Zeiger auf Arrayheader
- **$B2E3**: Arraylänge HIGH
- **$B2E5**: Aufruf vom DIM-Befehl?
- **$B2E7**: ja: RTS

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B261**: PUT ADDR OF 1ST ELEMENT IN ARYPNT
- **$B264**: MAKE SURE ENOUGH MEMORY LEFT
- **$B267**: POINT Y-REG AT VARIABLE NAME SLOT
- **$B269**: START SIZE COMPUTATION
- **$B26B**: ASSUME 5-BYTES PER ELEMENT
- **$B26D**: STUFF VARIABLE NAME IN ARRAY
- **$B271**: NOT INTEGER ARRAY
- **$B273**: INTEGER ARRAY, DECR. SIZE TO 4-BYTES
- **$B274**: POINT Y-REG AT NEXT CHAR OF NAME
- **$B275**: REST OF ARRAY NAME
- **$B279**: REAL ARRAY, STICK WITH SIZE = 5 BYTES
- **$B27B**: INTEGER OR STRING ARRAY, ADJUST SIZE
- **$B27C**: TO INTEGER=3, STRING=2 BYTES
- **$B27D**: STORE LOW-BYTE OF ARRAY ELEMENT SIZE
- **$B27F**: STORE NUMBER OF DIMENSIONS
- **$B281**: IN 5TH BYTE OF ARRAY
- **$B286**: DEFAULT DIMENSION = 11 ELEMENTS
- **$B288**: FOR HI-BYTE OF DIMENSION IF DEFAULT
- **$B28A**: DIMENSIONED ARRAY?
- **$B28C**: NO, USE DEFAULT VALUE
- **$B28E**: GET SPECIFIED DIM IN A,X
- **$B28F**: # ELEMENTS IS 1 LARGER THAN
- **$B290**: DIMENSION VALUE
- **$B296**: ADD THIS DIMENSION TO ARRAY DESCRIPTOR
- **$B29D**: MULTIPLY THIS DIMENSION BY RUNNING SIZE ((LOWTR)) * (STRNG2) --> A,X
- **$B2A0**: STORE RUNNING SIZE IN STRNG2
- **$B2A4**: RETRIEVE Y SAVED BY MULTIPLY.SUBSCRIPT
- **$B2A6**: COUNT DOWN # DIMS
- **$B2A8**: LOOP TILL DONE NOW A,X HAS TOTAL # BYTES OF ARRAY ELEMENTS
- **$B2AA**: COMPUTE ADDRESS OF END OF THIS ARRAY
- **$B2AC**: ...TOO LARGE, ERROR
- **$B2B7**: ...TOO LARGE, ERROR
- **$B2B9**: MAKE SURE THERE IS ROOM UP TO Y,A
- **$B2BC**: THERE IS ROOM SO SAVE NEW END OF TABLE
- **$B2BE**: AND ZERO THE ARRAY
- **$B2C2**: PREPARE FOR FAST ZEROING LOOP
- **$B2C4**: # BYTES MOD 256
- **$B2C6**: FULL PAGE
- **$B2C8**: CLEAR PAGE FULL
- **$B2CD**: POINT TO NEXT PAGE
- **$B2CF**: COUNT THE PAGES
- **$B2D1**: STILL MORE TO CLEAR
- **$B2D3**: RECOVER LAST DEC, POINT AT 1ST ELEMENT
- **$B2D6**: COMPUTE OFFSET TO END OF ARRAYS
- **$B2D8**: AND STORE IN ARRAY DESCRIPTOR
- **$B2E5**: WAS THIS CALLED FROM "DIM" STATEMENT?
- **$B2E7**: YES, WE ARE FINISHED
- **$B2E9**: NO, NOW NEED TO FIND THE ELEMENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*