---
id: edfe-command-serial-bus-to-unlisten
type: entity
title: command serial bus to UNLISTEN
aliases:
- command serial bus to UNLISTEN
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edfe-command-serial-bus-to-unlisten.md
  sha256: b46a4271a324f85e7b6d77d73ea26d923b3e0d2c3a543997ccd73469e7bb29da
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-edfe-command-serial-bus-to-unlisten
---

# command serial bus to UNLISTEN



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

## References
- Source: [[src-edfe-command-serial-bus-to-unlisten]]
