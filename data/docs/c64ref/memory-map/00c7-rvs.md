---
title: Screen reverse flag
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
  address: $00C7
  symbol: RVS
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: RVS field on flag
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzelle gibt an, ob die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: Reverse Chars. - 1=Yes, 0=No Used'
  - name: Memory Map
    author: Jim Butterfield
    description: Screen reverse flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: When the [CTRL][RVS-ON] characters are printer (CHR$(18)), this flag
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Normalerweise steht in dieser Speicherzelle eine 0, was mit PRINT
      PEEK(199)
  - name: 64map
    author: —
    description: 'Flag: Reverse On/Off; On = $01, Off = $00'
---

# RVS — Screen reverse flag ($00C7)

## Panoramica
Il registro o area di memoria RVS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00C7` (`199` decimale)
- **Range**: `$00C7`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
RVS field on flag

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzelle gibt an, ob die
auszugebenden Zeichen revers oder
normal dargestellt werden sollen
(0= normal, 1= revers).

### C64 Programmer's Reference Guide (Commodore)
Flag: Reverse Chars. - 1=Yes, 0=No Used

### Memory Map (Jim Butterfield)
Screen reverse flag

### Mapping the Commodore 64 (Sheldon Leemon)
When the [CTRL][RVS-ON] characters are printer (CHR$(18)), this flag
is set to 18 ($12), and the print routines will add 128 ($80) to the
screen code of each character which is printed, so that the character
will appear on the screen with its colors reversed.

POKEing this location directly with a nonzero number will achieve the
same results.  You should remember, however, that the contents of this
location are returned to 0 not only upon entry of a [CTRL][RVS-OFF]
character (CHR$(146)), but also at every carriage return.  When this
happens, characters printed thereafter appear with the normal
combination of colors.

### Reference (Joe Forster / STA)
Values:

* $00: Normal mode.
* $12: Reverse mode.

### 64'er Magazin (64'er)
Normalerweise steht in dieser Speicherzelle eine 0, was mit PRINT PEEK(199)
leicht nach geprüft werden kann.

Sobald in der Zelle 199 eine andere Zahl als 0 steht, werden alle Zeichen in
der reversen Darstellung gedruckt. Das Betriebssystem des Computers erhöht
nämlich in diesem Fall den jeweiligen Bildschirmcode der Zeichen um 128. Ein
Blick in eine Tabelle der Biidschirmcodes bestätigt, daß die Codes aller
reversen Zeichen um genau 128 höher sind als die der normalen Zeichen.

Den reversen Modus können wir bekanntlich direkt mit der Kombination der CTRL-
und der RVS-ON-Taste oder aber mit PRINT CHR$(18) herstellen. Wenn Sie aber
versuchen sollten, das direkt einzugeben, um dann wieder mit PRINT PEEK(199)
nachzuschauen, was jetzt in der Speicherzelle 199 steht, dann werden Sie
Schiffbruch erleiden. Das Betriebssystem setzt den Inhalt der Zelle 199 nach
einem »Wagenrücklauf«, hervorgerufen zum Beispiel durch die RETURN-Taste oder
nach einem PRINT-Befehl, der nicht mit einem Komma oder Semikolon abgeschlossen
ist, sogleich auf 0 zurück. Natürlich erfolgt das auch durch Drücken der CTRL-
und RVS-OFF-Taste.

Wir vermeiden die Rücksetzung durch einen Einzeiler:

    PRINT CHR$(18) "AAA" PEEK(199)

Wir erhalten drei reverse As und als Inhalt der Zelle 199auch die Zahl 18.
Dasselbe Ergebnis erhalten wir durch POKEn einer Zahl größer als 0 in die Zelle
199:

    POKE 199,4: PRINT"XX" PEEK(199)

Das Ergebnis beweist, daß diese Adresse sehr nützlich sein kann, zumal ihre
Abfrage beziehungsweise Beeinflussung auch innerhalb eines Programms erfolgen
kann.

### 64map (—)
Flag: Reverse On/Off; On = $01, Off = $00

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*