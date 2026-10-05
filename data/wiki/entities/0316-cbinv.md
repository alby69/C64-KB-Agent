---
id: 0316-cbinv
type: entity
title: Break interrupt vector ($FE66)
aliases:
- Break interrupt vector ($FE66)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0316-cbinv.md
  sha256: e5dc2483df5f0acc6387a65574f27820fcc3135c87028dc737decaa844aa334b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0316-cbinv
---

# Break interrupt vector ($FE66)



# CBINV — Break interrupt vector ($FE66) ($0316)

## Panoramica
Il registro o area di memoria CBINV è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0316` (`790` decimale)
- **Range**: `$0316`-`$0317`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
BRK instr RAM vector

### Commodore-64-intern-Buch (Commodore)
$FE66 BRK-Vektor

### C64 Programmer's Reference Guide (Commodore)
Vector: BRK Instr. Interrupt

### Memory Map (Jim Butterfield)
Break interrupt vector ($FE66)

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the routine which will be
executed anytime that a 6510 BRK instruction (00) is encountered.

The default value points to a routine that calls several of the Kernal
initialization routines such as RESTOR, IOINIT and part of CINT, and
then jumps through the BASIC warm start vector at 40962.  This is the
same routine that is used when the STOP and RESTORE keys are pressed
simultaneously, and is currently located at 65126 ($FE66).

A machine language monitor program will usually change this vector to
point to the monitor warm start address, so that break points may be
set that will return control to the monitor for debugging purposes.

### Reference (Joe Forster / STA)
Default: $FE66.

### 64'er Magazin (64'er)
Diese Routine ist im Texteinschub Nr. 35 nicht erwähnt, weil sie ein Teil der
NMI-Routine ist. Dieser Vektor zeigt auf die Adresse 65126 ($FE66) - beim VC 20
auf 65234 ($FED2). Die da beginnende Routine des Betriebssystems wird
aufgerufen, wenn der Maschinenbefehl BRK ausgeführt wird. Er führt letztlich zu
einem Warmstart, das heißt der Bildschirm wird gelöscht und der Cursor meldet
sich mit READY. Diese Routine wird auch durch das gleichzeitige Drücken der
STOP- und der RESTORE-Taste angestoßen.

### 64map (—)
Vector: BRK Instruction Interrupt Address ($FE66)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0316-cbinv]]
