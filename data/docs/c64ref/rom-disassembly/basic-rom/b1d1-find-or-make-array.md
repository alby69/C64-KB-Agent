---
title: find or make array
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
- b1d1-dimensionierte-variable-holen
- b218-search-array-table-for-this-array-name
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B1D1
  address_end: $B243
  symbol: find-or-make-array
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B1D1**: get DIM flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B1D1**: DIM Flag'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B205**: comma'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B1D1**: YES'
---

# $B1D1 — find or make array

## Disassemblatura
```assembly
.B1D1  A5 0C    LDA $0C   ; get DIM flag
.B1D3  05 0E    ORA $0E   ; OR with data type flag
.B1D5  48       PHA   ; push it
.B1D6  A5 0D    LDA $0D   ; get data type flag, $FF = string, $00 = numeric
.B1D8  48       PHA   ; push it
.B1D9  A0 00    LDY #$00   ; clear dimensions count now get the array dimension(s) and stack it (them) before the data type and DIM flag
.B1DB  98       TYA   ; copy dimensions count
.B1DC  48       PHA   ; save it
.B1DD  A5 46    LDA $46   ; get array name 2nd byte
.B1DF  48       PHA   ; save it
.B1E0  A5 45    LDA $45   ; get array name 1st byte
.B1E2  48       PHA   ; save it
.B1E3  20 B2 B1 JSR $B1B2   ; evaluate integer expression
.B1E6  68       PLA   ; pull array name 1st byte
.B1E7  85 45    STA $45   ; restore array name 1st byte
.B1E9  68       PLA   ; pull array name 2nd byte
.B1EA  85 46    STA $46   ; restore array name 2nd byte
.B1EC  68       PLA   ; pull dimensions count
.B1ED  A8       TAY   ; restore it
.B1EE  BA       TSX   ; copy stack pointer
.B1EF  BD 02 01 LDA $0102,X   ; get DIM flag
.B1F2  48       PHA   ; push it
.B1F3  BD 01 01 LDA $0101,X   ; get data type flag
.B1F6  48       PHA   ; push it
.B1F7  A5 64    LDA $64   ; get this dimension size high byte
.B1F9  9D 02 01 STA $0102,X   ; stack before flag bytes
.B1FC  A5 65    LDA $65   ; get this dimension size low byte
.B1FE  9D 01 01 STA $0101,X   ; stack before flag bytes
.B201  C8       INY   ; increment dimensions count
.B202  20 79 00 JSR $0079   ; scan memory
.B205  C9 2C    CMP #$2C   ; compare with ","
.B207  F0 D2    BEQ $B1DB   ; if found go do next dimension
.B209  84 0B    STY $0B   ; store dimensions count
.B20B  20 F7 AE JSR $AEF7   ; scan for ")", else do syntax error then warm start
.B20E  68       PLA   ; pull data type flag
.B20F  85 0D    STA $0D   ; restore data type flag, $FF = string, $00 = numeric
.B211  68       PLA   ; pull data type flag
.B212  85 0E    STA $0E   ; restore data type flag, $80 = integer, $00 = float
.B214  29 7F    AND #$7F   ; mask dim flag
.B216  85 0C    STA $0C   ; restore DIM flag
.B218  A6 2F    LDX $2F   ; set end of variables low byte (array memory start low byte)
.B21A  A5 30    LDA $30   ; set end of variables high byte (array memory start high byte) now check to see if we are at the end of array memory, we would be if there were no arrays.
.B21C  86 5F    STX $5F   ; save as array start pointer low byte
.B21E  85 60    STA $60   ; save as array start pointer high byte
.B220  C5 32    CMP $32   ; compare with end of arrays high byte
.B222  D0 04    BNE $B228   ; branch if not reached array memory end
.B224  E4 31    CPX $31   ; else compare with end of arrays low byte
.B226  F0 39    BEQ $B261   ; go build array if not found search for array
.B228  A0 00    LDY #$00   ; clear index
.B22A  B1 5F    LDA ($5F),Y   ; get array name first byte
.B22C  C8       INY   ; increment index to second name byte
.B22D  C5 45    CMP $45   ; compare with this array name first byte
.B22F  D0 06    BNE $B237   ; branch if no match
.B231  A5 46    LDA $46   ; else get this array name second byte
.B233  D1 5F    CMP ($5F),Y   ; compare with array name second byte
.B235  F0 16    BEQ $B24D   ; array found so branch no match
.B237  C8       INY   ; increment index
.B238  B1 5F    LDA ($5F),Y   ; get array size low byte
.B23A  18       CLC   ; clear carry for add
.B23B  65 5F    ADC $5F   ; add array start pointer low byte
.B23D  AA       TAX   ; copy low byte to X
.B23E  C8       INY   ; increment index
.B23F  B1 5F    LDA ($5F),Y   ; get array size high byte
.B241  65 60    ADC $60   ; add array memory pointer high byte
.B243  90 D7    BCC $B21C   ; if no overflow go check next array
```


