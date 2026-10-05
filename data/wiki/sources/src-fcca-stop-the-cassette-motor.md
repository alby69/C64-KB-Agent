---
id: src-fcca-stop-the-cassette-motor
type: source
title: 'Source Summary: stop the cassette motor'
aliases:
- stop the cassette motor
- fcca-stop-the-cassette-motor.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fcca-stop-the-cassette-motor.md
  sha256: 28093471e4193442f123af2193e026c2d0285109757ef2db632ac9de0e5db11e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: stop the cassette motor

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fcca-stop-the-cassette-motor.md`
**SHA256**: `28093471e4193442f123af2193e026c2d0285109757ef2db632ac9de0e5db11e`

## Summary



# $FCCA — stop the cassette motor

## Disassemblatura
```assembly
.FCCA  A5 01    LDA $01   ; read the 6510 I/O port
.FCCC  09 20    ORA #$20   ; mask xxxx xx1x, turn the cassette motor off
.FCCE  85 01    STA $01   ; save the 6510 I/O port
.FCD0  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FCCA**: read the 6510 I/O port
- **$FCCC**: mask xxxx xx1x, turn the cassette motor off
- **$FCCE**: save the 6510 I/O port

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile...
