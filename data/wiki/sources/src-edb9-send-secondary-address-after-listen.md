---
id: src-edb9-send-secondary-address-after-listen
type: source
title: 'Source Summary: send secondary address after LISTEN'
aliases:
- send secondary address after LISTEN
- edb9-send-secondary-address-after-listen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edb9-send-secondary-address-after-listen.md
  sha256: 3c87726fcbfc1a141ea9ec5c6b97d412ce3a791576ebc89104964cb01375c11b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: send secondary address after LISTEN

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/edb9-send-secondary-address-after-listen.md`
**SHA256**: `3c87726fcbfc1a141ea9ec5c6b97d412ce3a791576ebc89104964cb01375c11b`

## Summary



# $EDB9 — send secondary address after LISTEN

## Disassemblatura
```assembly
.EDB9  85 95    STA $95   ; save the deferred Tx byte
.EDBB  20 36 ED JSR $ED36   ; set the serial clk/data, wait and Tx the byte
```


## Commenti

### Original Disassembly (—)
- **$EDB9**: save the deferred Tx byte
- **$EDBB**: set the serial clk/data, wait and Tx the byte

### Commodore-64-intern-Buch (Commodore)
- **$EDB9**: Sekundäradresse speichern
- **$EDBB**: mit ATN HIGH ausgeben
- **$EDBE**: Port A laden
- ...