## Commenti

### Original Disassembly (—)
- **$B1D1**: get DIM flag
- **$B1D3**: OR with data type flag
- **$B1D5**: push it
- **$B1D6**: get data type flag, $FF = string, $00 = numeric
- **$B1D8**: push it
- **$B1D9**: clear dimensions count now get the array dimension(s) and stack it (them) before the data type and DIM flag
- **$B1DB**: copy dimensions count
- **$B1DC**: save it
- **$B1DD**: get array name 2nd byte
- **$B1DF**: save it
- **$B1E0**: get array name 1st byte
- **$B1E2**: save it
- **$B1E3**: evaluate integer expression
- **$B1E6**: pull array name 1st byte
- **$B1E7**: restore array name 1st byte
- **$B1E9**: pull array name 2nd byte
- **$B1EA**: restore array name 2nd byte
- **$B1EC**: pull dimensions count
- **$B1ED**: restore it
- **$B1EE**: copy stack pointer
- **$B1EF**: get DIM flag
- **$B1F2**: push it
- **$B1F3**: get data type flag
- **$B1F6**: push it
- **$B1F7**: get this dimension size high byte
- **$B1F9**: stack before flag bytes
- **$B1FC**: get this dimension size low byte
- **$B1FE**: stack before flag bytes
- **$B201**: increment dimensions count
- **$B202**: scan memory
- **$B205**: compare with ","
- **$B207**: if found go do next dimension
- **$B209**: store dimensions count
- **$B20B**: scan for ")", else do syntax error then warm start
- **$B20E**: pull data type flag
- **$B20F**: restore data type flag, $FF = string, $00 = numeric
- **$B211**: pull data type flag
- **$B212**: restore data type flag, $80 = integer, $00 = float
- **$B214**: mask dim flag
- **$B216**: restore DIM flag
- **$B218**: set end of variables low byte (array memory start low byte)
- **$B21A**: set end of variables high byte (array memory start high byte) now check to see if we are at the end of array memory, we would be if there were no arrays.
- **$B21C**: save as array start pointer low byte
- **$B21E**: save as array start pointer high byte
- **$B220**: compare with end of arrays high byte
- **$B222**: branch if not reached array memory end
- **$B224**: else compare with end of arrays low byte
- **$B226**: go build array if not found search for array
- **$B228**: clear index
- **$B22A**: get array name first byte
- **$B22C**: increment index to second name byte
- **$B22D**: compare with this array name first byte
- **$B22F**: branch if no match
- **$B231**: else get this array name second byte
- **$B233**: compare with array name second byte
- **$B235**: array found so branch no match
- **$B237**: increment index
- **$B238**: get array size low byte
- **$B23A**: clear carry for add
- **$B23B**: add array start pointer low byte
- **$B23D**: copy low byte to X
- **$B23E**: increment index
- **$B23F**: get array size high byte
- **$B241**: add array memory pointer high byte
- **$B243**: if no overflow go check next array

