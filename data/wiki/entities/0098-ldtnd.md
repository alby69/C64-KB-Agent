---
id: 0098-ldtnd
type: entity
title: How many open files
aliases:
- How many open files
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0098-ldtnd.md
  sha256: 019d27989e0fe9265e3e1202f32e9b6f974e97eb48df1e2d9a63433828748801
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0098-ldtnd
---

# How many open files



# LDTND — How many open files ($0098)

## Panoramica
Il registro o area di memoria LDTND è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0098` (`152` decimale)
- **Range**: `$0098`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Index to logical file

### Commodore-64-intern-Buch (Commodore)
In dieser Speicherzelle wird
festgehalten, wie viele Files gleichzeitig
geöffnet sind.

### C64 Programmer's Reference Guide (Commodore)
No. of Open Files / Index to File Table

### Memory Map (Jim Butterfield)
How many open files

### Mapping the Commodore 64 (Sheldon Leemon)
The number of currently open I/O files is stored here.  The maximum
number that can be open at one time is ten.  The number stored here is
used as the index to the end of the tables that hold the file numbers,
device numbers, and secondary address numbers (see locations 601-631
($0259-$0277) for more information about these tables).

CLOSE decreases this number and removes entries from the tables
referred to above, while OPEN increases it and adds the appropriate
information to the end of the tables.  The Kernal routine CLALL closes
all files by setting this number to 0, which effectively empties the
table.

### Reference (Joe Forster / STA)
Values: $00-$0A, 0-10.

### 64'er Magazin (64'er)
Ein File, oder auf Deutsch gesagt, eine Datei, wird mit dem Befehl OPEN
eröffnet. Nach OPEN folgt die Nummer der Datei; sie ist beliebig wählbar bis
maximal 255. Als zweites folgt die Nummer des Gerätes, mit dem die Verbindung
hergestellt werden soll.

Es ist erlaubt, mehrere Dateien gleichzeitig geöffnet zu halten, vorausgesetzt
die Nummern der Dateien sind verschieden.

In Speicherzelle 152 wird festgehalten, wieviel Dateien gleichzeitig geöffnet
sind. Dieses kleine Programm zeigt es uns deutlich:

    10 FOR K=10 TO 22
    20 PRINT PEEK (152),K
    30 OPEN K,0
    40 NEXT K

Mit der FOR...NEXT-Schleife der Zeilen 10 und 40 eröffnen wir 13 Dateien
hintereinander, und zwar - wie Zeile 30 uns deutlich macht - mit der Tastatur.
Die Tastatur hat die Nummer 0, der Drucker die Nummer 4, das Floppy-Gerät die
Nummer 8 und die Datasette die Nummer 1. Ich habe die Tastatur gewählt, obwohl
es keinen Sinn ergibt, weil sie die vielen Eröffnungen ohne zu unterbrechen
akzeptiert.

Nach RUN sehen wir links untereinander den Inhalt von 152, also die Anzahl der
eröffneten Dateien. Rechts steht jeweils die Nummer der eröffne-

In der 10. Zeile sehen wir jetzt die 10 als Inhalt von 152 und als neue
Dateinummer (Schleifenvariable K) wieder die 10. Das Programm bleibt aber
stehen und meldet FILE OPEN. Es hat recht, denn die Datei 10 ist bereits als
erste eröffnet, aber nicht wieder geschlossen worden.

Das Betriebssystem macht das so, daß jede der Dateinummern in eine Tabelle
geschrieben wird, die in den Speicherzellen 601 bis 610 stehen. Bei jedem OPEN-
Befehl wird dort nachgeschaut, ob die Filenummer existiert. Wenn ja, wird die
Fehlermeldung FILE OPEN ERROR ausgegeben. Bei jedem CLOSE-Befehl wird die
entsprechende Nummer aus der Tabelle gelöscht.

Wir können aber auch eine 0 in die Speicherzelle 152 POKEn, wodurch dem
Betriebssystem vorgegaukelt wird, daß keine Datei eröffnet ist. Schieben Sie im
Programm einfach die Zeile ein:

    45 POKE 152,0

und das Programm läuft ewig weiter.

Die Speicherzelle 152 ist also der Wächter über die Anzahl der eröffneten
Dateien. Steht sie auf 0, dann wird eine Neueröffnung am Anfang der Tabelle ab
601 eingetragen. Die Tabelle ihrerseits ist der Wächter über Exklusivität der
Dateinummern. Ich zeige Ihnen das noch genauer, wenn wir zu 601 kommen.

Sie werden vielleicht fragen, warum ich das so ausführlich beschreibe. Nun, in
einem Programm kann es sicher sehr nützlich sein, dieZelle 152 mit PEEK nach
der Datei-Lage abzufragen und entsprechend Maßnahmen zu treffen, ehe die
Fehlermeldung das Programm abbricht.

Mit POKE 152,0 aber müssen Sie aufpassen. Es ersetzt nämlich nicht (!!) den
CLOSE-Befehl. Probieren Sie es aus: Um das kleine Programm oben per Drucker
auszudrucken, brauchen wir:

    OPEN 1,4: CMD 1: LIST

Wenn Sie jetzt die Zeile 152 auf 0 POKEn und dann LIST eintippen, wird trotzdem
wieder auf dem Drucker gelistet und nicht auf dem Bildschirm. Die
vorgeschriebene Schließmethode mit

    PRINT #1:CLOSE1

geht jetzt aber auch nicht mehr, denn das Betriebssystem ist ja im Glauben, daß
keine Datei eröffnet ist - schöner Schlamassel!

Erst eine Neueröffnung bringt alles wieder in die Reihe. Also Vorsicht mit der
Anwendung der Speicherzelle 152. Eine Möglichkeit, alle Dateien auf einen
Schlag zu schließen, gibt es aber doch.

SYS 65511 besorgt das sowohl beim C 64 als auch beim VC 20.

### 64map (—)
Number of Open Files/Index to File Table

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0098-ldtnd]]
