---
title: perform STOP
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
- a82f-basic-befehl-stop
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A82F
  address_end: $A82F
  symbol: perform-stop
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A82F**: if carry set do BREAK instead of just END'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A82F**: C=1: Flag für STOP'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A82F**: CARRY=1 TO FORCE PRINTING "BREAK AT.."'
---

# $A82F — perform STOP

## Disassemblatura
```assembly
.A82F  B0 01    BCS $A832   ; if carry set do BREAK instead of just END
```


## Commenti

### Original Disassembly (—)
- **$A82F**: if carry set do BREAK instead of just END

### Commodore-64-intern-Buch (Commodore)
- **$A82F**: C=1: Flag für STOP

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A82F**: CARRY=1 TO FORCE PRINTING "BREAK AT.."

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*