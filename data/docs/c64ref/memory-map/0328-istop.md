---
title: Test-STOP vector ($F6ED)
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
- f6ed-stop-taste-abfragen
- stop
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
  address: $0328
  address_end: $0329
  symbol: ISTOP
  sources:
  - name: Original Source Comments
    author: Microsoft/Commodore
    description: ''
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: $F6ED STOP-Vektor
  - name: C64 Programmer's Reference Guide
    author: Commodore
    description: KERNAL STOP Routine Vector
  - name: Memory Map
    author: Jim Butterfield
    description: Test-STOP vector ($F6ED)
  - name: Mapping the Commodore 64
    author: Sheldon Leemon
    description: This vector points to the address of the routine that tests the STOP
  - name: Reference
    author: Joe Forster / STA
    description: 'Default: $F6ED.'
  - name: 64'er Magazin
    author: 64'er
    description: Der Vektor zeigt auf die Adresse 63213 ($F6ED) - beim VC 20 auf 63344
      ($F770).
  - name: 64map
    author: —
    description: 'Vector: Indirect entry to Kernal STOP Routine ($F6ED)'
---

# ISTOP — Test-STOP vector ($F6ED) ($0328)

## Panoramica
Il registro o area di memoria ISTOP è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0328` (`808` decimale)
- **Range**: `$0328`-`$0329`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F6ED STOP-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL STOP Routine Vector

### Memory Map (Jim Butterfield)
Test-STOP vector ($F6ED)

### Mapping the Commodore 64 (Sheldon Leemon)
This vector points to the address of the routine that tests the STOP
key.  The STOP key can be disabled by changing this with a POKE
808,239.  This will not disable the STOP/RESTORE combination, however.
To disable both STOP and STOP/ RESTORE, POKE 808,234 (POKEing 234 here
will cause the LIST command not to function properly).  To bring
things back to normal in either case, POKE 808, 237.

### Reference (Joe Forster / STA)
Default: $F6ED.

### 64'er Magazin (64'er)
Der Vektor zeigt auf die Adresse 63213 ($F6ED) - beim VC 20 auf 63344 ($F770).
Die dort beginnende Routine prüft, ob die STOP-Taste gedrückt ist. Durch
Verbiegen dieses Vektors kann die STOP-Taste abgeschaltet werden. Beim C 64
geht dies mit POKE 808,239; wieder eingeschaltet wird die STOP-Taste mit POKE
808,237. Beim VC 20 sind die Werte POKE 808,100 beziehungsweise POKE 808,112.

### 64map (—)
Vector: Indirect entry to Kernal STOP Routine ($F6ED)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*