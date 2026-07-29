---
title: ??
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
- ff6e-timer-fr-interrupt-setzen
- indcmp
- primm
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FF6E
  address_end: $FF7D
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF6E**: enable timer A interrupt'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FF6E**: Timer A Unterlauf'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FF80**: kernal version number'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FF6E**: Enable IRQ when timer B reaches zero'
---

# $FF6E — ??

## Disassemblatura
```assembly
.FF6E  A9 81    LDA #$81   ; enable timer A interrupt
.FF70  8D 0D DC STA $DC0D   ; save VIA 1 ICR
.FF73  AD 0E DC LDA $DC0E   ; read VIA 1 CRA
.FF76  29 80    AND #$80   ; mask x000 0000, TOD clock
.FF78  09 11    ORA #$11   ; mask xxx1 xxx1, load timer A, start timer A
.FF7A  8D 0E DC STA $DC0E   ; save VIA 1 CRA
.FF7D  4C 8E EE JMP $EE8E   ; set the serial clock out low and return
```


## Commenti

### Original Disassembly (—)
- **$FF6E**: enable timer A interrupt
- **$FF70**: save VIA 1 ICR
- **$FF73**: read VIA 1 CRA
- **$FF76**: mask x000 0000, TOD clock
- **$FF78**: mask xxx1 xxx1, load timer A, start timer A
- **$FF7A**: save VIA 1 CRA
- **$FF7D**: set the serial clock out low and return

### Commodore-64-intern-Buch (Commodore)
- **$FF6E**: Timer A Unterlauf
- **$FF70**: Interrupt Control Register
- **$FF73**: Control Register A
- **$FF76**: Bit 7 retten Uhrzeittrigger (50/60 Hz)
- **$FF78**: Timer A starten
- **$FF7A**: Control Register A
- **$FF7D**: seriellen Takt aus
- **$FF80**: BReaK

### Marko Mäkelä (Marko Mäkelä)
- **$FF80**: kernal version number

### Magnus Nyman (Magnus Nyman)
- **$FF6E**: Enable IRQ when timer B reaches zero
- **$FF70**: CIA#1 interrupt control register
- **$FF73**: CIA#1 control register A
- **$FF78**: Force load of timer A values -bit4, and start -bit0
- **$FF7A**: Action!
- **$FF7D**: Continue to 'serial clock off'

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*