---
title: perform READ
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
- 00a9-rez
- 00d7-data
- ac06-basic-befehl-read
- bit
- input
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AC06
  address_end: $AC0D
  symbol: perform-read
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AC06**: get DATA pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AC06**: DATA-Zeiger nach'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AC0A**: READ code'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AC06**: Y,X POINTS AT NEXT DATA STATEMENT'
---

# $AC06 — perform READ

## Disassemblatura
```assembly
.AC06  A6 41    LDX $41   ; get DATA pointer low byte
.AC08  A4 42    LDY $42   ; get DATA pointer high byte
.AC0A  A9 98    LDA #$98   ; set input mode = READ
.AC0C  2C       .BYTE $2C   ; makes next line BIT $00A9
.AC0D  A9 00    LDA #$00   ; set input mode = INPUT
```


## Commenti

### Original Disassembly (—)
- **$AC06**: get DATA pointer low byte
- **$AC08**: get DATA pointer high byte
- **$AC0A**: set input mode = READ
- **$AC0C**: makes next line BIT $00A9
- **$AC0D**: set input mode = INPUT

### Commodore-64-intern-Buch (Commodore)
- **$AC06**: DATA-Zeiger nach
- **$AC08**: $41/42 holen
- **$AC0A**: READ-Flag
- **$AC0D**: Flagwert laden
- **$AC0F**: und INPUT-Zeiger setzen
- **$AC11**: INPUT-Zeiger auf
- **$AC13**: Eingabequelle setzen
- **$AC15**: sucht Variable
- **$AC18**: Variablenadresse
- **$AC1A**: speichern
- **$AC1C**: LOW- und HIGH-Byte des
- **$AC1E**: Programmzeigers
- **$AC20**: in $4B/$4C
- **$AC22**: Zwischenspeichern
- **$AC24**: INPUT-Zeiger
- **$AC26**: (LOW und HIGH)
- **$AC28**: als Programmzeiger
- **$AC2A**: abspeichern
- **$AC2C**: CHRGOT letztes Zeichen holen
- **$AC2F**: Endzeichen? nein: $AC51
- **$AC31**: Eingabeflag
- **$AC33**: kein GET: $AC41
- **$AC35**: GETIN
- **$AC38**: Zeichen in Puffer schreiben
- **$AC3B**: Zeiger auf
- **$AC3D**: Puffer setzen
- **$AC3F**: unbedingter Sprung
- **$AC41**: READ: $ACB8
- **$AC43**: Eingabegerät holen
- **$AC45**: nicht Tastatur: $AC4A
- **$AC47**: Fragezeichen ausgeben
- **$AC4A**: zweites Fragezeichen ausgeben
- **$AC4D**: Programmzeiger setzen
- **$AC4F**: (LOW und HIGH)
- **$AC51**: CHRGET nächstes Zeichen holen
- **$AC54**: Typ-Flag
- **$AC56**: kein String: $AC89
- **$AC58**: Eingabeflag
- **$AC5A**: kein GET: $AC65
- **$AC5C**: Programmzeiger erhöhen
- **$AC5D**: und neu setzen ($0200)
- **$AC5F**: Wert laden und
- **$AC61**: Trennzeichen setzen
- **$AC63**: unbedingter Sprung
- **$AC65**: nächstes Zeichen
- **$AC67**: '"' Hochkomma?
- **$AC69**: ja: $AC72
- **$AC6B**: ':' Doppelpunktcode laden
- **$AC6D**: und abspeichern
- **$AC6F**: ',' Kommacode (Endzeichen
- **$AC71**: für Stringübertragung)
- **$AC72**: abspeichern
- **$AC74**: Programmzeiger laden
- **$AC76**: (LOW und HIGH)
- **$AC78**: und Übertrag addieren
- **$AC7A**: C = 0: $AC7D
- **$AC7C**: bei "'" um 1 erhöhen
- **$AC7D**: String übernehmen
- **$AC80**: Programmzeiger hinter String
- **$AC83**: String an Variable zuweisen
- **$AC86**: weiter machen
- **$AC89**: Ziffernstring in FAC holen
- **$AC8C**: INTEGER/REAL-Flag
- **$AC8E**: FAC an numerische Variable
- **$AC91**: CHRGOT: letztes Zeichen holen
- **$AC94**: Ende?
- **$AC96**: ',' Code?
- **$AC98**: ja: $AC9D
- **$AC9A**: zur Fehlerbehandlung
- **$AC9D**: Programmzeiger
- **$AC9F**: holen und
- **$ACA1**: in DATA-Zeiger
- **$ACA3**: abspeichern
- **$ACA5**: ursprüngliche
- **$ACA7**: Programmzeiger
- **$ACA9**: wieder zurückholen
- **$ACAB**: und speichern
- **$ACAD**: CHRGOT: letztes Zeichen holen
- **$ACB0**: Trennzeichen: $ACDF
- **$ACB2**: CKCOM: prüft auf Komma
- **$ACB5**: weiter
- **$ACB8**: nächstes Statement suchen
- **$ACBB**: Offset erhöhen
- **$ACBC**: Zeilenende?
- **$ACBD**: nein: $ACD1
- **$ACBF**: 'OUT OF DATA' Code
- **$ACC1**: Zeiger erhöhen
- **$ACC2**: Programmende?
- **$ACC4**: ja: 'OUT OF DATA', X = 0
- **$ACC6**: Zeiger erhöhen
- **$ACC7**: Zeilennummer (LOW) holen
- **$ACC9**: und abspeichern
- **$ACCB**: Zeiger erhöhen
- **$ACCC**: Zeilenummer (HIGH)
- **$ACCE**: Zeiger erhöhen
- **$ACCF**: Zeilennummer speichern
- **$ACD1**: Programmz. auf Statement
- **$ACD4**: CHRGOT letztes Zeichen holen
- **$ACD7**: und ins X-Reg.
- **$ACD8**: 'DATA' Code?
- **$ACDA**: nein: weitersuchen
- **$ACDC**: Daten lesen
- **$ACDF**: LOW- und HIGH-Byte des
- **$ACE1**: Input-Zeigers
- **$ACE3**: Eingabe-Flag
- **$ACE5**: kein DATA: $ACEA
- **$ACE7**: DATA-Zeiger setzen
- **$ACEA**: Zeiger setzen
- **$ACEC**: nächstes Zeichen holen
- **$ACEE**: Endzeichen: $ACFB
- **$ACF0**: Eingabe über Tastatur?
- **$ACF2**: nein: $ACFB
- **$ACF4**: Zeiger auf
- **$ACF6**: '?extra ignored' setzen
- **$ACF8**: String ausgeben
- **$ACFB**: Rücksprung
- **$ACFC**: '?extra ignored'
- **$AD0C**: '?redo from start'

### Marko Mäkelä (Marko Mäkelä)
- **$AC0A**: READ code
- **$AC67**: quote mark
- **$AC6B**: colon
- **$AC6F**: comma
- **$AC96**: comma
- **$ACBF**: error number
- **$ACD8**: DATA code
- **$ACF4**: low  ACFC
- **$ACF6**: high ACFC

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AC06**: Y,X POINTS AT NEXT DATA STATEMENT
- **$AC0A**: SET INPUTFLG = $98
- **$AC0D**: SET INPUTFLG = $00

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*