---
title: initialise SID, CIA and IRQ
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
- fda3-interrupt-initialisierung
- fddd-enable-timer
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FDA3
  address_end: $FDF6
  symbol: initialise-sid-cia-and-irq
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FDA3**: disable all interrupts'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FDA3**: Interrupt löschen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FDA5**: CIA#1 IRQ control register'
---

# $FDA3 — initialise SID, CIA and IRQ

## Disassemblatura
```assembly
.FDA3  A9 7F    LDA #$7F   ; disable all interrupts
.FDA5  8D 0D DC STA $DC0D   ; save VIA 1 ICR
.FDA8  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.FDAB  8D 00 DC STA $DC00   ; save VIA 1 DRA, keyboard column drive
.FDAE  A9 08    LDA #$08   ; set timer single shot
.FDB0  8D 0E DC STA $DC0E   ; save VIA 1 CRA
.FDB3  8D 0E DD STA $DD0E   ; save VIA 2 CRA
.FDB6  8D 0F DC STA $DC0F   ; save VIA 1 CRB
.FDB9  8D 0F DD STA $DD0F   ; save VIA 2 CRB
.FDBC  A2 00    LDX #$00   ; set all inputs
.FDBE  8E 03 DC STX $DC03   ; save VIA 1 DDRB, keyboard row
.FDC1  8E 03 DD STX $DD03   ; save VIA 2 DDRB, RS232 port
.FDC4  8E 18 D4 STX $D418   ; clear the volume and filter select register
.FDC7  CA       DEX   ; set X = $FF
.FDC8  8E 02 DC STX $DC02   ; save VIA 1 DDRA, keyboard column
.FDCB  A9 07    LDA #$07   ; DATA out high, CLK out high, ATN out high, RS232 Tx DATA high, video address 15 = 1, video address 14 = 1
.FDCD  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.FDD0  A9 3F    LDA #$3F   ; set serial DATA input, serial CLK input
.FDD2  8D 02 DD STA $DD02   ; save VIA 2 DDRA, serial port and video address
.FDD5  A9 E7    LDA #$E7   ; set 1110 0111, motor off, enable I/O, enable KERNAL, enable BASIC
.FDD7  85 01    STA $01   ; save the 6510 I/O port
.FDD9  A9 2F    LDA #$2F   ; set 0010 1111, 0 = input, 1 = output
.FDDB  85 00    STA $00   ; save the 6510 I/O port direction register
.FDDD  AD A6 02 LDA $02A6   ; get the PAL/NTSC flag
.FDE0  F0 0A    BEQ $FDEC   ; if NTSC go set NTSC timing else set PAL timing
.FDE2  A9 25    LDA #$25
.FDE4  8D 04 DC STA $DC04   ; save VIA 1 timer A low byte
.FDE7  A9 40    LDA #$40
.FDE9  4C F3 FD JMP $FDF3
.FDEC  A9 95    LDA #$95
.FDEE  8D 04 DC STA $DC04   ; save VIA 1 timer A low byte
.FDF1  A9 42    LDA #$42
.FDF3  8D 05 DC STA $DC05   ; save VIA 1 timer A high byte
.FDF6  4C 6E FF JMP $FF6E
```


## Commenti

