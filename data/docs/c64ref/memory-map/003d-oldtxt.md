---
title: 'Pointer : Basic statement for CONT'
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
  address: $003D
  address_end: $003E
  symbol: OLDTXT
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Points at statement to be exec'd next.
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Sobald eine neue BASIC-Zeile
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: BASIC Statement for CONT'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Pointer : Basic statement for CONT'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location contains the address (not the line number) of the text
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Die Abarbeitung der einzelnen Basic-Zeilen während eines Programmlaufs
      wird von
  - name: 64map
    author: —
    description: 'Pointer: BASIC Statement for CONT'
---

# OLDTXT — Pointer : Basic statement for CONT ($003D)

## Panoramica
Il registro o area di memoria OLDTXT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$003D` (`61` decimale)
- **Range**: `$003D`-`$003E`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Points at statement to be exec'd next.

### Commodore-64-intern-Buch (Commodore)
Sobald eine neue BASIC-Zeile
verarbeitet wird, holt sich das
Betriebssystem die aktuelle
Zeilennummer und speichert diese dann
in $003D-$003E als LOW- und HIGH-Byte ab.

### C64 Programmer's Reference Guide (Commodore)
Pointer: BASIC Statement for CONT

### Memory Map (Jim Butterfield)
Pointer : Basic statement for CONT

### Mapping the Commodore 64 (Sheldon Leemon)
This location contains the address (not the line number) of the text
of the BASIC statement that is being executed.  The value of TXTPTR
(122, $007A), the pointer tot he address of the BASIC text character
currently being scanned, is stored here each time a new BASIC line
begins execution.

END, STOP, and the STOP-key BREAK save the value of TXTPTR here, and
CONT restores this value to TXTPTR.  CONT will not continue if 62
($003E) has been changed to a zero by a LOAD, a modification to the
program text, or by error routines.

### Reference (Joe Forster / STA)
Values:

* $0000-$00FF: CONT'ing is not possible.
* $0100-$FFFF: Pointer to next BASIC instruction.

### 64'er Magazin (64'er)
Die Abarbeitung der einzelnen Basic-Zeilen während eines Programmlaufs wird von
einem kleinen Maschinencode-Programm, welches in den Speicherzellen 115 bis 138
steht (wir kommen noch dahin), gesteuert. In den Zellen 122 und 123 enthält es
die Adresse des letzten Bytes des gerade ausgeführten Basic-Befehls.

Sobald eine neue Basic-Zeile verarbeitet wird, holt das Betriebssystem diese
Adresse aus 122 und 123 und speichert sie in den hier zur Diskussion stehenden
Speicherzellen 61 und 62 ab, wie üblich als Low-/High-Byte.

Dasselbe geschieht bei jedem Befehl END, STOP, bei Fehlern mit dem Befehl INPUT
und durch das Drücken der STOP-Taste. Der Befehl CONT hingegen schaut in 61 und
62 nach und bringt die darin befindliche Adresse zurück in die Speicherzellen
122 und 123 zur Fortsetzung des Programms. Wenn aber in Zelle 62 inzwischen
eine 0 steht - und das geschieht bei einem LOAD-Befehl, durch Programm-Abbruch
mit Fehlermeldung und durch Eingabe neuer Basic-Zeilen beziehungsweise deren
Veränderungen mit abschließender RETURN-Taste - dann wird der CONT-Befehl nicht
ausgeführt.

Zur besseren Erklärung dieser in 61 und 62 als Zeiger stehenden Adresse einer
Basic-Zeile möchte ich Sie an den Texteinschub Nr. 7 erinnern, in dem ich den
Basic-Programmspeicher »sichtbar« gemacht habe, um die Wirkung der Verschiebung
des Zeigers in den Zellen 43 und 44 zu demonstrieren.

Wir nehmen dazu bitte noch einmal das kleine Demo-Programm für die Adressen 57
und 58 oben her und ersetzen die PEEK-Werte durch 61 und 62. Das Ausdrucken des
Inhalts von 61 und 62 legen wir aber an den Anfang jeder Zeile. Das Programm
sieht dann so aus:

    10 PRINT PEEK(61)+256*PEEK(62),"ZEILE 10"
    20 PRINT PEEK(61)+256*PEEK(62),:A=3:PRINT A
    30 PRINT PEEK(61)+256*PEEK(62),:B=5:PRINT B
    40 PRINT PEEK(61)+256*PEEK(62),A*B

Nach RUN erhalten wir jetzt auf der linken Seite Zahlen, die den jeweiligen
Basic-Speicher angeben, ab dem diese Zeile gespeichert ist. Wenn Sie ab diesen
Adressen mit der gerade erwähnten Methode aus Texteinschub Nr. 7 nachschauen,
finden Sie genau die Zeilen des kleinen Demo-Programms wieder.

Zur Anwendung dieses Zeigers kann ich wenig sagen. Ihn durch POKE zu verändern,
geht in Basic nicht, weil das Betriebssystem die richtigen Werte immer neu
eingibt. Man kann ihn allerdings abfragen, wenn man sich für die
Speicheradressen der Basic-Zeilen interessiert. Die einzige Anwendung dafür
kenne ich von S. Leemon, welche bei den Adressen 65 und 66 eingesetzt wird.

### 64map (—)
Pointer: BASIC Statement for CONT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*