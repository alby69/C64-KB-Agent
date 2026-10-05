---
id: 0328-istop
type: entity
title: Test-STOP vector ($F6ED)
aliases:
- Test-STOP vector ($F6ED)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0328-istop.md
  sha256: 2ce574817ed0a0fb2304a2395054212578b235a9dd25cab74e1360c4fa57b2ce
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0328-istop
---

# Test-STOP vector ($F6ED)



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

## References
- Source: [[src-0328-istop]]
