---
title: write tape leader IRQ routine
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
- fc6a-schreiben
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FC6A
  address_end: $FC91
  symbol: write-tape-leader-irq-routine
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FC6A**: set time constant low byte for bit = leader'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FC6A**: 120'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FC6A — write tape leader IRQ routine

## Disassemblatura
```assembly
.FC6A  A9 78    LDA #$78   ; set time constant low byte for bit = leader
.FC6C  20 AF FB JSR $FBAF   ; write time constant and toggle tape
.FC6F  D0 E3    BNE $FC54   ; if tape bit high restore registers and exit interrupt
.FC71  C6 A7    DEC $A7   ; decrement cycle count
.FC73  D0 DF    BNE $FC54   ; if not all done restore registers and exit interrupt
.FC75  20 97 FB JSR $FB97   ; new tape byte setup
.FC78  C6 AB    DEC $AB   ; decrement cassette leader count
.FC7A  10 D8    BPL $FC54   ; if not all done restore registers and exit interrupt
.FC7C  A2 0A    LDX #$0A   ; set index for tape write vector
.FC7E  20 BD FC JSR $FCBD   ; set the tape vector
.FC81  58       CLI   ; enable the interrupts
.FC82  E6 AB    INC $AB   ; clear cassette leader counter, was $FF
.FC84  A5 BE    LDA $BE   ; get cassette block count
.FC86  F0 30    BEQ $FCB8   ; if all done restore everything for STOP and exit the interrupt
.FC88  20 8E FB JSR $FB8E   ; copy I/O start address to buffer address
.FC8B  A2 09    LDX #$09   ; set nine synchronisation bytes
.FC8D  86 A5    STX $A5   ; save cassette synchronization byte count
.FC8F  86 B6    STX $B6
.FC91  D0 83    BNE $FC16   ; go do the next tape byte, branch always
```


## Commenti

### Original Disassembly (—)
- **$FC6A**: set time constant low byte for bit = leader
- **$FC6C**: write time constant and toggle tape
- **$FC6F**: if tape bit high restore registers and exit interrupt
- **$FC71**: decrement cycle count
- **$FC73**: if not all done restore registers and exit interrupt
- **$FC75**: new tape byte setup
- **$FC78**: decrement cassette leader count
- **$FC7A**: if not all done restore registers and exit interrupt
- **$FC7C**: set index for tape write vector
- **$FC7E**: set the tape vector
- **$FC81**: enable the interrupts
- **$FC82**: clear cassette leader counter, was $FF
- **$FC84**: get cassette block count
- **$FC86**: if all done restore everything for STOP and exit the interrupt
- **$FC88**: copy I/O start address to buffer address
- **$FC8B**: set nine synchronisation bytes
- **$FC8D**: save cassette synchronization byte count
- **$FC91**: go do the next tape byte, branch always

### Commodore-64-intern-Buch (Commodore)
- **$FC6A**: 120
- **$FC6C**: Bit auf Band schreiben
- **$FC6F**: Rückkehr vom Interrupt
- **$FC71**: Zähler erniedrigen
- **$FC73**: nicht null, dann Rückkehr vom Interrupt
- **$FC75**: Bitzähler für serielle Ausgabe setzen
- **$FC78**: falls Datenende nicht er- reicht, dann
- **$FC7A**: Rückkehr vom Interrupt
- **$FC7C**: IRQ
- **$FC7E**: IRQ auf $FBCD
- **$FC81**: Interrupt ermöglichen
- **$FC82**: Shortdauer
- **$FC84**: Zähler für Anzahl der Blocks
- **$FC86**: alle Blocks geschrieben ?
- **$FC88**: Adresse wieder auf Anfang setzen
- **$FC8B**: Zähler für
- **$FC8D**: Synchronisation
- **$FC8F**: Flag für Block geschrieben
- **$FC91**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*