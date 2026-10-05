---
id: src-edc7-send-secondary-address-after-talk
type: source
title: 'Source Summary: send secondary address after TALK'
aliases:
- send secondary address after TALK
- edc7-send-secondary-address-after-talk.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edc7-send-secondary-address-after-talk.md
  sha256: b25cbae0b3516320e8c8dee140d812ea345b0d66f3123ff0d57fbfcbf95686d6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: send secondary address after TALK

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/edc7-send-secondary-address-after-talk.md`
**SHA256**: `b25cbae0b3516320e8c8dee140d812ea345b0d66f3123ff0d57fbfcbf95686d6`

## Summary



# $EDC7 — send secondary address after TALK

## Disassemblatura
```assembly
.EDC7  85 95    STA $95   ; save the deferred Tx byte
.EDC9  20 36 ED JSR $ED36   ; set the serial clk/data, wait and Tx the byte
```


## Commenti

### Original Disassembly (—)
- **$EDC7**: save the deferred Tx byte
- **$EDC9**: set the serial clk/data, wait and Tx the byte

### Commodore-64-intern-Buch (Commodore)
- **$EDC7**: Sekundäradresse speichern
- **$EDC9**: mit ATN ausgeben
- **$EDCC**: Interruptflag setzen
-...
