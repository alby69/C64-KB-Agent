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
- 00d7-data
- eor
- fed6-eingabe
- ff07-nmi-routine-rs-232-ausgabe
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FED6
  address_end: $FF2D
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FED6**: read VIA 2 DRB, RS232 port'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FED6**: Port Register B'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FED6**: RS232 I/O port'
---

# $FED6 — ??

## Disassemblatura
```assembly
.FED6  AD 01 DD LDA $DD01   ; read VIA 2 DRB, RS232 port
.FED9  29 01    AND #$01   ; mask 0000 000x, RS232 Rx DATA
.FEDB  85 A7    STA $A7   ; save the RS232 received data bit
.FEDD  AD 06 DD LDA $DD06   ; get VIA 2 timer B low byte
.FEE0  E9 1C    SBC #$1C
.FEE2  6D 99 02 ADC $0299
.FEE5  8D 06 DD STA $DD06   ; save VIA 2 timer B low byte
.FEE8  AD 07 DD LDA $DD07   ; get VIA 2 timer B high byte
.FEEB  6D 9A 02 ADC $029A
.FEEE  8D 07 DD STA $DD07   ; save VIA 2 timer B high byte
.FEF1  A9 11    LDA #$11   ; set timer B single shot, start timer B
.FEF3  8D 0F DD STA $DD0F   ; save VIA 2 CRB
.FEF6  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.FEF9  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.FEFC  A9 FF    LDA #$FF
.FEFE  8D 06 DD STA $DD06   ; save VIA 2 timer B low byte
.FF01  8D 07 DD STA $DD07   ; save VIA 2 timer B high byte
.FF04  4C 59 EF JMP $EF59
.FF07  AD 95 02 LDA $0295   ; nonstandard bit timing low byte
.FF0A  8D 06 DD STA $DD06   ; save VIA 2 timer B low byte
.FF0D  AD 96 02 LDA $0296   ; nonstandard bit timing high byte
.FF10  8D 07 DD STA $DD07   ; save VIA 2 timer B high byte
.FF13  A9 11    LDA #$11   ; set timer B single shot, start timer B
.FF15  8D 0F DD STA $DD0F   ; save VIA 2 CRB
.FF18  A9 12    LDA #$12
.FF1A  4D A1 02 EOR $02A1   ; EOR with the RS-232 interrupt enable byte
.FF1D  8D A1 02 STA $02A1   ; save the RS-232 interrupt enable byte
.FF20  A9 FF    LDA #$FF
.FF22  8D 06 DD STA $DD06   ; save VIA 2 timer B low byte
.FF25  8D 07 DD STA $DD07   ; save VIA 2 timer B high byte
.FF28  AE 98 02 LDX $0298
.FF2B  86 A8    STX $A8
.FF2D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FED6**: read VIA 2 DRB, RS232 port
- **$FED9**: mask 0000 000x, RS232 Rx DATA
- **$FEDB**: save the RS232 received data bit
- **$FEDD**: get VIA 2 timer B low byte
- **$FEE5**: save VIA 2 timer B low byte
- **$FEE8**: get VIA 2 timer B high byte
- **$FEEE**: save VIA 2 timer B high byte
- **$FEF1**: set timer B single shot, start timer B
- **$FEF3**: save VIA 2 CRB
- **$FEF6**: get the RS-232 interrupt enable byte
- **$FEF9**: save VIA 2 ICR
- **$FEFE**: save VIA 2 timer B low byte
- **$FF01**: save VIA 2 timer B high byte
- **$FF07**: nonstandard bit timing low byte
- **$FF0A**: save VIA 2 timer B low byte
- **$FF0D**: nonstandard bit timing high byte
- **$FF10**: save VIA 2 timer B high byte
- **$FF13**: set timer B single shot, start timer B
- **$FF15**: save VIA 2 CRB
- **$FF1A**: EOR with the RS-232 interrupt enable byte
- **$FF1D**: save the RS-232 interrupt enable byte
- **$FF22**: save VIA 2 timer B low byte
- **$FF25**: save VIA 2 timer B high byte

### Commodore-64-intern-Buch (Commodore)
- **$FED6**: Port Register B
- **$FED9**: Bit für Receive Data isolie- ren
- **$FEDB**: und speichern
- **$FEDD**: Timer B LOW
- **$FEE0**: minus 28
- **$FEE2**: + LOW-Byte der Baudrate
- **$FEE5**: wieder abspeichern
- **$FEE8**: RS 232 Timerkon. für Baudrate
- **$FEEB**: HIGH-Byte addieren
- **$FEEE**: in Timer schreiben
- **$FEF1**: Timer B starten
- **$FEF3**: Control Register B
- **$FEF6**: CIA 2 NMI-Flag holen
- **$FEF9**: Interrupt Control Register
- **$FEFC**: Wert laden
- **$FEFE**: und damit
- **$FF01**: Timer setzen
- **$FF04**: Bit holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FED6**: RS232 I/O port
- **$FED9**: test bit0, received data
- **$FEDB**: store in INBIT
- **$FEDD**: lowbyte of timer B
- **$FEE2**: <BAUDOF
- **$FEE5**: store timer B
- **$FEE8**: highbyte of timer B
- **$FEEB**: >BAUDOF
- **$FEEE**: store timer B
- **$FEF3**: CIA#2 control register B
- **$FEF6**: ENABL
- **$FEF9**: CIA#2 interrupt control register
- **$FF04**: jump to RS232 receive routine

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*