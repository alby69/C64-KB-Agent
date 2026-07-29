---
title: RS232 Rx NMI
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
- ef59-empfangenes-bit-verarbeiten
- ef6e-handle-end-of-word-for-rs-232-input
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EF59
  address_end: $EF7C
  symbol: rs232-rx-nmi
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF59**: get start bit check flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EF59**: Startbit ?'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EF59**: RINONE, check for start bit?'
---

# $EF59 — RS232 Rx NMI

## Disassemblatura
```assembly
.EF59  A6 A9    LDX $A9   ; get start bit check flag
.EF5B  D0 33    BNE $EF90   ; if no start bit received go ??
.EF5D  C6 A8    DEC $A8   ; decrement receiver bit count in
.EF5F  F0 36    BEQ $EF97   ; if the byte is complete go add it to the buffer
.EF61  30 0D    BMI $EF70
.EF63  A5 A7    LDA $A7   ; get the RS232 received data bit
.EF65  45 AB    EOR $AB   ; EOR with the receiver parity bit
.EF67  85 AB    STA $AB   ; save the receiver parity bit
.EF69  46 A7    LSR $A7   ; shift the RS232 received data bit
.EF6B  66 AA    ROR $AA
.EF6D  60       RTS
.EF6E  C6 A8    DEC $A8   ; decrement receiver bit count in
.EF70  A5 A7    LDA $A7   ; get the RS232 received data bit
.EF72  F0 67    BEQ $EFDB
.EF74  AD 93 02 LDA $0293   ; get pseudo 6551 control register
.EF77  0A       ASL   ; shift the stop bit flag to Cb
.EF78  A9 01    LDA #$01   ; + 1
.EF7A  65 A8    ADC $A8   ; add receiver bit count in
.EF7C  D0 EF    BNE $EF6D   ; exit, branch always
```


## Commenti

### Original Disassembly (—)
- **$EF59**: get start bit check flag
- **$EF5B**: if no start bit received go ??
- **$EF5D**: decrement receiver bit count in
- **$EF5F**: if the byte is complete go add it to the buffer
- **$EF63**: get the RS232 received data bit
- **$EF65**: EOR with the receiver parity bit
- **$EF67**: save the receiver parity bit
- **$EF69**: shift the RS232 received data bit
- **$EF6E**: decrement receiver bit count in
- **$EF70**: get the RS232 received data bit
- **$EF74**: get pseudo 6551 control register
- **$EF77**: shift the stop bit flag to Cb
- **$EF78**: + 1
- **$EF7A**: add receiver bit count in
- **$EF7C**: exit, branch always

### Commodore-64-intern-Buch (Commodore)
- **$EF59**: Startbit ?
- **$EF5B**: verzweige wenn ja
- **$EF5D**: Bitzähler erniedrigen
- **$EF5F**: verzweige wenn alle Bits empfangen
- **$EF61**: verzweige wenn noch Stopbits zu erwarten
- **$EF63**: empfangenes Bit
- **$EF65**: mit Register für Parity verknüpfen
- **$EF67**: und abspeichern
- **$EF69**: empfangenes Bit ins Carry
- **$EF6B**: und in Empfangsregister schieben
- **$EF6D**: Rücksprung
- **$EF6E**: Bitzähler erniedrigen
- **$EF70**: Stopbit
- **$EF72**: verzweige wenn gleich Null
- **$EF74**: Kontrollregister laden
- **$EF77**: Bit 7 (Anzahl Stopbits) ins Carry
- **$EF78**: 1 laden und mit der Anzahl
- **$EF7A**: von Bits und Stopbits addieren
- **$EF7C**: verzweige wenn noch nicht alle Stopbits empfangen
- **$EF7E**: Wert für Freigabe von NMI über die Flagleitung
- **$EF80**: Wert NMI freigeben
- **$EF83**: auch im NMI Register
- **$EF86**: für RS 232 NMIs vermerken
- **$EF89**: und Flag für Startbit setzen
- **$EF8B**: Bitwert für
- **$EF8D**: NMI für Timer B löschen
- **$EF90**: Startbit laden
- **$EF92**: verzweige wenn ungleich Null
- **$EF94**: Flag für Startbit rücksetzen
- **$EF96**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EF59**: RINONE, check for start bit?
- **$EF5D**: BITC1, RS232 in bit count
- **$EF5F**: process received byte
- **$EF63**: INBIT, RS232 in bits
- **$EF65**: RIPRTY, RS232 in parity
- **$EF69**: INBIT, put input bit into carry
- **$EF6B**: RIDATA,
- **$EF6E**: BITC1
- **$EF70**: INBIT
- **$EF74**: M51CTR, 6551 control register image
- **$EF7A**: BITC1
- **$EF7C**: end

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*