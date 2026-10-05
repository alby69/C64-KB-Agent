---
id: edad-flag-errors
type: entity
title: FLAG ERRORS
aliases:
- FLAG ERRORS
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edad-flag-errors.md
  sha256: d408662dc05dfb325fb93d11f83d887ec6d76827a1b9c5f28e3c093dba8f5b10
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-edad-flag-errors
---

# FLAG ERRORS



# $EDAD — FLAG ERRORS

## Disassemblatura
```assembly
.EDAD  A9 80    LDA #$80   ; flag ?DEVICE NOT PRESENT
.EDAF  2C       .BYTE $2C   ; mask LDA #$03
.EDB0  A9 03    LDA #$03   ; flag write timeout
.EDB2  20 1C FE JSR $FE1C   ; set I/O status word
.EDB5  58       CLI
.EDB6  18       CLC
.EDB7  90 4A    BCC $EE03   ; always jump, do final handshake
```


## Commenti

### Magnus Nyman (Magnus Nyman)
- **$EDAD**: flag ?DEVICE NOT PRESENT
- **$EDAF**: mask LDA #$03
- **$EDB0**: flag write timeout
- **$EDB2**: set I/O status word
- **$EDB7**: always jump, do final handshake

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-edad-flag-errors]]