### Commodore-64-intern-Buch (Commodore)
- **$B1D1**: DIM Flag
- **$B1D3**: Integer Flag
- **$B1D5**: auf Stapel retten
- **$B1D6**: String Flag
- **$B1D8**: auf Stapel retten
- **$B1D9**: Anzahl der Indizes
- **$B1DB**: in Akku und
- **$B1DC**: auf Stapel retten
- **$B1DD**: 2. Buchstabe des Variablenn.
- **$B1DF**: und retten
- **$B1E0**: 1. Buchstabe der Variablenn.
- **$B1E2**: retten
- **$B1E3**: Index holen und nach Integer
- **$B1E6**: die zwei
- **$B1E7**: Bytes des
- **$B1E9**: Variablennamens zurückholen
- **$B1EA**: und wieder abspeichern
- **$B1EC**: Anzahl der Indizes
- **$B1ED**: holen und ins Y-Reg.
- **$B1EE**: Stapelzeiger als Zeiger setzen
- **$B1EF**: Variablenflags
- **$B1F2**: aus dem Stapel kopieren
- **$B1F3**: und oben auf den
- **$B1F6**: Stapel legen
- **$B1F7**: anstelle der
- **$B1F9**: Variablenflags
- **$B1FC**: Index LOW und HIGH in
- **$B1FE**: den Stapel kopieren
- **$B201**: Anzahl der Indizes erhöhen
- **$B202**: CHRGOT letztes Zeichen holen
- **$B205**: ',' Komma?
- **$B207**: ja: dann nächsten Index
- **$B209**: Anzahl der Indizes speichern
- **$B20B**: prüft auf Klammer zu
- **$B20E**: Flags vom
- **$B20F**: Stapel
- **$B211**: zurückholen
- **$B212**: und abspeichern
- **$B214**: Integerflag herstellen
- **$B216**: und abspeichern
- **$B218**: LOW- und HIGH-Byte des
- **$B21A**: Zeigers auf Arraytabelle
- **$B21C**: holen und
- **$B21E**: Zeiger merken
- **$B220**: Ende erreicht?
- **$B222**: nein: weiter
- **$B224**: mit Tabellenende vergleichen
- **$B226**: ja: nicht gefunden, anlegen
- **$B228**: Zeiger setzen
- **$B22A**: Namen aus Tabelle holen
- **$B22C**: Zeiger erhöhen
- **$B22D**: mit ges. Namen vergleichen
- **$B22F**: ungleich: $B237
- **$B231**: Vergleich mit
- **$B233**: zweitem Buchstaben
- **$B235**: gefunden: $B24D
- **$B237**: Zeiger erhöhen
- **$B238**: Suchzeiger zur
- **$B23A**: Feldlänge
- **$B23B**: Addieren
- **$B23D**: ergibt Zeiger auf
- **$B23E**: nächstes Array
- **$B23F**: gleiches System
- **$B241**: mit zweitem Byte
- **$B243**: und weiter suchen
- **$B245**: Nummer für 'bad subscript'
- **$B248**: Nummer für 'illegal quanti.'
- **$B24A**: Fehlermeldung ausgeben
- **$B24D**: Nummer für 'redim'd array'
- **$B24F**: DIM-Flag null?
- **$B251**: nein: dann Fehlermeldung
- **$B253**: Zeiger auf 1.Arrayelement
- **$B256**: Zahl der gefundenen Dimensio.
- **$B258**: Zeiger setzen
- **$B25A**: mit Dimensionen des Arrays vergleichen
- **$B25C**: ungleich: 'bad subscript'
- **$B25E**: sucht gewünschtes Element

### Marko Mäkelä (Marko Mäkelä)
- **$B205**: comma
- **$B245**: error number
- **$B248**: error number
- **$B24D**: error number

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B1D1**: YES
- **$B1D3**: SET HIGH BIT IF %
- **$B1D5**: SAVE VALTYP AND DIMFLG ON STACK
- **$B1D9**: COUNT # DIMENSIONS IN Y-REG
- **$B1DB**: SAVE #DIMS ON STACK
- **$B1DD**: SAVE VARIABLE NAME ON STACK
- **$B1E3**: EVALUATE SUBSCRIPT AS INTEGER
- **$B1E6**: RESTORE VARIABLE NAME
- **$B1EC**: RESTORE # DIMS TO Y-REG
- **$B1EE**: COPY VALTYP AND DIMFLG ON STACK
- **$B1EF**: TO LEAVE ROOM FOR THE SUBSCRIPT
- **$B1F7**: GET SUBSCRIPT VALUE AND PLACE IN THE
- **$B1F9**: STACK WHERE VALTYP &amp; DIMFLG WERE
- **$B201**: COUNT THE SUBSCRIPT
- **$B202**: NEXT CHAR
- **$B207**: COMMA, PARSE ANOTHER SUBSCRIPT
- **$B209**: NO MORE SUBSCRIPTS, SAVE #
- **$B20B**: NOW NEED ")"
- **$B20E**: RESTORE VALTYPE AND DIMFLG
- **$B214**: ISOLATE DIMFLG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*