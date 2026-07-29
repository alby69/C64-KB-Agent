---
title: 'Pointer : temporary strg stack'
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
- zero-page
difficulty: beginner
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - original_source_comments.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $0016
  symbol: TEMPPT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Initialized to point to TEMPST.
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Die Speicherzelle $0016 zeigt auf den
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Pointer Temporary String
  - name: Memory Map
    author: Jim Butterfield
    description: 'Pointer : temporary strg stack'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the next available slot in the temporary
  - name: Reference
    author: Joe Forster / STA
    description: 'Values: $19; $1C; $1F; $22.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Zeiger bezieht sich in seiner Wirkung auf die übernächsten
  - name: 64map
    author: —
    description: 'Pointer: Temporary String Stack'
---

# TEMPPT — Pointer : temporary strg stack ($0016)

## Panoramica
Il registro o area di memoria TEMPPT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0016` (`22` decimale)
- **Range**: `$0016`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Initialized to point to TEMPST.

### Commodore-64-intern-Buch (Commodore)
Die Speicherzelle $0016 zeigt auf den
nächsten freien Speicherplatz im
Stringstack.

### C64 Programmer's Reference Guide (Commodore)
Pointer Temporary String

### Memory Map (Jim Butterfield)
Pointer : temporary strg stack

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the next available slot in the temporary
string descriptor stack located at 25-33 ($0019-$0021).  Since that stack
has room for three descriptors of three bytes each, this location will
point to 25 ($0019) if the stack is empty, to 28 ($001C) if there is one
entry, to 31 ($001F) if there are two entries, and to 34 ($0022) if the
stack is full.

If BASIC needs to add an entry to the temporary string descriptor
stack, and this location holds a 34, indicating that the stack is
full, the FORMULA TOO COMPLEX error message is issued.  Otherwise, the
entry is added, and three is added to this pointer.

### Reference (Joe Forster / STA)
Values: $19; $1C; $1F; $22.

Default: $19.

### 64'er Magazin (64'er)
Dieser Zeiger bezieht sich in seiner Wirkung auf die übernächsten
Speicherzellen 25 bis 33 ($0019 bis $0021).

Diese werden als Stapelspeicher (Stack) für Angaben über vorläufige
Zeichenketten - auf englisch »Temporary String Descriptor« - verwendet.

Die Speicherzelle 22 ($0016) ihrerseits enthält einen Zeiger auf den jeweils
nächsten verfügbaren Platz in diesem Speicher ab Zelle 25. Da er eine Kapazität
von 3 * 3 Byte hat, zeigt der Zeiger auf die Zelle 25 ($0019), wenn er leer ist.
Bei einem Eintrag zeigt er auf 28 ($001C), bei zwei Einträgen auf 31 ($001F) und
schließlich auf 34 ($0022), wenn der Speicher voll ist.

Eine Zeichenkette ist dann »vorläufig«, wenn sie noch nicht einer
Stringvariablen zugeordnet worden ist, zum Beispiel »Mahlzeit« in dem Basic-
Befehl

    PRINT "MAHLZEIT".

Beim Einschalten setzt das Betriebssystem mit der Einschaltroutine ab Adresse
58303 ($E3BF) im C 64, beim VC 20 ab 58276 ($E3A4) den Zeigerauf 25. Die
Stringverwaltungsroutine ab 46215 ($B487) im C 64 beziehungsweise ab 54407
($D487) im VC 20 fragt bei String-Eingaben die Flagge ab. Nach jeder Eintragung
in den Speicher ab Zelle 25 wird der Zeiger um 3 weitergesetzt.

Sie können die Leerflagge 25 mit

    PRINT PEEK (22)

leicht nachprüfen.

Die anderen Eintragungen können nicht nachgeprüft werden, weil sie sofort auf
25 zurückgesetzt werden.

Wir können sie aber durch POKE beeinflussen; ob das sinnvoll ist, ist eine
andere Frage.

    10 POKE 22,34
    20 PRINT "MAHLZEIT"

Die Zahl 34 in Zelle 22 sagt dem Programm, daß der Speicher ab Zelle 25 voll
ist. Wir bekommen statt der MAHLZEIT eine Fehlermeldung serviert.

Mit einem POKE-Befehl, der als Argument die für den vorgesehenen Zweck
ungültige Zahl 35 verwendet:

    POKE 22,35

erreichen wir allerdings zwei interessante »Dreckeffekte«. Zum einen
unterdrückt der Befehl die Ausgabe des READY, zum anderen aber bewirkt er, daß
bei LIST ein Listing ohne Zeilennummern ausgedruckt wird, sowohl auf dem
Bildschirm als auch mit dem Drucker.

#### Das billigste editierfähige Textverarbeitungssystem

Die Idee dazu habe ich von Mike Apsey’s Hinweis in »Commodore User« Juli 1984.
Mit Zeilennummern versehen, läßt sich jeder beliebige Text schreiben,
verbessern, verschieben, abspeichern, aber nicht RUNen!!

Der POKE-Befehl von oben (POKE 22,35) gefolgt von einem CMD und LIST, druckt
dann alles brav als reinen Text aus. Die maximale Zeilenlänge entspricht der
Zeilenlänge des jeweiligen Computers.

Probieren Sie es aus:

    10 DER COMPUTER BIETET IN DER
    20 DATENFERNÜBERTRAGUNG
    30 UNGEAHNTE MÖGLICHKEITEN.
    40 ABER DIE GEFAHR
    50 USW. USW.
    60:

Jede Zeile wird mit der RETURN-Taste abgeschlossen. Damit auch alles gedruckt
wird, muß - zumindest bei meinem Drucker (1526) - eine »Leerzeile« folgen
(Zeile 60). Mit

    POKE 22,35:OPEN 1,4:CMD 1:LIST

wird der Text ohne Zeilennummern ausgedruckt. Sie können ihn vorher nach
Belieben verändern.

Wie gesagt, nur nicht mit RUN starten, denn das bringt unweigerlich eine
Fehlermeldung.

### 64map (—)
Pointer: Temporary String Stack

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*