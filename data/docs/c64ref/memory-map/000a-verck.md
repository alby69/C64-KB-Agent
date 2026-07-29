---
title: 0 = LOAD, 1 = VERIFY
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
- ece7-load
scraped_at: '2026-07-29'
c64ref:
  module: c64mem
  source_files:
  - reference.txt
  - commodore-64-intern-buch.txt
  - 64'er_magazin.txt
  - mapping_the_commodore_64.txt
  - memory_map.txt
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $000A
  symbol: VERCK
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Weil die Routine von LOAD und VERIFY
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Flag: 0 = Load, 1 = Verify'
  - name: Memory Map
    author: Jim Butterfield
    description: 0 = LOAD, 1 = VERIFY
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: BASIC uses one Kernal routine to perform either the LOAD or VERIFY
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: In Zelle 10 steht eine 0, wenn geladen wird und eine 1 bei einem
      VERIFY. Warum
  - name: 64map
    author: —
    description: 'Flag: 0 = Load, 1 = Verify'
---

# VERCK — 0 = LOAD, 1 = VERIFY ($000A)

## Panoramica
Il registro o area di memoria VERCK è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$000A` (`10` decimale)
- **Range**: `$000A`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Commodore-64-intern-Buch (Commodore)
Weil die Routine von LOAD und VERIFY
identisch ist, wird ein Flag benötigt,
um zu unterscheiden, ob ein LOAD oder
ein VERIFY-Vorgang ausgeführt worden
ist.

### C64 Programmer's Reference Guide (Commodore)
Flag: 0 = Load, 1 = Verify

### Memory Map (Jim Butterfield)
0 = LOAD, 1 = VERIFY

### Mapping the Commodore 64 (Sheldon Leemon)
BASIC uses one Kernal routine to perform either the LOAD or VERIFY
function, depending on whether the Accumulator (.A) is set to 0 or 1
upon entry to the routine.  BASIC sets the value of VERCK to 0 for a
LOAD, or 1 for a VERIFY.  Its contents are passed to the Kernal LOAD
routine, which in turn stores it in location 147 ($0093).

### Reference (Joe Forster / STA)
Values:

* $00: LOAD.
* $01-$FF: VERIFY.

### 64'er Magazin (64'er)
In Zelle 10 steht eine 0, wenn geladen wird und eine 1 bei einem VERIFY. Warum
das so ist, will ich kurz erläutern:

Die Basic-Routinen für LOAD beziehungsweise für VERIFY sind völlig identisch.
Was das Betriebssystem hinterher daraus machen muß, ist natürlich
unterschiedlich. Das Basic erspart sich eine doppelte Routine, zeigt aber mit
der Flagge in Speicherzelle 10 den Unterschied an.

Erwähnenswert ist noch, daß das Betriebssystem in einer Art Nationalismus seine
eigene Flagge aufzieht: Den Unterschied zwischen LOAD und VERIFY speichert es
seinerseits in Zelle 147 ($0093) ab. Soweit ich es sehen kann, sind Inhalt und
Bedeutung beider Speicherzellen völlig identisch.

Ich habe für Sie zwar kein Kochrezept zur Anwendung der LOAD-VERIFY-Flagge in
einem Programm vorrätig, möchte Sie aber trotzdem ein bißchen zum Spielen
anregen. Um meine Erklärung nachzuvollziehen, tippen Sie bitte direkt LOAD ein.

Den Ladevorgang brechen Sie mit der STOP-Taste ab und fragen dann den Inhalt
der Zelle 10 ab mit

    PRINT PEEK (10)

Wir erhalten eine 0.

Wiederholen Sie bitte diesen Vorgang, aber mit VERIFY. Wir erhalten jetzt eine
1 - Quod erat demonstrandum.

Wir können auch in die Zelle 10 hineinPOKEn. Die »Wachablösung« zwischen Basic
und Betriebssystem unter Hissen der Flagge in Zelle 10 findet beim VC 20 in der
Speicherzelle 57705, beim C 64 in 57708 statt. Bevor wir diese Maschinenroutine
mit SYS 57705 (SYS 57708) starten, geben wir mit dem Inhalt der Speicherzelle
10 an, ob es ein LOAD oder ein VERIFY sein soll.

Legen Sie ein Band mit Programm in die Datasette. Um ein LOAD zu erzeugen,
geben wir direkt ein:

    POKE 10,0:SYS 57705
    (POKE 10,0:SYS 57708)

Entsprechend der Anweisung auf dem Bildschirm drücken Sie PLAY, und das
Auffinden des ersten Programms wird mit LOAD gemeldet. Machen Sie das Ganze
noch einmal, diesmal aber POKEn Sie bitte eine 1 in die Zelle 10. Jetzt meldet
das Betriebssystem das Auffinden des Programms mit VERIFY.

Wie gesagt, vielleicht fällt Ihnen eine Anwendung dafür ein.

### 64map (—)
Flag: 0 = Load, 1 = Verify

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*