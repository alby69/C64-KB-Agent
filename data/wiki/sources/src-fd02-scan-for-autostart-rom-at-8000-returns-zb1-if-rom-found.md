---
id: src-fd02-scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found
type: source
title: 'Source Summary: scan for autostart ROM at $8000, returns Zb=1 if ROM found'
aliases:
- scan for autostart ROM at $8000, returns Zb=1 if ROM found
- fd02-scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd02-scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found.md
  sha256: f9b7cd12dc1dba54d5898e2a0bc3c8e04b2d2b6e6e1d30beb22db7cb38bf2f52
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scan for autostart ROM at $8000, returns Zb=1 if ROM found

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fd02-scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found.md`
**SHA256**: `f9b7cd12dc1dba54d5898e2a0bc3c8e04b2d2b6e6e1d30beb22db7cb38bf2f52`

## Summary



# $FD02 — scan for autostart ROM at $8000, returns Zb=1 if ROM found

## Disassemblatura
```assembly
.FD02  A2 05    LDX #$05   ; five characters to test
.FD04  BD 0F FD LDA $FD0F,X   ; get test character
.FD07  DD 03 80 CMP $8003,X   ; compare with byte in ROM space
.FD0A  D0 03    BNE $FD0F   ; exit if no match
.FD0C  CA       DEX   ; decrement index
.FD0D  D0 F5    BNE $FD04   ; loop if not all done
.FD0F  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FD02**: five charac...
