---
title: get parameters for POKE/WAIT
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
- b7eb-16-bit-und-8-bit-wert
- b7f1-evaluate-expression
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B7EB
  address_end: $B7F4
  symbol: get-parameters-for-pokewait
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B7EB**: evaluate expression and check is numeric, else do type
      mismatch'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B7EB**: FRMNUM holt numerischen Wert'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B7EB — get parameters for POKE/WAIT

## Disassemblatura
```assembly
.B7EB  20 8A AD JSR $AD8A   ; evaluate expression and check is numeric, else do type mismatch
.B7EE  20 F7 B7 JSR $B7F7   ; convert FAC_1 to integer in temporary integer
.B7F1  20 FD AE JSR $AEFD   ; scan for ",", else do syntax error then warm start
.B7F4  4C 9E B7 JMP $B79E   ; get byte parameter and return
```


## Commenti

### Original Disassembly (—)
- **$B7EB**: evaluate expression and check is numeric, else do type mismatch
- **$B7EE**: convert FAC_1 to integer in temporary integer
- **$B7F1**: scan for ",", else do syntax error then warm start
- **$B7F4**: get byte parameter and return

### Commodore-64-intern-Buch (Commodore)
- **$B7EB**: FRMNUM holt numerischen Wert
- **$B7EE**: FAC in Adressformat wandlen $14/$15
- **$B7F1**: CHKCOM prüft auf Komma
- **$B7F4**: holt Byte-Wert nach X

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*