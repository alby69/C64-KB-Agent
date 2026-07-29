---
title: NMI interrupt vector ($FE47)
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
related:
- fe47-standard-nmi-routine
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
  address: $0318
  address_end: $0319
  symbol: NMINV
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: NMI RAM vector
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $FE47 NMI-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: Non-Maskable Interrupt'
  - name: Memory Map
    author: Jim Butterfield
    description: NMI interrupt vector ($FE47)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the routine that will be executed
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $FE47.'
  - name: 64'er Magazin
    author: 64'er
    description: Der NMI-Interrupt ist im Texteinschub Nr. 35 »Dem Computer ins Wort
      fallen«
  - name: 64map
    author: —
    description: 'Vector: Hardware NMI Interrupt Address ($FE47)'
---

# NMINV — NMI interrupt vector ($FE47) ($0318)

## Panoramica
Il registro o area di memoria NMINV è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0318` (`792` decimale)
- **Range**: `$0318`-`$0319`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
NMI RAM vector

### Commodore-64-intern-Buch (Commodore)
$FE47 NMI-Vektor

### C64 Programmer's Reference Guide (Commodore)
Vector: Non-Maskable Interrupt

### Memory Map (Jim Butterfield)
NMI interrupt vector ($FE47)

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the routine that will be executed
when a Non-Maskable Interrupt (NMI) occurs (currently at 65095
($FE47)).

There are two possible sources for an NMI interrupt.  The first is the
RESTORE key, which is connected directly to the 6510 NMI line.  The
second is CIA #2, the interrupt line of which is connected to the 6510
NMI line.

When an NMI interrupt occurs, a ROM routine sets the Interrupt disable
flag, and then jumps through this RAM vector.  The default vector
points to an interrupt routine which checks to see what the cause of
the NMI was.

If the cause was CIA #2, the routine checks to see if one of the
RS-232 routines should be called.  If the source was the RESTORE key,
it checks for a cartridge, and if present, the cartridge is entered at
the warm start entry point.  If there is no cartridge, the STOP key is
tested.  If the STOP key was pressed at the same time as the RESTORE
key, several of the Kernal initialization routines such as RESTOR,
IOINIT and part of CINT are executed, and BASIC is entered through its
warm start vector at 40962.  If the STOP key was not pressed
simultaneously with the RESTORE, the interrupt will end without
letting the user know that anything happened at all when the RESTORE
key was pressed.

Since this vector controls the outcome of pressing the RESTORE key, it
can be used to disable the STOP/RESTORE sequence.  A simple way to do
this is to change this vector to point to the RTI instruction.  A
simple POKE 792,193 will accomplish this.  To set the vector back,
POKE 792,71.  Note that this will cut out all NMIs, including those
required for RS-232 I/O.

### Reference (Joe Forster / STA)
Default: $FE47.

### 64'er Magazin (64'er)
Der NMI-Interrupt ist im Texteinschub Nr. 35 »Dem Computer ins Wort fallen«
näher beschrieben. Der Vektor zeigt auf den Beginn dieser Routine ab
Speicherzelle 65095 ($FE47) - beim VC 20 ab 65197 ($FEAD).

Sobald ein NMI-Interrupt auftritt, wird zuerst durch Setzen der Interrupt-
Abschalt-Flagge (Interrupt Disable Flag) jede Unterbrechung durch den IRQ-
Interrupt unterbunden. Dann wird geprüft, wer den NMI-Interrupt ausgelöst hat,
und zwar in der Reihenfolge: RS232-Schnittstelle, RESTORE-Taste; eingestecktes
Modul und schließlich die STOP-Taste. Die letztere dient zum Sichem der
RESTORE-Taste. Nur wenn beide gemeinsam gedrückt werden, kommt die NMI-
Unterbrechung durch die RESTORE-Taste zur Auswirkung.

Da die RESTORE-Taste fast als erste abgefragt wird, kann sie und ihre
Kombination mit der STOP-Taste durch Verbiegen des Vektors in Speicherzelle 792
bis 793 abgeschaltet werden. Beim C 64 geht das mit POKE 792,193 - Wieder
eingeschaltet wird mit POKE 792,71. Beim VC 20 geht das mit POKE 792,91
beziehungsweise POKE 792,173 - Natürlich können Spezialisten durch Verbiegen
des Vektors auf andere Adressen ihre eigenen NMI-Routinen bauen.

### 64map (—)
Vector: Hardware NMI Interrupt Address ($FE47)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*