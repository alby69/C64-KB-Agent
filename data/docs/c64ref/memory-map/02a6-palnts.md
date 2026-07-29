---
title: Flag für PAL- (1) o. NTSC-Version (0)
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
  - c64_programmer's_reference_guide.txt
  - 64map.txt
  address: $02A6
  symbol: PALNTS
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: PAL vs NTSC flag 0=NTSC 1=PAL
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: Hier steht ein Wert, der angibt, ob es
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: PAL/NTSC Flag, 0= NTSC, 1 = PAL
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: At power-on, a test is performed to see if the monitor uses the NTSC
  - name: Reference
    author: Joe Forster / STA
    description: 'Values:'
  - name: 64'er Magazin
    author: 64'er
    description: Im Gegensatz zum VC 20, der entweder fest auf die deutsche Fernsehnorm
      PAL oder
  - name: 64map
    author: —
    description: 'Flag: TV Standard: $00 = NTSC, $01 = PAL'
---

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