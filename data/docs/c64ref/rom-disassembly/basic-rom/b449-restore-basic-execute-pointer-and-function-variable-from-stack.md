---
title: restore BASIC execute pointer and function variable from stack
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b449-restore-basic-execute-pointer-and-function-variable-from-stack
- b44f-store-five-bytes-from-stack-at-fncnam
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $B449
  address_end: $B464
  symbol: restore-basic-execute-pointer-and-function-variable-from-stack
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B449**: pull BASIC execute pointer low byte'
---

# $B449 — restore BASIC execute pointer and function variable from stack

## Disassemblatura
```assembly
.B449  68       PLA   ; pull BASIC execute pointer low byte
.B44A  85 7A    STA $7A   ; save BASIC execute pointer low byte
.B44C  68       PLA   ; pull BASIC execute pointer high byte
.B44D  85 7B    STA $7B   ; save BASIC execute pointer high byte put execute pointer and variable pointer into function
.B44F  A0 00    LDY #$00   ; clear index
.B451  68       PLA   ; pull BASIC execute pointer low byte
.B452  91 4E    STA ($4E),Y   ; save to function
.B454  68       PLA   ; pull BASIC execute pointer high byte
.B455  C8       INY   ; increment index
.B456  91 4E    STA ($4E),Y   ; save to function
.B458  68       PLA   ; pull current variable address low byte
.B459  C8       INY   ; increment index
.B45A  91 4E    STA ($4E),Y   ; save to function
.B45C  68       PLA   ; pull current variable address high byte
.B45D  C8       INY   ; increment index
.B45E  91 4E    STA ($4E),Y   ; save to function
.B460  68       PLA   ; pull ??
.B461  C8       INY   ; increment index
.B462  91 4E    STA ($4E),Y   ; save to function
.B464  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B449**: pull BASIC execute pointer low byte
- **$B44A**: save BASIC execute pointer low byte
- **$B44C**: pull BASIC execute pointer high byte
- **$B44D**: save BASIC execute pointer high byte put execute pointer and variable pointer into function
- **$B44F**: clear index
- **$B451**: pull BASIC execute pointer low byte
- **$B452**: save to function
- **$B454**: pull BASIC execute pointer high byte
- **$B455**: increment index
- **$B456**: save to function
- **$B458**: pull current variable address low byte
- **$B459**: increment index
- **$B45A**: save to function
- **$B45C**: pull current variable address high byte
- **$B45D**: increment index
- **$B45E**: save to function
- **$B460**: pull ??
- **$B461**: increment index
- **$B462**: save to function

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*