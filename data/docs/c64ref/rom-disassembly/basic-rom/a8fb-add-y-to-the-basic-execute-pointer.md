---
title: add Y to the BASIC execute pointer
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
- a8fb-add-y-to-txtptr
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $A8FB
  address_end: $A905
  symbol: add-y-to-the-basic-execute-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A8FB**: copy index to A'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $A8FB — add Y to the BASIC execute pointer

## Disassemblatura
```assembly
.A8FB  98       TYA   ; copy index to A
.A8FC  18       CLC   ; clear carry for add
.A8FD  65 7A    ADC $7A   ; add BASIC execute pointer low byte
.A8FF  85 7A    STA $7A   ; save BASIC execute pointer low byte
.A901  90 02    BCC $A905   ; skip increment if no carry
.A903  E6 7B    INC $7B   ; else increment BASIC execute pointer high byte
.A905  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A8FB**: copy index to A
- **$A8FC**: clear carry for add
- **$A8FD**: add BASIC execute pointer low byte
- **$A8FF**: save BASIC execute pointer low byte
- **$A901**: skip increment if no carry
- **$A903**: else increment BASIC execute pointer high byte

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*