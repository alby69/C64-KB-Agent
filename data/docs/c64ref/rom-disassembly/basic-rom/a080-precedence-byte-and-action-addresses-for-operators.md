---
title: precedence byte and action addresses for operators
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a080-adressen-1-der-operatoren
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A080
  address_end: $A09B
  symbol: precedence-byte-and-action-addresses-for-operators
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A080**: +'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A080**: $79, $B86A Addition'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A080**: plus'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A080**: $79, $B86A +'
---

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