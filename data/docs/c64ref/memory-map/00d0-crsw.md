---
title: Input from screen/from keyboard
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
  address: $00D0
  symbol: CRSW
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: INPUT vs GET flag
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier wird die Länge der zu
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: INPUT or GET from Keyboard'
  - name: Memory Map
    author: Jim Butterfield
    description: Input from screen/from keyboard
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This flag is used by the Kernal CHRIN (61783, $F157) routine to
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Speicherzelle wird von einer Routine des Betriebssystems verwendet,
      die
  - name: 64map
    author: —
    description: 'Flag: Input from Screen = $03, or Keyboard = $00'
---

# CRSW — Input from screen/from keyboard ($00D0)

## Panoramica
Il registro o area di memoria CRSW è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00D0` (`208` decimale)
- **Range**: `$00D0`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
INPUT vs GET flag

### Commodore-64-intern-Buch (Commodore)
Hier wird die Länge der zu
übertragenden Zeichen gespeichert.

### C64 Programmer's Reference Guide (Commodore)
Flag: INPUT or GET from Keyboard

### Memory Map (Jim Butterfield)
Input from screen/from keyboard

### Mapping the Commodore 64 (Sheldon Leemon)
This flag is used by the Kernal CHRIN (61783, $F157) routine to
indicate whether input is available from the screen (3), or whether a
new line should be obtained from the keyboard (0).

### Reference (Joe Forster / STA)
Values:

* $00: Return character reached, end of line.
* $01-$FF: Still reading characters from line.

### 64'er Magazin (64'er)
Diese Speicherzelle wird von einer Routine des Betriebssystems verwendet, die
das jeweils nächste Zeichen in den Arbeitsspeicher holt. Für sie ist wichtig zu
wissen, von welchem Eingabegerät dieses Zeichen geholt werden soll.

Wenn in der Zelle 208 eine 0 steht, wird damit die Tastatur als Eingabegerät
bestimmt. Das ist der Normalfall, mit dem wir per Tastendruck Zeichen auf den
Bildschirm tippen. Sobald aber statt einem Zeichen die RETURN-Taste gedrückt
wird, ändert sich der Inhalt der Speicherzelle 208. Die oben genannte Routine
überträgt nämlich jetzt den Inhalt der Zelle 213, in welcher die Länge der
derzeitigen logischen Zeile steht, nach 208. Dann holt sie das nächste Zeichen,
allerdings nicht von der Tastatur, sondern vom Bildschirm, und zwar das erste
Zeichen der gerade abgeschlossenen logischen Zeile. Auf diese Weise gelangen
die Anweisungen einer Zeile in den Arbeitsspeicher, wo sie im Direkt-Modus
sofort ausgeführt, im Programm-Modus aber gespeichert und erst nach RUN
ausgeführt werden.

Den Unterschied zwischen »logischer« und »echter« Zeile habe ich in dem
Texteinschub Nr. 23 näher beschrieben.

### 64map (—)
Flag: Input from Screen = $03, or Keyboard = $00

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*