### Original Disassembly (—)
- **$FDA3**: disable all interrupts
- **$FDA5**: save VIA 1 ICR
- **$FDA8**: save VIA 2 ICR
- **$FDAB**: save VIA 1 DRA, keyboard column drive
- **$FDAE**: set timer single shot
- **$FDB0**: save VIA 1 CRA
- **$FDB3**: save VIA 2 CRA
- **$FDB6**: save VIA 1 CRB
- **$FDB9**: save VIA 2 CRB
- **$FDBC**: set all inputs
- **$FDBE**: save VIA 1 DDRB, keyboard row
- **$FDC1**: save VIA 2 DDRB, RS232 port
- **$FDC4**: clear the volume and filter select register
- **$FDC7**: set X = $FF
- **$FDC8**: save VIA 1 DDRA, keyboard column
- **$FDCB**: DATA out high, CLK out high, ATN out high, RS232 Tx DATA high, video address 15 = 1, video address 14 = 1
- **$FDCD**: save VIA 2 DRA, serial port and video address
- **$FDD0**: set serial DATA input, serial CLK input
- **$FDD2**: save VIA 2 DDRA, serial port and video address
- **$FDD5**: set 1110 0111, motor off, enable I/O, enable KERNAL, enable BASIC
- **$FDD7**: save the 6510 I/O port
- **$FDD9**: set 0010 1111, 0 = input, 1 = output
- **$FDDB**: save the 6510 I/O port direction register
- **$FDDD**: get the PAL/NTSC flag
- **$FDE0**: if NTSC go set NTSC timing else set PAL timing
- **$FDE4**: save VIA 1 timer A low byte
- **$FDEE**: save VIA 1 timer A low byte
- **$FDF3**: save VIA 1 timer A high byte

### Commodore-64-intern-Buch (Commodore)
- **$FDA3**: Interrupt löschen
- **$FDA5**: ICR CIA 1
- **$FDA8**: ICR CIA 2 Port A CIA 1
- **$FDAB**: Tastatur Matrixzeile 0
- **$FDAE**: Wert laden
- **$FDB0**: CRA CIA 1 Timer A 'one shot'
- **$FDB3**: CRA CIA 2 Timer A 'one shot'
- **$FDB6**: CRB CIA 1 Timer B 'one shot'
- **$FDB9**: CRB CIA 2 Timer B 'one shot'
- **$FDBC**: Eingangs-Modus
- **$FDBE**: Datenrichtungsreg. B CIA 1
- **$FDC1**: Datenrichtungsreg. B CIA 2
- **$FDC4**: Lautstärke für SID auf Null
- **$FDC7**: Ausgabe-Modus
- **$FDC8**: Datenrichtungsreg. A CIA 1
- **$FDCB**: Videocontroller auf unterste 16 K
- **$FDCD**: Port A CIA 2, ATN löschen
- **$FDD0**: Bit 0 bis 5 auf Ausgabe
- **$FDD2**: Datenrichtungsreg. A CIA 2
- **$FDD5**: Normalwert laden und
- **$FDD7**: Speicheraufteilung neu setzen
- **$FDD9**: Bit 0-3 und 5 Ausgang, Bit 4 Eingang
- **$FDDB**: Datenrichtung Prozessorport
- **$FDDD**: NTSC-Version ?
- **$FDE0**: ja
- **$FDE2**: Wert für PAL-Version
- **$FDE4**: Timer für PAL-Version setzen
- **$FDE7**: $4025 = 16421 Zyklen
- **$FDE9**: NTSC-Version übergehen
- **$FDEC**: Wert für NTSC-Version
- **$FDEE**: Timer für NTSC-Version setzen
- **$FDF1**: $4295 = 17045 Zyklen
- **$FDF3**: Timer-HIGH setzen
- **$FDF6**: Interrupt durch Timer setzen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FDA5**: CIA#1 IRQ control register
- **$FDA8**: CIA#2 IRQ control register
- **$FDAB**: CIA#1 data port $ (keyboard)
- **$FDB0**: CIA#1 control register timer A
- **$FDB3**: CIA#2 control register timer A
- **$FDB6**: CIA#1 control register timer B
- **$FDB9**: CIA#2 control register timer B
- **$FDBE**: CIA#1 DDRB. Port B is input
- **$FDC1**: CIA#2 DDRB. Port B is input
- **$FDC4**: No sound from SID
- **$FDC8**: CIA#1 DDRA. Port A is output
- **$FDCB**: %00000111
- **$FDCD**: CIA#2 dataport A. Set Videobank to $0000-$3fff
- **$FDD0**: %00111111
- **$FDD2**: CIA#2 DDRA. Serial bus and videobank
- **$FDD5**: 6510 I/O port - %XX100111
- **$FDD9**: 6510 I/O DDR - %00101111

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*