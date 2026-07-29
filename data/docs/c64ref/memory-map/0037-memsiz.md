---
title: 'Pointer : Limit-of-memory'
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
  address: $0037
  address_end: $0038
  symbol: MEMSIZ
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Highest location in memory
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Dieser Zeiger gibt dem Interpreter an,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Highest Address Used by BASIC'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Pointer : Limit-of-memory'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The power-on/reset routine tests each byte of RAM until it comes
      to
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $A000, 40960.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Zeiger, in der Low-/High-Byte-Darstellung, gibt dem Basic-Übersetzer
      an,
  - name: 64map
    author: —
    description: 'Pointer: Highest Address available to BASIC ($A000)'
---

# MEMSIZ — Pointer : Limit-of-memory ($0037)

## Panoramica
Il registro o area di memoria MEMSIZ è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0037` (`55` decimale)
- **Range**: `$0037`-`$0038`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Highest location in memory

### Commodore-64-intern-Buch (Commodore)
Dieser Zeiger gibt dem Interpreter an,
welches die höchste von BASIC
verwendbare Speicheradresse ist.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Highest Address Used by BASIC

### Memory Map (Jim Butterfield)
Pointer : Limit-of-memory

### Mapping the Commodore 64 (Sheldon Leemon)
The power-on/reset routine tests each byte of RAM until it comes to
the BASIC ROM, and sets this pointer to the address of the highest byte
of consecutive RAM found (40959, $9FFF).

There are two circumstances under which this pointer may be changed
after power-up to reflect an address lower than the actual top of
consecutive RAM:

1.  Users may wish to lower this pointer themselves, in order to set
aside an area of free RAM that will not be disturbed by BASIC.  For
example, to set aside a 1K area at the top of BASIC, start your
program with the line:

        POKE 56,PEEK(56)-4:CLR

The CLR is necessary to insure that the string text will start below
your safe area.

You may wish to store machine language programs, sprites, or alternate
character sets in such an area.  For the latter two applications,
however, keep in mind the 16K addressing range limitation of the
VIC-II chip.  If you do not assign the VIC-II to a bank other than the
default memory bank of 0-16383 ($0-$3FFF), you must lower the top of
memory below 16383 ($3FFF) if you wish your sprite or character data
area to be within its addressing range.

2.  Then the RS-232 device (number 2) is opened, this pointer and the
pointer to the end of user RAM at 643 are lowered by 512 bytes in
order to create two 256-byte buffers, one for input and the other for
output.

Since the contents of these buffers will overwrite any variables at
the top of memory, a CLR command is issued at the time device 2 is
opened.  Therefore, the RS-232 device should be opened before defining
any variables, and before setting aside a safe area for machine
language programs or other uses, as described above.

### Reference (Joe Forster / STA)
Default: $A000, 40960.

### 64'er Magazin (64'er)
Dieser Zeiger, in der Low-/High-Byte-Darstellung, gibt dem Basic-Übersetzer an,
welches die höchste von Basic verwendbare Speicheradresse ist. Wie aus Bild 5
ersichtlich, ist diese Adresse zugleich der Anfang der als Variable
abgespeicherten Zeichenkette (Strings).

Normalerweise ist diese Adresse fest vorgegeben. Die folgende Tabelle 4 gibt
darüber Auskunft:

Tabelle 4: Ende des Programmspeichers

|                   | Adresse | Zeiger in 55 56 |
|-------------------|---------|-----------------|
| C 64              | 40960   | 0160            |
| VC 20 (Grundv.)   | 7680    | 030             |
| VC 20 (+3 KByte)  | 7680    | 030             |
| VC 20 (+8 KByte)  | 16384   | 064             |
| VC 20 (+16 KByte) | 24576   | 096             |
| VC 20 (+24 KByte) | 32768   | 0128            |

Beim Einschalten des Computers überprüft das Betriebssystem den gesamten RAM-
Speicher, bis es zur ersten ROM-Speicherzelle kommt, setzt den Zeiger in 55 und
56 auf diese Adresse und druckt den bekannten Kopf mit der verfügbaren
Speicherangabe auf den Bildschirm.

Normalerweise wird dieser Zeiger nicht geändert.

Es gibt aber zwei Gelegenheiten, bei denen eine Änderung dieses Zeigers
sinnvoll beziehungsweise notwendig ist.

##### Anwendung 1:

Es kommt oft vor, daß der gesamte Speicher nicht ausschließlich für Basic
benötigt wird, sondern daß ein freier Speicherbereich geschaffen wird, um zum
Beispiel Maschinenprogramme, selbst definierte Zeichen oder hochaufgelöste
Grafik unterzubringen, die aber nicht vom Basic-Programm überschrieben werden
können.

Bei der Besprechung der Zeiger in 43 und 44 haben wir das auch schon gemacht,
allerdings durch »Hochschieben« des Speicheranfangs. Mit dem Zeiger in 55 und
56 erreichen wir denselben Effekt, diesmal durch »Herunterdrücken« des
Speicherendes. Gegenüber den vier Schritten beim Hochschieben ist das
Herunterdrücken einfacher. Mit dem Befehl:

    POKE 56,PEEK(56)-1:CLR

schieben wir das Speicherende um 256 Byte nach unten, egal für welchen Computer
und welche Speichererweiterung. Mit -2 verschiebt sich das Ende um 512, mit-4
um 1024 Byte (also 1 KByte) nach unten. Wenn Sie eine feinere Verschiebung als
Vielfache von 256 benötigen, kommen Sie mit dem High-Byte in 56 allein nicht
aus, sondern Sie müssen auch einen entsprechenden Wert in 55 hineinPOKEn.

Der Befehl CLR ist notwendig, denn er setzt den Zeiger der Zellen 51 und 52
(siehe dort), das heißt das untere Ende des Speicherbereichs für Zeichenketten
auf dieselbe Adresse wie Zeiger 55 und 56. Dadurch wird erzwungen, daß die
Zeichenkette sozusagen als Ausgangslage unterhalb des heruntergedrückten
Speicherendes abgelegt wird.

##### Anwendung 2:

Über den User-Port (Steckerleiste an der Rückseite, neben dem Datasetten-
Anschluß) können VC 20 und C 64 mit anderen Geräten verbunden werden. Der
Datentransfer über diese Verbindung - sie heißt RS232-Schnittstelle - muß
allerdings programmiert werden. Diese RS232-Schnittstelle hat die Gerätenummer
2 (so wie der Drucker Nummer 4 und das Diskettengerät die Nummer 8 hat).

Wenn nun ein Gerät Nummer 2 mit einem OPEN-Befehl angewählt wird, wird
automatisch der Zeiger in 55 und 56 und der Zeiger in 643 um 512 Byte
heruntergedrückt, um je einen Eingangs- und Ausgangspufferspeicher zu erzeugen.
Da der Inhalt dieser Pufferspeicher alle Variable in diesen 512 Byte
überschreiben würde, wird auch der CLR-Befehl automatisch gegeben.

Es gilt daher als Vorschrift, daß bei RS232-Verbindungen zuerst der Datenkanal
durch OPEN eröffnet werden muß, bevor Variable, Felder und Zeichenketten
definiert werden.

### 64map (—)
Pointer: Highest Address available to BASIC ($A000)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*