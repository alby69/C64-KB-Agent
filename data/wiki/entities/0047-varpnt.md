---
id: 0047-varpnt
type: entity
title: Current variable address
aliases:
- Current variable address
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0047-varpnt.md
  sha256: ed18daacbd67bc2903166bc6b92deeee82a5c26bff6ab094a161ad7502efe35c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0047-varpnt
---

# Current variable address



# VARPNT — Current variable address ($0047)

## Panoramica
Il registro o area di memoria VARPNT è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0047` (`71` decimale)
- **Range**: `$0047`-`$0048`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Pointer to variable in memory

### Original Source Comments (Microsoft/Commodore)
Pointer into power of tens of "FOUT"

### Commodore-64-intern-Buch (Commodore)
In diesen Speicherzellen wird der
Zeiger auf den Variablenwert
abgelegt.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Current BASIC Variable Data

### Memory Map (Jim Butterfield)
Current variable address

### Mapping the Commodore 64 (Sheldon Leemon)
This location points to the address of the descriptor of the current
BASIC variable (see location 45 ($002D) for the format of a variable
descriptor).  Specifically, it points to the byte just after the
two-character variable name.

During a FN call, this location does not point to the dependent
variable (the A of FN A), so that a real variable of the same name
will not have its value changed by the call.

### Reference (Joe Forster / STA)
Pointer to value of current variable or FN function

### 64'er Magazin (64'er)
Ähnlich wie bei 69 und 70 wird hier während des Anrufes einer Variablen durch
ein Programm ein Wert zwischengespeichert, diesmal aber nicht der Name der
Variablen, sondern der 2-Byte-Wert, welcher direkt hinter dem Variablennamen
steht. Nähere Einzelheiten sind im Text der Speicherzellen 45 und 46
beschrieben.

Davon ausgenommen sind selbstdefinierte Funktionen. Wie im Texteinschub Nr. 12
»Darstellung der Variablen einer selbstdefinierten Funktion« gezeigt ist,
erscheinen diese ebenfalls im Variablenspeicher in einer Darstellung, welche
den normalen Variablen sehr ähnlich ist.

Damit nun eine normale oder Feld-Variable denselben Namen haben kann wie eine
Funktion, wird die oben genannte Zwischenspeicherung in 69 und 70 bei
Funktionen unterdrückt.

### 64map (—)
Pointer: to value of (VARNAM) if Integer, to descriptor if String

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0047-varpnt]]
