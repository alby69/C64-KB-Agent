---
title: 'Keyswitch PIA : STOP and RVS flags'
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
- 00c7-rvs
- stop
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
  address: $0091
  symbol: STKEY
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: STOP key flag
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: In dieser Speicherzelle wird vermerkt,
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: STOP key / RVS key'
  - name: Memory Map
    author: Jim Butterfield
    description: 'Keyswitch PIA : STOP and RVS flags'
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This location is updated every 1/60 second during the execution of
      the
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: In den Bildern 13 und 14 ist dargestellt, wie die Tasten des VC 20
      und des C 64
  - name: 64map
    author: —
    description: 'Flag: $7F = STOP key'
---

# STKEY — Keyswitch PIA : STOP and RVS flags ($0091)

## Panoramica
Il registro o area di memoria STKEY è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0091` (`145` decimale)
- **Range**: `$0091`
- **Dimensione**: `1 byte`
- **Permessi**: `R`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
STOP key flag

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle wird vermerkt,
ob die Stoptaste gedrückt worden ist
oder nicht.

### C64 Programmer's Reference Guide (Commodore)
Flag: STOP key / RVS key

### Memory Map (Jim Butterfield)
Keyswitch PIA : STOP and RVS flags

### Mapping the Commodore 64 (Sheldon Leemon)
This location is updated every 1/60 second during the execution of the
IRQ routine that reads the keyboard and updates the jiffy clock.

The value of the last row of the keyboard matrix is placed here.  That
row contains the STOP key, and although this location is used
primarily to detect when that key has been pressed, it can also detect
when any of the other keys in that row of the matrix have been
pressed.

In reading the keyboard matrix, a bit set to 1 means that no key has
been pressed, while a bit reset to 0 indicates that a key is pressed.
Therefore, the following values indicate the keystrokes detailed
below:

|     |     |                            |
|-----|-----|----------------------------|
| 255 | $FF | no key pressed             |
| 254 | $FE | 1 key pressed              |
| 253 | $FD | (left arrow) key pressed   |
| 251 | $FB | CTRL key pressed           |
| 247 | $F7 | 2 key pressed              |
| 239 | $EF | space bar pressed          |
| 223 | $DF | Commodore logo key pressed |
| 191 | $BF | Q key pressed              |
| 127 | $7F | STOP key pressed           |

VIC owners will notice that the 64's keyboard matrix is very different
from the VIC's.  One of the advantages of this difference is that you
can test for the STOP key by following a read of this location with a
BPL instruction, which will cause a branch to occur anytime that the
STOP key is pressed.

### Reference (Joe Forster / STA)
Values:

* $7F: Stop key is pressed.
* $FF: Stop key is not pressed.

### 64'er Magazin (64'er)
In den Bildern 13 und 14 ist dargestellt, wie die Tasten des VC 20 und des C 64
miteinander über eine Matrix verbunden sind.

60mal in der Sekunde unterbricht der Computer seine Arbeit, merkt sich, wo er
gerade ist und fragt dann unter anderem, ob die STOP-Taste gedrückt worden ist.
Dadurch wird erreicht, daß die STOP-Taste jederzeit Priorität hat.

Die Abfrage geht so vonstatten, daß das Betriebssystem über das im Bild 13 und
14 gezeigte Spaltenregister 56320 (beim VC 20: 37152) diejenige Tastenspalte
anwählt, in welcher sich die STOP-Taste befindet. Aus Bild 13 und 14 sehen wir,
daß dies die Spalte mit der Codenummer 127 beziehungsweise 247 ist. Ist in
dieser Spalte eine Taste gedrückt, wird an ihrer Stelle eine Null in das
Auslese-Register 56321 (VC 20: 37153) geschrieben. Die dadurch entstandene
Dualzahl wird in die Speicherzelle 145 gebracht.

Es ist sicher verständlich, daß auf diese Weise nicht nur die STOP-Taste,
sondern alle Tasten der Spalte 127 (247) abgefragt werden können. Ein kleines
Demonstrationsprogramm kann das beweisen:

    10 PRINT PEEK (656321);PEEK (145)
    20 GOTO 10

Beim VC 20 ist statt 56321 natürlich 37153 einzusetzen.

Das Zahlenband kann durch die Tasten der genannten Spalte - und nur durch diese
- beeinflußt werden.

### 64map (—)
Flag: $7F = STOP key

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*