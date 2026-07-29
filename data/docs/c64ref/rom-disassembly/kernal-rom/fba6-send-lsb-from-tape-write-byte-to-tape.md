---
title: send lsb from tape write byte to tape
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
- fba6-ein-bit-auf-band-schreiben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FBA6
  address_end: $FBC7
  symbol: send-lsb-from-tape-write-byte-to-tape
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FBA6**: get tape write byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FBA6**: Bit in $BD'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FBA6 — send lsb from tape write byte to tape

## Disassemblatura
```assembly
.FBA6  A5 BD    LDA $BD   ; get tape write byte
.FBA8  4A       LSR   ; shift lsb into Cb
.FBA9  A9 60    LDA #$60   ; set time constant low byte for bit = 0
.FBAB  90 02    BCC $FBAF   ; branch if bit was 0 set time constant for bit = 1 and toggle tape
.FBAD  A9 B0    LDA #$B0   ; set time constant low byte for bit = 1 write time constant and toggle tape
.FBAF  A2 00    LDX #$00   ; set time constant high byte write time constant and toggle tape
.FBB1  8D 06 DC STA $DC06   ; save VIA 1 timer B low byte
.FBB4  8E 07 DC STX $DC07   ; save VIA 1 timer B high byte
.FBB7  AD 0D DC LDA $DC0D   ; read VIA 1 ICR
.FBBA  A9 19    LDA #$19   ; load timer B, timer B single shot, start timer B
.FBBC  8D 0F DC STA $DC0F   ; save VIA 1 CRB
.FBBF  A5 01    LDA $01   ; read the 6510 I/O port
.FBC1  49 08    EOR #$08   ; toggle tape out bit
.FBC3  85 01    STA $01   ; save the 6510 I/O port
.FBC5  29 08    AND #$08   ; mask tape out bit
.FBC7  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FBA6**: get tape write byte
- **$FBA8**: shift lsb into Cb
- **$FBA9**: set time constant low byte for bit = 0
- **$FBAB**: branch if bit was 0 set time constant for bit = 1 and toggle tape
- **$FBAD**: set time constant low byte for bit = 1 write time constant and toggle tape
- **$FBAF**: set time constant high byte write time constant and toggle tape
- **$FBB1**: save VIA 1 timer B low byte
- **$FBB4**: save VIA 1 timer B high byte
- **$FBB7**: read VIA 1 ICR
- **$FBBA**: load timer B, timer B single shot, start timer B
- **$FBBC**: save VIA 1 CRB
- **$FBBF**: read the 6510 I/O port
- **$FBC1**: toggle tape out bit
- **$FBC3**: save the 6510 I/O port
- **$FBC5**: mask tape out bit

### Commodore-64-intern-Buch (Commodore)
- **$FBA6**: Bit in $BD
- **$FBA8**: Bit 0 in Carry
- **$FBA9**: Zeit für '0' Bit
- **$FBAB**: verzweige falls Carry=0
- **$FBAD**: Zeit für '1' Bit
- **$FBAF**: HIGH-Byte Timerwert laden
- **$FBB1**: Timer B LOW
- **$FBB4**: Timer B HIGH
- **$FBB7**: Interrupt-Flag löschen
- **$FBBA**: Timer
- **$FBBC**: B starten
- **$FBBF**: Tape-Write-Bit laden
- **$FBC1**: Ausgabe-Bit für Band invertieren
- **$FBC3**: und speichern
- **$FBC5**: augenblicklichen Pegel merken
- **$FBC8**: Block-Write-Flag
- **$FBC9**: Negativ
- **$FBCB**: Rückkehr vom Interrupt

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*