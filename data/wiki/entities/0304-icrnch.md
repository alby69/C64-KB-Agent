---
id: 0304-icrnch
type: entity
title: Crunch Basic tokens link
aliases:
- Crunch Basic tokens link
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0304-icrnch.md
  sha256: 8d88981d36ab999b640cfd713325eb12449a53464bb08604b200c145d8b6fa40
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0304-icrnch
---

# Crunch Basic tokens link



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

## References
- Source: [[src-0304-icrnch]]
