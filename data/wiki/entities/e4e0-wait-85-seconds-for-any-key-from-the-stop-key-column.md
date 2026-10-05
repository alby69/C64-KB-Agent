---
id: e4e0-wait-85-seconds-for-any-key-from-the-stop-key-column
type: entity
title: wait ~8.5 seconds for any key from the STOP key column
aliases:
- wait ~8.5 seconds for any key from the STOP key column
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e4e0-wait-85-seconds-for-any-key-from-the-stop-key-column.md
  sha256: 421ca4c8287418719c407807487659a6e5ebe8f1f837bb20adcb45a9b8c48471
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e4e0-wait-85-seconds-for-any-key-from-the-stop-key-column
---

# wait ~8.5 seconds for any key from the STOP key column



# $E4E0 — wait ~8.5 seconds for any key from the STOP key column

## Disassemblatura
```assembly
.E4E0  69 02    ADC #$02   ; set the number of jiffies to wait
.E4E2  A4 91    LDY $91   ; read the stop key column
.E4E4  C8       INY   ; test for $FF, no keys pressed
.E4E5  D0 04    BNE $E4EB   ; if any keys were pressed just exit
.E4E7  C5 A1    CMP $A1   ; compare the wait time with the jiffy clock mid byte
.E4E9  D0 F7    BNE $E4E2   ; if not there yet go wait some more
.E4EB  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E4E0**: set the number of jiffies to wait
- **$E4E2**: read the stop key column
- **$E4E4**: test for $FF, no keys pressed
- **$E4E5**: if any keys were pressed just exit
- **$E4E7**: compare the wait time with the jiffy clock mid byte
- **$E4E9**: if not there yet go wait some more

### Commodore-64-intern-Buch (Commodore)
- **$E4E0**: 2*256/60 = 8.5 Sekunden warten
- **$E4E2**: Flag testen
- **$E4E4**: und erhöhen
- **$E4E5**: Taste gedrückt ?
- **$E4E7**: Zeit noch nicht um ?,
- **$E4E9**: dann warten
- **$E4EB**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e4e0-wait-85-seconds-for-any-key-from-the-stop-key-column]]
