---
id: e891-output-cr
type: entity
title: output [CR]
aliases:
- output [CR]
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e891-output-cr.md
  sha256: 34afcce73e674a43a51701c836c9ec06307e0b218741b9559e79308fcc378acc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e891-output-cr
---

# output [CR]



# $E891 — output [CR]

## Disassemblatura
```assembly
.E891  A2 00    LDX #$00   ; clear X
.E893  86 D8    STX $D8   ; clear the insert count
.E895  86 C7    STX $C7   ; clear the reverse flag
.E897  86 D4    STX $D4   ; clear the cursor quote flag, $xx = quote, $00 = no quote
.E899  86 D3    STX $D3   ; save the cursor column
.E89B  20 7C E8 JSR $E87C   ; do newline
.E89E  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
```


## Commenti

### Original Disassembly (—)
- **$E891**: clear X
- **$E893**: clear the insert count
- **$E895**: clear the reverse flag
- **$E897**: clear the cursor quote flag, $xx = quote, $00 = no quote
- **$E899**: save the cursor column
- **$E89B**: do newline
- **$E89E**: restore the registers, set the quote flag and exit

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E893**: INSRT, disable insert mode
- **$E895**: RVS, disable reversed mode
- **$E897**: QTSW, disable quotes mode
- **$E899**: PNTR, put cursor at first column
- **$E89B**: go to next line
- **$E89E**: finish screen print

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e891-output-cr]]
