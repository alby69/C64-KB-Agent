---
title: Keyboard pointer
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
  address: $00F5
  address_end: $00F6
  symbol: KEYTAB
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Keyscan table indirect
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Diese Speicherzellen zeigen auf die
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Vector Keyboard Decode Table
  - name: Memory Map
    author: Jim Butterfield
    description: Keyboard pointer
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: KEYTAB points to the address of the keyboard matrix lookup table
  - name: Reference
    author: Joe Forster / STA
    description: Pointer to current conversion table during conversion from keyboard
      matrix co...
  - name: 64'er Magazin
    author: 64'er
    description: Bei der Diskussion der Speicherzelle 145 habe ich Ihnen gezeigt,
      wie das
  - name: 64map
    author: —
    description: 'Vector: Current Keyboard decoding Table. ($EB81)'
---

# KEYTAB — Keyboard pointer ($00F5)

## Panoramica
Il registro o area di memoria KEYTAB è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00F5` (`245` decimale)
- **Range**: `$00F5`-`$00F6`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Keyscan table indirect

### Commodore-64-intern-Buch (Commodore)
Diese Speicherzellen zeigen auf die
Tastatur-Dekodiertabelle.

### C64 Programmer's Reference Guide (Commodore)
Vector Keyboard Decode Table

### Memory Map (Jim Butterfield)
Keyboard pointer

### Mapping the Commodore 64 (Sheldon Leemon)
KEYTAB points to the address of the keyboard matrix lookup table
currently being used.  Although there are only 64 keys on the keyboard
matrix, each key can be used to print up to four different characters,
depending on whether it is struck by itself or in combination with the
SHIFT, CTRL, or Commodore logo keys.

The tables pointed to y this address hold the ASCII value of each of
the 64 keys for one of these possible combinations of keypresses.
When it comes time to print the character, the table that is used
determines which character is printed.

The addresses of the four tables are:

|       |       |                                                   |
|-------|-------|---------------------------------------------------|
| 60289 | $EB81 | default uppercase/graphics characters (unshifted) |
| 60354 | $EBC2 | shifted characters                                |
| 60419 | $EC03 | Commodore logo key characters                     |
| 60536 | $EC78 | CTRL characters                                   |

The concept of the keyboard matrix tables should not be confused with
changing the character sets from uppercase/graphics to
upper/lowercase.  The former involves determining what character is to
be placed into screen memory, while the latter involves determining
which character data table is to be used to decode the screen memory
into individual dots for the display of characters on the screen.
That character base is determined by location 53272 ($D018) of the
VIC-II chip.

### Reference (Joe Forster / STA)
Pointer to current conversion table during conversion from keyboard matrix codes to PETSCII codes

### 64'er Magazin (64'er)
Bei der Diskussion der Speicherzelle 145 habe ich Ihnen gezeigt, wie das
Drücken einer der 64 Tasten entschlüsselt wird.

Ein entschlüsselter Wert wird in Speicherzelle 145 zwischengespeichert und
gelangt dann als Tastencode in die Speicherzelle 203. Bei der Besprechung der
Zelle 203 wurden die Codewerte aufgelistet. Ich habe auch darauf hingewiesen,
daß die Codes der drei Steuertasten SHIFT, CTRL und COMMODORE (C=) separat in
der Zelle 653 stehen.

Diese Tastencodes sind sehr nützlich und vom Basic aus gut verwendbar. Im
Verkehr mit anderen Geräten sind sie aber nicht einsetzbar, da sie keiner
internationalen Norm entsprechen.

Eine derartige Norm bietet der sogenannte ASCII-Code. Deshalb rechnet, wo
notwendig, das Betriebssystem die Tastencodes in den ASCII-Code um.

Dazu stehen im Speicher des Betriebssystems vier Tabellen (Bild 22), die die
ASCII-Codewerte enthalten (in Klammern für den VC 20).

Die Umrechnung der Tastencodes in ASCII-Code ist sehr einfach. Der Tastencode
wird lediglich zu der Anfangsadresse der entsprechenden Tabelle hinzugezählt.
Die Summe ergibt die Adresse in derTabelle, in der der ASCII-Code für das
gedrückte Zeichen steht.

Als Beispiel nehmen wir das normale »G«, sein Tastencode ist 26 (VC 20:19). Zur
Anfangsadresse der normalen Tabelle 60289 (60510) dazugezählt, ergibt das 60315
(60529). Schauen wir in dieser Speicherzelle nach:

    PRINT PEEK(60315): REM BEIM C 64
    PRINT PEEK(60529): REM BEIM VC 20

In beiden Fällen erhalten wir die Zahl 71. Ein Blick in die ASCII-Tabelle des
Handbuchs bestätigt die Richtigkeit.

Der Vektor in den vorliegenden Speicherzellen 245/246 zeigt auf den Anfang der
vier Tabellen, und zwar in Abhängigkeit davon, ob und welche der drei
Steuertasten zusammen mit einer anderen Taste gedrückt worden ist. Auch das
kann ich Ihnen zeigen mit einer Programmzeile, welche ein Zahlenband erzeugt,
dessen Zahl durch die Steuertasten verändert wird. Sie werden sehen, es sind
die Anfangsadressen der vier Tabellen.

    10 PRINT PEEK(245)+256*PEEK(246):GOTO 10

### 64map (—)
Vector: Current Keyboard decoding Table. ($EB81)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*