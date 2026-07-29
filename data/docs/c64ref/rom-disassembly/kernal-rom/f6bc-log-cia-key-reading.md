---
title: LOG CIA KEY READING
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/magnus_nyman.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0091-stkey
- 00c7-rvs
- f6bc-vom-port
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F6BC
  address_end: $F6DC
  symbol: log-cia-key-reading
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F6BC**: Port B laden'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F6BC**: keyboard read register'
---

# $F6BC — LOG CIA KEY READING

## Disassemblatura
```assembly
.F6BC  AD 01 DC LDA $DC01   ; keyboard read register
.F6BF  CD 01 DC CMP $DC01
.F6C2  D0 F8    BNE $F6BC   ; wait for value to settle
.F6C4  AA       TAX
.F6C5  30 13    BMI $F6DA
.F6C7  A2 BD    LDX #$BD
.F6C9  8E 00 DC STX $DC00   ; keyboard write register
.F6CC  AE 01 DC LDX $DC01   ; keyboard read register
.F6CF  EC 01 DC CPX $DC01
.F6D2  D0 F8    BNE $F6CC   ; wait for value to settle
.F6D4  8D 00 DC STA $DC00
.F6D7  E8       INX
.F6D8  D0 02    BNE $F6DC
.F6DA  85 91    STA $91   ; STKEY, flag STOP/RVS
.F6DC  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F6BC**: Port B laden
- **$F6BF**: und
- **$F6C2**: entprellen
- **$F6C4**: Wert ins X-REG schieben
- **$F6C5**: verzweige falls STOP-Taste nicht gedrückt
- **$F6C7**: Bitmuster zur Abrage der Reihe mit SHIFT-Tasten
- **$F6C9**: in Port A schreiben
- **$F6CC**: Port B laden
- **$F6CF**: und
- **$F6D2**: entprellen
- **$F6D4**: Akku in Port A schreiben
- **$F6D7**: inhalt von Port B erhöhen
- **$F6D8**: verzweige falls ungleich Null (SHIFT-Taste gedrückt)
- **$F6DA**: Flag für Stop-Taste setzen
- **$F6DC**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$F6BC**: keyboard read register
- **$F6C2**: wait for value to settle
- **$F6C9**: keyboard write register
- **$F6CC**: keyboard read register
- **$F6D2**: wait for value to settle
- **$F6DA**: STKEY, flag STOP/RVS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*