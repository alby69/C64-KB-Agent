---
title: Crunch Basic tokens link
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
  address: $0304
  address_end: $0305
  symbol: ICRNCH
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: indirect CRUNCH (tokenization routine)
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $A57C Vektor für Umwandlung in Interpretercode
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: 'Vector: Tokenize BASIC Text'
  - name: Memory Map
    author: Jim Butterfield
    description: Crunch Basic tokens link
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the CRUNCH routine at 42364
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $A57C.'
  - name: 64'er Magazin
    author: 64'er
    description: Dieser Vektor zeigt auf 42364 ($A57C), beim VC 20 auf 50556 ($C57C).
      Dort
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to BASIC Tokenise Routine ($A57C)'
---

# ICRNCH — Crunch Basic tokens link ($0304)

## Panoramica
Il registro o area di memoria ICRNCH è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0304` (`772` decimale)
- **Range**: `$0304`-`$0305`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
indirect CRUNCH (tokenization routine)

### Commodore-64-intern-Buch (Commodore)
$A57C Vektor für Umwandlung in Interpretercode

### C64 Programmer's Reference Guide (Commodore)
Vector: Tokenize BASIC Text

### Memory Map (Jim Butterfield)
Crunch Basic tokens link

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the CRUNCH routine at 42364
($A57C).

### Reference (Joe Forster / STA)
Default: $A57C.

### 64'er Magazin (64'er)
Dieser Vektor zeigt auf 42364 ($A57C), beim VC 20 auf 50556 ($C57C). Dort
beginnt eine Routine, die nach dem Drücken der RETURN-Taste alle Anweisungen
der damit eingegebenen Zeile absucht und Text beziehungsweise Wörter, die nicht
zwischen Gänsefüßen stehen, als Basic-Befehle interpretiert und sie dann in
sogenannte »Token« umwandelt. Token sind Codezahlen, die im Computer anstelle
von Textbefehlen verwendet werden. Sie sind im Texteinschub Nr. 32 »Die
Kurzschrift von Basic« näher beschrieben.

Dieser Vektor kann verbogen werden, um zusätzliche Basic-Befehle zu erfinden
und in das Betriebssystem einzubauen.

### 64map (—)
Vector: Indirect entry to BASIC Tokenise Routine ($A57C)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*