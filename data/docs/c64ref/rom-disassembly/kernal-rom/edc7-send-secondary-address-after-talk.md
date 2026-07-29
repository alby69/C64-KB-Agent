---
title: send secondary address after TALK
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- edc7-ausgeben
- talk
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EDC7
  address_end: $EDC9
  symbol: send-secondary-address-after-talk
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EDC7**: save the deferred Tx byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EDC7**: Sekundäradresse speichern'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EDC7**: BSOUR, the serial bus buffer'
---

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