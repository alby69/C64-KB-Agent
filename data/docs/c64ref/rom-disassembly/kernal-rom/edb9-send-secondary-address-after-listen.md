---
title: send secondary address after LISTEN
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
- edb9-senden
- listen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EDB9
  address_end: $EDBB
  symbol: send-secondary-address-after-listen
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EDB9**: save the deferred Tx byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EDB9**: Sekundäradresse speichern'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EDB9**: store (A) in BSOUT, buffer for the serial bus'
---

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
- **$EDC1**: ATN rücksetzen, LOW
- **$EDC3**: und ausgeben
- **$EDC6**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EDB9**: store (A) in BSOUT, buffer for the serial bus
- **$EDBB**: handshake and send byte.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*