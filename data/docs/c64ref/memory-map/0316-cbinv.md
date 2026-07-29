---
title: Break interrupt vector ($FE66)
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
- fe66-warm-start-basic
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
  address: $0316
  address_end: $0317
  symbol: CBINV
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: BRK instr RAM vector
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $FE66 BRK-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: BRK Instr. Interrupt'
  - name: Memory Map
    author: Jim Butterfield
    description: Break interrupt vector ($FE66)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the routine which will be
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $FE66.'
  - name: 64'er Magazin
    author: 64'er
    description: Diese Routine ist im Texteinschub Nr. 35 nicht erwähnt, weil sie
      ein Teil der
  - name: 64map
    author: —
    description: 'Vector: BRK Instruction Interrupt Address ($FE66)'
---

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