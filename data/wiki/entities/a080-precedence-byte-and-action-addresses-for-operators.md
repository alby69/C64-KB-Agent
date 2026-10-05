---
id: a080-precedence-byte-and-action-addresses-for-operators
type: entity
title: precedence byte and action addresses for operators
aliases:
- precedence byte and action addresses for operators
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a080-precedence-byte-and-action-addresses-for-operators.md
  sha256: 232ab312f320d386b0b160cd7261aaa9bdc2637e81e2fb689e9b92298415fbd0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a080-precedence-byte-and-action-addresses-for-operators
---

# precedence byte and action addresses for operators



# $A080 — precedence byte and action addresses for operators

## Disassemblatura
```assembly
.A080  79 69 B8   ; +
.A083  79 52 B8   ; -
.A086  7B 2A BA   ; *
.A089  7B 11 BB   ; /
.A08C  7F 7A BF   ; ^
.A08F  50 E8 AF   ; AND
.A092  46 E5 AF   ; OR
.A095  7D B3 BF   ; >
.A098  5A D3 AE   ; =
.A09B  64 15 B0   ; <
```


## Commenti

### Original Disassembly (—)
- **$A080**: +
- **$A083**: -
- **$A086**: *
- **$A089**: /
- **$A08C**: ^
- **$A08F**: AND
- **$A092**: OR
- **$A095**: >
- **$A098**: =
- **$A09B**: <

### Commodore-64-intern-Buch (Commodore)
- **$A080**: $79, $B86A Addition
- **$A083**: $79, $B853 Subtraktion
- **$A086**: $7B, $BA2B Multiplikation
- **$A089**: $7B, $BB12 Division
- **$A08C**: $7F, $BF7B Potenzierung
- **$A08F**: $50, $AFE9 AND
- **$A092**: $46, $AFE6 OR
- **$A095**: $7D, $BFB4 Vorzeichenwechsel
- **$A098**: $5A, $AED4 NOT
- **$A09B**: $64, $B016 Vergleich

### Marko Mäkelä (Marko Mäkelä)
- **$A080**: plus
- **$A083**: minus
- **$A086**: multiply
- **$A089**: divide
- **$A08C**: power
- **$A08F**: AND
- **$A092**: OR
- **$A095**: negative
- **$A098**: NOT
- **$A09B**: greater / equal / less

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A080**: $79, $B86A +
- **$A083**: $79, $B853 -
- **$A086**: $7B, $BA2B *
- **$A089**: $7B, $BB12 /
- **$A08C**: $7F, $BF7B ^
- **$A08F**: $50, $AFE9 AND
- **$A092**: $46, $AFE6 OR (LOWEST PRECEDENCE)
- **$A095**: $7D, $BFB4 >
- **$A098**: $5A, $AED4 =
- **$A09B**: $64, $B016 <

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a080-precedence-byte-and-action-addresses-for-operators]]
