---
title: pack FAC1 into $5C
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
- bbc7-round-fac-store-in-temp2
- bit
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $BBC7
  address_end: $BBC9
  symbol: pack-fac1-into-5c
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BBC7**: set pointer low byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$BBC7**: low  005C'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BBC7**: PACK FAC INTO TEMP2'
---

# $BBC7 — pack FAC1 into $5C

## Disassemblatura
```assembly
.BBC7  A2 5C    LDX #$5C   ; set pointer low byte
.BBC9  2C       .BYTE $2C   ; makes next line BIT $57A2
```


## Commenti

### Original Disassembly (—)
- **$BBC7**: set pointer low byte
- **$BBC9**: makes next line BIT $57A2

### Marko Mäkelä (Marko Mäkelä)
- **$BBC7**: low  005C

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BBC7**: PACK FAC INTO TEMP2
- **$BBC9**: TRICK TO BRANCH

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*