---
id: edc7-send-secondary-address-after-talk
type: entity
title: send secondary address after TALK
aliases:
- send secondary address after TALK
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edc7-send-secondary-address-after-talk.md
  sha256: b25cbae0b3516320e8c8dee140d812ea345b0d66f3123ff0d57fbfcbf95686d6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-edc7-send-secondary-address-after-talk
---

# send secondary address after TALK



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
- **$EDCD**: DATA auf HIGH setzen
- **$EDD0**: ATN rücksetzen, LOW
- **$EDD3**: CLOCK auf LOW setzen
- **$EDD6**: CLOCK-IN holen
- **$EDD9**: auf CLOCK HIGH warten
- **$EDDB**: Interruptflag löschen
- **$EDDC**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EDC7**: BSOUR, the serial bus buffer
- **$EDC9**: handshake and send byte to the bus

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-edc7-send-secondary-address-after-talk]]
