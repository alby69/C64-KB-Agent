---
id: fd02-scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found
type: entity
title: scan for autostart ROM at $8000, returns Zb=1 if ROM found
aliases:
- scan for autostart ROM at $8000, returns Zb=1 if ROM found
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd02-scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found.md
  sha256: f9b7cd12dc1dba54d5898e2a0bc3c8e04b2d2b6e6e1d30beb22db7cb38bf2f52
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fd02-scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found
---

# scan for autostart ROM at $8000, returns Zb=1 if ROM found



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
- **$FD02**: five characters to test
- **$FD04**: get test character
- **$FD07**: compare with byte in ROM space
- **$FD0A**: exit if no match
- **$FD0C**: decrement index
- **$FD0D**: loop if not all done

### Commodore-64-intern-Buch (Commodore)
- **$FD02**: Zeiger setzen
- **$FD04**: Wert aus Tabelle holen und
- **$FD07**: ab $8000 vergleichen (CBM80)
- **$FD0A**: verzweige wenn ungleich
- **$FD0C**: Zeiger vermindern
- **$FD0D**: weiter wenn nicht 5 Bytes
- **$FD0F**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FD02**: 5 bytes to check
- **$FD04**: Identifier at $fd10
- **$FD07**: Compare with $8004
- **$FD0A**: NOT equal!
- **$FD0D**: until Z=1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fd02-scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found]]
