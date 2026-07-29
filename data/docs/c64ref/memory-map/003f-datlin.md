---
title: Current DATA line number
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
related:
- 00d7-data
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
  address: $003F
  address_end: $0040
  symbol: DATLIN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: 'Data line # -- remember for errors'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese beiden Speicherzellen enthalten
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Current DATA Line Number
  - name: Memory Map
    author: Jim Butterfield
    description: Current DATA line number
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location holds the line number of the current DATA statement
  - name: Reference
    author: Joe Forster / STA
    description: BASIC line number of current DATA item for READ
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzellen enthalten die Nummer der Basic-Zeile, in der
      gerade ein
  - name: 64map
    author: —
    description: Current DATA Line number
---

# DATLIN — Current DATA line number ($003F)

## Panoramica
Il registro o area di memoria DATLIN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$003F` (`63` decimale)
- **Range**: `$003F`-`$0040`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Data line # -- remember for errors

### Commodore-64-intern-Buch (Commodore)
Diese beiden Speicherzellen enthalten
die Zeilennummer einer DATA-Zeile, die
gerade vom READ-Befehl ausgelesen
wird.

### C64 Programmer's Reference Guide (Commodore)
Current DATA Line Number

### Memory Map (Jim Butterfield)
Current DATA line number

### Mapping the Commodore 64 (Sheldon Leemon)
This location holds the line number of the current DATA statement
being READ.  It should be noted that this information is not used to
determine where the next DATA item is read from (that is the job of
the pointer at 65-66 ($0041-$0042) below).  But if an error concerning the
DATA occurs, this number will be moved to 57 ($0039), so that the error
message will show that the error occurred in the line that contains
the DATA statement, rather than in the line that contains the READ
statement.

### Reference (Joe Forster / STA)
BASIC line number of current DATA item for READ

### 64'er Magazin (64'er)
Diese Speicherzellen enthalten die Nummer der Basic-Zeile, in der gerade ein
DATA-Befehl mit READ gelesen wird. Sobald in einer DATA-Zeile ein Fehler
gefunden wird, kommt diese Zeilennummer aus 63 und 64 in die Speicherzellen 57
und 58, um in der Fehlermeldung die fehlerhafte DATA-Zeile und nicht die
laufende READ-Zeile anzuzeigen. Auf diese Weise werden Syntax-Fehler in einer
DATA-Zeile angezeigt. Um andere Fehler, wie zum Beispiel ein fehlendes Komma
zwischen zwei DATA-Angaben anzuzeigen, können die Speicherzellen 63 und 64
eingesetzt werden.

In dem folgenden Programm wird in Zeile 20 geprüft, ob die DATA-Angaben größer
als 255 sind. Da bei einem fehlenden Komma die beiden Zahlen als eine Zahl
gelesen werden, wird dieser Fall erkannt und mit einem F versehen die Nummer
der DATA-Zeile ausgedruckt, in der das Komma fehlt.

    10 FOR X=1 TO 10:READ A:PRINTA
    20 IF A>255 THEN PRINT "F" PEEK(63) + 256*PEEK(64)
    30 NEXT X
    40 DATA 10,20,30
    50 DATA 40,50,60
    60 DATA 70,80,90,100

Sie können jetzt in den DATA-Zeilen Kommafehler einbauen, die vom Programm
angezeigt werden. Ein anderer häufiger Fehler, nämlich ein Komma am Ende einer
DATA-Zeile, kann damit leider nicht erkannt werden. Aber vielleicht fällt Ihnen
eine Prüfformel dazu ein.

### 64map (—)
Current DATA Line number

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*