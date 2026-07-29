---
title: Current DATA address
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
  address: $0041
  address_end: $0042
  symbol: DATPTR
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Initialized to point
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier ist die Adresse aufgeführt, ab
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Pointer: Current DATA Item Address'
  - name: Memory Map
    author: Jim Butterfield
    description: Current DATA address
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location points to the address (not the line number) within
      the
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to next DATA item for READ
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzellen enthalten in der Low-/High-Byte-Darstellung
      die Adresse im
  - name: 64map
    author: —
    description: 'Pointer: Used by READ - current DATA Item Address'
---

# DATPTR — Current DATA address ($0041)

## Panoramica
Il registro o area di memoria DATPTR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0041` (`65` decimale)
- **Range**: `$0041`-`$0042`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Initialized to point
at the zero in front of [TXTTAB]
by "RESTORE" which is called by "CLEARC".
updated by execution of a "READ".

### Commodore-64-intern-Buch (Commodore)
Hier ist die Adresse aufgeführt, ab
welcher der READ-Befehl nach der
nächsten DATA-Zeile sucht.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Current DATA Item Address

### Memory Map (Jim Butterfield)
Current DATA address

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address (not the line number) within the
BASIC program text area where DATA is currently being READ.  RESTORE
sets this pointer back to the address indicated by the start of BASIC
pointer at location 43 ($002B).

The sample program below shows how the order in which DATA statements
are READ can be changed using this pointer.  The current address of
the statement before the DATA statement is stored in a variable, and
then used to change this pointer.

    10 A1=PEEK(61):A2=PEEK(62)
    20 DATA THIS DATA WILL BE USED SECOND
    30 B1=PEEK(61):B2=PEEK(62)
    40 DATA THIS DATA WILL BE USED FIRST
    50 C1=PEEK(61):C2=PEEK(62)
    60 DATA THIS DATA WILL BE USED THIRD
    70 POKE 65,B1:POKE 66,B2:READ A$:PRINT A$
    80 POKE 65,A1:POKE 66,A2:READ A$:PRINT A$
    90 POKE 65,C1:POKE 66,C2:READ A$:PRINT A$

### Reference (Joe Forster / STA)
Pointer to next DATA item for READ

### 64'er Magazin (64'er)
Diese Speicherzellen enthalten in der Low-/High-Byte-Darstellung die Adresse im
Basic-Programmspeicher, ab welcher der READ-Befehl nach der nächsten DATA-Zeile
sucht.

Zu Beginn eines Programms steht in 65 und 66 als Adresse der Beginn des Basic-
Speichers, also derselbe Wert wie in den Speicherzellen 43 und 44. Der Befehl
RESTORE setzt den Zeiger immer auf diesen Anfangswert zurück. Ein Demo-Programm
zeigt uns das an (die Kommata sind wichtig für das Format der Darstellung auf
dem Bildschirm!):

    10 PRINT, PEEK(65)+256*PEEK(66)
    20 FOR X=1 TO 10:READ A
    30 PRINT A,PEEK(65)+256*PEEK(66)
    40 NEXT X
    50 DATA 10,20,30,40,50,60, 70,80,90,100
    60 RESTORE
    70 PRINT,PEEK(65)+256*PEEK(66)

Durch Verändern dieses Zeigers in 65 und 66 kann die Reihenfolge, mit der DATA-
Angaben gelesen werden, verändert werden, allerdings nur zeilenweise.

Wir brauchen dazu die oben beschriebenen Speicherzellen 61 und 62, deren
jeweiligen Inhalt wir ja mit PEEK abfragen können. Wenn wir das vor jeder DATA-
Zeile machen und diesen Wert einer Variablen zuweisen, haben wir die Adresse
gespeichert, hinter welcher die DATA-Zeile kommt. Durch POKEn dieser Adressen
in die Speicherzellen 65 und 66 vor einem READ-Befehl, wird diesem READ die
nächste DATA-Zeile vorgegeben und wir können so die Reihenfolge der DATA-Zeilen
ändern.

    10 A1=PEEK(61)+PEEK(62)*256
    20 DATA DAS IST DIE 1. ZEILE
    30 A2=PEEK(61)+PEEK(62)*256
    40 DATA DAS IST DIE 2.ZEILE
    50 A3=PEEK(61)+PEEK(62)*256
    60 DATA DAS IST DIE 3.ZEILE
    70 POKE 65,A3 AND 255:POKE 66,A3/256:READ A$:PRINT A$
    80 POKE 65,A1 AND 255:POKE 66,A1/256:READ A$:PRINT A$
    90 POKE 65,A2 AND 255:POKE 66,A2/256:READ A$:PRINT A$

Mit den Zeilen 70 bis 90 werden für jede DATA-Zeile eigene READ-Anweisungen
gegeben. Welche DATA-Zeile gelesen werden soll, wird durch die Variablen Ax und
Bx (x=1,2,3) bestimmt, mit denen der Zeiger in 65 und 66 »verbogen« wird. Auf
ein Detail will ich hier hinweisen:

Die Adresse 61 und 62 darf nicht mit zwei Befehlen, sondern muß mit einem
Befehl ausgelesen werden, da bei einem möglichen Page-Wechsel zwischen den zwei
Befehlen der Zeiger nicht verbogen, sondern abgeknickt wird.

Was passiert in der ersten Zeile des Demo-Programms?

    10 A1=PEEK(61):B1=PEEK(62)

Mit »A1=PEEK(61)« wird der Variablen A1 der Wert des Low-Bytes des Zeigers 61
und 62 zugewiesen. Dieser zeigt am Anfang einer Zeile auf das Null-Byte vor der
Linkadresse (hier 2048), so daß A1 den Wert (2048 AND 255)=0 erhält. Mit
»B1=PEEK(62)« wird der Variablen B1 der Wert des High-Bytes des Zeigers 61 und
62 zugewiesen. Dieser zeigt aber inzwischen auf das Trennzeichen (»:«) zwischen
den beiden Befehlen (hier 2061), so daß B1 den Wert (INT(2061/256)) = 8 erhält.
Als Zeiger auf das aktuelle DATA-Element erhalten wir die erwartete Adresse (A1
+ B1 * 256) = 2048.

Was aber, wenn Zeilenanfang und Trennzeichen nicht in derselben Page liegen?
Dazu setzen Sie bitte den Basic-Anfang um eine Stelle zurück:

    POKE43,0:POKE 2047,0:NEW

Die Zeiger auf den Zeilenanfang und das Trennzeichen werden dadurch ja
ebenfalls verändert, so daß A1 jetzt den Wert (2047 AND 255)=255 und B1 den
Wert (INT(2060/256))=8 erhält. Als Zeiger auf das aktuelle DATA-Element
erhalten wir nun die völlig unbrauchbare Adresse (A1+B1 * 256)=2303.

### 64map (—)
Pointer: Used by READ - current DATA Item Address

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*