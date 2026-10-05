---
id: 000e-intflg
type: entity
title: 'Type : 80 = integer, 00 = floating point'
aliases:
- 'Type : 80 = integer, 00 = floating point'
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/000e-intflg.md
  sha256: 6e9a85c57bf17252050cfeae420d69b0e7b17d481298328c90b90ef82f565fad
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-000e-intflg
---

# Type : 80 = integer, 00 = floating point



# INTFLG — Type : 80 = integer, 00 = floating point ($000E)

## Panoramica
Il registro o area di memoria INTFLG è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$000E` (`14` decimale)
- **Range**: `$000E`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Tells if integer

### Commodore-64-intern-Buch (Commodore)
Wenn eine Gleitkommazahl auftritt,
steht in der Speicherzelle $00, bei
einer ganzen Zahl eine $80.

### C64 Programmer's Reference Guide (Commodore)
Data Type: $80 = Integer, $00 = Floating

### Memory Map (Jim Butterfield)
Type : 80 = integer, 00 = floating point

### Mapping the Commodore 64 (Sheldon Leemon)
If data which BASIC is using is determined to be numeric, it is
further classified here as either a floating point number or as an
integer.  A 128 ($80) in this location identifies the number as an
integer, and a 0 indicates a floating point number.

### Reference (Joe Forster / STA)
Bits:

* Bit #7: 0 = Floating point; 1 = Integer.

### 64'er Magazin (64'er)
Sobald durch die Flagge in der vorherigen Zelle 13 eine Zahl signalisiert wird,
steht hier die Zahl 128 ($80), wenn es sich um eine ganze Zahl handelt, während
eine 0 die Zahl als Gleitkommazahl identifiziert.

Damit wollen wir ein bißchen experimentieren. Zeile 10 definiert eine
Gleitkommazahl, Zeile 20 druckt sie und die Flagge aus Zelle 14 aus.

    10 A=13.41
    20 PRINT A,PEEK (14)

Wir erhalten dieZahl 13.41 und als Flagge eine 0.

    30 B=INT (A)
    40 PRINT B,PEEK (14)

INT bildet die ganze Zahl von 13.41. Also müßte die Flagge in Zelle 14 auf 128
stehen. Weit gefehlt! Da intern auch die 13 als Gleitkommazahl berechnet wird,
erhalten wir immer noch eine 0.

    50 B%=A
    60 PRINT B%,PEEK (14)

Erst die Definition der Variablen B als ganze Zahl (mit %) ergibt die Flagge
128.

    70 D=16*B%
    80 PRINT D,PEEK (14)

Die Multiplikation einer ganzen Zahl mit der Ganzzahl-Variablen B% fällt in
dieselbe Kategorie wie Zeile 30 oben, da die Verarbeitung als Gleitkommazahl
erfolgt. Also erhalten wir zu Recht eine 0. Erst wenn D als ganze Zahl (Zeile
90) ausgewiesen wird, steht die Flagge wieder auf 128:

    90 D%=16*B%
    100 PRINT D%, PEEK (14)

### 64map (—)
Data type Flag: $00 = Floating point, $80 = Integer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-000e-intflg]]
