---
title: output a byte to the serial bus
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
- eddd-ausgeben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EDDD
  address_end: $EDEE
  symbol: output-a-byte-to-the-serial-bus
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EDDD**: test the deferred character flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EDDD**: noch ein Byte auszugeben ?'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EDDD**: C3PO flag, character in serial buffer'
---

# $EDDD — output a byte to the serial bus

## Disassemblatura
```assembly
.EDDD  24 94    BIT $94   ; test the deferred character flag
.EDDF  30 05    BMI $EDE6   ; if there is a deferred character go send it
.EDE1  38       SEC   ; set carry
.EDE2  66 94    ROR $94   ; shift into the deferred character flag
.EDE4  D0 05    BNE $EDEB   ; save the byte and exit, branch always
.EDE6  48       PHA   ; save the byte
.EDE7  20 40 ED JSR $ED40   ; Tx byte on serial bus
.EDEA  68       PLA   ; restore the byte
.EDEB  85 95    STA $95   ; save the deferred Tx byte
.EDED  18       CLC   ; flag ok
.EDEE  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EDDD**: test the deferred character flag
- **$EDDF**: if there is a deferred character go send it
- **$EDE1**: set carry
- **$EDE2**: shift into the deferred character flag
- **$EDE4**: save the byte and exit, branch always
- **$EDE6**: save the byte
- **$EDE7**: Tx byte on serial bus
- **$EDEA**: restore the byte
- **$EDEB**: save the deferred Tx byte
- **$EDED**: flag ok

### Commodore-64-intern-Buch (Commodore)
- **$EDDD**: noch ein Byte auszugeben ?
- **$EDDF**: verzweige wenn ja
- **$EDE1**: Carry setzen
- **$EDE2**: Flag für gepuffertes Byte setzen
- **$EDE4**: unbedingter Sprung
- **$EDE6**: Byte merken
- **$EDE7**: gepuffertes Byte auf Bus ausgeben
- **$EDEA**: Byte zurückholen und
- **$EDEB**: in Ausgaberegister holen
- **$EDED**: Carry löschen
- **$EDEE**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EDDD**: C3PO flag, character in serial buffer
- **$EDDF**: yes
- **$EDE1**: prepare for ROR
- **$EDE2**: set C3PO
- **$EDE4**: always jump
- **$EDE6**: temp store
- **$EDE7**: send data to serial bus
- **$EDEB**: store character in BSOUR
- **$EDED**: clear carry to indicate no errors

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*