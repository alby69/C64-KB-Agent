---
title: command serial bus to UNLISTEN
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
- edfe-unlisten-senden
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $EDFE
  address_end: $EE10
  symbol: command-serial-bus-to-unlisten
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EDFE**: set the UNLISTEN command'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EDFE**: Kennzeichnung für UNLISTEN'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $EDFE — command serial bus to UNLISTEN

## Disassemblatura
```assembly
.EDFE  A9 3F    LDA #$3F   ; set the UNLISTEN command
.EE00  20 11 ED JSR $ED11   ; send a control character
.EE03  20 BE ED JSR $EDBE   ; set serial ATN high 1ms delay, clock high then data high
.EE06  8A       TXA   ; save the device number
.EE07  A2 0A    LDX #$0A   ; short delay
.EE09  CA       DEX   ; decrement the count
.EE0A  D0 FD    BNE $EE09   ; loop if not all done
.EE0C  AA       TAX   ; restore the device number
.EE0D  20 85 EE JSR $EE85   ; set the serial clock out high
.EE10  4C 97 EE JMP $EE97   ; set the serial data out high and return
```


## Commenti

### Original Disassembly (—)
- **$EDFE**: set the UNLISTEN command
- **$EE00**: send a control character
- **$EE03**: set serial ATN high 1ms delay, clock high then data high
- **$EE06**: save the device number
- **$EE07**: short delay
- **$EE09**: decrement the count
- **$EE0A**: loop if not all done
- **$EE0C**: restore the device number
- **$EE0D**: set the serial clock out high
- **$EE10**: set the serial data out high and return

### Commodore-64-intern-Buch (Commodore)
- **$EDFE**: Kennzeichnung für UNLISTEN
- **$EE00**: ausgeben
- **$EE03**: ATN rücksetzen, LOW
- **$EE06**: X-Register merken
- **$EE07**: Warteschleife von
- **$EE09**: ca. 40 Mikrosekunden
- **$EE0A**: abwarten
- **$EE0C**: X-Register wiederholen
- **$EE0D**: CLOCK auf LOW setzen
- **$EE10**: DATA auf LOW setzen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*