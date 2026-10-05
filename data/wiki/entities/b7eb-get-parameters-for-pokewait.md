---
id: b7eb-get-parameters-for-pokewait
type: entity
title: get parameters for POKE/WAIT
aliases:
- get parameters for POKE/WAIT
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b7eb-get-parameters-for-pokewait.md
  sha256: 2b8e73330a4a4bb5ac276d01a3faf8d6229121e3d6af121eae1d902d58d4a1dc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b7eb-get-parameters-for-pokewait
---

# get parameters for POKE/WAIT



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

## References
- Source: [[src-b7eb-get-parameters-for-pokewait]]
