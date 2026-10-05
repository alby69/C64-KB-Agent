---
id: b853-perform-subtraction-fac1-from-fac2
type: entity
title: perform subtraction, FAC1 from FAC2
aliases:
- perform subtraction, FAC1 from FAC2
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b853-perform-subtraction-fac1-from-fac2.md
  sha256: 3bfc616a2f5d8d8bfa97311b7f1ef5074a142c2213428840e7534f4ff53ce131
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b853-perform-subtraction-fac1-from-fac2
---

# perform subtraction, FAC1 from FAC2



# $B853 — perform subtraction, FAC1 from FAC2

## Disassemblatura
```assembly
.B853  A5 66    LDA $66   ; get FAC1 sign (b7)
.B855  49 FF    EOR #$FF   ; complement it
.B857  85 66    STA $66   ; save FAC1 sign (b7)
.B859  45 6E    EOR $6E   ; EOR with FAC2 sign (b7)
.B85B  85 6F    STA $6F   ; save sign compare (FAC1 EOR FAC2)
.B85D  A5 61    LDA $61   ; get FAC1 exponent
.B85F  4C 6A B8 JMP $B86A   ; add FAC2 to FAC1 and return
.B862  20 99 B9 JSR $B999   ; shift FACX A times right (>8 shifts)
.B865  90 3C    BCC $B8A3   ; go subtract mantissas
```


## Commenti

### Original Disassembly (—)
- **$B853**: get FAC1 sign (b7)
- **$B855**: complement it
- **$B857**: save FAC1 sign (b7)
- **$B859**: EOR with FAC2 sign (b7)
- **$B85B**: save sign compare (FAC1 EOR FAC2)
- **$B85D**: get FAC1 exponent
- **$B85F**: add FAC2 to FAC1 and return
- **$B862**: shift FACX A times right (>8 shifts)
- **$B865**: go subtract mantissas

### Commodore-64-intern-Buch (Commodore)
- **$B853**: Die
- **$B855**: Vorzeichen
- **$B857**: umdrehen
- **$B859**: mit Vorzeichen von FAC
- **$B85B**: verknüpfen
- **$B85D**: Exponent von FAC
- **$B85F**: FAC = FAC + ARG
- **$B862**: Exponenten von FAC und ARG
- **$B865**: angleichen

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B853**: COMPLEMENT FAC AND ADD
- **$B859**: FIX SGNCPR TOO
- **$B85D**: MAKE STATUS SHOW FAC EXPONENT
- **$B85F**: JOIN FADD

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b853-perform-subtraction-fac1-from-fac2]]
