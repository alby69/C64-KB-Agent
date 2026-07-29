---
title: restore BASIC execute pointer from temp
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
- b7e2-copy-strng2-into-txtptr
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $B7E2
  address_end: $B7EA
  symbol: restore-basic-execute-pointer-from-temp
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B7E2**: get BASIC execute pointer low byte back'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B7E2 — restore BASIC execute pointer from temp

## Disassemblatura
```assembly
.B7E2  A6 71    LDX $71   ; get BASIC execute pointer low byte back
.B7E4  A4 72    LDY $72   ; get BASIC execute pointer high byte back
.B7E6  86 7A    STX $7A   ; save BASIC execute pointer low byte
.B7E8  84 7B    STY $7B   ; save BASIC execute pointer high byte
.B7EA  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B7E2**: get BASIC execute pointer low byte back
- **$B7E4**: get BASIC execute pointer high byte back
- **$B7E6**: save BASIC execute pointer low byte
- **$B7E8**: save BASIC execute pointer high byte

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*