---
id: 0318-nminv
type: entity
title: NMI interrupt vector ($FE47)
aliases:
- NMI interrupt vector ($FE47)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0318-nminv.md
  sha256: 7a56a834fa009d25ecd89923d6eaa34fd6de9f0c8f5cd8b960fb1eb4950bf06d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0318-nminv
---

# NMI interrupt vector ($FE47)



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

## References
- Source: [[src-0318-nminv]]
