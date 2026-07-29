---
title: IRQ save during tape I/O
source_url: https://github.com/mist64/c64ref/blob/main/src/c64mem/reference.txt
category: reference
topics:
- memory-map
- zero-page
- rom-layout
difficulty: intermediate
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
  address: $029F
  address_end: $02A0
  symbol: IRQTMP
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: Holds irq during tape ops
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Bei Kassettenoperationen wird hier in
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: Holds IRQ Vector During Tape I/O
  - name: Memory Map
    author: Jim Butterfield
    description: IRQ save during tape I/O
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: The routines that read and write tape data are driven by an IRQ
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Die Routinen des Betriebssystems, die Daten auf, beziehungsweise
      von Kassette
  - name: 64map
    author: —
    description: Temporary store for IRQ Vector during Tape operations
---

# IRQTMP — IRQ save during tape I/O ($029F)

## Panoramica
Il registro o area di memoria IRQTMP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$029F` (`671` decimale)
- **Range**: `$029F`-`$02A0`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Holds irq during tape ops

### Commodore-64-intern-Buch (Commodore)
Bei Kassettenoperationen wird hier in
LOW- und HIGH-Byte-Darstellung der
Vektor für die Interruptroutine
gespeichert.

### C64 Programmer's Reference Guide (Commodore)
Holds IRQ Vector During Tape I/O

### Memory Map (Jim Butterfield)
IRQ save during tape I/O

### Mapping the Commodore 64 (Sheldon Leemon)
The routines that read and write tape data are driven by an IRQ
interrupt.  In order to hook one of these routines into the interrupt,
the RAM IRQ vector at 788-789 ($0314-$0315) must be changed to point to
the address at which it starts.  Before that change is made, the old
IRQ vector address is saved at these locations, so that after the tape
I/O is finished, the interrupt that is used for scanning the keyboard,
checking the stop key, and updating the clock can be restored.

You will note that all of the above functions will be suspended during
tape I/O.

### Reference (Joe Forster / STA)
Values:

* $0000-$00FF: No datasette input/output took place yet or original pointer has been already restored.
* $0100-$FFFF: Original pointer, datasette input/output currently in progress.

### 64'er Magazin (64'er)
Die Routinen des Betriebssystems, die Daten auf, beziehungsweise von Kassette
ein- und ausgeben, werden durch die Interrupt-Routine gesteuert. Diese Routine
unterbricht normalerweise 60mal in der Sekunde alle Aktivitäten des Computers,
um diverse »Hausaufgaben« (Uhr weiterschalten, STOP-Taste abfragen und so
weiter) auszuführen. Bei Kassetten-Ein-/Ausgaben ist diese Interrupt-Routine
jedoch abgeschaltet. Dies wird dadurch erreicht, daß der Vektor in
Speicherzelle 788 und 789, der auf die Anfangsadresse der Interrupt-Routine
zeigt, auf eine Adresse der Kassetten-Routine gesetzt wird. Um nach der
Kassettenoperation weitermachen zu können, wird der »alte« Interrupt-Vektor in
dieser Speicherzelle 671 und 672 gespeichert.

### 64map (—)
Temporary store for IRQ Vector during Tape operations

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*