---
title: ATN sign/Comparison eval flag
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
  address: $0012
  symbol: TANSGN
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Used in determining sign of tangent
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Mask in use by relation operations
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Die Speicherzelle $0012 wird von den
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Flag TAN sign / Comparison Result
  - name: Memory Map
    author: Jim Butterfield
    description: ATN sign/Comparison eval flag
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is used to determine whether the sign of the value
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: Additionally, the string and numeric comparison routines use this
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Die Routinen des Basic-Übersetzers (Interpreter), welche die drei
  - name: 64'er Magazin
    author: 64'er
    description: Die Speicherzelle 18 wird auch noch von anderen Routinen des Basic-Interpreters
  - name: 64map
    author: —
    description: 'Flag: TAN sign/Comparative result'
---

# TANSGN — ATN sign/Comparison eval flag ($0012)

## Panoramica
Il registro o area di memoria TANSGN è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0012` (`18` decimale)
- **Range**: `$0012`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Used in determining sign of tangent

### Original Source Comments (Microsoft/Commodore)
Mask in use by relation operations

### Commodore-64-intern-Buch (Commodore)
Die Speicherzelle $0012 wird von den
trigonometrischen Funktionen zur
Bestimmung des Vorzeichens verwendet.
Zusätzlich dient die Speicherzelle $0012
als Vergleichsoperator für
Vergleichsoperationen.

### C64 Programmer's Reference Guide (Commodore)
Flag TAN sign / Comparison Result

### Memory Map (Jim Butterfield)
ATN sign/Comparison eval flag

### Mapping the Commodore 64 (Sheldon Leemon)
This location is used to determine whether the sign of the value
returned by the functions SIN or TAN is positive or negative.

### Mapping the Commodore 64 (Sheldon Leemon)
Additionally, the string and numeric comparison routines use this
location to indicate the outcome of the comparison.  For a comparison
of variable A to variable B, the value here will be 1 if A is greater
than B, 2 if A equals B, and 4 if a is less than B.  If more than one
comparison operator was used to compare the two variables (e.g., >= or
<=), the value here will be a combination of the above values.

### Reference (Joe Forster / STA)
Values:

* $00: Positive.
* $FF: Negative.

### 64'er Magazin (64'er)
Die Routinen des Basic-Übersetzers (Interpreter), welche die drei
trigonometrischen Funktionen SIN, COS und TAN berechnen, verwenden die
Speicherzelle 18 zur Bestimmung des Vorzeichens.

Zur Erinnerung: Die trigonometrischen Funktionen haben in den vier »Quadranten«
des Kreises (0-90, 90-180, 180-270, 270-360 Grad) nicht unbedingt dieselben
Vorzeichen. Die Vorzeichen ändern sich allerdings nur an den Grenzen der
Quadranten, wie in Bild 2 zu sehen ist. Die Flagge in Zelle 18 gibt das
Vorzeichen nicht direkt an, sondern auf Umwegen. Die Darstellung ist in der
folgenden Tabelle zusammengefaßt.

Dabei bedeutet »gleich«: 0-0-0-0 oder 255-255-255 »Wechsel«: 0-255-0-255 Da die
Erklärung mit »gleich« beziehungsweise »Wechsel« nicht gerade einleuchtend ist,
schlage ich vor, daß Sie sich das Ganze mit dem folgenden kleinen Programm
selbst anschauen, welches für viele Werte des Winkels im Bogenmaß - und in
kleinen Schritten - den Wert der Flagge, daneben den Winkel I und den Wert der
Funktion mit Vorzeichen ausdruckt.

    10 FOR I=0 TO 10 STEP 0.01
    20 PRINT PEEK(18);INT (I*100)/100;SIN(I):NEXT

Diese etwas umständliche Art, den Wert von I auszudrucken, vermeidet
Rundungsfehler und begrenzt den Ausdruck auf zwei Dezimalstellen. Wenn Sie die
Winkelwerte von I in Graden ausgedruckt haben wollen, können Sie eine ändere
Zeile 20 verwenden, welche die Umrechnungsformel vom Bogenmaß in Grade
verwendet: Winkel in Grad = Winkel im Bogenmaß * 180/π

    20 PRINT PEEK(18);INT(I*180/π);SIN(I):NEXT

Statt SIN können Sie genauso gut COS und TAN einsetzen.

In Bild 2 sind nicht nur die Kurven und die Bereiche der Vorzeichen, sondern
auch die Winkelbereiche sowohl im Bogenmaß als auch in Graden dargestellt.

### 64'er Magazin (64'er)
Die Speicherzelle 18 wird auch noch von anderen Routinen des Basic-Interpreters
beansprucht und zwar von allen, die einen Vergleich wie <, >, >= und so weiter
durchführen. Entsprechend der Art des Vergleichs steht dann in der Zelle 18
eine Ziffer von 0 bis 6.

Das folgende Programm macht das deutlich.

    10 A=2
    20 FOR I=1 TO 3
    30 IF I=A  THEN PRINT I; PEEK(18); "="
    40 IF I<>A THEN PRINT I; PEEK(18); "><"
    50 IF I>A  THEN PRINT I; PEEK(18); ">"
    60 IF I<A  THEN PRINT I; PEEK(18); "<"
    70 IF I>=A THEN PRINT I; PEEK(18); ">="
    80 IF I<=A THEN PRINT I; PEEK(18); "<="
    90 IF I<A OR I=A THEN PRINT I; PEEK(18); "< OR ="
    100 NEXT I

Kurz zur Erklärung dieser Zeilen: In der FOR..NEXT-Schleife wird die Variable I
mit der Konstanten A=2 verglichen. In den Zeilen 30 bis 90 werden alle
möglichen Vergleichsoperatoren durchgeprüft. Jeder der zutrifft, druckt den
Wert von I, den Wert der dann in Zelle 18 stehenden Flagge und schließlich den
Vergleichsoperator aus. Aus dem Resultat dieses Programms läßt sich folgende
Tabelle zusammenstellen:

| Vergleich | Flagge in 18 |
|-----------|--------------|
| < OR =    | 0            |
| > OR =    | 0            |
| >         | 1            |
| =         | 2            |
| >=        | 3            |
| <         | 4            |
| <>        | 5            |
| <=        | 6            |

Sie sehen, die Flagge für die kombinierten Vergleichsoperatoren entspricht der
Summe ihrer Einzelwerte. Nur die Verknüpfung über OR nicht, denn die ergibt 0.

### 64map (—)
Flag: TAN sign/Comparative result

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*