---
title: wait ~8.5 seconds for any key from the STOP key column
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
- e4e0-wartet-auf-commodore-taste
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E4E0
  address_end: $E4EB
  symbol: wait-85-seconds-for-any-key-from-the-stop-key-column
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E4E0**: set the number of jiffies to wait'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E4E0**: 2*256/60 = 8.5 Sekunden warten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: Nessun commento disponibile.
---

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