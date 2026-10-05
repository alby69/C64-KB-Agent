---
id: 02a6-palnts
type: entity
title: Flag für PAL- (1) o. NTSC-Version (0)
aliases:
- Flag für PAL- (1) o. NTSC-Version (0)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/02a6-palnts.md
  sha256: a3a16378092da58888c5a8c9f75f4f299ba00b806a0f1ae176a2d6470f5606b9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-02a6-palnts
---

# Flag für PAL- (1) o. NTSC-Version (0)



# PALNTS — Flag für PAL- (1) o. NTSC-Version (0) ($02A6)

## Panoramica
Il registro o area di memoria PALNTS è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$02A6` (`678` decimale)
- **Range**: `$02A6`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
PAL vs NTSC flag 0=NTSC 1=PAL

### Commodore-64-intern-Buch (Commodore)
Hier steht ein Wert, der angibt, ob es
sich um eine PAL- oder eine NTSC-
Version handelt.

### C64 Programmer's Reference Guide (Commodore)
PAL/NTSC Flag, 0= NTSC, 1 = PAL

### Mapping the Commodore 64 (Sheldon Leemon)
At power-on, a test is performed to see if the monitor uses the NTSC
(North American) or PAL (European) television standard.

This test is accomplished by setting a raster interrupt for scan line
311, and testing if the interrupt occurs.  Since NTSC monitors have
only 262 raster scan lines per screen, the interrupt will occur only
if a PAL monitor is used.  The results of that test are stored here,
with a 0 indicating an NTSC system in use, and one signifying a PAL
system.

This information is used by the routines which set the prescaler
values for the system IRQ timer, so that the IRQ occurs every 1/60
second.  Since the PAL system 02 clock runs a bit slower than the NTSC
version, this prescaler value must be adjusted accordingly.

### Reference (Joe Forster / STA)
Values:

* $00: NTSC.
* $01: PAL.

### 64'er Magazin (64'er)
Im Gegensatz zum VC 20, der entweder fest auf die deutsche Fernsehnorm PAL oder
aber auf die amerikanische Norm NTSC eingestellt ist, kann der C 64 beide
Normen verkraften. Diese beiden Normen beziehen sich unter anderem auf die
Anzahl der Zeilen und auf die Abtast-Geschwindigkeit des Lichtstrahls im
Fernsehgerät oder im Monitor. Das Betriebssystem des C 64 überprüft gleich beim
Einschalten, ob eine Rasterzeile 311 im angeschlossenen Sichtgerät vorhanden
ist. Ist sie nicht vorhanden, muß alles auf die NTSC-Norm eingestellt werden,
da diese nur 262 Rasterzeilen hat und mit einer internen Taktfrequenz von 14,3
MHz läuft. Ist eine Rasterzeile 311 vorhanden, wird auf PAL-Norm eingestellt
mit einer Taktfrequenz von 17,7 MHz. Das Resultat dieses Tests wird in der
Speicherzelle 678 gespeichert: als 0 für NTSC und 1 für PAL.

### 64map (—)
Flag: TV Standard: $00 = NTSC, $01 = PAL

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-02a6-palnts]]
