---
id: edbe-set-serial-atn-high
type: entity
title: set serial ATN high
aliases:
- set serial ATN high
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edbe-set-serial-atn-high.md
  sha256: f65e35d89c15287f219630ddc9b94e814140c82270d804670a38be0a99122bfb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-edbe-set-serial-atn-high
---

# set serial ATN high



# $EDBE — set serial ATN high

## Disassemblatura
```assembly
.EDBE  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EDC1  29 F7    AND #$F7   ; mask xxxx 0xxx, set serial ATN high
.EDC3  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.EDC6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EDBE**: read VIA 2 DRA, serial port and video address
- **$EDC1**: mask xxxx 0xxx, set serial ATN high
- **$EDC3**: save VIA 2 DRA, serial port and video address

### Magnus Nyman (Magnus Nyman)
- **$EDBE**: serial bus I/O port
- **$EDC1**: clear bit4, ie. ATN 1
- **$EDC3**: store to port

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-edbe-set-serial-atn-high]]
